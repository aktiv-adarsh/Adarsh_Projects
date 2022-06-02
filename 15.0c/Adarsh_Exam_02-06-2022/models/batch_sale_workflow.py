# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class BatchSaleWorkflow(models.Model):

    _name = 'batch_sale.workflow'
    _description = 'batch_sale_workflow'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", tracking=True, required=True)
    responsible = fields.Many2one('res.user', string="Responsible", tracking=True)
    operation_type = fields.Selection([('confirm,', 'Confirm,'), ('cancel,', 'Cancel,'),
                                       ('merge),', 'Merge),')], string='Operation Type', default="confirm",
                                      tracking=True)
    customer = fields.Many2one('res.partner', tracking=True, string="Customer")  # ('operation_type', '=', True)]
    status = fields.Selection([('draft', 'Draft'), ('done', 'Done'),
                               ('cancel', 'Cancel)')], string='State', default="draft", tracking=True)

    sale_order = fields.Many2many('res.partner', tracking=True, string="Sale Order")  # ('operation_type', '=', True)]
    operation_date = fields.Date(string="Operation date", tracking=True)


    """Those functions are called accordingly selection done by user"""
    def action_draft(self):
        self.state = 'draft'

    def action_done(self):
        self.state = 'done'

    def action_cancel(self):
        self.state = 'cancel'
