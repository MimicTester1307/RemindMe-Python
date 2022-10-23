from flask import Flask, render_template
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


@app.route('/')
def show_home():
    return render_template('index.html')


@app.route('/login')
def show_login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
