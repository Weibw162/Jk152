from django.contrib import admin

# Register your models here.

from .models import Per,Img,PerLike

class PerAdmin(admin.ModelAdmin):
    list_display = ["pk","username",'password']
class ImgAdmin(admin.ModelAdmin):
    list_display = ["pk","sn","like_num"]
class PerlikeAdmin(admin.ModelAdmin):
    list_display = ["pk","img","per"]


admin.site.register(Per, PerAdmin)
admin.site.register(Img,ImgAdmin)
admin.site.register(PerLike,PerlikeAdmin)