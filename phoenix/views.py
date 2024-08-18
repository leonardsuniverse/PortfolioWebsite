from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactEntry
from django.core.mail import send_mail
from django.conf import settings

def portfolio(request):
    return render(request, 'portfolio.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name', '')
            email = form.cleaned_data.get('email', '')
            subject = form.cleaned_data.get('subject', '')
            message = form.cleaned_data.get('message', '')

            # Save the new entry in the database
            ContactEntry.objects.create(name=name, email=email, subject=subject, message=message)

            # Ensure there are no more than 100 entries
            total_entries = ContactEntry.objects.count()
            if total_entries > 100:
                oldest_entries = ContactEntry.objects.order_by('timestamp')[:total_entries - 100]
                oldest_entries.delete()

            # Compose the email
            subject_email = f'Contact Form Submission from {name}'
            body = f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [from_email]

            # Send the email
            send_mail(subject_email, body, from_email, recipient_list)

            return redirect('contact_success')
        else:
            # Handle form errors
            print("Form errors:", form.errors)
    else:
        form = ContactForm()

    return render(request, 'portfolio.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')
