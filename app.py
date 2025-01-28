from flask import Flask, render_template

from dao.patient_monitoring_dao import PatientDAO

app = Flask(__name__)

# Configure database connection
db_host = 'localhost'
db_user = 'root'
db_password = '123456'
db_name = 'patient_monitoring'

# Create a PatientDAO instance
patient_dao = PatientDAO(host=db_host, user=db_user, password=db_password, database=db_name)


@app.route('/')
def index():
    # Connect to the database
    patient_dao.connect()

    # Get patients who have been hospitalized for more than 48 hours without new tests
    patients = patient_dao.get_patients_over_48_hours()

    # Disconnect from the database
    patient_dao.disconnect()

    # Render the patients' data in an HTML table
    return render_template('index.html', patients=patients)


if __name__ == '__main__':
    app.run(debug=True)