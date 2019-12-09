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


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = "auth_group"


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(
        AuthGroup, models.DO_NOTHING, related_name="auth_group_permissions_group"
    )
    permission = models.ForeignKey(
        "AuthPermission",
        models.DO_NOTHING,
        related_name="auth_group_permissions_permission",
    )

    class Meta:
        managed = False
        db_table = "auth_group_permissions"
        unique_together = (("group", "permission"),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey(
        "DjangoContentType",
        models.DO_NOTHING,
        related_name="auth_permission_content_type",
    )
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "auth_permission"
        unique_together = (("content_type", "codename"),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "auth_user"


class AuthUserGroups(models.Model):
    user = models.ForeignKey(
        AuthUser, models.DO_NOTHING, related_name="auth_user_groups_user"
    )
    group = models.ForeignKey(
        AuthGroup, models.DO_NOTHING, related_name="auth_user_groups_group"
    )

    class Meta:
        managed = False
        db_table = "auth_user_groups"
        unique_together = (("user", "group"),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(
        AuthUser, models.DO_NOTHING, related_name="auth_user_user_permissions_user"
    )
    permission = models.ForeignKey(
        AuthPermission,
        models.DO_NOTHING,
        related_name="auth_user_user_permissions_permission",
    )

    class Meta:
        managed = False
        db_table = "auth_user_user_permissions"
        unique_together = (("user", "permission"),)


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

    class Meta:
        managed = False
        db_table = "client_certs"


class ContractingOfficers(models.Model):
    id = models.UUIDField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "contracting_officers"


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


class Customers(models.Model):
    id = models.UUIDField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "customers"


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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        "DjangoContentType",
        models.DO_NOTHING,
        related_name="django_admin_log_content_type",
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        AuthUser, models.DO_NOTHING, related_name="django_admin_log_user"
    )

    class Meta:
        managed = False
        db_table = "django_admin_log"


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "django_content_type"
        unique_together = (("app_label", "model"),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_migrations"


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_session"


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


class InvoiceNumberTrackers(models.Model):
    standard_carrier_alpha_code = models.TextField(primary_key=True)
    year = models.IntegerField()
    sequence_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = "invoice_number_trackers"
        unique_together = (("standard_carrier_alpha_code", "year"),)


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


class PaymentRequests(models.Model):
    id = models.UUIDField(primary_key=True)
    is_final = models.BooleanField(blank=True, null=True)
    rejection_reason = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "payment_requests"


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

    class Meta:
        managed = False
        db_table = "personally_procured_moves"


class PpmOfficeUsers(models.Model):
    id = models.UUIDField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "ppm_office_users"


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


class ReContracts(models.Model):
    id = models.UUIDField(primary_key=True)
    code = models.CharField(unique=True, max_length=80)
    name = models.CharField(max_length=80)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "re_contracts"


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


class ReServices(models.Model):
    id = models.UUIDField(primary_key=True)
    code = models.CharField(unique=True, max_length=20)
    name = models.CharField(max_length=80)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "re_services"


class ReShipmentTypePrices(models.Model):
    id = models.UUIDField(primary_key=True)
    contract = models.ForeignKey(
        ReContracts, models.DO_NOTHING, related_name="re_shipment_type_prices_contract"
    )
    shipment_type = models.ForeignKey(
        "ReShipmentTypes",
        models.DO_NOTHING,
        related_name="re_shipment_type_prices_shipment_type",
    )
    market = models.CharField(max_length=1)
    factor_hundredths = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "re_shipment_type_prices"
        unique_together = (("contract", "shipment_type", "market"),)


class ReShipmentTypes(models.Model):
    id = models.UUIDField(primary_key=True)
    code = models.CharField(unique=True, max_length=20)
    name = models.CharField(max_length=80)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "re_shipment_types"


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


class Roles(models.Model):
    id = models.IntegerField(primary_key=True)
    role_type = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "roles"


class SchemaMigration(models.Model):
    version = models.CharField(unique=True, max_length=14)

    class Meta:
        managed = False
        db_table = "schema_migration"


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


class SocialSecurityNumbers(models.Model):
    id = models.UUIDField(primary_key=True)
    encrypted_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "social_security_numbers"


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


class Tariff400NgZip5RateAreas(models.Model):
    id = models.UUIDField(primary_key=True)
    zip5 = models.CharField(max_length=5, blank=True, null=True)
    rate_area = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "tariff400ng_zip5_rate_areas"


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


class TransportationInvoicingOfficers(models.Model):
    id = models.UUIDField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "transportation_invoicing_officers"


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


class TransportationOrderingOfficers(models.Model):
    id = models.UUIDField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "transportation_ordering_officers"


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


class UserRoles(models.Model):
    users = models.ForeignKey(
        "Users", models.DO_NOTHING, related_name="user_roles_users"
    )
    roles = models.ForeignKey(Roles, models.DO_NOTHING, related_name="user_roles_roles")

    class Meta:
        managed = False
        db_table = "user_roles"


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


class WeightTicketSetDocuments(models.Model):
    id = models.UUIDField(primary_key=True)
    vehicle_options = models.TextField(blank=True, null=True)
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
