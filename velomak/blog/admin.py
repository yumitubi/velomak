from django.contrib import admin
from velomak.blog.models import Posts, Category, Tags, Files, Section, Comms


class PollAdmin(admin.ModelAdmin):
    list_display = ('header', 'flag_enabled', 'section')
    fields = [
        'header',
        'prepost',
        'post',
        'date_pub',
        'tags',
        'categories',
        'flag_enabled',
        'not_publicate_main',
        'section'
    ]


class CategAdmin(admin.ModelAdmin):
    list_display = ('categ', 'enabled', 'weight')


class FilesAdmin(admin.ModelAdmin):
    list_display = ('title')


class SectionAdmin(admin.ModelAdmin):
    list_display = ('section', 'enabled')


class CommsAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'email',
        'post',
        'message',
        'datatime',
        'delete')


admin.site.register(Posts, PollAdmin)
admin.site.register(Category, CategAdmin)
admin.site.register(Tags)
admin.site.register(Section, SectionAdmin)
admin.site.register(Files)
admin.site.register(Comms, CommsAdmin)
