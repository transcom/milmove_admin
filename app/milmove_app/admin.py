# -*- coding: utf-8 -*-
import inspect
import sys

from django.contrib import admin

from .models import *  # noqa


class MilmoveModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Moves)
class MovesAdmin(MilmoveModelAdmin):
    ordering = ["-created_at"]
    date_hierarchy = "created_at"
    list_filter = ("selected_move_type", "status")
    list_display = ("locator", "orders", "selected_move_type", "status", "created_at")
    readonly_fields = ("id", "locator", "created_at", "updated_at")
    fields = (
        "id",
        "locator",
        "orders",
        "selected_move_type",
        "status",
        "cancel_reason",
        "created_at",
        "updated_at",
    )


# Keep this at the bottom of the file after all other ModelAdmins have been registered
clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)

for clsname, cls in clsmembers:
    if issubclass(cls, models.Model) and not admin.site.is_registered(cls):
        admin.site.register(cls, MilmoveModelAdmin)
