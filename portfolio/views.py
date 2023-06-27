from django.http import BadHeaderError, HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from my_portfolio.settings import DEFAULT_FROM_EMAIL
from .models import *
from blog.models import Blog

def index(request):
    cmpetances = Competence.objects.all()
    experience = Experience.objects.all()
    services = Service.objects.all()
    projets = Project.objects.all()
    clients = Client.objects.all()
    education = Education.objects.order_by('-date_debut')[:3]
    langs = Langue.objects.all()
    blogs = Blog.objects.order_by('-date_creation')[:3]
    categori = Categorie.objects.all()
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if nom and email and message:
            contact = Contact.objects.create(nom=nom, email=email, message=message)
            try:
                # Envoyer l'e-mail de notification
                subject = 'Nouveau message de contact Portfolio'
                message = f'Nom: {nom}\nEmail: {email}\nMessage: {message}'
                from_email = email
                to_email = [DEFAULT_FROM_EMAIL]
                send_mail(subject, message, from_email, to_email)
            except:
                print('Erreur lors de l\'envoi de l\'e-mail')
    return render(request, 'portfolio/index.html', locals())