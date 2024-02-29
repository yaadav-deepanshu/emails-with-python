import smtplib as smtp
from email.message import EmailMessage
from string import Template
from pathlib import Path

html=Template(Path("/media/deepanshu/POCO/Coding viscode/emails with python/index.html").read_text())

connection = smtp.SMTP_SSL('smtp.gmail.com', 465)

email = EmailMessage()

email_addr = 'yaadav.python@gmail.com'
email_passwd = 'gkzm kvvw awaa neku '

email['From'] = email_addr
email['To'] = 'yaadav.deepanshu@gmail.com'
email['Subject'] = 'Inquiry Regarding cloud engineer Developer Position in IoT at Ace Makers'


email.set_content(html.substitute({"name":"Deepanshu Yadav "}),"html")
connection.login(email_addr, email_passwd)
connection.send_message(email)
connection.close()
