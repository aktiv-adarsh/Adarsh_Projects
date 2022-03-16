
from odoo import models, fields, api

class college(models.Model):

    _name = 'college.college'
    _description = 'college.college'

    cname = fields.Char(string="College")
    cid = fields.Integer(string="College Id")
    caddress = fields.Text(string="College Address")

    """It will search record which is given on parameter"""
    def search_record(self):
        email_phone = self.env['res.partner'].search([]).read(['email', 'phone'])
        for rec in email_phone:
            print(rec)

    """Here condition apply in search_read() to get conditional records from database"""
    def search_true_record(self):
        # record = self.env['res.partner'].search([('email', '!=', False), ('phone','!=',False)]).read(['email', 'phone'])
                    # OR
        domain = [('email', '!=', False), ('phone', '!=', False)]
        fields = ['email', 'phone']
        record = self.env['res.partner'].search_read(domain, fields)

        for rec in record:
            print(rec)

    """This method accept set of Ids and return 'recordset' corresponding to IDs."""
    def browse_record(self):
        # rcd = self.env['sale.order'].browse([3, 15])
        for rec in self.env['sale.order'].browse([3, 15]):
            if rec.exists():
                print("ID: ",rec.id)
                print("ID: ",rec.name)
                print("Quotation Date: ",rec.date_order)
                print("User name: ",rec.partner_id.name)
            else:
                print(rec.name,"Is not present")
