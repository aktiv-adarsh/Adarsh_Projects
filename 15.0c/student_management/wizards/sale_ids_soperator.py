from odoo import models, fields, api, _


class SaleIdWizards(models.TransientModel):
    _name = 'student.wizard'
    _description = 'student.wizard'

    sale_2product = fields.Many2many('product.product', string="Sale 2 Products")

    def save_button(self):
        for rec in self:
            print("-------------", rec)

    def default_get(self):
        # get_env = self.env['product.product']
        res = super(SaleIdWizards, self).default_get(fields)
        print(".......................", res)
        print("---------------Default get------------")
        # rec = self.env['product.product'].browse(self.env.context.get('active_id'))
        for rec in self:
            rec.update({
                'order_line': [0, 0, 'product.id']
            })
            print("--------------------", rec)
        return res
