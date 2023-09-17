# Copyright (c) 2023, exam and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MockExam1(Document):
    def on_submit(self):
        count=0
        for answer in self.questions:
            correct_answer=frappe.get_list("Questions",filters={"questions":answer.question},fields=["answers"])
            if(answer.answer ==correct_answer[0]["answers"]):
                count+=5
        self.obtained_marks=count 
        new_doc=frappe.new_doc("Mock Exam Result 1")
        new_doc.student=self.student_name   
        new_doc.obtained_marks=self.obtained_marks
        new_doc.mock_exam=self.name
        new_doc.subject=self.subject
        new_doc.submission_time = frappe.utils.now()
        new_doc.total_marks=self.total_marks
        new_doc.submit()  
        
        
@frappe.whitelist()
def update_questions(subject):
    items=[]
    list=frappe.get_list("Questions" , filters={"subject":subject} , fields=["questions"])
    return list




