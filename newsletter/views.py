from django.shortcuts import render
from django.contrib import messages


def subscribe(request):
    """
    A Viewto handle email when user on submit 
    form
    """
    if request.method == "POST":
        messages.success(request, "We have received your email.")

    return render(request, "newsletter/newsletter.html")
