from django.shortcuts import render
from listings.models import User


def home(request):
    users = User.objects.all()
    return render(request,
                  'listings/home.html',
                  {'users': users},
                  )


def button(request):
    return render(request,
                  'listings/button.html',
                  )
