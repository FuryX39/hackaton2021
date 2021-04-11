from django.shortcuts import render
from .forms import OperationForm
from .models import Operation, User


def index(request):
    return render(request, 'index.html')


def postOperations(request):

    info = ''
    if request.method == 'POST':
        form = OperationForm(request.POST)
        if form.is_valid():
            queryset = User.objects.filter(nfc_code=form.nfc_code)
            if queryset:
                user = queryset.first()
                Operation.objects.create(user=user, mass=form.mass, trash_type=form.trash_type)
                info = 'Операция выполнена'
            else:
                info = 'Ошибка идентификации'
    return render(request, 'postOperations.html', {'info': info})
