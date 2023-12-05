from flask import Flask, render_template, request, redirect, session
from users import Users 

app = Flask(__name__)
app.secret_key = 'root'

@app.route('/')
def main_page():
    return render_template('create.html') 

@app.route('/create', methods=['POST'])
def create():
    print(request.form)
    Users.save(request.form)
    return redirect('/read')

@app.route('/read')
def read():
    my_users = Users.get_all()
    return render_template("read.html", my_users = my_users)

if __name__ == "__main__":
    app.run(debug=True)