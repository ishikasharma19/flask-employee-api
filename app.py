from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from datetime import datetime

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost/employee_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    department = db.Column(db.String(50))
    joining_date = db.Column(db.Date)


with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add_employee', methods=['POST'])
def add_employee():
    data = request.json
    try:
        new_employee = Employee(
            name=data['name'],
            email=data['email'],
            department=data['department'],
            joining_date=datetime.strptime(data['joining_date'], '%Y-%m-%d').date()
        )
        db.session.add(new_employee)
        db.session.commit()
        return jsonify({'message': 'Employee added successfully!'})
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Email already exists. Please use a different email.'}), 400


@app.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    result = []
    for emp in employees:
        result.append({
            'id': emp.id,
            'name': emp.name,
            'email': emp.email,
            'department': emp.department,
            'joining_date': emp.joining_date.strftime('%Y-%m-%d')
        })
    return jsonify({
        'total_employees': len(result),
        'employees': result
    })


if __name__ == '__main__':
    app.run(debug=True)
