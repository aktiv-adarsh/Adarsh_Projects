# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CalcCustomerAge(models.Model):

    _inherit = "res.partner"

    customer_dob = fields.Date(string="DOB", required=True)
    customer_age = fields.Integer(string="Age", compute="calc_age")

    """compute of customer_age will call this function to check the age"""
    @api.depends('customer_dob')
    def calc_age(self):
        if self.customer_dob:
            today_date = fields.Date.today()
            self.customer_age = (today_date - self.customer_dob).days / 365

        else:
            self.customer_age = 0
