from django.shortcuts import render

def contact(request):
    return render(request, 'contact/basic_contact.html', {'content':['Exemplo de texto para contato','email_de_exemplo@gmial.com']})
