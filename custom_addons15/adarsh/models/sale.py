# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    Customer_Reference = fields.Char(string="Customer_Reference", related="partner_id.customer_reference_dob")    # refer = fields.Many2One([('sale.order','partner_id')])
    # refer = fields.Reference([('sale.order','partner_id')])