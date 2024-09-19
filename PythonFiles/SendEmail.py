import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from dotenv import load_dotenv
import os

# Print the current working directory
print(f"Current working directory: {os.getcwd()}")

load_dotenv()

# Retrieve and print the password
password = os.getenv("password")
if password is None:
    print("Error: Password not found in environment variables.")
else:
    print(f"Password loaded: {password}")

# Email settings
sender_email = "rapamansalman@gmail.com"
receiver_email = "amansalman221@gmail.com"
subject = "Test Email from Python"
body = "This is a test email sent from Python using smtplib."


# Create the email content
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject

# Attach the body of the email
message.attach(MIMEText(body, 'plain'))

# Connect to the SMTP server
try:
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.starttls()  # Start TLS (Transport Layer Security)

    # Log in to your email account
    smtp_server.login(sender_email, password)

    # Send the email
    smtp_server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")

    # Close the connection
    smtp_server.quit()

except Exception as e:
    print(f"Error: {e}")
