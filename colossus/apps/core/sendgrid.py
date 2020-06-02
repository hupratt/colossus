# from django.conf import settings
# from decouple import Csv, config

# settings.configure('colossus.settings')
# print(settings.SENDGRID_API_KEY)

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email="from_email@example.com",
    to_emails="hprattdo@gmail.com",
    subject="Sending with Twilio SendGrid is Fun",
    html_content="<strong>and easy to do anywhere, even with Python</strong>",
)
try:
    sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)


data = {"ips": [{"ip": "192.168.1.1"}, {"ip": "192.*.*.*"}, {"ip": "192.168.1.3/32"}]}
response = sg.client.access_settings.whitelist.post(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)
