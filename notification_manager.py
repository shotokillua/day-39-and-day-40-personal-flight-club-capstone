from twilio.rest import Client
import smtplib

TWILIO_SID = "ACc9563c4a0df11b1cb81200a716b8620b"
TWILIO_AUTH_TOKEN = "da4310b1ee89f5bfc6b5c6e5bb36fad2"
TWILIO_VIRTUAL_NUMBER = "+18776413072"
TWILIO_VERIFIED_NUMBER = "+17133519231"
MY_EMAIL = "shotokillua55@gmail.com"
MY_PW = "hwoxibxdpyngtimt"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PW)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )