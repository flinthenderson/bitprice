import smtplib, ssl

port = 465
password = input("Your password:")
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login('vergil.whiskey@gmail.com', password)
