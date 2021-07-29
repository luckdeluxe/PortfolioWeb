from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail


def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    if request.method == 'POST':        
        #Instance form
        form = ContactForm(request.POST)

        #Verify form
        if form.is_valid():
            
            #Email sending
            subject = request.POST['subject'].capitalize()
            message = request.POST['message'] + ' ' + request.POST['email']
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['luckdeveloper@hotmail.com']
            send_mail(subject, message, email_from, recipient_list)
            
            form.cleaned_data
            return HttpResponseRedirect('/')

    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {'form': form})