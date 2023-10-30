from django.shortcuts import render
from .tasks import send_sms


def main(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        message = "I did it!!!"

        send_sms.delay(phone_number, message)

    return render(request, "main.html")
