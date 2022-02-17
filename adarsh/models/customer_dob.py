# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CustomerDob(models.Model):
    _inherit = "res.partner"

    Customer_dob = fields.Date(string="DOB", required=True)
    customer_reference_dob = fields.Char(string="Customer Reference")
    customer_street3 = fields.Char()