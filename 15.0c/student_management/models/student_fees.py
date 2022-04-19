from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import date


class StudentFees(models.Model):
    _name = 'student.fees'
    _description = 'student_fees'

    fees_student_id = fields.Many2one('student.management', string="Student ID")
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


    # @api.onchange('fees_student_id')
    # def save_button(self):
    #     rec = self.env['student.management'].browse(self.env.context.get('active_id'))
    #     print("\n --------Fees save_button ---------", rec, "\n")
    #     # for rec in self:
    #     print("-------------In For loop---------------")
    #     record.write({
    #         "fees_student_id": rec.sid,
    #         "fees_student_name": rec.sfirst_name,
    #         "fees_student_class": rec.student_class,
    #         "fees_student_medium": rec.student_medium,
    #         "fees_student_dob": rec.student_dob
    #     })
    #     print("-------------", rec, "---------------")

# @api.model
# def default_get(self, fields):
#     # current_id = self.env.context.get('active_model')
#     res = super(StudentFees, self).default_get(fields)
#     print("\n --------Fees default get ---------", res, "\n")
#     rec = self.env['student.management'].browse(self.env.context.get('active_id'))
#     res.update({
#         "fees_student_id": rec.sid,
#         "fees_student_name": rec.sfirst_name,
#         "fees_student_class": rec.student_class,
#         "fees_student_medium": rec.student_medium,
#         "fees_student_dob": rec.student_dob
#     })
#     return res
