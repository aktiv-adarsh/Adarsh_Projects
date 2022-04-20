from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import date, datetime


class StudentManagement(models.Model):
    _name = 'student.management'
    _description = 'student_management'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'student_id'

    student_img = fields.Binary()
    student_id = fields.Integer(string="Student ID", tracking=True)  # , compute="_student_id_generate")
    admission_year = fields.Date(string="Admission Year", tracking=True)
    student_class = fields.Integer(string="Student Class", tracking=True)
    student_fee = fields.Integer(string="Fees", compute="_student_fees_calc")

    student_medium = fields.Selection(string="Medium", selection=[('gujarati1', 'Gujarati'), ('hindi1', 'Hindi'),
                                                                  ('english1', 'English')],
                                      help='Select standard medium for study', tracking=True)
    student_division = fields.Selection([('a', 'A'), ('b', 'B'), ('c', 'C')], string="Division",
                                        help='Select student Division', tracking=True)
    student_paid_fees = fields.Integer(string="Paid Fees")  # , compute="_student_fees_calc")
    student_pending_fees = fields.Integer(string="Pending Fees", compute="_calculate_panding_fees")

    sfirst_name = fields.Char(string="First Name", tracking=True)
    smiddle_name = fields.Char(string="Middle Name", tracking=True)
    slast_name = fields.Char(string="Last Name", tracking=True)

    student_email = fields.Char(string="E-mail", tracking=True)
    student_phone = fields.Char(string="Phone", tracking=True)
    student_mobile = fields.Char(string="Mobile", tracking=True)

    student_address = fields.Char(string="Student Address", tracking=True)
    student_dob = fields.Date(string="Date Of Birth", tracking=True)
    student_gender = fields.Selection(string="Gender", selection=[('male', 'Male'), ('female', 'Female')],
                                      tracking=True)
    student_age = fields.Integer(string="Age", tracking=True, readonly=True)
    mother_tung_lang = fields.Selection(string="Mother Tung Language",
                                        selection=[('gujarati', 'Gujarati'), ('hindi', 'Hindi'),
                                                   ('english', 'English')],
                                        help='Select student mother tung language', tracking=True)

    student_contact_name = fields.Char(string="Parent Name", tracking=True)
    student_contact_no = fields.Integer(string="Contact No.", tracking=True)
    student_contact_email = fields.Char(string="E-mail", tracking=True)

    # course_ids = fields.One2many('student.courses', 'student_course_id', string="Student_Courses")
    student_course_id = fields.Many2many('student.courses', string="Student Course")

    @api.onchange('student_fee', 'student_paid_fees')
    def _calculate_panding_fees(self):
        for rec in self:
            rec.student_pending_fees = rec.student_fee - rec.student_paid_fees

    """Set and calculate(paid and pending fee)"""
    @api.onchange('student_class')
    def _student_fees_calc(self):
        student_std_fees = {'1': 1000, '2': 2000, '3': 3500, '4': 4500,
                            '5': 5500, '6': 6999, '7': 7999, '8': 8999, '9': 9999, '10': 10999, '11': 11999,
                            '12': 12999}
        for std, fee in student_std_fees.items():
            std = int(std)
            for rec in self:
                if rec.student_class == std:
                    rec.student_fee = fee

    """Though exceptions when standard > 12"""

    @api.onchange('student_class')
    def student_class_check(self):
        if int(self.student_class) > 13:
            raise UserError("Please enter class between 1 to 12")

    """Calculate student age by DOB"""

    @api.onchange('student_dob')
    def calc_stu_age(self):
        if self.student_dob:
            today_date1 = fields.Date.today()
            self.student_age = (today_date1 - self.student_dob).days / 365
        else:
            print("\n\n\n ------Student DOB Else------\n\n\n\n")
            self.student_age = 0

    def smart_button(self):
        print("\n\n --------- smart_button---------\n\n")


class StudentCourses(models.Model):
    _name = 'student.courses'
    _description = 'student_courses'

    # student_course_id = fields.Many2one('student.management', string="Student Course")

    # course_ids = fields.Many2one('student.management', 'student_course_id', string="Student_Courses")
    name = fields.Char(string="Course Name")
    # subject = fields.Selection([('maths', 'Maths'), ('sci', 'Science')])
    subject_code = fields.Integer(string="Subject Code")

    _sql_constraints = [
        ('subject_code_unique', 'unique (subject_code)', "Subject code Must Be Unique !")
    ]
    #
    # @api.model_create_multi
    # # @api.model
    # def create(self, vals):
    #     super(StudentManagement, self).create(vals)
    #     count = 1
    #     self.student_id = "{0:0^5}".format("2022" + str(count))
    #     # "{0:0^5}".format("2022" + str(count))
    #     # print("{0:0^2}".format("", 2022))
    #     # print("{0:*^20} was founded in {1:<15}!".format("GeeksforGeeks", 2009))
    #     count += 1

    # def _student_id_generate(self):
    #     student_id = "2022"
    #     global count
    #     if self.student_class:
    #         #     # for check_std in range(13):
    #         #     if self.student_class == check_std:
    #         # print("\n\n -------- ", check_std, type(check_std))
    #         self.student_id = student_id + str(count)
    #         count += 1
