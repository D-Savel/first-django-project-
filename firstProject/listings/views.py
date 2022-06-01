from collections import UserList
from django.shortcuts import render
from django.shortcuts import redirect
from listings.models import User
from listings.models import Project
from listings.forms import UserForm
from django.contrib import messages
import requests
import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()


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


def geoapi(request):

    ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
    # use api with your ip Address for retrieve geodata
    response = requests.get('http://ip-api.com/json/%s' % ip_address)
    geodata = response.json()
    lat = geodata['lat']
    lon = geodata['lon']
    API_KEY = env("API_KEY")
    # prepare url for display a map with api
    # API use api-key given by locationiq
    # API_KEY must be save in .env file at the root of the project (same as settings.py)
    # API_KEY=<YOUR_API_KEY> (without '')
    url = f"""https://maps.locationiq.com/v3/staticmap?key={API_KEY}&center=43.66,3.9726&size=800x800&zoom=13&markers=size:small|color:red|{lat},{lon}"""

    return render(request, 'listings/geoapi.html', {
        'ip': geodata['query'],
        'country': geodata['country'],
        'latitude': geodata['lat'],
        'longitude': geodata['lon'],
        'city': geodata['city'],
        'url': url
    })
