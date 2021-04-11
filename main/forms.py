from django import forms


class OperationForm(forms.Form):

    mass = forms.CharField(max_length=255)
    trash_type = forms.CharField(max_length=255)
    nfc_code = forms.CharField(max_length=255)
