from django import forms
from datetime import datetime


now = datetime.now()

TYPE_CHOICE = (
    ('capex', 'Capex'),
    ('opex', 'Opex'),
)

MONTH_CHOICE = (
    (1, 'January'),
    (2, 'February'),
    (3, 'March'),
    (4, 'April'),
    (5, 'May'),
    (6, 'June'),
    (7, 'July'),
    (8, 'August'),
    (9, 'September'),
    (10, 'October'),
    (11, 'November'),
    (12, 'December'),
)

class DateForm(forms.Form):
    month = forms.ChoiceField(choices=MONTH_CHOICE, label="Month",
            initial=TYPE_CHOICE[0][0])
    year = forms.IntegerField(min_value=0, initial=int(now.strftime("%Y")))
    type = forms.ChoiceField(choices=TYPE_CHOICE, label="Type",
            initial=TYPE_CHOICE[0][0])

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=200)