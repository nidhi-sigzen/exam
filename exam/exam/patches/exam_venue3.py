import frappe

def execute():
    
    if not frappe.get_meta("Student Exam Document 1").get_field("exam_venue"):
        custom_field = frappe.get_doc({
            "doctype": "Custom Field",
            "dt": "Student Exam Document 1",
            "fieldname": "exam_venue",
            "label": "Exam Venue",
            "fieldtype": "Data"
        })
        custom_field.insert()

   
    student_exams = frappe.get_all("Student Exam Document 1", filters={})
    for exam in student_exams:
        if not exam.get("exam_venue"):
            frappe.db.set_value("Student Exam Document 1", exam.name, "exam_venue", "Class 1")
