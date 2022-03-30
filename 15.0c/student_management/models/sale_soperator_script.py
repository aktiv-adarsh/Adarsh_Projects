
from odoo import models, fields, api


class SaleInheritRank(models.Model):

    _inherit = "sale.order"

    sale_customer_rank = fields.Integer(string="Customer Rank", related="partner_id.contacts_customer_rank")

    def wiz_pids(self):
        print("---------Wizard---------")

