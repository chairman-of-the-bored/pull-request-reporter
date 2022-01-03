import yagmail

def send_mail(api_key, from_address, recipients, subject, content):
    yag = yagmail.SMTP(from_address, api_key)
    yag.send(recipients, subject, content)
