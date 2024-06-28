from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = ["nombrep","correop","mensajep"]
        
class PaymentForm(forms.Form):
    amount = forms.DecimalField(label='Monto', initial=499980)  # Valor preestablecido de 100.0
    session_id = forms.CharField(label='ID de Sesión', initial='1')
    buy_order = forms.CharField(label='Orden de Compra', initial='asdfasda231')