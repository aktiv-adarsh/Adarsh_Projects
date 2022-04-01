from odoo import models, fields, api


class SaleIdWizards(models.TransientModel):

    _name = 'special.operator'
    _description = 'special.operator'

    sale_2product = fields.Many2many('product.product', string="Sale 2 Products")

    """Here selected product on wizard will be created on order_line(sale)"""
    def save_button(self):
        record = self.env['sale.order'].browse(self.env.context.get('active_id'))
        for rec in self.sale_2product:
            print("-------------In For loop---------------")
            record.write({'order_line': [(0, 0, {'product_id': rec.id})]})
            print("-------------", rec, "---------------")

