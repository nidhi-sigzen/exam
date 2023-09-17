# Copyright (c) 2023, exam and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns = get_columns()
    data = calculate_subject_averages(filters)
    return columns, data


def get_columns():
    columns = [
        {
            "fieldname": "subject",
            "label": "Subject",
            "fieldtype": "Data",
            "width":200
        },
        {
            "fieldname": "average_marks",
            "label": "Average marks",
            "fieldtype": "Float",
            "width":200
        },
    ]
    return columns


def calculate_subject_averages(filters=None):
    subject_averages = {}
    filter_list = []
    
    if filters.get("subject"):
        filter_list.append({"subject": filters["subject"]})
    
    marks = frappe.get_all("Mock Exam Result 1",filters=filter_list, fields=["subject", "obtained_marks"])

   
    for mark in marks:
        subject = mark.get("subject")
        marks_obtained = mark.get("obtained_marks")

        
        if subject not in subject_averages:
            subject_averages[subject] = {"total_marks": 0, "count": 0}

        
        subject_averages[subject]["total_marks"] += marks_obtained
        subject_averages[subject]["count"] += 1

    
    for subject, data in subject_averages.items():
        average = data["total_marks"] / data["count"]
        subject_averages[subject]["average_marks"] = average  

    
    data = [{"subject": subject, "average_marks": data["average_marks"]} for subject, data in subject_averages.items()]

    return data
