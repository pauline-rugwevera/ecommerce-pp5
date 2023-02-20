from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

def contactUs(request):

    """
    a view to display to display the contactform
    and handle form submission
    """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Thank you for your message!')
   
    else:
        form = ContactForm()
        messages.warning(request, 'Message not sent. Please try again.')

    form = ContactForm()
    template = 'contactus/contact_us.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
