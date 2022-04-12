
from odoo import models, fields, api
from odoo.tools.misc import xlwt
from xlwt import easyxf
from io import BytesIO
import base64


class HrMenuWizards(models.TransientModel):

    _name = 'excel.wizards'
    _description = 'excel.wizards'

    hr_excel_report_ids = fields.Many2many('hr.employee')
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    excel_file = fields.Binary(string="Excel File")

    def print_excel_data(self):

        filename = 'Timesheet.xls'
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet("Timesheet")
        header_style = easyxf('font:height 500; align: horiz center;font:bold True;')
        font_style = easyxf('font:height 200; align: horiz center;font:bold True;')

        Row1 = 2
        Row2 = 3
        Col1 = 1
        Col2 = 7
        print("\n ---- Reach after var----\n")
        worksheet.write_merge(Row1, Row2, Col1, Col2, "Timesheet", header_style)

        worksheet.col(0).width = 2000
        Row = 7
        Col = 0
        worksheet.col(0).width = 256 * 17
        worksheet.write(Row, Col, 'Employee Name', font_style)
        Col += 1
        worksheet.col(1).width = 256 * 22
        worksheet.write(Row, Col, 'Project', font_style)
        Col += 1
        worksheet.col(2).width = 256 * 31
        worksheet.write(Row, Col, 'Task', font_style)
        Col += 1
        worksheet.col(3).width = 256 * 21
        worksheet.write(Row, Col, 'Description', font_style)
        Col += 1
        worksheet.write(Row, Col, 'Hours', font_style)
        Col += 1
        worksheet.write(Row, Col, 'Start Date', font_style)
        Col += 1
        worksheet.write(Row, Col, 'End Date', font_style)

        total_time = 0
        Row = 9
        for rec in self.hr_excel_report_ids:
            """ rec has emp id """
            env_records = self.env['account.analytic.line'].search([('employee_id', '=', rec.id)])
            Col = 0
            emp_name = rec.name
            worksheet.write(Row, Col, emp_name)

            for env_rcd in env_records:
                worksheet.write(Row, 1, env_rcd.project_id.name)
                worksheet.write(Row, 2, env_rcd.task_id.name)
                worksheet.write(Row, 3, env_rcd.name)
                worksheet.write(Row, 4, env_rcd.unit_amount)
                worksheet.write(Row, 5, str(self.start_date))
                worksheet.write(Row, 6, str(self.end_date))
                total_time += env_rcd.unit_amount
                Row += 1
            worksheet.write(Row, 4, total_time)
            Row += 3

        fp = BytesIO()
        workbook.save(fp)
        fp.seek(0)
        excel_file = base64.encodebytes(fp.getvalue())
        fp.close()

        self.write({'excel_file': excel_file})
        url = ('web/content/?model=excel.wizards&download=true&field=excel_file&id=%s&filename=%s' % (self.id, filename))

        if self.excel_file:
            return {'type': 'ir.actions.act_url',
                    'url': url,
                    'target': 'new'
                    }
