
from odoo import models, fields, api, _


class ConfigInstall(models.TransientModel):

    """Here setting is inherited on TransientModel"""
    _inherit = 'res.config.settings'

    today_date = fields.Date.today()
    module_hr = fields.Boolean(string="Employees")
    current_month_order_ids = fields.Many2many('sale.order', domain=[('date_order', 'like', 'today_date.month')])

    # @api.model
    # def get_values(self):
    #     res = super(ConfigInstall, self).get_values()
    #     env_rec = self.env['ir.config_parameter'].get_param('exam.current_month_order_ids', self.current_month_order_ids)
    #     res.update({
    #     "current_month_order_ids": env_rec.order_line})
    #     return res
    #
    # def set_values(self):
    #     res = super(ConfigInstall, self).set_values()
    #     self.env['ir.config_parameter'].set_param('exam.current_month_order_ids', self.current_month_order_ids)
    #     return res
