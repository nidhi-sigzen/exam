# Copyright (c) 2023, exam and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MockExam1(Document):
    pass

@frappe.whitelist()
def update_questions(subject):
    print("edrfghujikljhugytfdeswdfgthuji")
    items=[]
    list=frappe.get_list("Questions" , filters={"subject":subject} , fields=["questions"])
    return list




@frappe.whitelist()
def calculate_obtained_marks(mock_exam_doc):
    
    mock_exam = frappe.db.get_list("Mock Exam 1", mock_exam_doc)

    obtained_marks = 0
    
 
    for child in mock_exam.questions:
        question = child.question
        user_answer = child.answer

        
        correct_answer = frappe.db.get_value("Questions", {"questions": question}, "answers")
        print("nidhi")
   
        if user_answer == correct_answer:
            obtained_marks += 5  
   
    mock_exam.obtained_marks = obtained_marks
    mock_exam.save()

