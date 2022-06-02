from odoo import fields, models, api
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    discount_boolean = fields.Boolean(compute="_hello", store=True)

    @api.depends('partner_id')
    def _hello(self):
        boolean_values = self.env['ir.config_parameter'].get_param(
            'pro_discount')
        print("====================\n\n", boolean_values)
        # self.discount_boolean = boolean_values

    def discount_search(self):

        for rec in self:
            pro_discount = self.env['promotional.discount'].search(
                [('start_date', '<=', rec.date_order),
                 ('end_date', '>=', rec.date_order),
                 ('min_order_amount', '<=', rec.amount_total)]
            )

            if len(pro_discount) == 0:
                raise ValidationError("Not Available Any Discount ")

            discount_amount = []
            for i in pro_discount:
                if i.discount_type == 'per':
                    amount = (rec.amount_total * i.discount)/100
                    discount_amount.append(amount)
                elif i.discount_type == 'fa':
                    discount_amount.append(i.discount)

            sale_order_line_obj = self.env['sale.order.line']

            if discount_amount:
                sale_order_line_obj.create({
                    'product_id': 45,
                    'order_id': self.id,
                    'price_unit': -float(min(discount_amount)),
                    })
