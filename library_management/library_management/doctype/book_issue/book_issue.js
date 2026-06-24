// Copyright (c) 2026, Sujeet and contributors
// For license information, please see license.txt

frappe.ui.form.on('Book Issue', {
	refresh: function(frm) {
		if (frm.doc.status !== "Returned") {
			frm.add_custom_button(__("Return"), function() {
				submit_return(frm);
			});
		}
	}
});

const submit_return = (frm) => {
	frappe.prompt(
		[
			{
				label: "Return Date",
				fieldname: "return_date",
				fieldtype: "Date",
				reqd: 1,
				default: frappe.datetime.get_today()
			}
		],
		function(values) {
			frappe.call({
				method: "library_management.library_management.doctype.book_issue.book_issue.handle_book_return",
				args: {
					name: frm.doc.name,
					return_date: values.return_date
				},
				callback: function(r) {
					if (!r.exc) {
						frappe.msgprint(__("Book Returned Successfully"));
						frm.reload_doc();
					}
				}
			});
		},
		__("Return Book"),
		__("Submit")
	);
};
