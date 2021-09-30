from django import forms


class MoneyForm(forms.Form):
    spent = forms.IntegerField()
    get_money = forms.IntegerField()
