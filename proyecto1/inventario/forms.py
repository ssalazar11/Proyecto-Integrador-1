from django.forms import ModelForm
from .models import producto

class productoForm(ModelForm):
    class Meta:
        model = producto
        fields = '__all__'