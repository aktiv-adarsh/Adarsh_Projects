from odoo import models, fields, api, _


# from odoo.exceptions import UserError


# from datetime import date

class StudentFees(models.Model):
    _name = 'student.fees'
    _description = 'student_fees'

    fees_sid = fields.Integer(string="Student ID")
    fees_student_name = fields.Char(string="Student Name")
    fees_student_class = fields.Integer(string="Student Class")
    fees_student_medium = fields.Char(string="Student Medium")
    fees_student_dob = fields.Date(string="Student DOB")

    # @api.onchange('fees_sid')
    def save_button(self):
        rec = self.env['student.management'].browse(self.env.context.get('active_id'))
        print("\n --------Fees save_button ---------", rec, "\n")
        # for rec in self:
        print("-------------In For loop---------------")
        record.write({
            "fees_sid": rec.sid,
            "fees_student_name": rec.sfirst_name,
            "fees_student_class": rec.student_class,
            "fees_student_medium": rec.student_medium,
            "fees_student_dob": rec.student_dob
        })
        print("-------------", rec, "---------------")

# @api.model
# def default_get(self, fields):
#     # current_id = self.env.context.get('active_model')
#     res = super(StudentFees, self).default_get(fields)
#     print("\n --------Fees default get ---------", res, "\n")
#     rec = self.env['student.management'].browse(self.env.context.get('active_id'))
#     res.update({
#         "fees_sid": rec.sid,
#         "fees_student_name": rec.sfirst_name,
#         "fees_student_class": rec.student_class,
#         "fees_student_medium": rec.student_medium,
#         "fees_student_dob": rec.student_dob
#     })
#     return res
