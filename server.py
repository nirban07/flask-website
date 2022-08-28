import csv
from flask import Flask, render_template,request,redirect, url_for

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")



def writetocsv(data):
    with open("database.csv",mode="a") as file:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_write = csv.writer(file,delimiter=",",quotechar='|',quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow([email,subject,message])

def writetodatabase(data):
    with open("databse.txt",mode="a") as file:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file.write(f"\n{email},{subject},{message}")

@app.route('/form_submitted', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        writetocsv(request.form.to_dict())
    return redirect('/thankyou')