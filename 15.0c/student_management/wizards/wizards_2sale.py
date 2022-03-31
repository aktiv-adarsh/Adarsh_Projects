from odoo import models, fields, api


class Wizard2Sale(models.Model):

    _inherit = "sale.order"

    save_on_wizard = fields.Many2many('product.product')









    # def default_get(self):
    #     # get_env = self.env['product.product']
    #     res = super(Wizard2Sale, self).default_get()
    #     print(".......................", res)
    #     print("---------------Default get------------")
    #     # rec = self.env['product.product'].browse(self.env.context.get('active_id'))
    #     # for rec in self:
    #     #     rec.write({
    #     #         'order_line': [0, 0, (rec, 'product_id.id')]
    #     #     })
    #     #     print("--------------------", rec)
    #     sale_dict = {
    #         # 'partner_id': 11,
    #         'order_line': [(0, 0, 'sale_2product')]}
    #     return sale_dict

    """The default_get() will return the customize give data"""
    #
    # @api.model
    # def default_get(self, fields):
    #     # current_id = self.env.context.get('active_model')
    #     res = super(WizardSale, self).default_get(fields)
    #     print(".......................", res)
    #     rec = self.env['sale.order'].browse(self.env.context.get('active_id'))
    #     res.update({
    #         "customer": rec.partner_id.name,
    #         "customer_email": rec.cemail,
    #         "sales_person": rec.user_id.name,
    #         "sales_person_contact": rec.user_id.phone,
    #         "payment_terms": rec.payment_term_id
    #     })
    #     return res

    #
    # def sale_save_button(self):
    #     print("----------------Btn call-----------------",self)
