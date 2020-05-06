from django.contrib import admin
from movie.models import *

# Register your models here.
admin.site.register(Movie)
admin.site.register(User)
admin.site.register(Comment)