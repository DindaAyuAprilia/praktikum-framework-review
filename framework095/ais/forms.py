from django import forms
from .models.students import Students  # Impor kelas model secara langsung

class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students  # Gunakan kelas model, bukan modul
        fields = '__all__'
