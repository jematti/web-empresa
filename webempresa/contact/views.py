from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def Contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')   
            message = request.POST.get('message', '')
            
            # CORREGIDO: El subject y el body ahora están bien separados
            email = EmailMessage(
                "Personal: Nuevo mensaje de contacto",  # Subject (ASUNTO)
                f"De {name} <{email}>\n\nEscribió:\n\n{message}",  # Body (CUERPO)
                "no-contestar@inbox.mailtrap.io",  # From (REMITENTE)
                ["pattofeliz96@gmail.com"],  # To (DESTINATARIOS)
                reply_to=[email]  # Reply-to (RESPUESTA)
            )
            try:
                email.send()
                return redirect(reverse('contact') + '?ok')
            except:
                # algo no ha salido bien
                return redirect(reverse('contact') + '?fail')

    return render(request, 'contact/contact.html', {'form': contact_form})