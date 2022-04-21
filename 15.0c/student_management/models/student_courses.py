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
    course_credit = fields.Integer(string="Subject Credit", tracking=True)
    subject_code = fields.Integer(string="Subject Code", required=True, tracking=True)

    """sql_cons.. will generate unique course id"""
    _sql_constraints = [
        ('subject_code_unique', 'unique (subject_code)', "Subject code Must Be Unique !")
    ]