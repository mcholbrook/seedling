from django.contrib import admin
from .models import Profile, Seed, Note, Conversation, Message, Todo, Garden
# Register your models here.
admin.site.register(Profile)
admin.site.register(Seed)
admin.site.register(Note)
admin.site.register(Conversation)
admin.site.register(Message)
admin.site.register(Todo)
admin.site.register(Garden)