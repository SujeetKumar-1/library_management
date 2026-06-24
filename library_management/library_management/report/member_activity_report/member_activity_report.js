// Copyright (c) 2026, Sujeet and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Member Activity Report"] = {
	"filters": [
		{
			"fieldname": "member",
			"fieldtype": "Link",
			"label": "Library Member",
			"options": "Member"
		},
		{
			"fieldname": "status",
			"fieldtype": "Select",
			"label": "Status",
			"options": "\nIssued\nReturned\nOverdue"
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
