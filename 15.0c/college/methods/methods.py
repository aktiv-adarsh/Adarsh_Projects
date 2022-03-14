# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OrmMethods(models.Model):

    _inherit = "sale.order"

    @api.model
    def default_get(self,fields=[]):
        res = super(OrmMethods,self).defaulf_get(fields)
        res['partner_id'] = self.env.partner_id
        res['email'] = self.env.email
        res['user'] = self.env.name
        res['payment_term_id'] = self.env.payment_term_id
        return res

