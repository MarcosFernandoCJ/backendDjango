from django import forms
from .models import Roles, Users, UserRoles

class AssignRoleForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=Users.objects.all(), label="Select User")
    role = forms.ModelChoiceField(queryset=Roles.objects.all(), label="Select Role")
    
    class Meta:
        model = UserRoles
        fields = ['user', 'role']
