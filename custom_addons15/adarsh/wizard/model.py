# -*- coding: utf-8 -*-

from odoo import models, fields, api


class wizard(models.TransientModel):
    _name = 'wizard.wizard'
    _description = 'wizard.wizard'

    name = fields.Char(string="Name", required=True)
    html_wid = fields.Html()
    description = fields.Text()

    # m2o_fields1_id = fields.Many2one('smartview.smartview', string="Many2One1")

    def Wizard1(self):
        print("Adarsh Donga")
