// Copyright (c) 2026, Sujeet and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Overdue Books Report"] = {
	"filters": [
		{
			"fieldname": "book",
			"fieldtype": "Link",
			"label": "Book Name",
			"options": "Books"
		},
		{
			"fieldname": "member",
			"fieldtype": "Link",
			"label": "Library Member",
			"options": "Library Member"
		},
		{
			"fieldname": "from_date",
			"fieldtype": "Date",
			"label": "From Date",
		},
		{
			"fieldname": "to_date",
			"fieldtype": "Date",
			"label": "To Date",
		},
	]
};
