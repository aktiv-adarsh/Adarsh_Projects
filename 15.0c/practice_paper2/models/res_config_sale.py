from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ResConfigSalePaper(models.TransientModel):

    _inherit = 'res.config.settings'

    check_promotional_discount = fields.Boolean(string="Promotional Discount")

    @api.model
    def get_values(self):
        res = super(ResConfigSalePaper, self).get_values()
        env_data = self.env['ir.config_parameter'].get_param('practice_paper2.check_promotional_discount')
        print("\n---------env_data--", env_data, "----------", type(env_data))
        if env_data:
            res.update({'check_promotional_discount': env_data})
            print("\n-------IF-Get_Val----", res, "------------\n")

        return res

    def set_values(self):
        self.env['ir.config_parameter'].set_param('practice_paper2.check_promotional_discount', self.check_promotional_discount)
        res = super(ResConfigSalePaper, self).set_values()
        print("\n---------Set-Val-[", res, "]------------\n", self.check_promotional_discount, self.check_promotional_discount)
