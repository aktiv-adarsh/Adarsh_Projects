# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):

    _inherit = "product.template"

    is_rental = fields.Boolean(string="IsRental")
    m2o_id = fields.Many2one('rental.type',string="M2O")
