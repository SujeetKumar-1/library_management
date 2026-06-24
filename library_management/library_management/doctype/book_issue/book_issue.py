# Copyright (c) 2026, Sujeet and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import today, add_days, date_diff, getdate

class BookIssue(Document):
	def validate(self):

		settings = frappe.get_single("Library Settings")

		if not self.issue_date:
			self.issue_date = today()

		if not self.due_date:
			self.due_date = add_days(
				self.issue_date,
				settings.loan_period_days or 14
			)
	
	def before_insert(self):
		available_copies = frappe.db.get_value("Books", self.book, "available_copies")
		if not available_copies or available_copies <= 0:
			frappe.throw(f"Book({self.book}) is out of stock.")

		if self.due_date and getdate(self.due_date) < getdate(today()):
			self.status = "Overdue"
	
	def after_insert(self):
		available_copies = frappe.db.get_value(
			"Books",
			self.book,
			"available_copies"
		) or 0

		new_available = available_copies - 1

		update_fields = {
			"available_copies": new_available,
			"status": "Out of Stock" if new_available <= 0 else "Available"
		}

		frappe.db.set_value(
			"Books",
			self.book,
			update_fields
		)

@frappe.whitelist()
def handle_book_return(name, return_date):
	if not name or not return_date:
		frappe.throw("Book Issue ID or Return Date is missing.")

	issue_doc = frappe.get_doc("Book Issue", name)

	if issue_doc.status == "Returned":
		frappe.throw("This book has already been returned.")

	return_date = getdate(return_date)
	due_date = getdate(issue_doc.due_date)

	issue_doc.status = "Returned"
	issue_doc.return_date = return_date
	issue_doc.fine_amount = 0

	if return_date > due_date:
		fine_per_day = frappe.db.get_single_value(
			"Library Settings",
			"fine_per_day"
		) or 0

		overdue_days = date_diff(return_date, due_date)

		if overdue_days > 0:
			issue_doc.fine_amount = fine_per_day * overdue_days

			create_fine_management_entry(issue_doc, overdue_days)

	issue_doc.save(ignore_permissions=True)

	book = frappe.get_doc("Books", issue_doc.book)
	book.available_copies += 1
	if book.available_copies > 0:
		book.status = "Available"
		
	book.save(ignore_permissions=True)

	return {
		"success": True,
		"fine_amount": issue_doc.fine_amount or 0
	}

def create_fine_management_entry(doc, overdue_days):
	if not overdue_days:
		return

	if frappe.db.exists(
		"Fine Management",
		{"book_issue": doc.name}
	):
		return

	new_fine = frappe.new_doc("Fine Management")
	new_fine.member = doc.member
	new_fine.book_issue = doc.name
	new_fine.overdue_days = overdue_days
	new_fine.fine_amount = doc.fine_amount
	new_fine.status = "Pending"

	new_fine.insert(ignore_permissions=True)
