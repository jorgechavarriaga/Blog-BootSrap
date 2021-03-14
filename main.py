"""
*************************************************************************
*    Course: 100 Days of Code - Dra. Angela Yu                          *
*    Author: Jorge Chavarriaga                                          *
*    Day: 59- BLOG - upgraded with bootstrap                            *
*    Date: 2021-01-20                                                   *
*************************************************************************
"""

from flask import Flask, render_template, request
import requests
from post import Post
import smtplib

url = 'https://api.npoint.io/43644ec4f0013682fc0d'
my_email = "jachavar.python.2020@gmail.com"
to_email = "jorge.chavarriaga@gmail.com"
my_password = "pc98589587JM"

posts = requests.get(url).json()

app = Flask(__name__)

@app.route('/')
def get_all_posts():

    return render_template("index.html", all_posts=posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html", msg_sent=False)
    else:
        send_mail(request.form['name'], request.form['email'], request.form['phone'], request.form['message'] )
        return render_template("contact.html", msg_sent=True)


def send_mail(name, email, phone, message):
    message_email = f"Subject: Blog Contact\n\n \n" \
                    f"Message from: {name}\n" \
                    f"Email: {email}\n" \
                    f"Phone: {phone}\n" \
                    f"Message: {message}\n"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                            msg=message_email)


if __name__ == "__main__":
    app.run(debug=True)