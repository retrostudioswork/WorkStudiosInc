from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm

from .models import Portfolio, Team, Services, About, Clients, FooterLinks

def index(request):

    form = ContactForm(request.POST or None)

    if form.is_valid():
        form_name = form.cleaned_data.get("name")
        form_subject = form.cleaned_data.get("subject")
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")

        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email,from_email]
        subject = form_subject

        contact_message = " %s: %s via %s "%(form_name, form_message, form_email)

        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email)

        #send_mail(subject,message,from_email, email, fail_silently=False)
        print (form_email,form_name,form_subject, form_message)


    portfolios = Portfolio.objects.all().order_by('-date_added')
    services = Services.objects.all().order_by('title')
    teams = Team.objects.all().order_by('date_added')
    about = About.objects.latest('id')
    clients = Clients.objects.all()
    footer = FooterLinks.objects.all()

    context = {'footer':footer, 'form':form, 'portfolios': portfolios, 'services':services, 'teams':teams, 'about':about, 'clients':clients}

    return render(request, 'guestbook/index.html',context)


def terms(request):
    return render(request, 'guestbook/terms.html')

def privacy(request):
    return render(request, 'guestbook/privacy.html')
