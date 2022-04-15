# -*- coding: utf-8 -*-
# test_demo Database
from odoo import models, fields, api


class PioneerAccountMove(models.Model):
    _inherit = 'account.move.line'

    delivery_address_id = fields.Many2one('res.partner', string="Delivery Address",
                                          domain=[('parent_id', '=', 'vendor_id'), ('type', '=', 'delivery')])
    vendor_id = fields.Many2one('res.partner', string="vendor", domain=[('supplier_rank', '>', 0)])
    vendor_price = fields.Float(string="vendor Price")
    planned_gp = fields.Float(string="Planned GP%")
    description = fields.Char(string="Description", compute="_concat_address_label")

    @api.onchange('vendor_price')
    def calc_planned_gp(self):
        if self.vendor_price and self.price_unit:
            self.planned_gp = ((self.price_unit - self.vendor_price) / self.price_unit) * 100

    def _concat_address_label(self):
        for rec in self:
            if self.delivery_address_id:
                rec.description = '%s  -  %s' % (rec.delivery_address_id.name, rec.name)
            else:
                self.description = ""


class PioneerServerActions(models.Model):
    _inherit = 'account.move'

    def action_update(self):
        print("\n -----In Func------ \n")
        res = []
        for rec in self.invoice_line_ids:
            print("\n\n\n",rec,"\n\n\n")
            # if rec not in res:
            #     res.append(rec)
            #     self.create({'move_type': 'in_invoice', 'partner_id': self.vendor_id,
            #                                        'invoice_line_ids': (
            #                                            {
            #                                                'product_id': self.product_id,
            #                                                'name': self.product_id.name,
            #                                                'quantity': 1.00,
            #                                                'price_unit': self.vendor_price})
            #                  })
        # env_rec = self.env('account.move').create({'move_type': 'out_invoice', 'partner_id': self.vendor_id,
        #                                            'invoice_line_ids': (
        #                                                {
        #                                                    'product_id': self.product_id,
        #                                                    'name': self.product_id.name,
        #                                                    'quantity': 1.00,
        #                                                    'price_unit': self.vendor_price})
        #                                            })
        # print("\n\n --------- ", env_rec, "---------")
        # return res
