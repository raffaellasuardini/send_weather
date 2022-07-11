from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class Email(Mail):
    def __init__(self, receiver, sender, subject, body, key):
        Mail.__init__(self, from_email=sender, to_emails=receiver, subject=subject, html_content=body)
        self.from_email = sender
        self.to_emails = receiver
        self.subject = subject
        self.html_content = body
        self.key = key

    def send(self):
        try:
            sg = SendGridAPIClient(self.key)
            message = Mail(self.from_email, self.to_emails, self.subject, self.html_content)
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)
