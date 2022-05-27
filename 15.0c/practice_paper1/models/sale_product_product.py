from odoo import models, fields, api
from odoo.exceptions import ValidationError


class PracticePaper(models.Model):
    _inherit = 'product.product'

    qty_on_order = fields.Float(string="Quantity on order")


class PracticeSaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    max_qty_allowed = fields.Float(related='product_id.qty_on_order', string="Max. Qty Allowed")

    # if product_uom_qty <= max_qty_allowed:
    #     raise ValidationError("===Sorry====")
    # # if product_uom_qty_unique <= max_qty_allowed:
    #     raise ValidationError('Next Check Number should only contains numbers.')
