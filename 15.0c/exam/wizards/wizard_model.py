# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ExamWizard(models.TransientModel):

    _name = 'exam.wizard'
    _description = 'exam.wizard'

    m2o_product_id = fields.Many2many('product.template', string="Product Many2One1")

    def Wizard1(self):
        print("------------Save data-------", self)
