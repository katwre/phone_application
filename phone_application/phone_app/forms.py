 
from phone_application.phone_app.widgets import *
from django import forms


class ProductForm(forms.Form):
  key = forms.CharField(max_length=400, widget=MyTypeaheadWidget(),help_text="")

  def clean(self):
    cleaned_data = self.cleaned_data
    desk = cleaned_data.get("key")
    if len(key)==0:
	raise forms.ValidationError("Invalid key!")
    return cleaned_data