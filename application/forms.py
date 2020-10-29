from django import forms


# form for edit product
class CreateProdForm(forms.Form):
    name = forms.CharField(label="Название")
    cost = forms.FloatField(label="Цена")


class UpdateProdForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput)
    name = forms.CharField(label="Название")
    cost = forms.FloatField(label="Цена")