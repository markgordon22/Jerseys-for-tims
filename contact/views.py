from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm
from django.template.loader import render_to_string
from django.contrib import messages


def contact(request):
    """ a view to access contact page/form """
    template = 'contact/contact.html'

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for your enquiry. \
                             We will get back to you as soon as possible!")

            instance = form.save()
            """Send email confirming message received"""
            sender_email = instance.email
            matter = render_to_string(
                'contact/confirmation_emails/message_received_subject.txt',
                {'instance': instance})
            matter_body = render_to_string(
                'contact/confirmation_emails/message_received_body.txt',
                {'instance': instance,
                 'contact_email': settings.DEFAULT_FROM_EMAIL})
            send_mail(
                matter,
                matter_body,
                settings.DEFAULT_FROM_EMAIL,
                [sender_email],
            )

            return render(request, 'contact/contact_success.html')

        else:
            messages.error(request, 'Message not sent.'
                           ' Please ensure the form is valid!')

    form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, template, context)

