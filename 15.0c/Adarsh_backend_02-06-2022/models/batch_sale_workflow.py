# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.osv import expression


class BatchSaleWorkflow(models.Model):
    """This Class contains different action on buttons
    and changing state of statusbar and perform conditionally search."""

    _name = 'batch_sale.workflow'
    _description = 'batch_sale_workflow'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", tracking=True, required=True)
    responsible_id = fields.Many2one('res.users', string="Responsible", tracking=True)
    operation_type = fields.Selection([('confirm', 'Confirm'), ('cancel', 'Cancel'),
                                    ('merge', 'Merge')], string='Operation Type', default="confirm",
                                      tracking=True)
    customer_id = fields.Many2one('res.partner', tracking=True, string="Customer")
    status = fields.Selection([('draft', 'Draft'), ('done', 'Done'),
                               ('cancel', 'Cancel)')], string='State', default="draft", tracking=True)

    sale_order_ids = fields.Many2many('sale.order', tracking=True, string="Sale Order")
    operation_date = fields.Date(string="Operation date", tracking=True)

    def action_draft(self):
        """On click of 'Set to Draft' button change
        the current state to 'Draft' state of statusbar"""
        self.status = 'draft'

    @api.onchange('responsible_id')
    def change_user_id(self):
        """Display only those sales order whose sales
        person is selected above on responsible_id field"""
        domain = {'sale_order_ids': [('user_id', '=', self.responsible_id.id), ('state', 'in', ['draft', 'sent'])]}
        return domain

    # @api.model
    def action_done(self, view_id=None, view_type=False, toolbar=False, submenu=False):
        """On click of 'Proceed Operation' button, change
        the current state to 'Done' state of statusbar"""
        self.status = 'done'
        self.sale_order_ids.date_order = self.operation_date

    def action_cancel(self):
        """On click of 'Cancel' button change the
        current state to 'Cancel' state of statusbar"""
        self.status = 'cancel'

    # @api.onchange('operation_type')
    # def action_confirm(self):
    #     record = self.sale_order_ids.search([''])
