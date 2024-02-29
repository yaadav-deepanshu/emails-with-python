import smtplib
from email.message import EmailMessage

# Create an EmailMessage object
email = EmailMessage()

# Set email parameters
email['From'] = 'Deepanshu Yadav'
email['To'] = 'yaadav.deepanshu@gmail.com'
email['Subject'] = 'Hi, my name is Deepanshu and I am looking for a job'

# Set email content
email.set_content('''
Subject: Inquiry Regarding Full Stack Developer Position in IoT at Ace Makers

Dear Hiring Manager,

I hope this email finds you well. My name is Deepanshu Yadav, and I am writing to inquire about any potential openings for a Full Stack Developer position in the field of IoT at Ace Makers.

I am a passionate and experienced Full Stack Developer with a strong background in IoT technologies. Over the years, I have gained expertise in developing end-to-end solutions for IoT projects, ranging from sensor integration and data collection to building robust web-based applications for data visualization and control.

My skills include proficiency in both front-end and back-end development technologies, including but not limited to:

Front-end: HTML, CSS, JavaScript (React.js, Angular, Vue.js)
Back-end: Node.js, Express.js, Django, Flask
Database: SQL (MySQL, PostgreSQL), NoSQL (MongoDB)
IoT Platforms: Raspberry Pi, Arduino, MQTT, AWS IoT, Azure IoT

I am particularly drawn to Ace Makers due to its reputation for innovation and commitment to pushing the boundaries in the IoT space. I am excited about the opportunity to contribute my skills and experience to your team and to be a part of the exciting projects you are working on.

If there is currently a need for a Full Stack Developer with expertise in IoT technologies at Ace Makers, I would be thrilled to further discuss how my background aligns with your requirements. I am available at your earliest convenience for an interview or further discussions.

Thank you for considering my inquiry. I have attached my resume for your reference. I look forward to hearing from you soon.

Warm regards,

Deepanshu Yadav 
8728081860
[Your Resume Attached]
''')

# Connect to the SMTP server and send the email
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('yaadav.practice@gmail.com', 'Batm@n3107')  # Replace with your Gmail credentials
    smtp.send_message(email)

print('Email sent successfully')
