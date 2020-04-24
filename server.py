from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template("index.html")


'''
For render templates need to create a 
template folder for HTML/CSS/JS files
'''


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(f"{page_name}.html")


def write_to_file(data):
    with open("database.txt", 'a') as database:
        email = data["Email"]
        subject = data["Subject"]
        message = data["Message"]
        database.write(f"\n\n ***New Message received*** \n Email: {email} \n Subject: {subject} \n Message: {message} ")


def write_to_csv(data):
    with open("database.csv", 'a') as database2:
        fieldnames = ["Email","Subject", "Message"]
        csv_writer = csv.DictWriter(database2, fieldnames=fieldnames)
        csv_writer.writerow(data)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect("/thankyou")
    else:
        return "Something went wrong, try again"