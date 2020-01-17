# -*- coding: utf-8 -*-
import inspect
import sys

from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import *  # noqa

# Special-case verbose names
Addresses._meta.verbose_name = "address"
Addresses._meta.verbose_name_plural = "addresses"

# Special-case string representations
DutyStations.__str__ = lambda self: self.name
Moves.__str__ = lambda self: self.locator
Orders.__str__ = lambda self: self.orders_number
PersonallyProcuredMoves.__str__ = (
    lambda self: f"{self.pickup_postal_code} to {self.destination_postal_code}"
)
ServiceMembers.__str__ = lambda self: " ".join(
    filter(
        None,
        (
            self.last_name + "," if self.last_name else ",",
            self.first_name,
            self.middle_name,
        ),
    )
)
Tariff400NgZip3S.__str__ = (
    lambda self: f"{self.zip3}: {self.basepoint_city}, {self.state}"
)


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
    list_display = (
        "locator",
        "orders_link",
        "selected_move_type",
        "status",
        "created_at",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "id",
                    "locator",
                    "orders_link",
                    "selected_move_type",
                    "status",
                    "cancel_reason",
                    "show",
                )
            },
        ),
        ("Timestamps", {"fields": ("created_at", "updated_at",)}),
    )

    def orders_link(self, obj):
        return mark_safe(
            '<a href="{}">{}</a>'.format(
                reverse("admin:milmove_app_orders_change", args=(obj.orders.pk,)),
                obj.orders,
            )
        )

    orders_link.short_description = "orders"
    orders_link.admin_order_field = "orders__orders_number"


@admin.register(Orders)
class OrdersAdmin(MilmoveModelAdmin):
    ordering = ["-created_at"]
    date_hierarchy = "created_at"
    list_filter = ("status",)
    list_display = (
        "orders_number",
        "service_member_link",
        "new_duty_station_link",
        "status",
        "created_at",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "id",
                    "orders_number",
                    "service_member_link",
                    "orders_type",
                    "new_duty_station_link",
                    "issue_date",
                    "report_by_date",
                    "status",
                    "has_dependents",
                    "uploaded_orders_link",
                    "orders_type_detail",
                    "tac",
                    "department_indicator",
                    "spouse_has_pro_gear",
                    "sac",
                )
            },
        ),
        ("Timestamps", {"fields": ("created_at", "updated_at",)}),
    )

    def service_member_link(self, obj):
        return mark_safe(
            '<a href="{}">{}</a>'.format(
                reverse(
                    "admin:milmove_app_servicemembers_change",
                    args=(obj.service_member.pk,),
                ),
                obj.service_member,
            )
        )

    service_member_link.short_description = "service member"
    service_member_link.admin_order_field = "service_member__last_name"

    def new_duty_station_link(self, obj):
        return mark_safe(
            '<a href="{}">{}</a>'.format(
                reverse(
                    "admin:milmove_app_dutystations_change",
                    args=(obj.new_duty_station.pk,),
                ),
                obj.new_duty_station,
            )
        )

    new_duty_station_link.short_description = "new duty station"
    new_duty_station_link.admin_order_field = "new_duty_station__name"

    def uploaded_orders_link(self, obj):
        return mark_safe(
            '<a href="{}">{}</a>'.format(
                reverse(
                    "admin:milmove_app_documents_change", args=(obj.uploaded_orders.pk,)
                ),
                obj.uploaded_orders,
            )
        )

    uploaded_orders_link.short_description = "uploaded orders"


# Keep this at the bottom of the file after all other ModelAdmins have been registered
clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)

for clsname, cls in clsmembers:
    if issubclass(cls, models.Model) and not admin.site.is_registered(cls):
        admin.site.register(cls, MilmoveModelAdmin)
