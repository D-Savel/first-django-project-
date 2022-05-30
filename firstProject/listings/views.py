from django.shortcuts import render
from listings.models import User
from listings.models import Project
from listings.forms import UserForm


def home(request):
    users = User.objects.all()
    projects = Project.objects.all()
    return render(request,
                  'listings/home.html',
                  {'users': users,
                   'projects': projects,
                   },
                  )


def button(request):
    return render(request,
                  'listings/button.html',
                  )


def userDetail(request, id):
    user = User.objects.get(id=id)
    return render(request,
                  'listings/userDetail.html',
                  {'user': user})
