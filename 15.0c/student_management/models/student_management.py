
from odoo import models, fields, api

class StudentManagement(models.Model):

    _name = 'student.management'
    _description = 'student_management'

    # name = fields.Many2one('hr.employee', string="Project2 student")
    sid = fields.Integer(string="Student ID", required=True)
    admission_year = fields.Date(string="Admission Year", required=True)

    sfirst_name = fields.Char(string="First Name")
    smiddle_name = fields.Char(string="Middle Name")
    slast_name = fields.Char(string="Last Name")

    student_address = fields.Char(string="Student Address")
    student_dob = fields.Date(string="Date Of Birth")
    student_age = fields.Integer(string="Age")
    mother_tung_lang = fields.Selection(string="Mother Tung Language",
    selection=[('gujarati', 'Gujarati'), ('hindi', 'Hindi'), ('english', 'English')],
    help='Select student mother tung language')

    student_contact_name = fields.Char(string="Person Name")
    student_contact_no = fields.Integer(string="Contact Number")
    student_email = fields.Char(string="Contact E-mail")
