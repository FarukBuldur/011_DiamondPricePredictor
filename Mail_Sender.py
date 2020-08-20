import smtplib,ssl
import base64
from email.mime.text import MIMEText

def email_sender(receiver_email, message_params):


    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "diamondpredictor@gmail.com"
    #receiver_email = "farukbuldur@gmail.com"
    password_encry = b'ZGlhbW9uZDEyMzQ/'

    #message = """\
    #Subject: Your Diamond Price Prediction
#
 #   """ + message_params +""" ."""

    message = f"<h3>New Diamond Prediction</h3><ul><li>Predicted Price: {message_params[0]}</li><li>Carat: {message_params[1]}</li><li>Cut: {message_params[2]}</li><li>Color: {message_params[3]}</li><li>Clarity: {message_params[4]}</li><li>Comments: {message_params[5]}</li></ul>"

    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Your Diamond Price Prediction'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, base64.b64decode(password_encry).decode("utf-8"))
        server.sendmail(sender_email, receiver_email, msg.as_string())


