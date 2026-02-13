from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'mehakjindal6789@gmail.com'
app.config['MAIL_PASSWORD'] = 'ccse eyjp qrze gywi'

mail = Mail(app)


@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        singer = request.form["singer"]
        videos = request.form["videos"]
        duration = request.form["duration"]
        email = request.form["email"]

        os.system(f'py -3.11 102303792.py "{singer}" {videos} {duration} output.mp3')

        msg = Message("Your Mashup File",
                      sender="yourgmail@gmail.com",
                      recipients=[email])
        msg.body = "Your mashup is attached."
        msg.attach("output.mp3", "audio/mp3",
                   open("output.mp3","rb").read())

        mail.send(msg)
        return "Mashup Created & Email Sent Successfully!"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
