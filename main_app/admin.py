from django.contrib import admin
from .models import Task, Manager, TeamMember, Project
# Register your models here.
admin.site.register(Manager)
admin.site.register(TeamMember)
admin.site.register(Task)
admin.site.register(Project)