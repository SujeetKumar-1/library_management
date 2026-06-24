# Copyright (c) 2026, Sujeet and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class FineManagement(Document):
	def validate(self):
		self.paid_amount = self.paid_amount or 0
		self.waiver_amount = self.waiver_amount or 0

		if self.paid_amount < 0:
			frappe.throw("Paid Amount cannot be negative.")

		if self.waiver_amount < 0:
			frappe.throw("Waiver Amount cannot be negative.")

		if self.waiver_amount and not self.waiver_reason:
			frappe.throw("Please add a valid readon for waiver.")

		total_adjustment = (
			self.paid_amount +
			self.waiver_amount
		)

		if total_adjustment > self.fine_amount:
			frappe.throw(
				"Paid + Waiver Amount cannot exceed Fine Amount."
			)

		self.outstanding_amount = (
			self.fine_amount -
			total_adjustment
		)

		if self.outstanding_amount == 0:

			if self.waiver_amount == self.fine_amount:
				self.status = "Waived"
			else:
				self.status = "Paid"

		elif self.paid_amount > 0:
			self.status = "Partially Paid"

		else:
			self.status = "Pending"
			
	def after_insert(self):
		if self.member:
			member_doc = frappe.get_doc(
				"Library Member",
				self.member
			)

			member_doc.outstanding_fine = (
				member_doc.outstanding_fine or 0
			) + self.fine_amount

			member_doc.save(ignore_permissions=True)

	    
	def on_update(self):
		doc_before_save = self.get_doc_before_save()
		if doc_before_save:
			if self.status != "Pending":
				update_member_outstanding_amount(self, doc_before_save)

def update_member_outstanding_amount(doc, old_doc):
	if not doc.member or not frappe.db.exists("Library Member", doc.member):
		return
	
	member = frappe.get_doc("Library Member", doc.member)

	outstanding_fine = member.outstanding_fine or 0

	old_adjustment = (old_doc.paid_amount or 0) + (old_doc.waiver_amount or 0)
	new_adjustment = (doc.paid_amount or 0) + (doc.waiver_amount or 0)

	delta = new_adjustment - old_adjustment

	if delta <= 0:
		return

	member.outstanding_fine = max(
		outstanding_fine - delta,
		0
	)
	
	member.save(ignore_permissions=True)
