from django.shortcuts import render
from .models import Operation, User, Trash
from django.utils.crypto import get_random_string


def index(request):
    return render(request, 'index.html')


def postOperations(request):

    info = ''
    new_password = ''
    if request.method == 'POST':
        form = request.POST

        queryset = User.objects.filter(nfc_code=form.get('nfc_code'))
        if queryset and Trash.objects.filter(password=form.get('trashPassword')):
            user = queryset.first()
            Operation.objects.create(user=user, mass=form.get('mass'), trash_type=form.get('trash_type'))
            info = 'Операция выполнена'
            Trash.objects.filter(password=form.get('trashPassword')).update(password=new_password)
            new_password = get_random_string(length=32)
        else:
            info = 'Ошибка идентификации'

    return render(request, 'postOperations.html', {'new_password': new_password, 'info': info})
