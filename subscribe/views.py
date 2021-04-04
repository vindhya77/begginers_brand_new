from django.shortcuts import render
from sendgrid_project.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail,EmailMessage


def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = str(sub['subject'].value())
        message = str(sub['message'].value())
        recepient = str(sub['Email'].value())
        attachment = request.FILES['attach']
        msg = EmailMessage(subject,
            message, EMAIL_HOST_USER, [recepient])
        msg.content_subtype = "html"
        msg.attach(attachment.name, attachment.read(), attachment.content_type)
        # msg.attach_file("/home/dev/Downloads/2019113.jpg")
        msg.send()
        # send_mail(subject,
            # message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'subscribe/success.html', {'recepient': recepient})
    return render(request, 'subscribe/index.html', {'form':sub})