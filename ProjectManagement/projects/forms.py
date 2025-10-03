from django import forms
from tempus_dominus.widgets import DatePicker
from projects.models import Project


class ProjectForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 3, 'placeholder': "Describe your project here..."}
        ),
        label="Project Description",
        required=True
    )
    start_date = forms.DateTimeField(
        widget=DatePicker(
            attrs={
                'append': 'fa fa-calender'
            }
        )
    )
    class Meta: 
        model = Project
        fields = ['name', 'owner','team', 'description', 'status','priority','start_date', 'due_date']

