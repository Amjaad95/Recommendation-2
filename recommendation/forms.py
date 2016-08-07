from django import forms
from django.forms import ModelForm
from .models import Recommendation
from django.contrib.auth.models import User



class RecommendationForm(ModelForm):
    class Meta:
        model = Recommendation
        fields = ['description', 'image', 'category']