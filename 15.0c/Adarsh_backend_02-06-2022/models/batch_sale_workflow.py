# -*- coding: utf-8 -*-

from odoo import models, fields, api


# from odoo.osv import expression


class BatchSaleWorkflow(models.Model):
    """This Class contains different action of buttons and
    changing state of statusbar and perform conditionally searching."""

    _name = 'batch_sale.workflow'
    _description = 'batch_sale_workflow'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    sequence = fields.Char(string="Name", required=True, copy=False, readonly=True,
                           index=True, default='New')
    name = fields.Char(string="Name", tracking=True)
    responsible_id = fields.Many2one('res.users', string="Responsible", tracking=True)
    operation_type = fields.Selection([('confirm', 'Confirm'), ('cancel', 'Cancel'),
                                       ('merge', 'Merge')], string='Operation Type',
                                      default="confirm", tracking=True)
    customer_id = fields.Many2one('res.partner', tracking=True, string="Customer")
    status = fields.Selection([('draft', 'Draft'), ('done', 'Done'),
                               ('cancel', 'Cancel)')], string='State', default="draft",
                              tracking=True)
    state = fields.Selection([('draft', 'Draft'), ('done', 'Done'),
                               ('cancel', 'Cancel)')], string='State', default="draft",
                              tracking=True)

    sale_order_ids = fields.Many2many('sale.order', tracking=True, string="Sale Order")
    operation_date = fields.Date(string="Operation date", required=True, tracking=True)

    def action_draft(self):
        """On click of 'Set to Draft' button change
        the current state to 'Draft' state of statusbar"""
        self.status = 'draft'

    @api.onchange('responsible_id')
    def change_user_id(self):
        """Display only those sales order whose sales
        person is selected above on responsible_id field"""

        return {'domain': {'sale_order_ids': [('user_id', '=', self.responsible_id.id)]}}

    @api.onchange('operation_type', 'customer_id')
    def action_confirm(self):
        """At the selection of different state function call"""

        if self.operation_type == 'confirm':
            print("\n\n\n ****** OnChange Operation type confirm *********\n\n\n")
            return {'domain': {
                'sale_order_ids': [('user_id', '=', self.responsible_id.id),
                                   ('state', 'in', ['draft', 'sent'])]}}

        elif self.operation_type == 'cancel':
            print("\n\n\n ****** OnChange Operation type Cancel *********\n\n\n")
            return {'domain': {
                'sale_order_ids': [('user_id', '=', self.responsible_id.id),
                                   ('state', 'in', ['draft', 'sent', 'sale'])]}}

        elif self.operation_type == 'merge':
            print("\n\n\n ****** OnChange Operation type Merge *********\n\n\n")
            return {'domain': {
                'sale_order_ids': [('user_id', '=', self.responsible_id.id),
                                   ('partner_id', '=', self.customer_id.id),
                                   ('state', 'in', ['draft', 'sent'])]}}
        else:
            print("\n\n ****** ERROR in 'action_confirm' Function *** \n\n\n")

    def action_done(self):
        """On click of 'Proceed Operation' button,
        change the current state to 'Done' state"""
        self.status = 'done'
        self.sale_order_ids.date_order = self.operation_date

        get_rec_id = self.sale_order_ids.ids
        task = self.env['sale.order'].search([('id', 'in', get_rec_id)])

        if self.sale_order_ids:
            if self.operation_type == 'confirm':

                print("\n\n\n\n ********** 1 BTN Clicked, get rec id * ", get_rec_id, "\n\n\n")
                print("\n\n\n\n ********** 1 BTN Clicked, TASK * ", task, "\n\n\n")
                for rec in task:
                    rec.action_confirm()

            elif self.operation_type == 'cancel':

                for rec in task:
                    rec.action_cancel()
                print("\n\n\n ****** Action type cancel *********\n\n\n")

            elif self.operation_type == 'merge':
                print("\n\n\n ****** Action type Merge *********\n\n\n")
                print("\n\n ********** 1 BTN Clicked, get rec id * ", get_rec_id, "\n\n\n")
                print("\n\n ********** 1 BTN Clicked, TASK * ", task, "\n\n\n")
                print("\n ----------- SO * ", self.sale_order_ids)
                print("\n ----------- SO.ids * ", self.sale_order_ids.ids, "\n\n\n")

                for rec in self.sale_order_ids:
                    print("\n\n\n ******** REC *", rec)
                    record = task.create({
                        'partner_id': self.customer_id.id,
                        'date_order': self.operation_date,
                    })

                    print("\n ******** Record *", record)
                    print("\n ******** ALL SO_Line *", rec.order_line)
                    print("\n ******** ALL SO_Line *", rec.order_line.ids)
                    for os_line in rec.order_line:
                        print("\n **** ----> SO_Line -> ", os_line)
                        # record.create({'order_line': os_line})
                        record.create({'order_line': [(0, 0, os_line)]})
                    rec.action_cancel()
            else:
                print("\n\n\n ****** ERROR at Merge state ***** \n\n\n")

        else:
            print("\n\n\n ******** ERROR at Action_Done BTN ******\n\n\n")

    def action_cancel(self):
        """change the current state to 'Cancel'
         state of statusbar and make readonly form"""
        self.status = 'cancel'

    @api.model
    def create(self, vals):
        """Function call for Auto-generate sequence no."""
        if vals.get('sequence', 'New') == 'New':
            vals['sequence'] = self.env['ir.sequence'].next_by_code('count_sequence') or 'New'
        res = super(BatchSaleWorkflow, self).create(vals)
        return res
