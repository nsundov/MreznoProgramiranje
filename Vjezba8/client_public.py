import smtplib
import email.utils
from email.mime.text import MIMEText


msg = MIMEText('This is the body of the message.')


msg['Subject'] = 'Simple test message'


server = smtplib.SMTP_SSL('smtp.gmail.com:465')
server.login('nsundov@gmail.com', '')
server.sendmail('nsundov@gmail.com', 'anteprojic@gmail.com', msg.as_string())
server.quit()