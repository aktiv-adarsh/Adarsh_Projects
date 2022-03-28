
from odoo import models, fields, api, _

class StudentManagement(models.Model):

    _name = 'student.management'
    _description = 'student_management'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    sid = fields.Integer(string="Student ID", tracking=True, required=True)
    admission_year = fields.Date(string="Admission Year", tracking=True)

    sfirst_name = fields.Char(string="First Name", tracking=True)
    smiddle_name = fields.Char(string="Middle Name", tracking=True)
    slast_name = fields.Char(string="Last Name", tracking=True)

    student_address = fields.Char(string="Student Address", tracking=True)
    student_dob = fields.Date(string="Date Of Birth", tracking=True)
    student_gender = fields.Selection(string="Gender", selection=[('male', 'Male'), ('female', 'Female')], tracking=True)
    student_age = fields.Integer(string="Age", tracking=True)
    mother_tung_lang = fields.Selection(string="Mother Tung Language",
                                        selection=[('gujarati', 'Gujarati'), ('hindi', 'Hindi'), ('english', 'English')],
                                        help='Select student mother tung language', tracking=True)

    student_contact_name = fields.Char(string="Person Name", tracking=True)
    student_contact_no = fields.Integer(string="Contact Number", tracking=True)
    student_email = fields.Char(string="Contact E-mail", tracking=True)
