import frappe



@frappe.whitelist()
def get_permission_query_for_examresult(user=None):
    if not user:
        user = frappe.session.user
    user_roles = frappe.get_roles(user)
    if user != 'Administrator' and 'Student' in user_roles:
        
        conditions=""" (`tabMock Exam Result 1`.owner = '{user}')""".format(user=user)
        return conditions
    else:
        pass
    
@frappe.whitelist()
def get_permission_query_for_exam(user=None):
    if not user:
        user = frappe.session.user
    user_roles = frappe.get_roles(user)
    if user != 'Administrator' and 'Student' in user_roles:
        
        conditions=""" (`tabMock Exam 1`.owner = '{user}')""".format(user=user)
        return conditions
    else:
        pass
    
    
@frappe.whitelist()
def get_permission_query_for_student(user=None):
    if not user:
        user = frappe.session.user
    name=user_name(user)
    user_roles = frappe.get_roles(user)
    if user != 'Administrator' and 'Student' in user_roles:
        
        conditions=""" (`tabStudent 2`.student_name = '{name}')""".format(name=name)
        return conditions
    else:
        pass
    
def user_name(user):
    doc=frappe.get_doc("User",user)
    full_name=doc.full_name
    return full_name
    