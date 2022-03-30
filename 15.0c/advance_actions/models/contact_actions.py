# -*- coding: utf-8 -*-
# test_demo Database
from odoo import models, fields, api


class SaleActions(models.Model):

    _inherit = 'res.partner'

    def action_update(self):
        self.write({'name': 'Brandon Freeman', 'email': 'Abc@brandon.freeman55@example.com', 'phone': "(355)-687-3262"})

    def action_create_data(self):
        self.create({'name': 'New Record', 'email': 'New@records.com', 'phone': "(123)-456-7890"})


class ScheduleAction(models.Model):
    _inherit = 'sale.order'

    def action_schedule_quotation(self):
        if self.state == 'draft':
            self.write({'state': 'sent'})

    @api.model
    def demo_action(self):
        print("action------------works-----------")
        for rec in self.search([('state', '=', 'draft')]):
            rec.write({'state': 'sent'})
