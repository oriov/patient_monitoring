# patient monitoring
This repo represent the solution for patient monitoring web application


### how to run the project locally
1. download mysql latest image: docker pull mysql:latest
2. Run a MySQL Container: docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=123456 -d -p 3306:3306 mysql:latest
3. download some mysql client tool like mysql workbench
3. create database called `patient_monitoring` 
4. download python3.11
5. create venv: python3.11 -m venv venv
6. activate venv: source venv/bin/activate
7. run: pip install -r requirements.txt
8. create tables by running: alembic upgrade head
9. load csv files under static folder to the database
10. run: python3.11 app.py
11. open browser and go to: http://localhost:5000
