from django.shortcuts import render,redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


def portfolio(request):
    return render(request, 'portfolio.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Compose the email
            subject = f'Contact Form Submission from {name}'
            body = f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [from_email]

            # Send the email
            send_mail(subject, body, from_email, recipient_list)

            return redirect('contact_success')
    else:
        form = ContactForm()
    
    return render(request, 'portfolio.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')