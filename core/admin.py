from django.contrib import admin

from core.models import Member, Settings, Cluster

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ('type', 'user', 'created_at', 'updated_at')
    list_per_page = 25
    list_select_related = True


class SettingsAdmin(admin.ModelAdmin):
    list_display = ('member', 'type', 'key', 'label', 'value', 'created_at', 'updated_at')
    list_per_page = 25
    list_select_related = True


class ClusterAdmin(admin.ModelAdmin):
    list_display = ('parent', 'name', 'type', 'created_at', 'updated_at')
    list_per_page = 25
    list_select_related = True

admin.site.register(Member, MemberAdmin)
admin.site.register(Settings, SettingsAdmin)
admin.site.register(Cluster, ClusterAdmin)
