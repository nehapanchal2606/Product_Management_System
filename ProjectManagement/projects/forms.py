from django import forms
from tempus_dominus.widgets import DatePicker
from projects.models import Project
from django.contrib.auth.models import User


class ProjectForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 3, 'placeholder': "Describe your project here..."}
        ),
        label=False,
        required=True
    )

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': "Enter the name of your project here ..."}
        ),
        required=True,
        label=False
    )

    start_date = forms.DateTimeField(
        widget=DatePicker(
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle' : True,
            }
        )
    )
    due_date = forms.DateTimeField(
        widget=DatePicker(
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle' : True,
            }
        )
    )
    class Meta: 
        model = Project
        fields = ['name', 'owner','team', 'description', 'client_company','status','priority','start_date', 'due_date']

