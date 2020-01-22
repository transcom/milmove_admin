# -*- coding: utf-8 -*-
import inspect
import sys
from dataclasses import dataclass

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

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


@dataclass
class LinkField:
    field_name: str
    admin_order_field: str = None
    short_description: str = None
    func_name: str = None


# Inspired by https://stackoverflow.com/a/46527083
class RelatedObjectLinkMixin(object):
    """
    Mixin for ModelAdmins to include a "link_fields" option.  This should be set to a tuple of related model
    fields in which you want to generate a special "<field>_link" callable that would show the string
    representation of the related object that is linked to that object's change page in the admin.

    As show below, each link field can either be:
      1) a field name -- the field can be a link by using <field>_link in the field list, but it will
         get a default label and won't be sortable.
      2) a LinkField object -- in addition to the field name, you can also optionally pass in a field
         to use for ordering, a short description, and even change the "<field>_link" name.

    Example:
        link_fields = (
            "uploaded_orders",
            LinkField("service_member", "service_member__last_name"),
        )
        list_display = [..., 'service_member_link', ...]
        fields = [..., 'uploaded_orders_link', ...]
    """

    link_fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.link_fields:
            for link_fields_item in self.link_fields:
                admin_order_field = func_name = None
                if isinstance(link_fields_item, LinkField):
                    field_name = link_fields_item.field_name
                    admin_order_field = link_fields_item.admin_order_field
                    short_description = (
                        link_fields_item.short_description
                        or field_name.replace("_", " ")
                    )
                    func_name = link_fields_item.func_name
                else:
                    field_name = short_description = link_fields_item

                if not func_name:
                    func_name = field_name + "_link"
                setattr(
                    self,
                    func_name,
                    self._generate_link_func(
                        field_name, admin_order_field, short_description
                    ),
                )

    def _generate_link_func(self, field_name, admin_order_field, short_description):
        def _func(obj):
            related_obj = getattr(obj, field_name)
            if not related_obj:
                return None
            url = reverse(
                f"admin:{related_obj._meta.app_label}_{related_obj._meta.model_name}_change",
                args=(related_obj.pk,),
            )
            return format_html('<a href="{}">{}</a>', url, related_obj)

        _func.short_description = short_description
        if admin_order_field:
            _func.admin_order_field = admin_order_field

        return _func


class MilmoveModelAdmin(RelatedObjectLinkMixin, admin.ModelAdmin):
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
    link_fields = (LinkField("orders", "orders__orders_number"),)
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


@admin.register(Orders)
class OrdersAdmin(MilmoveModelAdmin):
    ordering = ["-created_at"]
    date_hierarchy = "created_at"
    list_filter = ("status",)
    link_fields = (
        LinkField("service_member", "service_member__last_name"),
        LinkField("new_duty_station", "new_duty_station__name"),
        "uploaded_orders",
    )
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


# Keep this at the bottom of the file after all other ModelAdmins have been registered
clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)

for clsname, cls in clsmembers:
    if issubclass(cls, models.Model) and not admin.site.is_registered(cls):
        admin.site.register(cls, MilmoveModelAdmin)
