# -*- coding: utf-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccessCodes(models.Model):
    id = models.UUIDField(primary_key=True)
    service_member = models.ForeignKey(
        "ServiceMembers",
        models.DO_NOTHING,
        related_name="access_codes_service_member",
        blank=True,
        null=True,
    )
    code = models.TextField(unique=True)
    move_type = models.TextField()
    created_at = models.DateTimeField()
    claimed_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "access_codes"
        verbose_name = "access code"


class Addresses(models.Model):
    id = models.UUIDField(primary_key=True)
    street_address_1 = models.CharField(max_length=255)
    street_address_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    street_address_3 = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "addresses"
        verbose_name = "addresse"


class AdminUsers(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey(
        "Users",
        models.DO_NOTHING,
        related_name="admin_users_user",
        blank=True,
        null=True,
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    organization = models.ForeignKey(
        "Organizations",
        models.DO_NOTHING,
        related_name="admin_users_organization",
        blank=True,
        null=True,
    )
    role = models.TextField()  # This field type is a guess.
    email = models.CharField(unique=True, max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deactivated = models.BooleanField()
    active = models.BooleanField()

    class Meta:
        managed = False
        db_table = "admin_users"
        verbose_name = "admin user"


class BackupContacts(models.Model):
    id = models.UUIDField(primary_key=True)
    service_member_id = models.UUIDField()
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    permission = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "backup_contacts"
        verbose_name = "backup contact"


class ClientCerts(models.Model):
    id = models.UUIDField(primary_key=True)
    sha256_digest = models.CharField(max_length=64, blank=True, null=True)
    subject = models.TextField(blank=True, null=True)
    allow_dps_auth_api = models.BooleanField(blank=True, null=True)
    allow_orders_api = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    allow_air_force_orders_read = models.BooleanField()
    allow_air_force_orders_write = models.BooleanField()
    allow_army_orders_read = models.BooleanField()
    allow_army_orders_write = models.BooleanField()
    allow_coast_guard_orders_read = models.BooleanField()
    allow_coast_guard_orders_write = models.BooleanField()
    allow_marine_corps_orders_read = models.BooleanField()
    allow_marine_corps_orders_write = models.BooleanField()
    allow_navy_orders_read = models.BooleanField()
    allow_navy_orders_write = models.BooleanField()
    allow_prime = models.BooleanField()

    class Meta:
        managed = False
        db_table = "client_certs"
        verbose_name = "client cert"


class ContractingOfficers(models.Model):
    id = models.UUIDField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "contracting_officers"
        verbose_name = "contracting officer"


class Contractor(models.Model):
    id = models.UUIDField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    name = models.CharField(max_length=80)
    contract_number = models.CharField(unique=True, max_length=80)
    type = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = "contractor"
        verbose_name = "contractor"


class Customers(models.Model):
    id = models.UUIDField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.OneToOneField(
        "Users", models.DO_NOTHING, related_name="customers_user", blank=True, null=True
    )
    dod_id = models.TextField()
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    agency = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    current_address = models.ForeignKey(
        Addresses,
        models.DO_NOTHING,
        related_name="customers_current_address",
        blank=True,
        null=True,
    )
    destination_address = models.ForeignKey(
        Addresses,
        models.DO_NOTHING,
        related_name="customers_destination_address",
        blank=True,
        null=True,
    )

    class Meta:
        managed = False
        db_table = "customers"
        verbose_name = "customer"


class DistanceCalculations(models.Model):
    id = models.UUIDField(primary_key=True)
    origin_address = models.ForeignKey(
        Addresses,
        models.DO_NOTHING,
        related_name="distance_calculations_origin_address",
    )
    destination_address = models.ForeignKey(
        Addresses,
        models.DO_NOTHING,
        related_name="distance_calculations_destination_address",
    )
    distance_miles = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "distance_calculations"
        verbose_name = "distance calculation"


class Documents(models.Model):
    id = models.UUIDField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    service_member = models.ForeignKey(
        "ServiceMembers", models.DO_NOTHING, related_name="documents_service_member"
    )
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "documents"
        verbose_name = "document"


class DpsUsers(models.Model):
    id = models.UUIDField(primary_key=True)
    login_gov_email = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deactivated = models.BooleanField()
    active = models.BooleanField()

    class Meta:
        managed = False
        db_table = "dps_users"
        verbose_name = "DPS user"


class DutyStationNames(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.TextField(unique=True)
    duty_station = models.ForeignKey(
        "DutyStations",
        models.DO_NOTHING,
        related_name="duty_station_names_duty_station",
    )
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "duty_station_names"
        verbose_name = "duty station name"


class DutyStations(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    affiliation = models.CharField(max_length=255)
    address = models.ForeignKey(
        Addresses, models.DO_NOTHING, related_name="duty_stations_address"
    )
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    transportation_office = models.ForeignKey(
        "TransportationOffices",
        models.DO_NOTHING,
        related_name="duty_stations_transportation_office",
        blank=True,
        null=True,
    )

    class Meta:
        managed = False
        db_table = "duty_stations"
        verbose_name = "duty station"


class ElectronicOrders(models.Model):
    id = models.UUIDField(primary_key=True)
    orders_number = models.CharField(max_length=255)
    edipi = models.CharField(max_length=255)
    issuer = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "electronic_orders"
        unique_together = (("issuer", "orders_number"),)
        verbose_name = "electronic order"


class ElectronicOrdersRevisions(models.Model):
    id = models.UUIDField(primary_key=True)
    electronic_order = models.ForeignKey(
        ElectronicOrders,
        models.DO_NOTHING,
        related_name="electronic_orders_revisions_electronic_order",
    )
    seq_num = models.IntegerField()
    given_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    family_name = models.CharField(max_length=255)
    name_suffix = models.CharField(max_length=255, blank=True, null=True)
    affiliation = models.CharField(max_length=255)
    paygrade = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255)
    date_issued = models.DateTimeField()
    no_cost_move = models.BooleanField()
    tdy_en_route = models.BooleanField()
    tour_type = models.CharField(max_length=255)
    orders_type = models.CharField(max_length=255)
    has_dependents = models.BooleanField()
    losing_uic = models.CharField(max_length=255, blank=True, null=True)
    losing_unit_name = models.CharField(max_length=255, blank=True, null=True)
    losing_unit_city = models.CharField(max_length=255, blank=True, null=True)
    losing_unit_locality = models.CharField(max_length=255, blank=True, null=True)
    losing_unit_country = models.CharField(max_length=255, blank=True, null=True)
    losing_unit_postal_code = models.CharField(max_length=255, blank=True, null=True)
    gaining_uic = models.CharField(max_length=255, blank=True, null=True)
    gaining_unit_name = models.CharField(max_length=255, blank=True, null=True)
    gaining_unit_city = models.CharField(max_length=255, blank=True, null=True)
    gaining_unit_locality = models.CharField(max_length=255, blank=True, null=True)
    gaining_unit_country = models.CharField(max_length=255, blank=True, null=True)
    gaining_unit_postal_code = models.CharField(max_length=255, blank=True, null=True)
    report_no_earlier_than = models.DateTimeField(blank=True, null=True)
    report_no_later_than = models.DateTimeField(blank=True, null=True)
    hhg_tac = models.CharField(max_length=255, blank=True, null=True)
    hhg_sdn = models.CharField(max_length=255, blank=True, null=True)
    hhg_loa = models.CharField(max_length=255, blank=True, null=True)
    nts_tac = models.CharField(max_length=255, blank=True, null=True)
    nts_sdn = models.CharField(max_length=255, blank=True, null=True)
    nts_loa = models.CharField(max_length=255, blank=True, null=True)
    pov_shipment_tac = models.CharField(max_length=255, blank=True, null=True)
    pov_shipment_sdn = models.CharField(max_length=255, blank=True, null=True)
    pov_shipment_loa = models.CharField(max_length=255, blank=True, null=True)
    pov_storage_tac = models.CharField(max_length=255, blank=True, null=True)
    pov_storage_sdn = models.CharField(max_length=255, blank=True, null=True)
    pov_storage_loa = models.CharField(max_length=255, blank=True, null=True)
    ub_tac = models.CharField(max_length=255, blank=True, null=True)
    ub_sdn = models.CharField(max_length=255, blank=True, null=True)
    ub_loa = models.CharField(max_length=255, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "electronic_orders_revisions"
        verbose_name = "electronic orders revision"


class Entitlements(models.Model):
    id = models.UUIDField(primary_key=True)
    dependents_authorized = models.BooleanField(blank=True, null=True)
    total_dependents = models.IntegerField(blank=True, null=True)
    non_temporary_storage = models.BooleanField(blank=True, null=True)
    privately_owned_vehicle = models.BooleanField(blank=True, null=True)
    storage_in_transit = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    authorized_weight = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "entitlements"
        verbose_name = "entitlement"


class FuelEiaDieselPrices(models.Model):
    id = models.UUIDField(primary_key=True)
    pub_date = models.DateField()
    rate_start_date = models.DateField()
    rate_end_date = models.DateField()
    eia_price_per_gallon_millicents = models.IntegerField()
    baseline_rate = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "fuel_eia_diesel_prices"
        verbose_name = "fuel EIA diesel price"


class InvoiceNumberTrackers(models.Model):
    standard_carrier_alpha_code = models.TextField(primary_key=True)
    year = models.IntegerField()
    sequence_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = "invoice_number_trackers"
        unique_together = (("standard_carrier_alpha_code", "year"),)
        verbose_name = "invoice number tracker"


class Invoices(models.Model):
    id = models.UUIDField(primary_key=True)
    status = models.CharField(max_length=255)
    invoiced_date = models.DateTimeField()
    invoice_number = models.CharField(unique=True, max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    approver = models.ForeignKey(
        "OfficeUsers", models.DO_NOTHING, related_name="invoices_approver"
    )
    upload = models.ForeignKey(
        "Uploads",
        models.DO_NOTHING,
        related_name="invoices_upload",
        blank=True,
        null=True,
    )

    class Meta:
        managed = False
        db_table = "invoices"
        verbose_name = "invoice"


class JppsoRegionStateAssignments(models.Model):
    id = models.UUIDField(primary_key=True)
    jppso_region = models.ForeignKey(
        "JppsoRegions",
        models.DO_NOTHING,
        related_name="jppso_region_state_assignments_jppso_region",
        blank=True,
        null=True,
    )
    state_name = models.TextField(unique=True)
    state_abbreviation = models.TextField(unique=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "jppso_region_state_assignments"
        verbose_name = "JPPSO region state assignment"


class JppsoRegions(models.Model):
    id = models.UUIDField(primary_key=True)
    code = models.TextField(unique=True)
    name = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "jppso_regions"
        verbose_name = "JPPSO region"


class MoveDocuments(models.Model):
    id = models.UUIDField(primary_key=True)
    move = models.ForeignKey(
        "Moves", models.DO_NOTHING, related_name="move_documents_move"
    )
    document = models.ForeignKey(
        Documents, models.DO_NOTHING, related_name="move_documents_document"
    )
    move_document_type = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    title = models.CharField(max_length=255)
    personally_procured_move = models.ForeignKey(
        "PersonallyProcuredMoves",
        models.DO_NOTHING,
        related_name="move_documents_personally_procured_move",
        blank=True,
        null=True,
    )
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "move_documents"
        unique_together = (("move", "document"),)
        verbose_name = "move document"


class MoveOrders(models.Model):
    id = models.UUIDField(primary_key=True)
    customer = models.ForeignKey(
        Customers,
        models.DO_NOTHING,
        related_name="move_orders_customer",
        blank=True,
        null=True,
    )
    origin_duty_station = models.ForeignKey(
        DutyStations,
        models.DO_NOTHING,
        related_name="move_orders_origin_duty_station",
        blank=True,
        null=True,
    )
    destination_duty_station = models.ForeignKey(
        DutyStations,
        models.DO_NOTHING,
        related_name="move_orders_destination_duty_station",
        blank=True,
        null=True,
    )
    entitlement = models.ForeignKey(
        Entitlements,
        models.DO_NOTHING,
        related_name="move_orders_entitlement",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    confirmation_number = models.TextField(blank=True, null=True)
    order_number = models.TextField(blank=True, null=True)
    grade = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "move_orders"
        verbose_name = "move order"


class MoveTaskOrders(models.Model):
    id = models.UUIDField(primary_key=True)
    move_order = models.ForeignKey(
        MoveOrders,
        models.DO_NOTHING,
        related_name="move_task_orders_move_order",
        blank=True,
        null=True,
    )
    reference_id = models.CharField(max_length=255, blank=True, null=True)
    is_available_to_prime = models.BooleanField()
    is_canceled = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "move_task_orders"
        verbose_name = "move task order"


class Moves(models.Model):
    id = models.UUIDField(primary_key=True)
    selected_move_type = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    orders = models.ForeignKey("Orders", models.DO_NOTHING, related_name="moves_orders")
    status = models.CharField(max_length=255)
    locator = models.CharField(unique=True, max_length=6, blank=True, null=True)
    cancel_reason = models.CharField(max_length=255, blank=True, null=True)
    show = models.BooleanField()

    class Meta:
        managed = False
        db_table = "moves"
        verbose_name = "move"


class MovingExpenseDocuments(models.Model):
    id = models.UUIDField(primary_key=True)
    move_document = models.ForeignKey(
        MoveDocuments,
        models.DO_NOTHING,
        related_name="moving_expense_documents_move_document",
    )
    moving_expense_type = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    requested_amount_cents = models.IntegerField(blank=True, null=True)
    payment_method = models.CharField(max_length=255, blank=True, null=True)
    receipt_missing = models.BooleanField(blank=True, null=True)
    storage_start_date = models.DateField(blank=True, null=True)
    storage_end_date = models.DateField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "moving_expense_documents"
        verbose_name = "moving expense document"


class MtoServiceItems(models.Model):
    id = models.UUIDField(primary_key=True)
    move_task_order = models.ForeignKey(
        MoveTaskOrders,
        models.DO_NOTHING,
        related_name="mto_service_items_move_task_order",
        blank=True,
        null=True,
    )
    mto_shipment = models.ForeignKey(
        "MtoShipments",
        models.DO_NOTHING,
        related_name="mto_service_items_mto_shipment",
        blank=True,
        null=True,
    )
    re_service = models.ForeignKey(
        "ReServices",
        models.DO_NOTHING,
        related_name="mto_service_items_re_service",
        blank=True,
        null=True,
    )
    meta_id = models.UUIDField(blank=True, null=True)
    meta_type = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "mto_service_items"
        verbose_name = "MTO service item"


class MtoShipments(models.Model):
    id = models.UUIDField(primary_key=True)
    move_task_order = models.ForeignKey(
        MoveTaskOrders,
        models.DO_NOTHING,
        related_name="mto_shipments_move_task_order",
        blank=True,
        null=True,
    )
    scheduled_pickup_date = models.DateField(blank=True, null=True)
    requested_pickup_date = models.DateField(blank=True, null=True)
    customer_remarks = models.TextField(blank=True, null=True)
    pickup_address = models.ForeignKey(
        Addresses,
        models.DO_NOTHING,
        related_name="mto_shipments_pickup_address",
        blank=True,
        null=True,
    )
    destination_address = models.ForeignKey(
        Addresses,
        models.DO_NOTHING,
        related_name="mto_shipments_destination_address",
        blank=True,
        null=True,
    )
    secondary_pickup_address = models.ForeignKey(
        Addresses,
        models.DO_NOTHING,
        related_name="mto_shipments_secondary_pickup_address",
        blank=True,
        null=True,
    )
    secondary_delivery_address = models.ForeignKey(
        Addresses,
        models.DO_NOTHING,
        related_name="mto_shipments_secondary_delivery_address",
        blank=True,
        null=True,
    )
    prime_estimated_weight = models.IntegerField(blank=True, null=True)
    prime_estimated_weight_recorded_date = models.DateField(blank=True, null=True)
    prime_actual_weight = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    shipment_type = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = "mto_shipments"
        verbose_name = "MTO shipment"


class Notifications(models.Model):
    id = models.UUIDField(primary_key=True)
    service_member = models.ForeignKey(
        "ServiceMembers",
        models.DO_NOTHING,
        related_name="notifications_service_member",
        blank=True,
        null=True,
    )
    ses_message_id = models.TextField()
    notification_type = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "notifications"
        verbose_name = "notification"


class OfficeEmails(models.Model):
    id = models.UUIDField(primary_key=True)
    transportation_office = models.ForeignKey(
        "TransportationOffices",
        models.DO_NOTHING,
        related_name="office_emails_transportation_office",
    )
    email = models.TextField()
    label = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "office_emails"
        verbose_name = "office email"


class OfficePhoneLines(models.Model):
    id = models.UUIDField(primary_key=True)
    transportation_office = models.ForeignKey(
        "TransportationOffices",
        models.DO_NOTHING,
        related_name="office_phone_lines_transportation_office",
    )
    number = models.TextField()
    label = models.TextField(blank=True, null=True)
    is_dsn_number = models.BooleanField()
    type = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "office_phone_lines"
        verbose_name = "office phone line"


class OfficeUsers(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey(
        "Users",
        models.DO_NOTHING,
        related_name="office_users_user",
        blank=True,
        null=True,
    )
    last_name = models.TextField()
    first_name = models.TextField()
    middle_initials = models.TextField(blank=True, null=True)
    email = models.TextField(unique=True)
    telephone = models.TextField()
    transportation_office = models.ForeignKey(
        "TransportationOffices",
        models.DO_NOTHING,
        related_name="office_users_transportation_office",
    )
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deactivated = models.BooleanField()
    active = models.BooleanField()

    class Meta:
        managed = False
        db_table = "office_users"
        verbose_name = "office user"


class Orders(models.Model):
    id = models.UUIDField(primary_key=True)
    service_member = models.ForeignKey(
        "ServiceMembers", models.DO_NOTHING, related_name="orders_service_member"
    )
    issue_date = models.DateField()
    report_by_date = models.DateField()
    orders_type = models.CharField(max_length=255)
    has_dependents = models.BooleanField()
    new_duty_station = models.ForeignKey(
        DutyStations, models.DO_NOTHING, related_name="orders_new_duty_station"
    )
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uploaded_orders = models.ForeignKey(
        Documents, models.DO_NOTHING, related_name="orders_uploaded_orders"
    )
    orders_number = models.CharField(max_length=255, blank=True, null=True)
    orders_type_detail = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255)
    tac = models.CharField(max_length=255, blank=True, null=True)
    department_indicator = models.CharField(max_length=255, blank=True, null=True)
    spouse_has_pro_gear = models.BooleanField()
    sac = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "orders"
        verbose_name = "order"


class Organizations(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    poc_email = models.CharField(max_length=255, blank=True, null=True)
    poc_phone = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "organizations"
        verbose_name = "organization"


class PaymentRequests(models.Model):
    id = models.UUIDField(primary_key=True)
    is_final = models.BooleanField()
    rejection_reason = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    move_task_order = models.ForeignKey(
        MoveTaskOrders,
        models.DO_NOTHING,
        related_name="payment_requests_move_task_order",
    )
    status = models.TextField()  # This field type is a guess.
    requested_at = models.DateTimeField()
    reviewed_at = models.DateTimeField(blank=True, null=True)
    sent_to_gex_at = models.DateTimeField(blank=True, null=True)
    received_by_gex_at = models.DateTimeField(blank=True, null=True)
    paid_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "payment_requests"
        verbose_name = "payment request"


class PaymentServiceItemParams(models.Model):
    id = models.UUIDField(primary_key=True)
    payment_service_item = models.ForeignKey(
        "PaymentServiceItems",
        models.DO_NOTHING,
        related_name="payment_service_item_params_payment_service_item",
    )
    service_item_param_key = models.ForeignKey(
        "ServiceItemParamKeys",
        models.DO_NOTHING,
        related_name="payment_service_item_params_service_item_param_key",
    )
    value = models.CharField(max_length=80)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "payment_service_item_params"
        unique_together = (("payment_service_item", "service_item_param_key"),)
        verbose_name = "payment service item param"


class PaymentServiceItems(models.Model):
    id = models.UUIDField(primary_key=True)
    payment_request = models.ForeignKey(
        PaymentRequests,
        models.DO_NOTHING,
        related_name="payment_service_items_payment_request",
    )
    service_item = models.ForeignKey(
        MtoServiceItems,
        models.DO_NOTHING,
        related_name="payment_service_items_service_item",
    )
    status = models.TextField()  # This field type is a guess.
    price_cents = models.IntegerField()
    rejection_reason = models.CharField(max_length=255, blank=True, null=True)
    requested_at = models.DateTimeField()
    approved_at = models.DateTimeField(blank=True, null=True)
    denied_at = models.DateTimeField(blank=True, null=True)
    sent_to_gex_at = models.DateTimeField(blank=True, null=True)
    paid_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "payment_service_items"
        verbose_name = "payment service item"


class PersonallyProcuredMoves(models.Model):
    id = models.UUIDField(primary_key=True)
    move = models.ForeignKey(
        Moves, models.DO_NOTHING, related_name="personally_procured_moves_move"
    )
    size = models.CharField(max_length=255, blank=True, null=True)
    weight_estimate = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    pickup_postal_code = models.CharField(max_length=255, blank=True, null=True)
    additional_pickup_postal_code = models.CharField(
        max_length=255, blank=True, null=True
    )
    destination_postal_code = models.CharField(max_length=255, blank=True, null=True)
    days_in_storage = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=255)
    has_additional_postal_code = models.BooleanField(blank=True, null=True)
    has_sit = models.BooleanField(blank=True, null=True)
    has_requested_advance = models.BooleanField()
    advance_id = models.UUIDField(blank=True, null=True)
    estimated_storage_reimbursement = models.CharField(
        max_length=255, blank=True, null=True
    )
    mileage = models.IntegerField(blank=True, null=True)
    planned_sit_max = models.IntegerField(blank=True, null=True)
    sit_max = models.IntegerField(blank=True, null=True)
    incentive_estimate_min = models.IntegerField(blank=True, null=True)
    incentive_estimate_max = models.IntegerField(blank=True, null=True)
    advance_worksheet = models.ForeignKey(
        Documents,
        models.DO_NOTHING,
        related_name="personally_procured_moves_advance_worksheet",
        blank=True,
        null=True,
    )
    net_weight = models.IntegerField(blank=True, null=True)
    original_move_date = models.DateField(blank=True, null=True)
    actual_move_date = models.DateField(blank=True, null=True)
    total_sit_cost = models.IntegerField(blank=True, null=True)
    submit_date = models.DateTimeField(blank=True, null=True)
    approve_date = models.DateTimeField(blank=True, null=True)
    reviewed_date = models.DateTimeField(blank=True, null=True)
    has_pro_gear = models.TextField(
        blank=True, null=True
    )  # This field type is a guess.
    has_pro_gear_over_thousand = models.TextField(
        blank=True, null=True
    )  # This field type is a guess.

    class Meta:
        managed = False
        db_table = "personally_procured_moves"
        verbose_name = "personally procured move"


class PpmOfficeUsers(models.Model):
    id = models.UUIDField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "ppm_office_users"
        verbose_name = "PPM office user"


class ProofOfServiceDocs(models.Model):
    id = models.UUIDField(primary_key=True)
    payment_request = models.ForeignKey(
        PaymentRequests,
        models.DO_NOTHING,
        related_name="proof_of_service_docs_payment_request",
    )
    upload = models.ForeignKey(
        "Uploads", models.DO_NOTHING, related_name="proof_of_service_docs_upload"
    )
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "proof_of_service_docs"
        unique_together = (("payment_request", "upload"),)
        verbose_name = "proof of service doc"


class ReContractYears(models.Model):
    id = models.UUIDField(primary_key=True)
    contract = models.ForeignKey(
        "ReContracts", models.DO_NOTHING, related_name="re_contract_years_contract"
    )
    name = models.CharField(max_length=80)
    start_date = models.DateField()
    end_date = models.DateField()
    escalation = models.DecimalField(max_digits=6, decimal_places=5)
    escalation_compounded = models.DecimalField(max_digits=6, decimal_places=5)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "re_contract_years"
        verbose_name = "RE contract year"


class ReContracts(models.Model):
    id = models.UUIDField(primary_key=True)
    code = models.CharField(unique=True, max_length=80)
    name = models.CharField(max_length=80)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "re_contracts"
        verbose_name = "RE contract"


class ReDomesticAccessorialPrices(models.Model):
    id = models.UUIDField(primary_key=True)
    contract = models.ForeignKey(
        ReContracts,
        models.DO_NOTHING,
        related_name="re_domestic_accessorial_prices_contract",
    )
    service = models.ForeignKey(
        "ReServices",
        models.DO_NOTHING,
        related_name="re_domestic_accessorial_prices_service",
    )
    services_schedule = models.IntegerField()
    per_unit_cents = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "re_domestic_accessorial_prices"
        unique_together = (("contract", "service", "services_schedule"),)
        verbose_name = "RE domestic accessorial price"


class ReDomesticLinehaulPrices(models.Model):
    id = models.UUIDField(primary_key=True)
    contract = models.ForeignKey(
        ReContracts,
        models.DO_NOTHING,
        related_name="re_domestic_linehaul_prices_contract",
    )
    weight_lower = models.IntegerField()
    weight_upper = models.IntegerField()
    miles_lower = models.IntegerField()
    miles_upper = models.IntegerField()
    is_peak_period = models.BooleanField()
    domestic_service_area = models.ForeignKey(
        "ReDomesticServiceAreas",
        models.DO_NOTHING,
        related_name="re_domestic_linehaul_prices_domestic_service_area",
    )
    price_millicents = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "re_domestic_linehaul_prices"
        unique_together = (
            (
                "contract",
                "weight_lower",
                "weight_upper",
                "miles_lower",
                "miles_upper",
                "is_peak_period",
                "domestic_service_area",
            ),
        )
        verbose_name = "RE domestic linehaul price"


class ReDomesticOtherPrices(models.Model):
    id = models.UUIDField(primary_key=True)
    contract = models.ForeignKey(
        ReContracts, models.DO_NOTHING, related_name="re_domestic_other_prices_contract"
    )
    service = models.ForeignKey(
        "ReServices", models.DO_NOTHING, related_name="re_domestic_other_prices_service"
    )
    is_peak_period = models.BooleanField()
    schedule = models.IntegerField()
    price_cents = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "re_domestic_other_prices"
        unique_together = (("contract", "service", "is_peak_period", "schedule"),)
        verbose_name = "RE domestic other price"


class ReDomesticServiceAreaPrices(models.Model):
    id = models.UUIDField(primary_key=True)
    contract = models.ForeignKey(
        ReContracts,
        models.DO_NOTHING,
        related_name="re_domestic_service_area_prices_contract",
    )
    service = models.ForeignKey(
        "ReServices",
        models.DO_NOTHING,
        related_name="re_domestic_service_area_prices_service",
    )
    is_peak_period = models.BooleanField()
    domestic_service_area = models.ForeignKey(
        "ReDomesticServiceAreas",
        models.DO_NOTHING,
        related_name="re_domestic_service_area_prices_domestic_service_area",
    )
    price_cents = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "re_domestic_service_area_prices"
        unique_together = (
            ("contract", "service", "is_peak_period", "domestic_service_area"),
        )
        verbose_name = "RE domestic service area price"


class ReDomesticServiceAreas(models.Model):
    id = models.UUIDField(primary_key=True)
    base_point_city = models.CharField(max_length=80)
    state = models.CharField(max_length=80)
    service_area = models.CharField(unique=True, max_length=80)
    services_schedule = models.IntegerField()
    sit_pd_schedule = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "re_domestic_service_areas"
        verbose_name = "RE domestic service area"


class ReIntlAccessorialPrices(models.Model):
    id = models.UUIDField(primary_key=True)
    contract = models.ForeignKey(
        ReContracts,
        models.DO_NOTHING,
        related_name="re_intl_accessorial_prices_contract",
    )
    service = models.ForeignKey(
        "ReServices",
        models.DO_NOTHING,
        related_name="re_intl_accessorial_prices_service",
    )
    market = models.CharField(max_length=1)
    per_unit_cents = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "re_intl_accessorial_prices"
        unique_together = (("contract", "service", "market"),)
        verbose_name = "RE intl accessorial price"


class ReIntlOtherPrices(models.Model):
    id = models.UUIDField(primary_key=True)
    contract = models.ForeignKey(
        ReContracts, models.DO_NOTHING, related_name="re_intl_other_prices_contract"
    )
    service = models.ForeignKey(
        "ReServices", models.DO_NOTHING, related_name="re_intl_other_prices_service"
    )
    is_peak_period = models.BooleanField()
    rate_area = models.ForeignKey(
        "ReRateAreas", models.DO_NOTHING, related_name="re_intl_other_prices_rate_area"
    )
    per_unit_cents = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "re_intl_other_prices"
        unique_together = (("contract", "service", "is_peak_period", "rate_area"),)
        verbose_name = "RE intl other price"


class ReIntlPrices(models.Model):
    id = models.UUIDField(primary_key=True)
    contract = models.ForeignKey(
        ReContracts, models.DO_NOTHING, related_name="re_intl_prices_contract"
    )
    service = models.ForeignKey(
        "ReServices", models.DO_NOTHING, related_name="re_intl_prices_service"
    )
    is_peak_period = models.BooleanField()
    origin_rate_area = models.ForeignKey(
        "ReRateAreas", models.DO_NOTHING, related_name="re_intl_prices_origin_rate_area"
    )
    destination_rate_area = models.ForeignKey(
        "ReRateAreas",
        models.DO_NOTHING,
        related_name="re_intl_prices_destination_rate_area",
    )
    per_unit_cents = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "re_intl_prices"
        unique_together = (
            (
                "contract",
                "service",
                "is_peak_period",
                "origin_rate_area",
                "destination_rate_area",
            ),
        )
        verbose_name = "RE intl price"


class ReRateAreas(models.Model):
    id = models.UUIDField(primary_key=True)
    is_oconus = models.BooleanField()
    code = models.CharField(unique=True, max_length=20)
    name = models.CharField(max_length=80)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "re_rate_areas"
        verbose_name = "RE rate area"


class ReServices(models.Model):
    id = models.UUIDField(primary_key=True)
    code = models.CharField(unique=True, max_length=20)
    name = models.CharField(max_length=80)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "re_services"
        verbose_name = "RE service"


class ReShipmentTypePrices(models.Model):
    id = models.UUIDField(primary_key=True)
    contract = models.ForeignKey(
        ReContracts, models.DO_NOTHING, related_name="re_shipment_type_prices_contract"
    )
    service = models.ForeignKey(
        ReServices, models.DO_NOTHING, related_name="re_shipment_type_prices_service"
    )
    market = models.CharField(max_length=1)
    factor = models.DecimalField(max_digits=3, decimal_places=2)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "re_shipment_type_prices"
        unique_together = (("contract", "service", "market"),)
        verbose_name = "RE shipment type price"


class ReTaskOrderFees(models.Model):
    id = models.UUIDField(primary_key=True)
    contract_year = models.ForeignKey(
        ReContractYears,
        models.DO_NOTHING,
        related_name="re_task_order_fees_contract_year",
    )
    service = models.ForeignKey(
        ReServices, models.DO_NOTHING, related_name="re_task_order_fees_service"
    )
    price_cents = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "re_task_order_fees"
        unique_together = (("contract_year", "service"),)
        verbose_name = "RE task order fee"


class ReZip3S(models.Model):
    id = models.UUIDField(primary_key=True)
    zip3 = models.CharField(unique=True, max_length=3)
    domestic_service_area = models.ForeignKey(
        ReDomesticServiceAreas,
        models.DO_NOTHING,
        related_name="re_zip3s_domestic_service_area",
    )
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "re_zip3s"
        verbose_name = "RE zip3"


class Reimbursements(models.Model):
    id = models.UUIDField(primary_key=True)
    requested_amount = models.IntegerField()
    method_of_receipt = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    requested_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "reimbursements"
        verbose_name = "reimbursement"


class Roles(models.Model):
    id = models.UUIDField(primary_key=True)
    role_type = models.TextField(unique=True, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    role_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "roles"
        verbose_name = "role"


class SchemaMigration(models.Model):
    version = models.CharField(unique=True, max_length=14)

    class Meta:
        managed = False
        db_table = "schema_migration"
        verbose_name = "schema migration"


class ServiceItemParamKeys(models.Model):
    id = models.UUIDField(primary_key=True)
    key = models.CharField(max_length=80)
    description = models.CharField(max_length=255)
    type = models.TextField()  # This field type is a guess.
    origin = models.TextField()  # This field type is a guess.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "service_item_param_keys"
        verbose_name = "service item param key"


class ServiceMembers(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.OneToOneField(
        "Users", models.DO_NOTHING, related_name="service_members_user"
    )
    edipi = models.TextField(blank=True, null=True)
    affiliation = models.TextField(blank=True, null=True)
    rank = models.TextField(blank=True, null=True)
    first_name = models.TextField(blank=True, null=True)
    middle_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    suffix = models.TextField(blank=True, null=True)
    telephone = models.TextField(blank=True, null=True)
    secondary_telephone = models.TextField(blank=True, null=True)
    personal_email = models.TextField(blank=True, null=True)
    phone_is_preferred = models.BooleanField(blank=True, null=True)
    email_is_preferred = models.BooleanField(blank=True, null=True)
    residential_address = models.ForeignKey(
        Addresses,
        models.DO_NOTHING,
        related_name="service_members_residential_address",
        blank=True,
        null=True,
    )
    backup_mailing_address = models.ForeignKey(
        Addresses,
        models.DO_NOTHING,
        related_name="service_members_backup_mailing_address",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    social_security_number = models.ForeignKey(
        "SocialSecurityNumbers",
        models.DO_NOTHING,
        related_name="service_members_social_security_number",
        blank=True,
        null=True,
    )
    duty_station = models.ForeignKey(
        DutyStations,
        models.DO_NOTHING,
        related_name="service_members_duty_station",
        blank=True,
        null=True,
    )
    requires_access_code = models.BooleanField()

    class Meta:
        managed = False
        db_table = "service_members"
        verbose_name = "service member"


class ServiceParams(models.Model):
    id = models.UUIDField(primary_key=True)
    service = models.ForeignKey(
        ReServices, models.DO_NOTHING, related_name="service_params_service"
    )
    service_item_param_key = models.ForeignKey(
        ServiceItemParamKeys,
        models.DO_NOTHING,
        related_name="service_params_service_item_param_key",
    )
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "service_params"
        unique_together = (("service", "service_item_param_key"),)
        verbose_name = "service param"


class SignedCertifications(models.Model):
    id = models.UUIDField(primary_key=True)
    submitting_user = models.ForeignKey(
        "Users", models.DO_NOTHING, related_name="signed_certifications_submitting_user"
    )
    move = models.ForeignKey(
        Moves, models.DO_NOTHING, related_name="signed_certifications_move"
    )
    certification_text = models.TextField()
    signature = models.TextField()
    date = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    personally_procured_move = models.ForeignKey(
        PersonallyProcuredMoves,
        models.DO_NOTHING,
        related_name="signed_certifications_personally_procured_move",
        blank=True,
        null=True,
    )
    certification_type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "signed_certifications"
        verbose_name = "signed certification"


class SocialSecurityNumbers(models.Model):
    id = models.UUIDField(primary_key=True)
    encrypted_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "social_security_numbers"
        verbose_name = "social security number"


class Tariff400NgFullPackRates(models.Model):
    id = models.UUIDField(primary_key=True)
    schedule = models.IntegerField(blank=True, null=True)
    weight_lbs_lower = models.IntegerField(blank=True, null=True)
    weight_lbs_upper = models.IntegerField(blank=True, null=True)
    rate_cents = models.IntegerField(blank=True, null=True)
    effective_date_lower = models.DateField(blank=True, null=True)
    effective_date_upper = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "tariff400ng_full_pack_rates"
        verbose_name = "Tariff400NG full pack rate"


class Tariff400NgFullUnpackRates(models.Model):
    id = models.UUIDField(primary_key=True)
    schedule = models.IntegerField(blank=True, null=True)
    rate_millicents = models.IntegerField(blank=True, null=True)
    effective_date_lower = models.DateField(blank=True, null=True)
    effective_date_upper = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "tariff400ng_full_unpack_rates"
        verbose_name = "Tariff400NG full unpack rate"


class Tariff400NgItemRates(models.Model):
    id = models.UUIDField(primary_key=True)
    code = models.CharField(max_length=255)
    schedule = models.IntegerField(blank=True, null=True)
    weight_lbs_lower = models.IntegerField()
    weight_lbs_upper = models.IntegerField()
    rate_cents = models.IntegerField()
    effective_date_lower = models.DateField()
    effective_date_upper = models.DateField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "tariff400ng_item_rates"
        verbose_name = "Tariff400NG item rate"


class Tariff400NgItems(models.Model):
    id = models.UUIDField(primary_key=True)
    code = models.CharField(max_length=255)
    discount_type = models.CharField(max_length=255)
    allowed_location = models.CharField(max_length=255)
    item = models.CharField(max_length=255)
    measurement_unit_1 = models.CharField(max_length=255)
    measurement_unit_2 = models.CharField(max_length=255)
    rate_ref_code = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    requires_pre_approval = models.BooleanField()

    class Meta:
        managed = False
        db_table = "tariff400ng_items"
        verbose_name = "Tariff400NG item"


class Tariff400NgLinehaulRates(models.Model):
    id = models.UUIDField(primary_key=True)
    distance_miles_lower = models.IntegerField(blank=True, null=True)
    distance_miles_upper = models.IntegerField(blank=True, null=True)
    weight_lbs_lower = models.IntegerField(blank=True, null=True)
    weight_lbs_upper = models.IntegerField(blank=True, null=True)
    rate_cents = models.IntegerField(blank=True, null=True)
    effective_date_lower = models.DateField(blank=True, null=True)
    effective_date_upper = models.DateField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "tariff400ng_linehaul_rates"
        verbose_name = "Tariff400NG linehaul rate"


class Tariff400NgServiceAreas(models.Model):
    id = models.UUIDField(primary_key=True)
    service_area = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    services_schedule = models.IntegerField(blank=True, null=True)
    linehaul_factor = models.IntegerField(blank=True, null=True)
    service_charge_cents = models.IntegerField(blank=True, null=True)
    effective_date_lower = models.DateField(blank=True, null=True)
    effective_date_upper = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    sit_185a_rate_cents = models.IntegerField(blank=True, null=True)
    sit_185b_rate_cents = models.IntegerField(blank=True, null=True)
    sit_pd_schedule = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "tariff400ng_service_areas"
        verbose_name = "Tariff400NG service area"


class Tariff400NgShorthaulRates(models.Model):
    id = models.UUIDField(primary_key=True)
    cwt_miles_lower = models.IntegerField(blank=True, null=True)
    cwt_miles_upper = models.IntegerField(blank=True, null=True)
    rate_cents = models.IntegerField(blank=True, null=True)
    effective_date_lower = models.DateField(blank=True, null=True)
    effective_date_upper = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "tariff400ng_shorthaul_rates"
        verbose_name = "Tariff400NG shorthaul rate"


class Tariff400NgZip3S(models.Model):
    id = models.UUIDField(primary_key=True)
    zip3 = models.CharField(max_length=3, blank=True, null=True)
    basepoint_city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    service_area = models.TextField(blank=True, null=True)
    rate_area = models.TextField(blank=True, null=True)
    region = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "tariff400ng_zip3s"
        verbose_name = "Tariff400NG zip3"


class Tariff400NgZip5RateAreas(models.Model):
    id = models.UUIDField(primary_key=True)
    zip5 = models.CharField(max_length=5, blank=True, null=True)
    rate_area = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "tariff400ng_zip5_rate_areas"
        verbose_name = "Tariff400NG zip5 rate area"


class TrafficDistributionLists(models.Model):
    id = models.UUIDField(primary_key=True)
    source_rate_area = models.CharField(max_length=255)
    destination_region = models.CharField(max_length=255)
    code_of_service = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "traffic_distribution_lists"
        unique_together = (
            ("source_rate_area", "destination_region", "code_of_service"),
        )
        verbose_name = "traffic distribution list"


class TransportationInvoicingOfficers(models.Model):
    id = models.UUIDField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "transportation_invoicing_officers"
        verbose_name = "transportation invoicing officer"


class TransportationOffices(models.Model):
    id = models.UUIDField(primary_key=True)
    shipping_office = models.ForeignKey(
        "self",
        models.DO_NOTHING,
        related_name="transportation_offices_shipping_office",
        blank=True,
        null=True,
    )
    name = models.TextField()
    address = models.ForeignKey(
        Addresses, models.DO_NOTHING, related_name="transportation_offices_address"
    )
    latitude = models.FloatField()
    longitude = models.FloatField()
    hours = models.TextField(blank=True, null=True)
    services = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    gbloc = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "transportation_offices"
        verbose_name = "transportation office"


class TransportationOrderingOfficers(models.Model):
    id = models.UUIDField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.OneToOneField(
        "Users",
        models.DO_NOTHING,
        related_name="transportation_ordering_officers_user",
        blank=True,
        null=True,
    )

    class Meta:
        managed = False
        db_table = "transportation_ordering_officers"
        verbose_name = "transportation ordering officer"


class TransportationServiceProviderPerformances(models.Model):
    id = models.UUIDField(primary_key=True)
    performance_period_start = models.DateField()
    performance_period_end = models.DateField()
    traffic_distribution_list = models.ForeignKey(
        TrafficDistributionLists,
        models.DO_NOTHING,
        related_name="transportation_service_provider_performances_traffic_distribution_list",
    )
    quality_band = models.IntegerField(blank=True, null=True)
    offer_count = models.IntegerField()
    best_value_score = models.FloatField()
    transportation_service_provider = models.ForeignKey(
        "TransportationServiceProviders",
        models.DO_NOTHING,
        related_name="transportation_service_provider_performances_transportation_service_provider",
    )
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    rate_cycle_start = models.DateField()
    rate_cycle_end = models.DateField()
    linehaul_rate = models.DecimalField(max_digits=65535, decimal_places=65535)
    sit_rate = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = "transportation_service_provider_performances"
        verbose_name = "transportation service provider performance"


class TransportationServiceProviders(models.Model):
    id = models.UUIDField(primary_key=True)
    standard_carrier_alpha_code = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    enrolled = models.BooleanField()
    name = models.TextField(blank=True, null=True)
    supplier_id = models.TextField(blank=True, null=True)
    poc_general_name = models.TextField(blank=True, null=True)
    poc_general_email = models.TextField(blank=True, null=True)
    poc_general_phone = models.TextField(blank=True, null=True)
    poc_claims_name = models.TextField(blank=True, null=True)
    poc_claims_email = models.TextField(blank=True, null=True)
    poc_claims_phone = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "transportation_service_providers"
        verbose_name = "transportation service provider"


class Uploads(models.Model):
    id = models.UUIDField(primary_key=True)
    document = models.ForeignKey(
        Documents,
        models.DO_NOTHING,
        related_name="uploads_document",
        blank=True,
        null=True,
    )
    uploader = models.ForeignKey(
        "Users", models.DO_NOTHING, related_name="uploads_uploader"
    )
    filename = models.TextField()
    bytes = models.BigIntegerField()
    content_type = models.TextField()
    checksum = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    storage_key = models.CharField(max_length=1024, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "uploads"
        verbose_name = "upload"


class Users(models.Model):
    id = models.UUIDField(primary_key=True)
    login_gov_uuid = models.UUIDField(unique=True)
    login_gov_email = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deactivated = models.BooleanField()
    active = models.BooleanField()

    class Meta:
        managed = False
        db_table = "users"
        verbose_name = "user"


class UsersRoles(models.Model):
    user = models.ForeignKey(Users, models.DO_NOTHING, related_name="users_roles_user")
    role = models.ForeignKey(Roles, models.DO_NOTHING, related_name="users_roles_role")
    id = models.UUIDField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "users_roles"
        verbose_name = "users role"


class WeightTicketSetDocuments(models.Model):
    id = models.UUIDField(primary_key=True)
    weight_ticket_set_type = models.TextField(blank=True, null=True)
    vehicle_nickname = models.TextField(blank=True, null=True)
    move_document = models.ForeignKey(
        MoveDocuments,
        models.DO_NOTHING,
        related_name="weight_ticket_set_documents_move_document",
        blank=True,
        null=True,
    )
    empty_weight = models.IntegerField(blank=True, null=True)
    empty_weight_ticket_missing = models.BooleanField(blank=True, null=True)
    full_weight = models.IntegerField(blank=True, null=True)
    full_weight_ticket_missing = models.BooleanField(blank=True, null=True)
    weight_ticket_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    trailer_ownership_missing = models.BooleanField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "weight_ticket_set_documents"
        verbose_name = "weight ticket set document"
