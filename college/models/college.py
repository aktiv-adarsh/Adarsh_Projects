
from odoo import models, fields, api

class college(models.Model):

    _name='college.college'
    _description='college.college'

    cname = fields.Char(string="College Name")
    cid = fields.Integer(string="College Id")
    caddress = fields.Text(string="College Address")
