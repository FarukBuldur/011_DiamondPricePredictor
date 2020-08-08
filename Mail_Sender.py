import smtplib,ssl
import base64

def email_sender(receiver_email, message_params):


    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "diamondpredictor@gmail.com"
    #receiver_email = "farukbuldur@gmail.com"
    password_encry = b'ZGlhbW9uZDEyMzQ/'

    message = """\
    Subject: Your Diamond Price Prediction

    """ + message_params +""" ."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, base64.b64decode(password_encry).decode("utf-8"))
        server.sendmail(sender_email, receiver_email, message)


