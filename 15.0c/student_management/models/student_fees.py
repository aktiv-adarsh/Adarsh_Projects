from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import date


class StudentFees(models.Model):
    _name = 'student.fees'
    _description = 'student_fees'

    fees_student_id = fields.Many2one('student.management', string="Student ID", required=True)
    fees_student_name = fields.Char(related='fees_student_id.sfirst_name', string="Student Name")
    fees_student_dob = fields.Date(related='fees_student_id.student_dob', string="Student DOB")
    fees_student_gender = fields.Selection(related='fees_student_id.student_gender', string="Student Gender")

    fees_student_class = fields.Integer(related='fees_student_id.student_class', string="Student Class")
    fees_student_division = fields.Selection(related='fees_student_id.student_division', string="Student Division")
    fees_student_medium = fields.Selection(related='fees_student_id.student_medium', string="Student Medium")
    fees_admission_year = fields.Date(related='fees_student_id.admission_year', string="Admission Year")

    fees_student_fee = fields.Integer(related='fees_student_id.student_fee', string="Standard Fees")
    fees_student_paid_fees = fields.Integer(related='fees_student_id.student_paid_fees', string="Paid Fees")

    #
    # fees_student_contact_name = fields.Char(related='fees_student_id.student_contact_name', string="Parent Name")
    # fees_student_contact_no = fields.Char(related='fees_student_id.student_contact_no', string="Contact No.")
    # fees_student_email = fields.Char(related='fees_student_id.student_email', string="Email Address")
