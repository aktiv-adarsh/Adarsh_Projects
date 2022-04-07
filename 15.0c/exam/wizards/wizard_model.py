# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ExamWizard(models.TransientModel):
    _name = 'exam.wizard'
    _description = 'exam.wizard'

    m2o_product_id = fields.Many2one('product.template', string="Product Many2One1", required=True)
    product_qnty = fields.Float(string="Quantity")
    product_price = fields.Float(string="Unit Price")

    def so_button_action(self):
        # record = self.env['res.partner'].browse(self.env.context.get('active_id').partner_id.id)
        # record = self.env['res.partner'].search([('active_id', '=', self.env.context.get('active_id'))])
        print("\n-----------------", self._context.get('context_records'), "------------\n")
        # for rec in self.m2o_product_id:
        #     print("-------------In For loop---------------")
        #     record.write({'order_line': [(0, 0, {'product_id': rec.id})]})
        #     print("-------------", rec, "---------------")

        # def Wizard1(self):
        #     print("------------Save data-------", self)
