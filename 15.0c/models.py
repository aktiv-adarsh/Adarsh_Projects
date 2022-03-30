# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class AdvanceActions(models.Model):

    _name = 'advance.actions'
    _description = 'advance_actions'

    actions_id = fields.Integer(string="ID", required=True)
    actions_name = fields.Char(string="Name")

    # @api.model
    # def create(self, values):
    #     if values.get('sequences', ('name')) == ('name'):
    #         values['sequences'] = self.env['ir.sequence'].next_by_code('adarsh.adarsh') or _('name')
    #     res = super(adarsh, self).create(values)
    #     return res
