# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CustomerData(models.Model):

    _inherit = "res.partner"

    customer_reference = fields.Char(string="Customer Reference")

    """name_get() will display multiple given fields records on other field"""
    def name_get(self):
        res = []
        for field in self:
            res.append((fields.id, '%s -%s' % (fields.customer_reference, field.name)))
            print("Cus ref------------------",field.customer_reference)
            print("Name ------------------",field.name)
            print("Field ------------------",field)
        return res

    """name_search is use to customize search (to search inside multiple fields) on relational fields.
        example, To provide suggestions based on a partial
        value for a relational field."""
    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        """search email and phone of customer field."""
        domain = []
        args = args or []
        if name:
            domain = args + ['|', ('email', operator, name), ('phone', operator, name)]
            print("Email or Phone ---------------",name)
        return super(CustomerData, self).search(domain, limit=limit).name_get()
