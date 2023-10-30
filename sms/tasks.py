from celery import shared_task
from twilio.rest import Client
from django.conf import settings

client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)


@shared_task
def send_sms(receiver, message):
    print('Go into task!')
    message = client.messages.create(
        body=message,
        from_="+16562130708",
        to=receiver,
    )

    return message.sid
