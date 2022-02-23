# -*- coding: utf-8 -*-

from odoo import models, fields, api


class adarsh(models.TransientModel):
    _name = 'adarsh.adarsh'
    _description = 'adarsh.adarsh'

    name = fields.Char(string="Name", required=True)
    html_wid = fields.Html()
    description = fields.Text()
    # Wizard1 = fields.Char()
    # cancel = fields.Char()

    def Wizard1(self):
        print("dcndjsc")
        # return {'name':'Wizard1'}
