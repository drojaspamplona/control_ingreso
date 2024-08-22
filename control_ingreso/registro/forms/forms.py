from django import forms
from registro.models import Employee, Visitor, Attendance

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'document_id', 'area']
        widgets = {
            'area': forms.Select(),
        }

class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['name', 'document_id']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['employee', 'visitor', 'check_out', 'reason_for_leaving_early']
        widgets = {
            'check_out': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'reason_for_leaving_early': forms.TextInput(attrs={'placeholder': 'Razón para salida temprana'})
        }
