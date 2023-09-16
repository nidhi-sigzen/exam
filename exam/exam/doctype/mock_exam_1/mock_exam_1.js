// Copyright (c) 2023, exam and contributors
// For license information, please see license.txt

frappe.ui.form.on('Mock Exam 1', {
	
	subject: function (frm) {   console.log("hey")
		if (frm.doc.subject) {
		  frappe.call({
			method:
			  "exam.exam.doctype.mock_exam_1.mock_exam_1.update_questions",
			args: {
				subject: frm.doc.subject
			},
			callback: function (r) {
				if (r.message) {
					r.message.forEach(function (i)
					{
						console.log(i)
						frm.add_child(
							'questions',{
								question:i.questions
							}
						)
					})
                    frm.refresh_field("questions")
				}
			  },
		})
	}
}
})
