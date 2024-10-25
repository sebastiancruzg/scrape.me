from django import forms

class ScrapeForm(forms.Form):
    search_query = forms.CharField(min_length=4, max_length=100, required=True)
    resource_tag = forms.CharField(required=True)
