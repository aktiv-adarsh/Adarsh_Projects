# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class WizardsStudentFee(models.TransientModel):
    _name = 'wizard.feebtn'
    _description = 'wizard_feebtn'

    wizards_student_fee = fields.Integer(string="Standard Fees", readonly=True)
    wizards_student_paid_fees = fields.Integer(string="Paid Fees")
    student_pending_fees = fields.Integer(string="Pending Fees", readonly=True)

    print("\n\n ----------- wizards_student_fee = ", wizards_student_fee, "---\n")
    print("----------- student_pending_fees = ", student_pending_fees, "---\n\n")

    """On save btn update data on main sheet"""

    @api.onchange('wizards_student_fee')
    def Wizards_submit_btn(self):
        print("\n\n ----------- Wizard1------  \n\n")
        #
        record = self.env['student.management'].browse(self.env.context.get('active_id'))
        for rec in self:
            # if int(rec.wizards_student_paid_fees) <= int(self.student_fee / 2):
            if rec.wizards_student_paid_fees <= rec.student_pending_fees:
                print("\n-------------In For loop--------", self.student_pending_fees)
                record.student_paid_fees += rec.wizards_student_paid_fees
            else:
                raise ValidationError("You should not pay more then panding fees..!")
            # record.create({'student_pending_fees': rec.student_pending_fees})

        print("-------------", record.student_pending_fees, "---------------", record, "\n\n")

    """To get details in wizards"""

    @api.model
    def default_get(self, fields):
        res = super(WizardsStudentFee, self).default_get(fields)
        rec = self.env['student.management'].browse(self.env.context.get('active_id'))
        res.update({
            "wizards_student_fee": rec.student_fee,
            "student_pending_fees": rec.student_pending_fees,
        })
        return res
