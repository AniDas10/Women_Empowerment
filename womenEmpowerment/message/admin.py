from django.contrib import admin
from .models import Message, Feedback, Comment
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver')
    
    def get_ordering(self, request):
        return ['id']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver')
    
    def get_ordering(self, request):
        return ['id']

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone')
    
    def get_ordering(self, request):
        return ['id']

admin.site.register(Message, MessageAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Feedback, FeedbackAdmin)