from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ResConfigSalePaper(models.TransientModel):

    _inherit = 'res.config.settings'

    check_promotional_discount = fields.Boolean(string="Promotional Discount")
