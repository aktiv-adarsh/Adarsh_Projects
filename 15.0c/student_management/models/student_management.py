from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import date, datetime
from odoo.tools.misc import xlwt
from xlwt import easyxf
from io import BytesIO
import base64


class StudentManagement(models.Model):
    _name = 'student.management'
    _description = 'student_management'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'student_id'

    student_img = fields.Binary()
    excel_file = fields.Binary(string="Excel File")

    student_id = fields.Integer(string="Student ID", tracking=True, required=True)  # , compute="_student_id_generate")
    admission_year = fields.Date(string="Admission Year", tracking=True)
    # student_class = fields.Char(string="Student Class", tracking=True)
    student_college = fields.Selection([('sal', 'SAL')], default="sal", string="College",
                                       help='Select student Department', tracking=True)
    student_class = fields.Selection(
        [('computer', 'Computer Engineering'), ('it', 'IT Engineering'), ('mechanical', 'Mechanical Engineering'),
         ('civil', 'Civil Engineering'), ('automobile', 'Automobile Engineering')], string="Department",
        help='Select student Department', tracking=True, required=True)
    student_sem = fields.Selection(
        [('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8)],
        string="Semester", help='Select student Semester', tracking=True)

    # student_medium = fields.Selection(string="Medium", selection=[('gujarati1', 'Gujarati'), ('hindi1', 'Hindi'), ('english1', 'English')], help='Select standard medium for study', tracking=True)
    student_division = fields.Selection([('a', 'A'), ('b', 'B'), ('c', 'C')], string="Division",
                                        help='Select student Division', tracking=True)
    student_fee = fields.Integer(string="College Fees", compute="_compute_fees_calc", tracking=True)
    student_paid_fees = fields.Integer(string="Paid Fees", tracking=True)  # , compute="_student_fees_calc")
    student_pending_fees = fields.Integer(string="Pending Fees", compute="_compute_pending_fees", tracking=True)

    sfirst_name = fields.Char(string="First Name", tracking=True, required=True)
    smiddle_name = fields.Char(string="Middle Name", tracking=True)
    slast_name = fields.Char(string="Last Name", tracking=True)

    student_email = fields.Char(string="E-mail", tracking=True, required=True)
    student_phone = fields.Char(string="Phone", tracking=True)
    student_mobile = fields.Char(string="Mobile", tracking=True)

    student_address = fields.Char(string="Student Address", tracking=True)
    student_state = fields.Many2one('res.country.state', string="State", tracking=True)
    student_country = fields.Many2one('res.country', string="Country", tracking=True, readonly=True)
    student_dob = fields.Date(string="Date Of Birth", tracking=True)
    student_gender = fields.Selection(string="Gender", selection=[('male', 'Male'), ('female', 'Female')],
                                      tracking=True)
    student_age = fields.Integer(string="Age", tracking=True, readonly=True, compute="calc_stu_age")
    mother_tung_lang = fields.Selection(string="Mother Tung Language",
                                        selection=[('gujarati', 'Gujarati'), ('hindi', 'Hindi'),
                                                   ('english', 'English')], help='Select student mother tung language',
                                        tracking=True)

    student_contact_name = fields.Char(string="Parent Name", tracking=True, required=True)
    student_contact_no = fields.Integer(string="Contact No.", tracking=True)
    student_contact_email = fields.Char(string="E-mail", tracking=True, required=True)
    student_parent_gender = fields.Selection(string="Gender", selection=[('male', 'Male'), ('female', 'Female')],
                                             tracking=True)

    # course_ids = fields.One2many('student.courses', 'student_course_id', string="Student_Courses")
    student_course_id = fields.Many2many('student.courses', string="Student Course")
    student_holidays = fields.Many2one('student.events', string="Student Course")
    student_mark_average = fields.Integer(compute="_compute_mark_avg")
    course_student_exam_status = fields.Char(string="Exam Status")#, compute="compute_student_result_status")

    _sql_constraints = [
        ('student_id_unique', 'unique (student_id)', "This id ID already exist! ")
    ]

    @api.onchange("student_state")
    def check_country(self):
        if self.student_state:
            for rec in self:
                rec.student_country = rec.student_state.country_id

    @api.onchange('student_course_id')
    def _compute_mark_avg(self):
        """It will compute student percentage"""
        count = 0
        percentage = 0
        total = 0
        if self.student_course_id:
            for rec in self.student_course_id:
                print("\n\n--student_course_id------", rec.name, "-----\n\n")
                print("\n\n----course_student_obtain_mark----", rec.course_student_obtain_mark, "-----\n\n")
                total += rec.course_student_obtain_mark
                count += 1
            # self.student_mark_average = int(total) / count
            percentage = int(total) / count
            print("\n\n--==** -- percentage------", percentage, "-----\n\n")
            self.student_mark_average = (percentage * 100) / 70
            print("\n\n--==** -- student_mark_average------", self.student_mark_average, "-----\n\n")
        else:
            self.student_mark_average = 0

    @api.onchange('student_course_id')
    def compute_student_result_status(self):
        """Display Pass/Fail msg or Though exceptions when standard > 70"""
        # if self.student_course_id:
        for rec in self.student_course_id:
            if int(rec.course_student_obtain_mark) < 23:
                self.course_student_exam_status = "Sorry! You have not cleared this exam"
                print("\n\n", self.course_student_exam_status)
                break
            elif int(rec.course_student_obtain_mark) > 70:
                raise UserError(_('The Mark must be < 70.'))
            else:
                self.course_student_exam_status = "Congratulations..You have successfully Pass the exam"
                print("\n\n", self.course_student_exam_status)

    @api.depends('student_fee', 'student_paid_fees')
    def _compute_pending_fees(self):
        """Calculate pending fees only"""

        for rec in self:
            if rec.student_fee:
                rec.student_pending_fees = rec.student_fee - rec.student_paid_fees
            else:
                rec.student_pending_fees = 0

    @api.onchange('student_class')
    def _compute_fees_calc(self):
        """Set and calculate only paid fees"""

        student_std_fees = {'computer': 60000, 'it': 65000, 'mechanical': 50000, 'civil': 56000,
                            'automobile': 67000}
        for rec in self:
            if rec.student_class:
                rec.student_fee = student_std_fees[str(rec.student_class)]
                print("\n\n-----------------IF-----------------\n\n")
            else:
                print("\n-----------------???-----------------\n")
                rec.student_fee = 0

    # @api.onchange('student_class')
    # def student_class_check(self):
    #   """This fun was written for student class. At a time helpless."""
    #     """Though exceptions when standard > 12"""
    #
    #     if len(self.student_class) > 13:
    #         raise UserError("Please enter class between 1 to 12")
    #     else:
    #         print("\n\n\n --------- \n\n\n")

    @api.onchange('student_dob')
    def calc_stu_age(self):
        """Calculate student age by DOB"""

        if self.student_dob:
            today_date1 = fields.Date.today()
            self.student_age = (today_date1 - self.student_dob).days / 365
        else:
            print("\n\n\n ------Student DOB Else------\n\n\n\n")
            self.student_age = 0

    # def smart_button(self):
    #     print("\n\n --------- smart_button---------\n\n")

    def server_action_generate_excel_report(self):
        """Here, Func will generate excel report of all student"""

        print("\n\n --------- Server Actions---------\n\n")

        filename = 'Student_Report.xls'
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet("Report1")
        header_style = easyxf('font:height 500; align: horiz center;font:bold True;')
        font_style = easyxf('font:height 200; align: horiz center;font:bold True;')
        sheet_data_style = easyxf('font:height 200; align: horiz center;')

        Row1 = 2
        Row2 = 3
        Col1 = 0
        Col2 = 8
        print("\n ---- Reach after var----\n")
        worksheet.write_merge(Row1, Row2, Col1, Col2, "Students Report", header_style)

        worksheet.col(0).width = 2000
        Row = 7
        Col = 0
        worksheet.col(0).width = 256 * 12
        worksheet.write(Row, Col, 'Student ID', font_style)

        Col += 1
        worksheet.col(1).width = 256 * 17
        worksheet.write(Row, Col, 'Admission Year', font_style)

        Col += 1
        worksheet.col(2).width = 256 * 22
        worksheet.write(Row, Col, 'Name', font_style)

        Col += 1
        worksheet.col(3).width = 256 * 12
        worksheet.write(Row, Col, 'College', font_style)

        Col += 1
        worksheet.col(4).width = 256 * 20
        worksheet.write(Row, Col, 'Department', font_style)

        Col += 1
        worksheet.write(Row, Col, 'Division', font_style)
        #
        # Col += 1
        # worksheet.write(Row, Col, 'Medium', font_style)

        Col += 1
        worksheet.col(6).width = 256 * 15
        worksheet.write(Row, Col, 'College Fees', font_style)

        Col += 1
        worksheet.col(7).width = 256 * 15
        worksheet.write(Row, Col, 'Paid Fees', font_style)

        Col += 1
        worksheet.col(8).width = 256 * 15
        worksheet.write(Row, Col, 'Pending Fees', font_style)

        total_student = 0
        total_standard_fees = 0
        total_paid_fees = 0
        total_pending_fees = 0

        Row = 9
        """It will get all student data in sequence"""

        for rec in self:
            print("\n\n ---------Rec--", self, "-------\n\n")
            worksheet.write(Row, 0, rec.student_id, sheet_data_style)
            print("\n\n***********rec.student_id == ", rec.student_id, "---")
            total_student += 1

            worksheet.write(Row, 1, str(rec.admission_year), sheet_data_style)
            print("**********rec.admission_year == ", rec.admission_year, "---")

            worksheet.write(Row, 2, rec.sfirst_name, sheet_data_style)
            print("**********rec.sfirst_name == ", rec.sfirst_name, "---")
            print("**********str((rec.sfirst_name == ", str(rec.sfirst_name), "---\n")

            worksheet.write(Row, 3, rec.student_college, sheet_data_style)
            print("**********rec.student_class == ", rec.student_college, "---")

            worksheet.write(Row, 4, rec.student_class, sheet_data_style)
            print("**********rec.student_class == ", rec.student_class, "---")

            worksheet.write(Row, 5, rec.student_division, sheet_data_style)
            print("**********rec.student_division == ", rec.student_division, "---")

            worksheet.write(Row, 6, rec.student_fee, sheet_data_style)
            total_standard_fees += rec.student_fee
            print("**********rec.student_fee == ", rec.student_fee, "---")

            worksheet.write(Row, 7, rec.student_paid_fees, sheet_data_style)
            total_paid_fees += rec.student_paid_fees
            print("**********rec.student_paid_fees == ", rec.student_paid_fees, "---")

            worksheet.write(Row, 8, rec.student_pending_fees, sheet_data_style)
            total_pending_fees += rec.student_pending_fees
            Row += 1
            print("**********rec.student_pending_fees == ", rec.student_pending_fees, "-END--\n\n\n")

        Row += 2
        worksheet.write(Row, 0, "Total: {}".format(total_student), font_style)
        worksheet.write(Row, 6, "Total: {}".format(total_standard_fees), font_style)
        worksheet.write(Row, 7, "Total: {}".format(total_paid_fees), font_style)
        worksheet.write(Row, 8, "Total: {}".format(total_pending_fees), font_style)
        print("\n\n------****rec.total_student == ", total_student, "-END--")
        print("------********rec.total_standard_fees == ", total_standard_fees, "-END--")
        print("------****rec.total_paid_fees == ", total_paid_fees, "-END--")
        print("------****rec.total_pending_fees == ", total_pending_fees, "-END--\n\n\n")

        fp = BytesIO()
        print("****rec.BytesIO() == ", fp, "-END--")
        workbook.save(fp)
        print("****rec.workbook == ", workbook, "-END--")
        print("****rec.workbook == ", workbook.save(fp), "-END--")
        fp.seek(0)
        print("****fp.seek(0) == ", fp.seek(0), "-END--")
        excel_file = base64.encodebytes(fp.getvalue())
        print("****excel_file == ", excel_file, "-END--")
        fp.close()
        print("****fp.close() == ", fp.close(), "-END--")

        self.write({'excel_file': excel_file})
        print("\n****self.write == ", self.write({'excel_file': excel_file}), "-END--")
        print("****self.write == ", excel_file, "-END--\n\n\n\n")

        print("\n\n --------- Self ----\n", self, "-----\n\n")
        print("\n\n --------- Self.id ----\n", self.ids, "-----\n\n")

        url = ('web/content?model=student.management&download=true&field=excel_file&id=%s&filename=%s' % (
            self.ids[0], filename))
        print("\n\n --------- url ----\n", url, "-----\n\n")
        # if self.excel_file:
        return {'type': 'ir.actions.act_url',
                'url': url,
                'target': 'new'
                }


class StudentEvents(models.Model):
    _name = 'student.events'
    _description = 'student_events'

    event_name = fields.Char(string="Festival Name", required=True)
    event_date = fields.Date(string="Festival Date")
