# -*- coding: utf-8 -*-
# test_demo Database
from odoo import models, fields, api, _


class ButtonOnSaleOrder(models.Model):

    _inherit = 'sale.order'

    @api.depends('partner_id')
    def boolean_values(self):
        res = super(ButtonOnSaleOrder, self).get_values()
        env_data = self.env['ir.config_parameter'].get_param('practice_paper2.check_promotional_discount')
        print("\n ************ env_data--", env_data)
        print("----------\n\n", type(env_data))
