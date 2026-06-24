# Copyright (c) 2026, Sujeet and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import today, add_to_date

def execute(filters=None):
	columns = get_columns()
	conditions = get_conditon(filters)
	data = get_data(filters, conditions)
	
	return columns, data

def get_columns():
	cols = [
		{
			"fieldname": "member",
			"fieldtype": "Data",
			"label": "Member"
		},
		{
			"fieldname": "fine_amount",
			"fieldtype": "Currency",
			"label": "Fine Amount"
		},
		{
			"fieldname": "status",
			"fieldtype": "Data",
			"label": "Status"
		}
	]

	return cols

def get_data(filters, conditions):
	data = frappe.db.sql(f"""
		SELECT
			
			member, fine_amount, status
			
		FROM `tabFine Management`
		{conditions}
	""", as_dict=1)

	return data

def get_conditon(filters):
	from_date = filters.get("from_date")
	to_date = filters.get("to_date")
	if from_date and to_date:
		if from_date > to_date:
			frappe.throw(f"From date({from_date}) must earlier then To date({to_date})")
	
	if not to_date:
		to_date = today()
	
	if not from_date:
		from_date = add_to_date(to_date, days=-7)
	
	conditions = f" WHERE creation BETWEEN '{from_date} 00:00:00' AND '{to_date} 23:59:00'"

	if filters.get("status"):
		status = filters.get("status")
		conditions += f" AND status = '{status}'"
	
	if filters.get("member"):
		member = filters.get("member")
		conditions += f" AND member = '{member}'"
	
	return conditions
