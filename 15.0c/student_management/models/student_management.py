from odoo import models, fields, api, _
from odoo.exceptions import UserError


# from datetime import date

class StudentManagement(models.Model):
    _name = 'student.management'
    _description = 'student_management'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # count = 1
    sid = fields.Integer(string="Student ID", tracking=True, required=True)#, compute="_student_id_generate")
    admission_year = fields.Date(string="Admission Year", tracking=True)

    student_class = fields.Integer(string="Student Class", tracking=True)
    student_medium = fields.Selection(string="Medium",
                                      selection=[('gujarati1', 'Gujarati'), ('hindi1', 'Hindi'),
                                                 ('english1', 'English')],
                                      help='Select standard medium for study', tracking=True)
    student_division = fields.Selection([('a', 'A'), ('b', 'B'), ('c', 'C')], string="Division",
                                        help='Select student Division', tracking=True)

    sfirst_name = fields.Char(string="First Name", tracking=True)
    smiddle_name = fields.Char(string="Middle Name", tracking=True)
    slast_name = fields.Char(string="Last Name", tracking=True)

    student_address = fields.Char(string="Student Address", tracking=True)
    student_dob = fields.Date(string="Date Of Birth", tracking=True)
    student_gender = fields.Selection(string="Gender", selection=[('male', 'Male'), ('female', 'Female')],
                                      tracking=True)
    student_age = fields.Integer(string="Age", tracking=True, readonly=True)
    mother_tung_lang = fields.Selection(string="Mother Tung Language",
                                        selection=[('gujarati', 'Gujarati'), ('hindi', 'Hindi'),
                                                   ('english', 'English')],
                                        help='Select student mother tung language', tracking=True)

    student_contact_name = fields.Char(string="Person Name", tracking=True)
    student_contact_no = fields.Integer(string="Contact Number", tracking=True)
    student_email = fields.Char(string="Contact E-mail", tracking=True)

    student_fee = fields.Integer(string="Fees", compute="_student_fees_calc")#, compute="_student_fees_calc")
    student_paid_fees = fields.Integer(string="Paid Fees")#, compute="_student_fees_calc")
    student_pending_fees = fields.Integer(string="Pending Fees", compute="_student_fees_calc", readonly=True)

    print("-----------------Reach at func---------------")

    @api.onchange('student_class')
    def _student_fees_calc(self):
        student_std_fees = {'1': 1000, '2': 2000, '3': 3500, '4': 4500,
                            '5': 5500, '6': 6999, '7': 7999, '8': 8999, '9': 9999, '10': 10999, '11': 11999,
                            '12': 12999}
        for std, fee in student_std_fees.items():
            std = int(std)
            if self.student_class == std:
                self.student_fee = fee
                self.student_pending_fees = self.student_fee - self.student_paid_fees


    @api.onchange('student_class')
    def student_class_check(self):
        if int(self.student_class) > 13:
            raise UserError("Please enter class between 1 to 12")

    # def _student_id_generate(self):
    #     student_id = "2022"
    #     global count
    #     if self.student_class:
    #         #     # for check_std in range(13):
    #         #     if self.student_class == check_std:
    #         # print("\n\n -------- ", check_std, type(check_std))
    #         self.sid = student_id + str(count)
    #         count += 1

    @api.onchange('student_dob')
    def calc_stu_age(self):
        if self.student_dob:
            today_date1 = fields.Date.today()
            self.student_age = (today_date1 - self.student_dob).days / 365
        else:
            self.student_age = 0
