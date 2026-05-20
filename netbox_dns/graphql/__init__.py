from .schema import (
    NetBoxDNSDNSSECKeyTemplateQuery,
    NetBoxDNSDNSSECPolicyQuery,
    NetBoxDNSNameServerQuery,
    NetBoxDNSRecordQuery,
    NetBoxDNSRecordTemplateQuery,
    NetBoxDNSRegistrarQuery,
    NetBoxDNSRegistrationContactQuery,
    NetBoxDNSViewQuery,
    NetBoxDNSZoneQuery,
    NetBoxDNSZoneTemplateQuery,
)

schema = [
    NetBoxDNSNameServerQuery,
    NetBoxDNSViewQuery,
    NetBoxDNSZoneQuery,
    NetBoxDNSRecordQuery,
    NetBoxDNSDNSSECKeyTemplateQuery,
    NetBoxDNSDNSSECPolicyQuery,
    NetBoxDNSRegistrationContactQuery,
    NetBoxDNSRegistrarQuery,
    NetBoxDNSZoneTemplateQuery,
    NetBoxDNSRecordTemplateQuery,
]
