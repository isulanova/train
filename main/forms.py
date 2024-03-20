from django import forms

from main.models import images_data

class DogImgForm(forms.Form):
    class Meta:
        model = images_data
        fields = ("image",)

    image = forms.ImageField(required=False)