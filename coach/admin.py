from django.contrib import admin

# Register your models here.

from .models import coach, session, exercise, category, difficulty, task, salle

admin.site.register(coach)
admin.site.register(session)
admin.site.register(exercise)
admin.site.register(category)
admin.site.register(difficulty)
admin.site.register(task)
admin.site.register(salle)