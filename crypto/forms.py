from django import forms


class CalculatorForm(forms.Form):
    price_1 = forms.FloatField(label='price_1', widget=forms.NumberInput(attrs={'placeholder': "Ціна"}))
    value_1 = forms.FloatField(label='value_1', widget=forms.NumberInput(attrs={'placeholder': "Кількість"}))
    price_2 = forms.FloatField(label='price_2', widget=forms.NumberInput(attrs={'placeholder': "Ціна"}))
    value_2 = forms.FloatField(label='value_2', widget=forms.NumberInput(attrs={'placeholder': "Кількість"}))
