from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import *


class StudentFees(models.Model):
    _name = 'student.fees'
    _description = 'student_fees'

    student_img = fields.Binary()
    fees_student_id = fields.Many2one('student.management', string="Student ID", required=True)
    fees_student_name = fields.Char(related='fees_student_id.sfirst_name', string="Student Name")
    fees_student_dob = fields.Date(related='fees_student_id.student_dob', string="Student DOB")
    fees_student_gender = fields.Selection(related='fees_student_id.student_gender', string="Student Gender")

    fees_student_class = fields.Selection(related='fees_student_id.student_class', string="Student Department")
    fees_student_division = fields.Selection(related='fees_student_id.student_division', string="Student Division")
    fees_student_college = fields.Selection(related='fees_student_id.student_college', string="Student College")
    fees_student_sem = fields.Selection(related='fees_student_id.student_sem', string="Student Semester")
    fees_admission_year = fields.Date(related='fees_student_id.admission_year', string="Admission Year")

    fees_student_fee = fields.Integer(related='fees_student_id.student_fee', string="Standard Fees")
    fees_student_paid_fees = fields.Integer(related='fees_student_id.student_paid_fees', string="Paid Fees")
    fees_date_today = fields.Date(string='Receipt Date', default=str(datetime.now()))


    """sql_cons.. will generate unique fees id"""
    _sql_constraints = [
        ('fees_student_id_unique', 'unique (fees_student_id)', "This id receipt already exist! ")
    ]
    #
    # fees_student_contact_name = fields.Char(related='fees_student_id.student_contact_name', string="Parent Name")
    # fees_student_contact_no = fields.Char(related='fees_student_id.student_contact_no', string="Contact No.")
    # fees_student_email = fields.Char(related='fees_student_id.student_email', string="Email Address")

    # print("\n\n ----------- BEFORE FUNC -----------\n\n")
    #
    # def name_get(self):
    #     """name_get() will display multiple given fields records on one field"""
    #     res = []
    #     print("\n\n ----------- IN FUNC -----------\n\n")
    #     if self._context.get('fees_student_id'):
    #         print("\n\n--------fees_student_name -- ", self.fees_student_name)
    #         for field in self:
    #
    #             if field.fees_student_name == False:
    #                 res.append((field.id, '%s' % (field.fees_student_id)))
    #                 print("\n\n------IF--RES -- ", res)
    #
    #             else:
    #                 res.append(('%s - %s' % (field.fees_student_id, field.fees_student_name)))
    #                 print("\n\n------ELSE--RES -- ", res)
    #
    #         print("\n\n-----Customer country--------", field.fees_student_id)
    #         print("-----Customer Name ------------------", field.fees_student_name)
    #         print("-----Only Field ------------------", field)
    #     else:
    #         for field in self:
    #             res.append((field.id, '%s' % (field.fees_student_name)))
    #     return res
