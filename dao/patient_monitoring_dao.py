import mysql.connector
from mysql.connector import Error

class PatientDAO:
    def __init__(self, host, user, password, database):
        """Initialize the DAO class with database connection parameters"""
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        """Establish a connection to the MySQL database"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Successfully connected to the database.")
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None

    def disconnect(self):
        """Close the database connection"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed.")

    def get_patients_over_48_hours(self):
        """Fetch patients hospitalized for more than 48 hours without new tests"""
        query = """
            SELECT 
                patient_id,
                first_name,
                last_name,
                date_of_birth,
                DATE_FORMAT(STR_TO_DATE(CONCAT(admission_date, ' ', admission_time),
                                '%m/%d/%Y %h:%i:%s %p'),
                        '%Y-%m-%d %H:%i:%s') admission_date,
                last_time_results,
                department,
                room_number
            FROM
                patient_information
                    JOIN
                admissions USING (patient_id)
                    JOIN
                (SELECT 
                    MAX(STR_TO_DATE(CONCAT(performed_date, ' ', performed_time), '%m/%d/%Y %h:%i:%s %p')) last_time_results,
                        patient_id
                FROM
                    admissions
                JOIN lab_tests USING (patient_id)
                JOIN lab_results USING (test_id)
                WHERE
                    (release_date IS NULL
                        OR release_time IS NULL)
                        AND TIMESTAMPDIFF(HOUR, STR_TO_DATE(CONCAT(admission_date, ' ', admission_time), '%m/%d/%Y %h:%i:%s %p'), NOW()) > 48
                GROUP BY patient_id
                HAVING TIMESTAMPDIFF(HOUR, MAX(STR_TO_DATE(CONCAT(performed_date, ' ', performed_time), '%m/%d/%Y %h:%i:%s %p')), NOW()) > 48) last_time_results USING (patient_id)
        """
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            return results  # Returns the list of patients as dictionaries
        except Error as e:
            print(f"Error while executing the query: {e}")
            return None
        finally:
            cursor.close()

if __name__ == '__main__':
    dao = PatientDAO('localhost','root', '123456', 'patient_monitoring')
    dao.connect()

    # Get patients hospitalized for over 48 hours without new tests
    patients = dao.get_patients_over_48_hours()
    if patients:
        for patient in patients:
            print(patient)

    # Get a specific patient by ID
    patient_data = dao.get_patient_by_id(12345)
    if patient_data:
        print(patient_data)

    # Disconnect from the database
    dao.disconnect()

