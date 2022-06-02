# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class PromotionalDiscount(models.Model):

    _name = 'promotional.discount'
    _description = 'promotional_discount.'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    discount_type = fields.Selection([('%', 'Percentage'), ('$', 'Fixed_Amount')], string='Discount Type', tracking=True)
    name = fields.Char(string="Name", tracking=True, required=True)
    discount = fields.Float(string="Discount", tracking=True)

    minimum_order_amount = fields.Float(string="Minimum Order Amount", default=100, tracking=True)
    start_date = fields.Date(string="Start Date", tracking=True)
    end_date = fields.Date(string="End Date", tracking=True)

    comp_currency_id = fields.Many2one('res.currency', default=20, readonly=True)