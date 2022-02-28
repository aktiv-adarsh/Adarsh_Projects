# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Smart_View(models.Model):
    _name = 'smartview.smartview'
    _description = 'smartview'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", required=True, tracking=True)
    email = fields.Char(string="Email", tracking=True)
    contactno = fields.Integer(string="Contact No", size=20, tracking=True)
    rating = fields.Selection([('a','1'),('b','2'),('c','3'),('d','4'),('e','5'),('f','6')], tracking=True)
    count = fields.Integer(string="record count", compute="", tracking=True)

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
        # vals = {'name': 'dsrshD', 'contactno': 10}
        vals['email']="Abc@gmail.com"
        vals['contactno']=1234567890
        res = super(Smart_View, self).create(vals)
        # print("Res is: ", res)
        # print("Values is: ",vals)
        # print("Self is: ",self)
        return res

    def write(self,vals):
        print("Write Vals: ",vals)
        rtn = super(Smart_View, self).write(vals)
        print("Return vals is: ",rtn)
        return rtn

    def unlink(self):
        print("Unlink method is:-- ",self)
        rten = super(Smart_View, self).unlink()
        print("After return:-- ", rten)
        return rten

    @api.returns('mail.message', lambda value: value.id)
    def message_post(self, **kwargs):
        return super(Smart_View, self._post_author()).message_post(**kwargs)