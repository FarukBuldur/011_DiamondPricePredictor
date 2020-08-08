import smtplib,ssl

def email_sender(receiver_email, message_params):


    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "diamondpredictor@gmail.com"
    #receiver_email = "farukbuldur@gmail.com"
    password = "diamond1234?"

    message = """\
    Subject: Your Diamond Price Prediction

    """ + message_params +""" ."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)



email_sender("farukbuldur@gmail.com", "TESTTESTTEST")