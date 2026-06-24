import frappe
from frappe.utils import today, getdate

def mark_overdue_books():

    books = frappe.get_all(
        "Book Issue",
        filters={
            "status": "Issued"
        },
        fields=["name", "due_date"]
    )

    for row in books:
        if getdate(row.due_date) < getdate(today()):
            frappe.db.set_value(
                "Book Issue",
                row.name,
                "status",
                "Overdue"
            )