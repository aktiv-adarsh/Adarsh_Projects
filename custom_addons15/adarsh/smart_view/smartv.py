# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Smart_View(models.Model):
    _name = 'smartview.smartview'
    _description = 'smartview'

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email")
    contactno = fields.Integer(string="Contact No", size=20)
    rating = fields.Selection([('a','1'),('b','2'),('c','3'),('d','4'),('e','5'),('f','6')])
    count = fields.Integer(string="record count", compute="")

#     _sql_constraints = [
#         ('contactno_uniq', 'unique(contactno)', 'This user name already exist !')
#     ]

    @api.constrains('name')
    def check_name(self):
        for record in self:
            if len(record.name) >= 7:
                raise ValidationError(("Len of %s is greater than 7" % record.name))

    def sbutton(self):
        print("Button clicked")

    @api.model
    def create(self, vals):
        vals = {'name': 'ABC', 'standard': 10}
        res = super(smartview, self).create(vals)
        return res
