
from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD') 

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # You can add Flask-Mail here to send emails
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        flash('Message sent successfully!', 'success')
        return redirect('/contact')
    return render_template('contact.html')

port = int(os.environ.get("PORT", 5000))
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)