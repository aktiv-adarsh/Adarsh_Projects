from odoo import fields, models, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    promotional_discount = fields.Boolean()

    @api.model
    def set_values(self):
        self.env['ir.config_parameter'].set_param('pro_discount',
                                                  self.promotional_discount)

        super(ResConfigSettings, self).set_values()

    @api.model
    def get_values(self):
        rec = super(ResConfigSettings, self).get_values()

        rec['promotional_discount'] = self.env['ir.config_parameter'].get_param('pro_discount')

        return rec
