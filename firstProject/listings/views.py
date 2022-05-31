from collections import UserList
from django.shortcuts import render
from django.shortcuts import redirect
from listings.models import User
from listings.models import Project
from listings.forms import UserForm
from django.contrib import messages

usersLength = len(User.objects.all())


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


def addUser(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(
                request, f"""L'utilisateur {user.firstName} {user.lastName} a été crée.""")
            return redirect('userDetail', user.id)
    else:
        form = UserForm()

    return render(request,
                  'listings/addUser.html',
                  {'form': form})


def userUpdate(request, id):
    user = User.objects.get(id=id)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            messages.success(
                request, f"""L'utilisateur {user.firstName} {user.lastName} a été mis a jour.""")
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('userDetail', user.id)
    else:
        form = UserForm(instance=user)

    return render(request,
                  'listings/userUpdate.html',
                  {'form': form})


def userDelete(request, id):
    user = User.objects.get(id=id)

    if request.method == 'POST':
        user.delete()
        messages.info(
            request, f"""L'utilisateur {user.firstName} {user.lastName} a été supprimé.""")
        return redirect('home')
    return render(request,
                  'listings/userDelete.html',
                  {'user': user})
