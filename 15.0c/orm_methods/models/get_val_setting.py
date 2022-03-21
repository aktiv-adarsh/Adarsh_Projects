
from odoo import models, fields, api

class Get_Val_Setting(models.TransientModel):

    _inherit = 'res.config.settings'

    check_setting = fields.Boolean(string="Check It")
    html_setting = fields.Html(string="Html Field")
