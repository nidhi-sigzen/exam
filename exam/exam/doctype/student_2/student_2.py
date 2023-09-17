# Copyright (c) 2023, exam and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Student2(Document):
	pass



def before_insert(doc, method):
   
    if doc.doctype == "Student 2":
        
        student_name = doc.student_name
        user = frappe.new_doc("User")
        user.update({
            "email": student_name + "@gmail.com",
            "first_name": frappe.utils.get_fullname(student_name),
            "new_password": "Sigzen@123#",
            "user_type":"System User"
            
        })
        user.insert()
        user.add_roles("Student")
