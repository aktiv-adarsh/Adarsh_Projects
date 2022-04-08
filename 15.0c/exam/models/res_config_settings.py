
from odoo import models, fields, api, _
from datetime import *


class ConfigInstall(models.TransientModel):

    """Here setting is inherited on TransientModel"""
    _inherit = 'res.config.settings'

    # today_date = fields.Date.today()
    # Exam = fields.Binary(string="Image")

    today_date = date.today()
    module_hr = fields.Boolean(string="Employees")
    print("\n------------Month-[", today_date.month, "]---------\n")
    current_month_order_ids = fields.Many2many('sale.order', domain=[('date_order', '>=',
                                               datetime(datetime.today().year, datetime.today().month, 1)),
                                              ('date_order', '<',
                                               datetime(datetime.today().year, datetime.today().month+1, 1))])

    @api.model
    def get_values(self):
        res = super(ConfigInstall, self).get_values()
        env_data = self.env['ir.config_parameter'].get_param('exam.current_month_order_ids')
        print("\n---------env_data--", env_data, "----------", type(env_data))
        if env_data:
            res.update(current_month_order_ids=[(6, 0, eval(env_data))])
            print("\n--------Get_Val-For---", res, "------------\n")

        return res

    def set_values(self):
        self.env['ir.config_parameter'].set_param('exam.current_month_order_ids', self.current_month_order_ids.ids)
        res = super(ConfigInstall, self).set_values()
        print("\n---------Set-Val-[", res, "]------------\n", self.current_month_order_ids, self.current_month_order_ids.ids)
