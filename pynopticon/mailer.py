import os

import sendgrid
import sendgrid.helpers.mail

sendgrid_api_key = os.environ["SENDGRID_API_KEY"]

def send_email(sg, to_email, from_email, subject, text):
  from_email = sendgrid.helpers.mail.Email(from_email)
  to_email = sendgrid.helpers.mail.To(to_email)
  content = sendgrid.helpers.mail.Content("text/plain", text)
  mail = sendgrid.helpers.mail.Mail(from_email, to_email, subject, content)
  response = sg.client.mail.send.post(request_body=mail.get())

  if response.status_code not in range(200, 203):
    print("Error sending email")
    print(response.status_code)
