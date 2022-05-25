
from odoo import models, fields, api


class PracticePaper(models.Model):

    _inherit = 'product.product'

    qty_on_order = fields.Float(string="Quantity on order")

    @api.onchange('qty_on_order')
    def assign_vals_on_line(self):
        print("\n\n\nIn the func\n\n\n")
        record = self.env['sale.order.line']  # .browse(self.env.context['max_qty_allowed.id'])
        print("\n\n --------record = ", record, "\n\n")
        record.max_qty_allowed = [(6, 0, self.qty_on_order)]
        print("--------max_qty_allowed = ", record.max_qty_allowed, "\n\n\n")


class PracticeSaleOrderLine(models.Model):

    _inherit = 'sale.order.line'

    max_qty_allowed = fields.Float(string="Max. Qty Allowed")
    # products_variants_id = fields.Many2one(comodel_name='product.product')
    # max_qty_allowed = fields.Float(related='products_variants_id.qty_on_order', string="Max. Qty Allowed")
