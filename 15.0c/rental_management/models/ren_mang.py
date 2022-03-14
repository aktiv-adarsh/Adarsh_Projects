# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class RentalManagement(models.Model):

    _name = 'rental.management'
    _description = 'rental_management'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", tracking=True, required=True)
    customer = fields.Many2one('res.partner',string="Customer", tracking=True)
    rental_type = fields.Many2one('rental.type',string="Rental Type", tracking=True)
    start_date = fields.Datetime(string="Start Date", tracking=True)
    end_date = fields.Datetime(string="End Date", tracking=True)
    rental_prod = fields.Many2one('product.product',string="Description", tracking=True)
    price = fields.Float(string="Description", tracking=True)
    state = fields.Selection(selection=[('draft', 'Draft'), ('waiting', 'Waiting'), ('approve', 'approve'), ('cancel', 'Cancelled')], string='Select Options')

    """Those functions are called accordingly selection done by user"""
    def action_draft(self):
        self.state = 'draft'

    def action_waiting(self):
        self.write({'state': 'waiting'})

    def action_approve(self):
        self.state = 'approved'

    def action_cancel(self):
        self.state = 'cancel'

    # def rental_type(self):
    #     for rec in self:
    #         if rec in rental_type:
    #             return rec

    #access_rental_management,rental.management,model_rental_management,base.group_user,1,1,1,1