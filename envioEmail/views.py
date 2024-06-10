from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    send_mail("Hola desde mi proyecto en Django!",
             "Hola, este es un mensaje automatizado.",
             "villafuertequispealex@gmail.com",
             ["kaviyof447@cnurbano.com"],
            fail_silently=False
    )
    return render(request, 'send/index.html')