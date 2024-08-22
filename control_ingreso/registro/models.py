from django.db import models

class Area(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre del Área')

    class Meta:
        db_table = 'hr.areas'
        verbose_name = 'Área'
        verbose_name_plural = 'Áreas'

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Nombre')
    last_name = models.CharField(max_length=100, verbose_name='Apellido')
    document_id = models.CharField(max_length=20, verbose_name='Número de Documento')
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name='Área')

    class Meta:
        db_table = 'hr.employees'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Visitor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    document_id = models.CharField(max_length=20, verbose_name='Número de Documento')

    class Meta:
        db_table = 'logs.visitors'
        verbose_name = 'Visitante'
        verbose_name_plural = 'Visitantes'

    def __str__(self):
        return self.name

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Empleado')
    visitor = models.ForeignKey(Visitor, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Visitante')
    check_in = models.DateTimeField(auto_now_add=True, verbose_name='Hora de Entrada')
    check_out = models.DateTimeField(null=True, blank=True, verbose_name='Hora de Salida')
    reason_for_leaving_early = models.CharField(max_length=100, null=True, blank=True, verbose_name='Razón de Salida Temprana')

    class Meta:
        db_table = 'logs.attendances'
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'

    def __str__(self):
        if self.employee:
            return f"{self.employee} - {self.check_in}"
        if self.visitor:
            return f"{self.visitor} - {self.check_in}"
        return f"Check-in at {self.check_in}"
