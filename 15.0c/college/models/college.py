
from odoo import models, fields, api

class college(models.Model):

    _name='college.college'
    _description='college.college'

    cname = fields.Char(string="College")
    cid = fields.Integer(string="College Id")
    caddress = fields.Text(string="College Address")


    def search_record(self):
        print(self.env['res.partner'].search([]).read(['email']))

    def search_true_record(self):
        record = self.env['res.partner'].search(['email','=',True]).read(['email'])
        for rec in record:
            print(rec)