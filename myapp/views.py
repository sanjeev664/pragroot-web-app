from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.views import View
# from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags


def home(request):
    if request.method == 'POST':
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        msg = request.POST.get('message')
        username = (fname + lname)
        # data = EmailMessage(username, msg, to=[settings.EMAIL_HOST_USER])
        # data.send()   
        context = {
            'username': fname + lname,
            'email': email,
            'phone': phone,
            'message': msg,
        }
        print(context)
        html_content = render_to_string('myapp/email.html', context)
        text_context = strip_tags(html_content)
        new_email = EmailMultiAlternatives(
            'Testing Mail',
            text_context,
            email,
            [settings.EMAIL_HOST_USER],
        )
        new_email.attach_alternative(text_context, 'text/html')
        new_email.send()
        return HttpResponseRedirect('/success/')
    else:
        # send_mail('Subject here', 'Here is the message.', 'sunilrajputdev@gmail.com',[settings.EMAIL_HOST_USER], fail_silently=False)
        # email.send()
        return render(request, 'myapp/index.html')

class HomePage(View):
    def get(self, request):
        return render(request, "myapp/index.html")

    def post(self, request):
        fname = request.POST.get("first_name")
        lname = request.POST.get("last_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        msg = request.POST.get("message")
        context = {
            "username": fname + lname,
            "email": email,
            "phone": phone,
            "message": msg,
        }
        # try:
        html_content = render_to_string('myapp/email.html', context)
        text_content = strip_tags(html_content)
        new_email = EmailMultiAlternatives(
            #subject
            "Testing Mail",
            #content
            text_content,
            #from email
            email,
            # rec list
            [settings.EMAIL_HOST_USER]
        )
        new_email.attach_alternative(html_content, "text/html")
        new_email.send()
        # except SMTPNotSupportedError as e:
        #     return HttpResponse("Invalid header found !")
        return HttpResponseRedirect("/success/")


class ContanctView(View):
    def get(self, request):
        return render(request, 'myapp/contact.html')

    def post(self, request):
        # form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            # subject = form.cleaned_data["subject"]
            phone = form.cleaned_data["phone"]
            message = form.cleaned_data["message"]
            try:
                send_mail(
                    subject,
                    first_name,
                    last_name,
                    message,
                    ["sunil.raj8650142042@gmail.com"],
                )
            except BadHeaderError:
                return HttpResponse("Invalid header Found!")
            return HttpResponseRedirect("/success/")


class SuccessView(View):
    def get(self, request):
        return HttpResponse("Success! Thanks for this message.")


# send_mail('That’s your subject', 'That’s your message body', ‘sunilrajputdev@gmail.com’,['sunil.pragmainfosoft@gmail.com'], 'sunil.pragmainfosoft@gmail.com', 'sunil@1996',fail_silently = False)