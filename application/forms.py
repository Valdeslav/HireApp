from django import forms


# form for edit product
class CreateProdForm(forms.Form):
    name = forms.CharField(label="Название")
    cost = forms.FloatField(label="Цена", min_value=1, max_value=10000)


class UpdateProdForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput)
    name = forms.CharField(label="Название")
    cost = forms.FloatField(label="Цена", min_value=1, max_value=10000)