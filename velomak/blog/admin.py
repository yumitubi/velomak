from django.contrib import admin
from velomak.blog.models import Posts, Category, Tags, Files

class PollAdmin(admin.ModelAdmin):
    # ...
    list_display = ('header', 'flag_enabled')

class CategAdmin(admin.ModelAdmin):
    list_display = ('categ', 'enabled', 'weight')
    
class FilesAdmin(admin.ModelAdmin):
    list_display = ('title')

admin.site.register(Posts, PollAdmin)
admin.site.register(Category, CategAdmin)
admin.site.register(Tags)
admin.site.register(Files)
# admin.site.register(Comments)
