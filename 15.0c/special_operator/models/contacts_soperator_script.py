

from odoo import models, fields, api
from odoo.exceptions import UserError


class SpecialOperator(models.Model):

    _inherit = "res.partner"

    contacts_customer_rank = fields.Integer(string="Customer Rank", required=True)

    """call when customer rank grater then 10"""
    @api.onchange('contacts_customer_rank')
    def check_customer_rank(self):
        if self.contacts_customer_rank > 10:
            raise UserError("Please, Enter customer rank from 0 to 9")
