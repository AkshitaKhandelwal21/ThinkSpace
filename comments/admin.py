from django.contrib import admin

from .models import Comment

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ('post','content')
    actions = ['approve_comments']

    # def approve_comments(self, request, queryset):
    #     queryset.update(is_approved=True)

admin.site.register(Comment, CommentAdmin)
