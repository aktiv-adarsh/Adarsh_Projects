# -*- coding: utf-8 -*-

from odoo import models, fields, api


class WizardsStudentFee(models.TransientModel):
    _name = 'wizard.feebtn'
    _description = 'wizard_feebtn'

    wizards_student_fee = fields.Integer(string="Standard Fees")
    wizards_student_paid_fees = fields.Integer(string="Paid Fees")
    student_pending_fees = fields.Integer(string="Pending Fees", compute="_student_fees_calc")

    print("\n\n ----------- wizards_student_fee = ", wizards_student_fee, "---\n")
    print("----------- student_pending_fees = ", student_pending_fees, "---\n\n")

    """On save btn update data on main sheet"""
    def Wizard1(self):
        print("\n\n ----------- Wizard1------  \n\n")
        #
        # record = self.env['student.management'].browse(self.env.context.get('active_id'))
        # for rec in self:
        #     print("-------------In For loop---------------")
        #     record.update(pending_fees=[(6, 0, rec)])
        #     print("-------------", rec, "---------------")

    """To get details in wizards"""
    @api.model
    def default_get(self, fields):
        res = super(WizardsStudentFee, self).default_get(fields)
        rec = self.env['student.management'].browse(self.env.context.get('active_id'))
        res.update({
            "wizards_student_fee": rec.student_fee,
        })
        return res


    @api.onchange('wizards_student_paid_fees')
    def _student_fees_calc(self):
        self.student_pending_fees = self.wizards_student_fee - self.wizards_student_paid_fees
        print("\n\n ----------- student_pending_fees = ", self.student_pending_fees, "---\n")
