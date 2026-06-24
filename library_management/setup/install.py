import frappe
from frappe import _
from frappe.utils import cstr

def after_install():
    create_default_roles()
    create_default_role_profiles()

def create_default_roles():
    roles = ["Library Administrator", "Library Staff", "Accounts Staff", "Management"]
    for role_name in roles:
        if not frappe.db.exists("Role", role_name):
            frappe.get_doc({
                "doctype": "Role",
                "role_name": role_name,
            }).insert()

def create_default_role_profiles():
    if not frappe.db.exists("Role Profile", "Library Administrator"):
        role_profile = frappe.get_doc(
            {
                "doctype": "Role Profile",
                "role_profile": "Library Administrator",
            }
        )
        roles = [
            "Accounts Manager",
            "Report Manager",
            "Translator",
            "Library Administrator",
            "Accounts User",
            "Inbox User",
            "Prepared Report User",
        ]
        # add roles to role profile
        for role in roles:
            role_profile.append("roles", {"role": role})
        role_profile.insert()

    if not frappe.db.exists("Role Profile", "Library Staff"):
        role_profile = frappe.get_doc(
            {
                "doctype": "Role Profile",
                "role_profile": "Library Staff",
            }
        )
        roles = [
            "Accounts Manager",
            "Report Manager",
            "Translator",
            "Library Staff",
            "Accounts User",
            "Inbox User",
            "Prepared Report User",
            "System Manager",
        ]
        # add roles to role profile
        for role in roles:
            role_profile.append("roles", {"role": role})
        role_profile.insert()

    if not frappe.db.exists("Role Profile", "Accounts Staff"):
        role_profile = frappe.get_doc(
            {
                "doctype": "Role Profile",
                "role_profile": "Accounts Staff",
            }
        )
        roles = [
            "Accounts Staff",
        ]
        for role in roles:
            role_profile.append("roles", {"role": role})
        role_profile.insert()
    
    if not frappe.db.exists("Role Profile", "Management"):
        role_profile = frappe.get_doc(
            {
                "doctype": "Role Profile",
                "role_profile": "Management",
            }
        )
        roles = [
            "Management",
        ]
        for role in roles:
            role_profile.append("roles", {"role": role})
        role_profile.insert()

