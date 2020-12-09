from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'description', 'data']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'title',

            }),
            'description': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'description',
                
            }),
            'data': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата',
                'type': 'date',
                


                
            }),
            

            
        }