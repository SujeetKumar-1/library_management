# Copyright (c) 2026, Sujeet and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Books(Document):
	def validate(self):
		if self.is_new():
			if not self.available_copies:
				self.available_copies = self.total_copies

		if self.available_copies <= 0:
			self.status = "Out of Stock"
		else:
			self.status = "Available"
