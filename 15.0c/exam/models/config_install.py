
from odoo import models, fields, api, _


class ConfigInstall(models.TransientModel):

    """Here setting is inherited on TransientModel"""
    _inherit = 'res.config.settings'

    today_date = fields.Date.today()
    module_hr = fields.Boolean(string="Employees")
    print("\n------------Month-[", today_date.month, "]---------\n")
    current_month_order_ids = fields.Many2many('sale.order', domain=[('date_order', 'like', 'today_date.month')])



    #
    # @api.model
    # def get_values(self):
    #     res = super(ConfigInstall, self).get_values()
    #     print("--------Get-Val--", res, "----------")
    #     for rec in self.current_month_order_ids:
    #         res.update({"order_line": self.env['ir.config_parameter'][(0, 0, {'product_id': rec.id})]})
    #         print("\n--------Get_Val-For---", res, "------------\n")
    #
    #     return res
    #
    # def set_values(self):
    #     res = super(ConfigInstall, self).set_values()
    #     self.env['ir.config_parameter'].set_param('exam.current_month_order_ids', self.current_month_order_ids)
    #     print("\n---------Set-Val-[", res, "]------------\n")
    #     return res




