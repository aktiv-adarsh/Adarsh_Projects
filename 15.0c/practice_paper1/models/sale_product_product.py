
from odoo import models, fields, api


class PracticePaper(models.Model):

    _inherit = 'product.product'

    qty_on_order = fields.Float(string="Quantity on order", default=1.0)


class PracticeSaleOrderLine(models.Model):

    _inherit = 'sale.order.line'

    max_qty_allowed = fields.Float(string="Max. Qty Allowed")
