# Copyright (c) 2023, exam and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns=get_columns()
    data = average_mark_data(filters)
    return columns, data


def get_columns():
    columns = [

        {
            "fieldname": "subject_name",
            "label": ("Subject Name"),
            "fieldtype": "Data"
            
        },
        {
            "fieldname": "average_marks",
            "label": ("Average Marks"),
            "fieldtype": "Data",
           
        }
        
    ]
    return columns

def average_mark_data(filters=None):
    data = []
    
    avg_marks = frappe.get_list("Exam Result", filters=[], fields=["subject_name", "average_marks"])
    for marks in avg_marks:
            

            row = {
                "subject_name": marks.subject_name,
                "average_marks": marks.average_marks
                
            }
            data.append(row)
            
    return data