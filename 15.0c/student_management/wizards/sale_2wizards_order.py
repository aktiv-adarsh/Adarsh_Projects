from odoo import models, fields, api, _


class SaleIdWizards(models.TransientModel):

    _name = 'student.wizard'
    _description = 'student.wizard'

    sale_2product = fields.Many2many('product.product', string="Sale 2 Products")

    def save_button(self):
        print("---------------",self, "----------------------")

    def save_button(self):
        # super(SaleIdWizards, self).save_button()
        print("-------------In Default get---------------")
        record = self.env['product.product'].browse(self.env.context.get('active_id'))
        print("-------------After Env---------------")
        for rec in self.sale_2product:
            print("-------------In For loop---------------")
            record.write({'order_line': [0, 0, {'product_id': rec.id}]})
            print("--------------------", rec)
            print("-------------", rec, "---------------")

