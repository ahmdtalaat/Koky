from django.forms import ModelForm, TextInput
from microurl.models import MicroUrl


class URLform(ModelForm):
    def __init__(self, *args, **kwargs):
        super(URLform, self).__init__(*args, **kwargs)
        self.fields['longurl'].widget.attrs['style'] = "width:500px"
        self.fields['longurl'].label = False

    class Meta:
        model = MicroUrl
        fields = ['longurl']
        widgets = {
            "longurl": TextInput(attrs={'class': 'input', 'placeholder': 'Enter a url'})
        }
