from django import forms

class CurrencyConversionForm(forms.Form):
    source_currency = forms.CharField(max_length=3)
    target_currency = forms.CharField(max_length=3)
    amount = forms.DecimalField(max_digits=10, decimal_places=2)