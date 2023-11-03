from flask import Flask
import psycopg2

app = Flask(__name)

def get_patient_data():
    conn = psycopg2.connect(
        database="patient_db",
        user="user",
        password="password",
        host="db",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/')
def index():
    patient_data = get_patient_data()
    return f"Patient Data: {patient_data}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
