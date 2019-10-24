# -*- coding: utf-8 -*-
import inspect
import sys

from django.contrib import admin

from .models import *  # noqa

clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)

for clsname, cls in clsmembers:
    if clsname not in ["Moves"]:
        admin.site.register(cls)


@admin.register(Moves)
class MovesAdmin(admin.ModelAdmin):
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
