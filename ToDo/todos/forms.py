from django import forms

from .models import Tasks

class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=100, label="Title", widget=forms.TextInput(attrs={'class': 'text-black mt-1 text-2xl block w-full rounded-md border-orange-300 shadow-sm focus:border-pink-400 focus:ring focus:ring-pink-200'}))
    description = forms.CharField(
        widget=forms.Textarea(attrs={"class": " text-black mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-400 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"}
        ),
        label="Description")
    priority = forms.IntegerField(label="Priority", widget=forms.NumberInput(attrs={'class': 'text-black mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-400 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'}))
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'priority']