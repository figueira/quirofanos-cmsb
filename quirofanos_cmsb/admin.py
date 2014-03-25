from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from quirofanos_cmsb.models import Cuenta

class CuentaInline(admin.StackedInline):
    model = Cuenta
    can_delete = False
    verbose_name_plural = 'cuenta'

class UserAdmin(UserAdmin):
    inlines = (CuentaInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)