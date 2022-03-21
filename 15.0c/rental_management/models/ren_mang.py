# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class RentalManagement(models.Model):

    _name = 'rental.management'
    _description = 'rental_management'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", tracking=True, required=True)
    customer_id = fields.Many2one('res.partner',string="Customer", tracking=True)
    rental_man_type_id = fields.Many2one('rental.type',string="Rental Type", tracking=True)
    start_date = fields.Datetime(string="Start Date", tracking=True)
    end_date = fields.Datetime(string="End Date", tracking=True)
    rental_prod_id = fields.Many2one('product.product', tracking=True, domain=[('is_rental', '=', True)])
    price = fields.Float(string="Price", tracking=True, related='rental_prod_id.list_price')
    state = fields.Selection([('draft', 'Draft'), ('waiting', 'Waiting'),
                             ('approve', 'Approve'), ('cancel', 'Cancelled')], string='State', default="draft", tracking=True)

    """Those functions are called accordingly selection done by user"""
    def action_draft(self):
        self.state = 'draft'

    def action_waiting(self):
        self.state = 'waiting'

    def action_approve(self):
        self.state = 'approve'

    def action_cancel(self):
        self.state = 'cancel'
