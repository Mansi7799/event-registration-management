from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

# -------------------------------
# MySQL Configuration
# -------------------------------
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'bts.army7'      
app.config['MYSQL_DB'] = 'eventdb'

mysql = MySQL(app)

# -------------------------------
# Home Page
# -------------------------------
@app.route('/')
def home():

    registrations = []

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM registrations")
    registrations = cur.fetchall()
    cur.close()

    return render_template(
        'index.html',
        registrations=registrations
    )


# Submit Record
@app.route('/add', methods=['POST'])
def add():

    fullname = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']
    event_name = request.form['event_name']

    cur = mysql.connection.cursor()

    cur.execute(
        """
        INSERT INTO registrations
        (fullname, email, phone, event_name)
        VALUES (%s, %s, %s, %s)
        """,
        (fullname, email, phone, event_name)
    )

    mysql.connection.commit()
    cur.close()

    return redirect('/')

# View Records
@app.route('/view', methods=['POST'])
def view():

    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM registrations")

    registrations = cur.fetchall()

    cur.close()

    return render_template(
        'index.html',
        registrations=registrations
    )

# Update Record
@app.route('/update', methods=['POST'])
def update():

    id = request.form['id']
    fullname = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']
    event_name = request.form['event_name']

    cur = mysql.connection.cursor()

    cur.execute(
        """
        UPDATE registrations
        SET fullname=%s,
            email=%s,
            phone=%s,
            event_name=%s
        WHERE id=%s
        """,
        (fullname, email, phone, event_name, id)
    )

    mysql.connection.commit()
    cur.close()

    return redirect('/')

# Delete Record By ID
@app.route('/delete', methods=['POST'])
def delete():

    id = request.form['id']

    cur = mysql.connection.cursor()

    cur.execute(
        "DELETE FROM registrations WHERE id=%s",
        (id,)
    )

    mysql.connection.commit()
    cur.close()

    return redirect('/')

# Run Application
if __name__ == '__main__':
    app.run(debug=True, port=8000)