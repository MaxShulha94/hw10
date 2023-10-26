from django.shortcuts import render
from .tasks import send_sms


def main(request):
    send_sms.delay('+380957723261', 'Hello!')
    return render(request, "main.html")
