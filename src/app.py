from flask import Flask, request, jsonify, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configuración de la conexión a la base de datos
db_config = {
    'user': 'root',
    'password': '2631',
    'host': 'localhost',
    'database': 'nomina_db'
}

@app.route('/')
def index():
    return render_template('index.html')

# Gestión de empleados
@app.route('/empleados', methods=['GET'])
def list_employees():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM empleados")
    empleados = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('employees.html', empleados=empleados)

@app.route('/empleados/nuevo', methods=['GET'])
def create_employee_form():
    return render_template('employee_form.html', mode='Crear', empleado=None)

@app.route('/empleados', methods=['POST'])
def save_employee():
    data = request.form
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    if data['id']:
        cursor.execute("""
            UPDATE empleados SET cedula=%s, nombre=%s, departamento=%s, puesto=%s, salario_mensual=%s, nomina_id=%s
            WHERE id=%s
        """, (data['cedula'], data['nombre'], data.get('departamento'), data.get('puesto'), data['salario_mensual'], data['nomina_id'], data['id']))
    else:
        cursor.execute("""
            INSERT INTO empleados (cedula, nombre, departamento, puesto, salario_mensual, nomina_id)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (data['cedula'], data['nombre'], data.get('departamento'), data.get('puesto'), data['salario_mensual'], data['nomina_id']))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('list_employees'))

@app.route('/empleados/<int:id>/editar', methods=['GET'])
def edit_employee_form(id):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM empleados WHERE id = %s", (id,))
    empleado = cursor.fetchone()
    cursor.close()
    connection.close()
    return render_template('employee_form.html', mode='Editar', empleado=empleado)

@app.route('/empleados/eliminar', methods=['POST'])
def delete_employee():
    id = request.form['employee_id']
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM empleados WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('list_employees'))

# Gestión de tipos de ingresos
@app.route('/tipos_ingresos', methods=['GET'])
def list_income_types():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tipos_ingresos")
    ingresos = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('income_types.html', ingresos=ingresos)

@app.route('/tipos_ingresos/nuevo', methods=['GET'])
def create_income_type_form():
    return render_template('income_type_form.html', mode='Crear', ingreso=None)

@app.route('/tipos_ingresos', methods=['POST'])
def save_income_type():
    data = request.form
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    if data['id']:
        cursor.execute("""
            UPDATE tipos_ingresos SET nombre=%s, depende_salario=%s, estado=%s
            WHERE id=%s
        """, (data['nombre'], data['depende_salario'], data['estado'], data['id']))
    else:
        cursor.execute("""
            INSERT INTO tipos_ingresos (nombre, depende_salario, estado)
            VALUES (%s, %s, %s)
        """, (data['nombre'], data['depende_salario'], data['estado']))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('list_income_types'))

@app.route('/tipos_ingresos/<int:id>/editar', methods=['GET'])
def edit_income_type_form(id):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tipos_ingresos WHERE id = %s", (id,))
    ingreso = cursor.fetchone()
    cursor.close()
    connection.close()
    return render_template('income_type_form.html', mode='Editar', ingreso=ingreso)

@app.route('/tipos_ingresos/eliminar', methods=['POST'])
def delete_income_type():
    id = request.form['id']
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM tipos_ingresos WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('list_income_types'))

# Gestión de tipos de deducciones
@app.route('/tipos_deducciones', methods=['GET'])
def list_deduction_types():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tipos_deducciones")
    deducciones = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('deduction_types.html', deducciones=deducciones)

@app.route('/tipos_deducciones/nuevo', methods=['GET'])
def create_deduction_type_form():
    return render_template('deduction_type_form.html', mode='Crear', deduccion=None)

@app.route('/tipos_deducciones', methods=['POST'])
def save_deduction_type():
    data = request.form
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    if data['id']:
        cursor.execute("""
            UPDATE tipos_deducciones SET nombre=%s, depende_salario=%s, estado=%s
            WHERE id=%s
        """, (data['nombre'], data['depende_salario'], data['estado'], data['id']))
    else:
        cursor.execute("""
            INSERT INTO tipos_deducciones (nombre, depende_salario, estado)
            VALUES (%s, %s, %s)
        """, (data['nombre'], data['depende_salario'], data['estado']))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('list_deduction_types'))

@app.route('/tipos_deducciones/<int:id>/editar', methods=['GET'])
def edit_deduction_type_form(id):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tipos_deducciones WHERE id = %s", (id,))
    deduccion = cursor.fetchone()
    cursor.close()
    connection.close()
    return render_template('deduction_type_form.html', mode='Editar', deduccion=deduccion)

@app.route('/tipos_deducciones/eliminar', methods=['POST'])
def delete_deduction_type():
    id = request.form['id']
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM tipos_deducciones WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('list_deduction_types'))

if __name__ == '__main__':
    app.run(debug=True)
