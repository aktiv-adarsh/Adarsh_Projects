# -*- coding: utf-8 -*-
# test_demo Database
from odoo import models, fields, api, _


class SaleOrderEmail(models.Model):
    _inherit = 'sale.order'

    """Send E-mail to the current customer when it has confirm state"""
    # @api.depends('state')
    def sale_email_send_action(self):
        if self.state == 'sale':
            print("\n------ Func In----------")
            template_id = self.env.ref('sale_order_email.sale_order_email').id
            template = self.env['mail.template'].browse(template_id)
            template.send_mail(self.id, force_send=True)
            print("\n------ Func end----------\n")
