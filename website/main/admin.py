from django.contrib import admin


# Register your models here.
from.models import Student

class StudentAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "firstname","email", "timestamp"]
	list_filter = ["timestamp"]
	search_fields = ["firstname","lastname","username","country","email"]

	class Meta:
		model = Student


admin.site.register(Student, StudentAdmin)