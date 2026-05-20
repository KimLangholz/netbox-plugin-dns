import strawberry
import strawberry_django

from .types import (
    NetBoxDNSDNSSECKeyTemplateType,
    NetBoxDNSDNSSECPolicyType,
    NetBoxDNSNameServerType,
    NetBoxDNSRecordTemplateType,
    NetBoxDNSRecordType,
    NetBoxDNSRegistrarType,
    NetBoxDNSRegistrationContactType,
    NetBoxDNSViewType,
    NetBoxDNSZoneTemplateType,
    NetBoxDNSZoneType,
)


@strawberry.type(name="Query")
class NetBoxDNSNameServerQuery:
    netbox_dns_nameserver: NetBoxDNSNameServerType = strawberry_django.field()
    netbox_dns_nameserver_list: list[NetBoxDNSNameServerType] = (
        strawberry_django.field()
    )


@strawberry.type(name="Query")
class NetBoxDNSViewQuery:
    netbox_dns_view: NetBoxDNSViewType = strawberry_django.field()
    netbox_dns_view_list: list[NetBoxDNSViewType] = strawberry_django.field()


@strawberry.type(name="Query")
class NetBoxDNSZoneQuery:
    netbox_dns_zone: NetBoxDNSZoneType = strawberry_django.field()
    netbox_dns_zone_list: list[NetBoxDNSZoneType] = strawberry_django.field()


@strawberry.type(name="Query")
class NetBoxDNSRecordQuery:
    netbox_dns_record: NetBoxDNSRecordType = strawberry_django.field()
    netbox_dns_record_list: list[NetBoxDNSRecordType] = strawberry_django.field()


@strawberry.type(name="Query")
class NetBoxDNSDNSSECKeyTemplateQuery:
    netbox_dns_dnssec_key_template: NetBoxDNSDNSSECKeyTemplateType = (
        strawberry_django.field()
    )
    netbox_dns_dnssec_key_template_list: list[NetBoxDNSDNSSECKeyTemplateType] = (
        strawberry_django.field()
    )


@strawberry.type(name="Query")
class NetBoxDNSDNSSECPolicyQuery:
    netbox_dns_dnssec_policy: NetBoxDNSDNSSECPolicyType = strawberry_django.field()
    netbox_dns_dnssec_policy_list: list[NetBoxDNSDNSSECPolicyType] = (
        strawberry_django.field()
    )


@strawberry.type(name="Query")
class NetBoxDNSRegistrationContactQuery:
    netbox_dns_registration_contact: NetBoxDNSRegistrationContactType = (
        strawberry_django.field()
    )
    netbox_dns_registration_contact_list: list[NetBoxDNSRegistrationContactType] = (
        strawberry_django.field()
    )


@strawberry.type(name="Query")
class NetBoxDNSRegistrarQuery:
    netbox_dns_registrar: NetBoxDNSRegistrarType = strawberry_django.field()
    netbox_dns_registrar_list: list[NetBoxDNSRegistrarType] = strawberry_django.field()


@strawberry.type(name="Query")
class NetBoxDNSZoneTemplateQuery:
    netbox_dns_zone_template: NetBoxDNSZoneTemplateType = strawberry_django.field()
    netbox_dns_zone_template_list: list[NetBoxDNSZoneTemplateType] = (
        strawberry_django.field()
    )


@strawberry.type(name="Query")
class NetBoxDNSRecordTemplateQuery:
    netbox_dns_record_template: NetBoxDNSRecordTemplateType = strawberry_django.field()
    netbox_dns_record_template_list: list[NetBoxDNSRecordTemplateType] = (
        strawberry_django.field()
    )
