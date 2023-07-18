from django.contrib import admin
from Petstagram.accounts.models import PetstagramUser

# Register your models here.


class PetstagramUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')


admin.site.register(PetstagramUser, PetstagramUserAdmin)
