// Copyright (c) 2026, Sujeet and contributors
// For license information, please see license.txt

frappe.ui.form.on('Fine Management', {
	refresh: function (frm) {
		if (frm.doc.status !== "Paid") {
			frm.add_custom_button(
				"Mark Fully Paid",
				() => {
					frappe.confirm(
						__(
							`Are you sure you want to mark this fine as fully paid?<br><br>
							Fine Amount: ₹${frm.doc.fine_amount}<br>
							Waiver Amount: ₹${frm.doc.waiver_amount || 0}`
						),
						() => {

							frm.set_value(
								"paid_amount",
								(frm.doc.fine_amount || 0) -
								(frm.doc.waiver_amount || 0)
							);

							frm.set_value(
								"payment_date",
								frappe.datetime.nowdate()
							);

							frm.save()
								.then(() => {
									frappe.show_alert({
										message: __("Fine marked as fully paid."),
										indicator: "green"
									});
								});
						}
					);
				}
			);
		}
	}
});
