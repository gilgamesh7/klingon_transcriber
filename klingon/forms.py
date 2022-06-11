from django import forms

class InputKlingonForm(forms.Form):
    input_klingon = forms.CharField(label="Enter Klingon Text", max_length=255, initial=' ')