// Copyright (c) 2023, exam and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Student Exam Performance"] = {
	"filters": [
		{
			"fieldname": "student",
			"label": "Student",
			"fieldtype": "Link",
			"options": "Student 2"
		},
	]
};
