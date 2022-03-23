# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CustomerCountry(models.Model):

    _inherit = "res.partner"

    # customer_country = fields.Many2one('res.partner', string="Customer country")

    """name_get() will display multiple given fields records on other field"""

    def name_get(self):
        result = []
        print("--------------------Function called-----------")
        if self._context.get('orm_methods.cus_country'):
            print("--------------------IN--Function called-----------")

            for field in self:
                result.append(field.id, '%s - %s' % (field.country_id, field.name))
                print("Cus country------------------", field.country_id)
                print("Country Name ------------------", field.name)
                print("Field ------------------", field)
        return result
