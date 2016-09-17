from django.contrib import admin
from tasks.models import Task, TaskOutput, TaskType, Unit

admin.site.register(Task)
admin.site.register(TaskOutput)
admin.site.register(TaskType)
admin.site.register(Unit)
