from django.shortcuts import render
from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')

        message = f""" 
            name: {name}
            email: {email}
            message:{message}
        """

        send_mail(
            subject ,
            message ,
            email ,
            ['mohammedemad1899@gmail.com', 'mohamedemad100899@gmail.com'],
            fail_silently=False
        )

    return render(request, 'contact/contact.html')