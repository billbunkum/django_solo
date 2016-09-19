from django.contrib import admin

from .models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
	display = ('name', 'created', 'bio', 'github_url',)

admin.site.register(Student, StudentAdmin)