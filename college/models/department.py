
from odoo import models, fields, api

class college(models.Model):

    _inherit='college.college'

    cname = fields.Char(string="Department Name")
    cid = fields.Integer(string="Department Id")
    caddress = fields.Text(string="Department Address")
