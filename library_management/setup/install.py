import frappe
from frappe import _
from frappe.utils import cstr

def after_install():
    create_default_roles()
    create_default_role_profiles()
    default_library_settings()
    create_demo_data()

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

def default_library_settings():
    if frappe.db.exists("Library Settings", "Library Settings"):
        return

    settings = frappe.new_doc("Library Settings")
    settings.loan_period_days = 14
    settings.fine_per_day = 10
    settings.save(ignore_permissions=True)

def create_demo_data():

    create_book_categories()
    create_books()
    create_members()
    create_book_issue()

def create_book_categories():

    categories = [
        "Programming",
        "Science",
        "Fiction"
    ]

    for category in categories:

        if not frappe.db.exists(
            "Book Category",
            category
        ):

            doc = frappe.new_doc("Book Category")
            doc.category_name = category
            doc.insert(ignore_permissions=True)
        
def create_books():

    books = [
        {
            "book_title": "Learning Python",
            "author": "Mark Lutz",
            "isbn": "978111945789",
            "category": "Programming",
            "total_copies": 5,
            "available_copies": 5,
            "rack_location": "A-1"
        },
        {
            "book_title": "Clean Code",
            "author": "Robert Martin",
            "isbn": "9780132350884",
            "category": "Programming",
            "total_copies": 3,
            "available_copies": 3,
            "rack_location": "A-2"
        }
    ]

    for data in books:

        if not frappe.db.exists(
            "Books",
            {
                "isbn": data["isbn"]
            }
        ):

            doc = frappe.get_doc({
                "doctype": "Books",
                **data
            })

            doc.insert(ignore_permissions=True)

def create_members():

    members = [
        {
            "member_name": "John Doe",
            "email": "john@example.com",
            "member_type": "Student"
        },
        {
            "member_name": "Jane Smith",
            "email": "jane@example.com",
            "member_type": "Staff"
        }
    ]

    for data in members:

        if not frappe.db.exists(
            "Library Member",
            {
                "email": data["email"]
            }
        ):

            doc = frappe.get_doc({
                "doctype": "Library Member",
                **data
            })

            doc.insert(ignore_permissions=True)

def create_book_issue():

    member = frappe.db.get_value(
        "Library Member",
        {},
        "name"
    )

    book = frappe.db.get_value(
        "Books",
        {},
        "name"
    )

    if not member or not book:
        return

    if frappe.db.exists("Book Issue", {}):
        return

    issue = frappe.get_doc({
        "doctype": "Book Issue",
        "member": member,
        "book": book,
    })

    issue.insert(ignore_permissions=True)