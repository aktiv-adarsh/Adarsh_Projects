# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DiffMethod(models.Model):

    _inherit = 'res.partner'

    def read(self, fields):
        records = self.email.search()
        records = self.phone.search()
        return records.read(['fields'])

    # def browse(self, domain=(), context=None):
    #     return self.model.with_context(context or {}).search(domain)
