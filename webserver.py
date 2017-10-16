from flask import Flask, request, render_template
import os
import requests
app = Flask(__name__,static_url_path="/static")

@app.route('/')
def index():
  #day_of_week = request.args.get('day_of_week','sunday')
  return render_template("index.html")

@app.route('/index')
def index1():
  return render_template("index.html")

@app.route('/about_us')
def aboutUs():
  return render_template("about_us.html")

# @app.route('/contactus')
# def contactUs():
#   return render_template("contactus.html")

@app.route('/8_Experiments_in_Motivation')
def blog1():
  return render_template("8_Experiments_in_Motivation.html")

@app.route('/A_Mindful_Shift_of_Focus')
def blog2():
  return render_template("A_Mindful_Shift_of_Focus.html")

@app.route('/How_to_Develop_an_Awesome_Sense_of_Direction')
def blog3():
  return render_template("How_to_Develop_an_Awesome_Sense_of_Direction.html")

@app.route('/Training_to_Be_a_Good_Writer')
def blog4():
  return render_template("Training_to_Be_a_Good_Writer.html")

@app.route('/What_Productivity_Systems_Wont_Solve')
def blog5():
  return render_template("What_Productivity_Systems_Wont_Solve.html")

@app.route('/contactus', methods=['GET'])
def send_email_GET():
    return render_template("contactus.html")


@app.route('/contact', methods=['POST'])
def send_email():
    print("Entered send_email")
    print
    message = request.form.get("comments")
    print("message: ", message)
    notifications = []
    data = {'from': os.environ["INFO253_MAILGUN_FROM_EMAIL"],'to': os.environ["INFO253_MAILGUN_TO_EMAIL"],'subject': "You just sent a message",'text': message}
    auth = (os.environ["INFO253_MAILGUN_USER"], os.environ["INFO253_MAILGUN_PASSWORD"])
    # auth = ("api", "key-ae18a13317ed4b8cb61ba88358409b79")
    print(auth)
    r = requests.post("https://api.mailgun.net/v3/{}/messages".format(os.environ["INFO253_MAILGUN_DOMAIN"]),auth=auth,data=data)
    print(r.text)
    if r.status_code == requests.codes.ok:
        notifications.append("Your email was sent")
    else:
        notifications.append("You email was not sent. Please try again later")
    return render_template("contactus.html", notifications=notifications)
