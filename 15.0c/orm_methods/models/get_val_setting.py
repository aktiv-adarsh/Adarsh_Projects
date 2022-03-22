
from odoo import models, fields, api

class GetValSetting(models.TransientModel):

    _inherit = 'res.config.settings'

    check_setting = fields.Boolean(string="Check It")
    html_setting = fields.Html(string="Html Field")

    # call_fun = fields.Boolean(string='Active', config_parameter='orm_methods.html_setting')

    @api.onchange('check_setting')
    def onchange_name(self):
        if self.check_setting == False:
            self.html_setting = False

    @api.model
    def get_values(self):

        res = super(GetValSetting, self).get_values()
        self.env['ir.config_parameter'].get_param('orm_methods.check_setting')
        return res

    @api.model
    def set_values(self):

        res = super(GetValSetting, self).set_values()
        self.env['ir.config_parameter'].set_param('rental_management.check_setting', self.html_setting)
        return res
