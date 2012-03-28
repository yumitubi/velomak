from django.contrib import admin
from velomak.blog.models import Posts, Category # , Comments

admin.site.register(Posts)
admin.site.register(Category)
# admin.site.register(Comments)
