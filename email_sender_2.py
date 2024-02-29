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

# email.set_content('''
# Dear Hiring Manager,

# I hope this email finds you well. My name is Deepanshu Yadav, and I am writing to inquire about any potential openings for a Full Stack Developer position in the field of IoT at Ace Makers.

# I am a passionate and experienced Full Stack Developer with a strong background in IoT technologies. Over the years, I have gained expertise in developing end-to-end solutions for IoT projects, ranging from sensor integration and data collection to building robust web-based applications for data visualization and control.

# My skills include proficiency in both front-end and back-end development technologies, including but not limited to:

# Front-end: HTML, CSS, JavaScript (React.js, Angular, Vue.js)
# Back-end: Node.js, Express.js, Django, Flask
# Database: SQL (MySQL, PostgreSQL), NoSQL (MongoDB)
# IoT Platforms: Raspberry Pi, Arduino, MQTT, AWS IoT, Azure IoT

# I am particularly drawn to Ace Makers due to its reputation for innovation and commitment to pushing the boundaries in the IoT space. I am excited about the opportunity to contribute my skills and experience to your team and to be a part of the exciting projects you are working on.

# If there is currently a need for a Full Stack Developer with expertise in IoT technologies at Ace Makers, I would be thrilled to further discuss how my background aligns with your requirements. I am available at your earliest convenience for an interview or further discussions.

# Thank you for considering my inquiry. I have attached my resume for your reference. I look forward to hearing from you soon.

# Warm regards,

# Deepanshu Yadav 
# 8728081860
# [Your Resume Attached]
# ''')
email.set_content(html.substitute({"name":"tim"}),"html")
connection.login(email_addr, email_passwd)
connection.send_message(email)
connection.close()
