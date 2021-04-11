from django.shortcuts import render
from .models import Operation, User


def index(request):
    return render(request, 'index.html')


def postOperations(request):

    info = ''
    if request.method == 'POST':
        form = request.POST
        if form.is_valid():
            queryset = User.objects.filter(nfc_code=form.get('nfc_code'))
            if queryset:
                user = queryset.first()
                Operation.objects.create(user=user, mass=form.get('mass'), trash_type=form.get('trash_type'))
                info = 'Операция выполнена'
            else:
                info = 'Ошибка идентификации'
        else:
            info = 'Invalid form'
    return render(request, 'postOperations.html', {'info': info})
