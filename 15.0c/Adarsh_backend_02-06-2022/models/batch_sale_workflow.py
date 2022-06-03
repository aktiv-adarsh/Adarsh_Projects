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

    sale_order_ids = fields.Many2many('sale.order', tracking=True, string="Sale Order") #('user_id', 'like', 'responsible_id'),
    operation_date = fields.Date(string="Operation date", tracking=True)

    def action_draft(self):
        """On click of 'Set to Draft' button change
        the current state to 'Draft' state of statusbar"""
        self.status = 'draft'

    @api.onchange('')

    @api.model
    def action_done(self, view_id=None, view_type=False, toolbar=False, submenu=False):
        """On click of 'Proceed Operation' button change
        the current state to 'Done' state of statusbar"""
        print("\n\n ******* In Func *********\n\n")
        self.status = 'done'
        # self.operation_type = "confirm"

        print("\n\n******** Before context ************\n\n\n")
        context = self._context
        print("\n\n ********* Context call ***********\n\n\n")
        res = super(BatchSaleWorkflow, self).action_done(view_id=view_id, view_type=view_type, toolbar=toolbar,
                                                         submenu=submenu)

        print("\n\n ******* Before IF *********\n\n")
        if context.get('turn_view_readonly'):  # Check for context value
            doc = etree.XML(res['arch'])
            print("\n\n ******* After IF *********\n\n")
            if view_type == 'form':  # Applies only for form view
                print("\n\n ******* Before INNER IF *********\n\n")
                for node in doc.xpath("//field"):  # All the view fields to readonly
                    # node.get('readonly', '1')
                    print("\n\n *****IN LOOP****** \n\n")
                    node.set('modifiers', simplejson.dumps({"readonly": True}))

                res['arch'] = etree.tostring(doc)
        return res

    def action_cancel(self):
        """On click of 'Cancel' button change the
        current state to 'Cancel' state of statusbar"""
        self.status = 'cancel'

    # @api.onchange('responsible_id')
    # def sale_search_records(self):
    #     """Function will search the different user's records"""
    #     # call = super(BatchSaleWorkflow, self).sale_search_records()
    #     print("\n\n\n\n ***********responsible_id***", self.responsible_id, "*************")
    #     print("\n ************responsible_id.name**", self.responsible_id.name, "*************")
    #     print("\n ***********sale_order_ids***", self.sale_order_ids, "*************\n\n\n\n\n")
    #     records = self.env['sale.order'].search([])
    #     print("\n ************USer_id.name**", records.user_id, "*************")
    #     data = records.read([('responsible_id', '=', 'user_id')])
    #     print("\n ************self.sale_order_ids**", data, "*************")
