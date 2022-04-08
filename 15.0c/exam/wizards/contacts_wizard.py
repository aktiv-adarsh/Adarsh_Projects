# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import *


class ExamWizard(models.TransientModel):
    _name = 'exam.wizard'
    _description = 'exam.wizard'

    o2m_product_id = fields.One2many('exam.wizard1', 'wizard_id', string="Product One2Many", required=True)

    def so_button_action(self):

        record = self._context.get('context_records')
        for rec_create in record:
            print("\n-----------Contact_id = ", rec_create, "---------\n")
            so_create = self.env['sale.order'].create({
                'partner_id': rec_create,
                'date_order': date.today()
            })
            print("\n------------sale Order id = ", so_create, "---------")

            print("\n-------------Record Type = ", type(record), "------------\n")

            for rec in self.o2m_product_id:
                print("-------------In For loop---------------")
                print("----------Loop--O2M_pd = ", self.o2m_product_id, "---------------")
                print("----------Loop--Rec = ", rec, "---------------")
                print("----------Rec--ID = ", rec.m2o_product_id1.id, "---------------")
                so_create.write({'order_line': [(0, 0, {'product_id': rec.m2o_product_id1.id,
                                                        'product_uom_qty': rec.product_qnty,
                                                        'price_unit': rec.product_price})]})



class ExamWizard1(models.TransientModel):

    _name = 'exam.wizard1'
    _description = 'exam.wizard1'

    wizard_id = fields.Many2one('exam.wizard')
    m2o_product_id1 = fields.Many2one('product.template', string="Product Many2One1", required=True)
    product_qnty = fields.Float(string="Quantity")
    product_price = fields.Float(string="Unit Price")
