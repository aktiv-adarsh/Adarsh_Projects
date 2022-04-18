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

    """Calculate planned_gp according to vendor_price"""

    @api.onchange('vendor_price')
    def calc_planned_gp(self):
        if self.vendor_price and self.price_unit:
            self.planned_gp = ((self.price_unit - self.vendor_price) / self.price_unit) * 100

    """It will concatenate cus_address & name(label) into
    Description field of invoice_line_ids"""

    def _concat_address_label(self):
        for rec in self:
            if self.delivery_address_id:
                rec.description = '%s  -  %s' % (rec.delivery_address_id.name, rec.name)
            else:
                self.description = ""


class PioneerServerActions(models.Model):
    _inherit = 'account.move'

    """On server action create 'in_invoice(vendor bill)' where 
    partner_id = vendor_id, price_unit = vendor_price and generate bill according to vendor."""

    def server_action_generate_in_invoice_bill(self):
        print("\n -----In Func------ \n")
        res = []
        for rec in self.invoice_line_ids:
            print("\n ----- For rec -- ", rec, "\n")

            if rec.vendor_id not in res:
                print("\n --------------- IF - Vendor id -- ", rec.vendor_id, "\n")

                res.append(rec.vendor_id)
                print("\n ----------------- IF res[] -- ", res, "\n")

                record = self.create({'move_type': 'in_invoice', 'partner_id': rec.vendor_id})
                print("\n -----------------Create Record ------", record)

                line_ids = self.invoice_line_ids.search([('vendor_id', '=', rec.vendor_id.id),
                                                         ('id', 'in', [line.id for line in self.invoice_line_ids])])
                print("\n ----------------- Line Ids ------", line_ids)

                for line_id in line_ids:
                    record.write({'invoice_line_ids': [(0, 0, {'product_id': line_id.product_id,
                                                               'price_unit': line_id.vendor_price,
                                                               'quantity': line_id.quantity,
                                                               'delivery_address_id': line_id.delivery_address_id,
                                                               'planned_gp': line_id.planned_gp})]})
                    print("\n ----------------For - Line Id ------", line_id)
