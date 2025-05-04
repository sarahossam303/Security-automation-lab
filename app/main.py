# main.py
from flask import Flask, request, render_template_string, redirect, url_for
import os

app = Flask(__name__)

HTML_HOME = '''
<h1>Welcome to Demo App</h1>
<p><a href="/login">Login</a> | <a href="/form">Form</a></p> | <a href="/redirect?next=https://www.google.com">google.com</a>
'''

HTML_LOGIN = '''
<h2>Login</h2>
<form method="POST">
  Username: <input name="username"><br>
  Password: <input type="password" name="password"><br>
  <input type="submit" value="Login">
</form>
'''

HTML_FORM = '''
<h2>Contact Form</h2>
<form method="POST">
  Name: <input name="name"><br>
  Message: <textarea name="message"></textarea><br>
  <input type="submit" value="Send">
</form>
'''

@app.route("/")
def home():
    return HTML_HOME

@app.route("/redirect")
def open_redirect():
    next_url = request.args.get("next", "/")
    return redirect(next_url)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Insecure login (just echoing inputs - for ZAP to detect)
        username = request.form.get("username", "")
        return f"<p>Hello {username}, login attempt detected!</p>"
    return HTML_LOGIN

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        # Insecurely display user input
        name = request.form.get("name", "")
        message = request.form.get("message", "")
        return f"<p>Thanks {name}, we got your message: {message}</p>"
    return HTML_FORM

def rce_with_os_system():
    user_input = input("Enter a shell command: ")
    # Critical RCE vulnerability: unsanitized input to os.system
    os.system(user_input)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

