from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    send_mail("Hello from PrettyPrinted",
             "Hello there, This is an automated message.",
             "sirahib555@morxin.com",
             ["kaviyof447@cnurbano.com"],
            fail_silently=False
    )
    return render(request, 'send/index.html')