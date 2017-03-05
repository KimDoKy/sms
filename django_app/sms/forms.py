import re

from django import forms
from django.core.exceptions import ValidationError


class SMSForm(forms.Form):
    recipient_numbers = forms.CharField(
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'size': '100',
            }
        )
    )
    content = forms.CharField(widget=forms.Textarea())

    def clean_recipient_numbers(self):
        cleaned_numbers = []
        error_numbers = []
        p = re.compile(r'^0\d{9}\d?$')
        number_string = self.cleaned_data['recipient_numbers']
        sub_string = re.sub(r'\s|-', '', number_string)
        numbers = re.split(r',|\.', sub_string)
        for number in numbers:
            if re.match(p, number):
                cleaned_numbers.append(number)
            else:
                error_numbers.append(number)

        if error_numbers:
            raise ValidationError('Invalid phone number format! {}'.format(', '.join(error_numbers)))

        return cleaned_numbers

    # def clean_content(self):
    #     content_string = self.cleaned_data['content']
    #     # if len(content_string) >= 200:
    #     #     print("200자 이하로 작성해주세요")
    #     # else:
    #     #     return content_string
    #     return content_string
