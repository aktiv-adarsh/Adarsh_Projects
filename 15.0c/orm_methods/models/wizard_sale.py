
from odoo import models, fields, api

class WizardSale(models.TransientModel):

    _name = 'wizard.sales'
    _description = 'wizard.sales'

    customer = fields.Char(string="Customer")
    customer_email = fields.Char(string="Customer E-mail")
    sales_person = fields.Char(string="Sales Person")
    sales_person_contact = fields.Char(string="Sales Person Contact")
    payment_terms = fields.Char(string="Payment Terms")

    """The default_get() will return the customize give data"""
    @api.model
    def default_get(self,fields):
        # current_id = self.env.context.get('active_model')
        res = super(WizardSale, self).default_get(fields)
        print(".......................",res)
        rec = self.env['sale.order'].browse(self.env.context.get('active_id'))
        res.update({
            "customer": rec.partner_id.name,
            "customer_email": rec.cemail,
            "sales_person": rec.user_id.name,
            "sales_person_contact": rec.user_id.phone,
            "payment_terms": rec.payment_term_id
        })
        return res


        # customer_email = self.env.user.email
        # sales_person = self.env.user.name
        # sales_person_contact = self.env.user.work_phone
        # payment_terms = self.env.user.property_supplier_payment_term_id
        # print(customer)
