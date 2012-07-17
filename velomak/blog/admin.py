from django.contrib import admin
from velomak.blog.models import Posts, Category # , Comments

class PollAdmin(admin.ModelAdmin):
    # ...
    list_display = ('header', )

admin.site.register(Posts, PollAdmin)
admin.site.register(Category)
# admin.site.register(Comments)
