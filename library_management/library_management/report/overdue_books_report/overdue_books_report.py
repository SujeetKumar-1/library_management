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
			"fieldname": "book",
			"fieldtype": "Data",
			"label": "Book Name"
		},
		{
			"fieldname": "member",
			"fieldtype": "Data",
			"label": "Member"
		},
		{
			"fieldname": "due_date",
			"fieldtype": "Data",
			"label": "Due Date"
		},
		{
			"fieldname": "days_overdue",
			"fieldtype": "Data",
			"label": "Days Overdue"
		},
	]

	return cols
def get_data(filters, conditions):
	data = frappe.db.sql(f"""
		SELECT
			book,
			member,
			due_date,
			DATEDIFF(CURDATE(), due_date) AS days_overdue
		FROM `tabBook Issue`
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
	
	conditions = f" WHERE due_date BETWEEN '{from_date} 00:00:00' AND '{to_date} 23:59:00'"

	if filters.get("book"):
		book = filters.get("book")
		conditions += f" AND book = '{book}'"
	
	if filters.get("member"):
		member = filters.get("member")
		conditions += f" AND member = '{member}'"
	
	return conditions
