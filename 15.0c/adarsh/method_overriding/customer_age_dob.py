# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date


class CustomerAgeDob(models.Model):

    _inherit = "res.partner"

    custome_dob = fields.Date(string="DOB", required=True)
    customer_age = fields.Integer(string="Age", compute="calc_age")

    @api.depends('custome_dob')
    def calc_age(self):
        if self.custome_dob:
            today_date = fields.Date.today()
            print("----------------",today_date, "----------------")
            self.customer_age = (date(today_date) - date(self.custome_dob.month)) / 12
            print("----------------", self.customer_age, "----------------")
            # if self.customer_age <= 0:
            #     self.customer_age = 0
            #     self.customer_age = (today_date - self.custome_dob).days / 30
            #     # self.customer_age = date(self.customer_age).strftime('%m')

        else:
            self.customer_age = 0
