from django import forms

class DateForm(forms.Form):
    month = forms.IntegerField(min_value=1, max_value=31)
    year = forms.IntegerField(min_value=0)