# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Decorator(models.Model):
    _inherit = "sale.order"

    cnum = fields.Char(string="Contact no")
    cemail = fields.Char(string="E-mail")

    @api.onchange('partner_id')
    def onchange_cnum_id(self):
        for rec in self:
            if self.partner_id:
                self.cnum = rec.partner_id.phone
                self.cemail = rec.partner_id.email

    @api.constrains('payment_term_id', 'partner_id')
    def constrains_payment_id(self):
        for rec in self:
            if rec.payment_term_id != rec.partner_id.property_supplier_payment_term_id:
                raise ValidationError('Both are not matching')
