from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from .models import Employee, Visitor, Attendance
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from registro.forms.forms import EmployeeForm, VisitorForm, AttendanceForm
from django.db.models import Sum, F, ExpressionWrapper, DurationField
from django.contrib import messages

@login_required
def home_view(request):
    return render(request, 'home.html')

@login_required
def register_entry_view(request):
    return render(request, 'register_entry.html')

class SignupView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('home') 
        return render(request, 'registration/signup.html', {'form': form})
    
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee/employee_list.html', {'employees': employees})

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees')
    else:
        form = EmployeeForm()
    
    return render(request, 'employee/employee_form.html', {'form': form})

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee/employee_form.html', {'form': form})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, 'Empleado eliminado exitosamente.')
        return redirect('employees')
    return render(request, 'employee/employee_confirm_delete.html', {'employee': employee})

# Visitantes/Proveedores CRUD
@login_required
def visitor_list(request):
    visitors = Visitor.objects.all()
    return render(request, 'visitors/visitor_list.html', {'visitors': visitors})

def visitor_create(request):
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visitors')
    else:
        form = VisitorForm()
    return render(request, 'visitors/visitor_form.html', {'form': form})

def visitor_update(request, pk):
    visitor = get_object_or_404(Visitor, pk=pk)
    if request.method == 'POST':
        form = VisitorForm(request.POST, instance=visitor)
        if form.is_valid():
            form.save()
            return redirect('visitors')
    else:
        form = VisitorForm(instance=visitor)
    return render(request, 'visitors/visitor_form.html', {'form': form})

def visitor_delete(request, pk):
    visitor = get_object_or_404(Visitor, pk=pk)
    if request.method == 'POST':
        visitor.delete()
        messages.success(request, 'Visitante eliminado exitosamente.', extra_tags='success')
        return redirect('visitors')
    return render(request, 'visitors/visitor_confirm_delete.html', {'visitor': visitor})

# Reportes
def attendance_report(request):
    report_type = request.GET.get('report_type', 'employees')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if report_type == 'employees':
        if start_date and end_date:
            attendances = Attendance.objects.filter(employee__isnull=False, check_in__date__range=[start_date, end_date])
        else:
            attendances = Attendance.objects.filter(employee__isnull=False)
    elif report_type == 'visitors':
        if start_date and end_date:
            attendances = Attendance.objects.filter(visitor__isnull=False, check_in__date__range=[start_date, end_date])
        else:
            attendances = Attendance.objects.filter(visitor__isnull=False)

    # Calculate total hours
    total_hours = attendances.annotate(
        duration=ExpressionWrapper(F('check_out') - F('check_in'), output_field=DurationField())
    ).aggregate(total_duration=Sum('duration'))

    # Calculate duration for each attendance
    for attendance in attendances:
        if attendance.check_out:
            duration = attendance.check_out - attendance.check_in
            attendance.duration = duration
        else:
            attendance.duration = None

    return render(request, 'attendance/attendance_report.html', {
        'attendances': attendances,
        'total_hours': total_hours['total_duration'],
    })
def evacuation_report(request):
    current_time = timezone.now()
    employees_inside = Attendance.objects.filter(employee__isnull=False, check_out__isnull=True).count()
    visitors_inside = Attendance.objects.filter(visitor__isnull=False, check_out__isnull=True).count()
    total_inside = employees_inside + visitors_inside

    return render(request, 'attendance/evacuation_report.html', {
        'employees_inside': employees_inside,
        'visitors_inside': visitors_inside,
        'total_inside': total_inside,
        'current_time': current_time,
    })
