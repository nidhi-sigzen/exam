// Copyright (c) 2023, exam and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Average Mark"] = {
	"filters": [
        {
			"fieldname": "subject",
			"label": "Subject",
			"fieldtype": "Link",
			"options": "Subject"
		},
	]
};
