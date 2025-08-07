
from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mail import Mail, Message
import os

application = Flask(__name__)


application.config['MAIL_SERVER'] = 'smtp.gmail.com'
application.config['MAIL_PORT'] = 587
application.config['MAIL_USE_TLS'] = True
application.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
application.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD') 

mail = Mail(application)

@application.route('/')
def home():
    return render_template('index.html')

@application.route('/projects')
def projects():
    return render_template('projects.html')


@application.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Compose email
        msg = Message(f"New Message from {name}",
                      sender=email,
                      recipients=['asingopaul66@gmail.com'])  # Replace with your receiving email

        msg.body = f"From: {name} <{email}>\n\nMessage:\n{message}"

        try:
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
        except Exception as e:
            print("Error:", e)
            flash('There was an error sending your message.', 'danger')

        return redirect(url_for('contact'))

    return render_template('contact.html')

port = int(os.environ.get("PORT", 5000))
if __name__ == '__main__':
    application.run(host="0.0.0.0", port=port)
