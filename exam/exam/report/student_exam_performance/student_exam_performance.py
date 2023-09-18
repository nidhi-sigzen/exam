# Copyright (c) 2023, exam and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    
    
    columns=get_columns()
    data = exam_performance(filters)
    chart = get_chart_data(filters)
    
    return columns, data, "Student Exam Performance",chart


def get_columns():
    columns = [

        {
            "fieldname": "subject",
            "label": ("Subject"),
            "fieldtype": "Data",
            "width":200,
            
        },
        {
            "fieldname": "student",
            "label": ("Student Name"),
            "fieldtype": "Data",
            "width":200
        },
        {
            "fieldname": "obtained_marks",
            "label": ("Obtained Marks"),
            "fieldtype": "Data",
            "width":200
        }
        
    ]
    return columns

def exam_performance(filters=None):
    data = []
    filter_list=[]
    
    if filters.get("student"):
        filter_list.append({"student": filters["student"]})
        
    avg_marks = frappe.db.get_list("Mock Exam Result 1", filters=filter_list, fields=["subject","student", "obtained_marks"])
    for marks in avg_marks:
            

            row = {
                "subject": marks.subject,
                "student": marks.student,
                "obtained_marks": marks.obtained_marks
                
            }
            data.append(row)
            
    return data

def get_chart_data(filters=None):
    print(filters.student)
    chart_data=[]
    filter_list=[]
    if filters.student:
        filter_list.append({"student": filters["student"]})
        
        
    avg_marks = frappe.db.get_list("Mock Exam Result 1", filters=filter_list,fields=["subject","student","student_name", "obtained_marks"])
    for marks in avg_marks:
        chart_data.append(
            {
                'label': marks.student,
                'obtained_marks': marks.obtained_marks
            }
        )
    chart = {
        "data": {
            "labels": [data['label'] for data in chart_data],
            "datasets": [
                {
                    "name": ("Obtained Marks"),
                    "values": [data['obtained_marks'] for data in chart_data],
                }
            ]
        },
        "type": "bar",
        "colors": ["#228B22","#2947ff", "#f44336", "#aeff62", "#e91e63", "#9c27b0", "#743ee2", "#006400","#00FFFF"],
    }
    return chart

