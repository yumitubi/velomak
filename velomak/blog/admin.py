from django.contrib import admin
from velomak.blog.models import Posts, Category, Tags

class PollAdmin(admin.ModelAdmin):
    # ...
    list_display = ('header', 'flag_enabled')

class CategAdmin(admin.ModelAdmin):
    list_display = ('categ', 'enabled', 'weight')

admin.site.register(Posts, PollAdmin)
admin.site.register(Category, CategAdmin)
admin.site.register(Tags)
# admin.site.register(Comments)
