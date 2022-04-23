from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import date, datetime


class StudentCourses(models.Model):
    """Created New model 'student.course' to use relations on student.man"""

    _name = 'student.courses'
    _description = 'student_courses'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # student_course_id = fields.Many2one('student.management', string="Student Course")

    # course_ids = fields.Many2one('student.management', 'student_course_id', string="Student_Courses")
    student_img = fields.Binary()
    name = fields.Char(string="Subject Name", required=True, tracking=True)
    subject_code = fields.Integer(string="Subject Code", required=True, tracking=True)

    course_credit = fields.Integer(string="Subject Credit", tracking=True)
    course_student_mark = fields.Integer(string="Mark", default=100)
    course_student_required_mark = fields.Integer(string="Required Mark", default=32)
    course_student_obtain_mark = fields.Integer(string="Obtain Mark")

    course_student_mark_sum = fields.Integer(string="Mark Total")
    course_student_mark_avg = fields.Integer(string="Mark Total")
    course_student_exam_status = fields.Char(string="Mark Total")

    """sql_cons.. will generate unique course id"""
    _sql_constraints = [
        ('subject_code_unique', 'unique (subject_code)', "Subject code Must Be Unique !")
    ]

    @api.depends('course_student_obtain_mark')
    def student_mark_checking_check(self):
        """Though exceptions when standard > 12"""

        if int(self.course_student_obtain_mark) < 32:
            self.course_student_exam_status = "Sorry! You have not cleared this exam"
            print("\n\n", self.course_student_exam_status)
        else:
            self.course_student_exam_status = "You have Pass exam successfully"
            print("\n\n", self.course_student_exam_status)

    # @api.onchange('student_mark')
    # def calc_student_marks(self):
    #     print("\n\n--------In Func----\n")
    #     for rec in self.student_mark:
    #         rec.student_mark_total += rec
    #         print("\n\n-----Res--", rec.student_mark_total)
