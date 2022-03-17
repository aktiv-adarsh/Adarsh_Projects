# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

class SaleBtnLine(models.Model):

    _inherit = "sale.order"

    def confirm_sale(self):
        print("Confirm call....")

    def action_confirm(self):
        res = super(SaleBtnLine, self).action_confirm()
        for i in self:
            if len(i.order_line) > 4:
                raise UserError("Please keep record line less than 4")
        return res
