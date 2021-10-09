from django import forms
from django.contrib.admin import widgets


ENCODING_TYPES = [
    ('choose', 'Choose Type'),
    ('hex', 'Hexidecimal'),
    ('bin', 'Binary'),
    ('ascii', 'ascii'),
]

DIRECTION = [
    ('encode', 'Encode'),
    ('decode', 'Decode'),
]



class EncodeForm(forms.Form):
  
    option = forms.CharField(widget=forms.RadioSelect(choices=DIRECTION))
    input_type = forms.CharField(label='Input', required=True, widget=forms.Select(choices=ENCODING_TYPES))
    output_type = forms.CharField(label='Output', required=True, widget=forms.Select(choices=ENCODING_TYPES))
    input_text = forms.CharField(widget=forms.Textarea, required=True)
    #output = forms.CharField(widget=forms.Textarea)

    def clean(self):
        data = super().clean()
        field_name = 'input_type'
        field_name_2 = 'output_type'
        field_name_3 = 'input_text'
        field_value = self.cleaned_data[field_name]
        field_value_2 = self.cleaned_data[field_name_2]
        field_value_3 = self.cleaned_data[field_name_3]


        if field_value_2 == field_value:
            raise forms.ValidationError('Check entry. Input choices must be different')

        elif field_value == 'choose' or field_value == 'choose':
            raise forms.ValidationError('Check entry. No input type chosen')

        elif field_value_2 == 'choose' or field_value == 'choose':
            raise forms.ValidationError('Check entry. No output type chosen')

        return data

    
