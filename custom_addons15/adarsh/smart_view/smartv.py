# -*- coding: utf-8 -*-
"""1.) ValidationError means that type of error which is always fix like,
        contact no must be 10 digit long.
   2.) UserDefineError means some conditions are given by user if condition is not satisfy
        then it will raise an error like, name not be duplicate"""

from datetime import datetime
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Smart_View(models.Model):

    _name = 'smartview.smartview'
    _description = 'smartview'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", tracking=True)
    email = fields.Char(string="Email", tracking=True)
    contact_no = fields.Integer(string="Contact No", size=20, tracking=True)
    rating = fields.Selection([('a', '1'), ('b', '2'), ('c', '3'), ('d', '4'), ('e', '5'), ('f', '6')], tracking=True)
    count = fields.Integer(string="record count", compute="", tracking=True)
    # defaults=fields.Datetime(string="Date", default=datetime.now()) #date with time
    defaults = fields.Datetime(string="Date", default=fields.Datetime.now)  # date with time sec

    m2o_fields_id = fields.Many2one('res.partner',string="Many2One")
    o2m_field_ids = fields.One2many('adarsh.adarsh','m2o_fields1_id',string="One2Many")



    """When some conditions are fix then use sql constrains"""
#     _sql_constraints = [
#         ('contact_no_uniq', 'unique(contact_no)', 'This user name already exist !')
#     ]

    """@api constrains are use when user wants to give multiple condition which 
        can not give to 'sql constrains' at that place we use api constrain"""
    @api.constrains('name')
    def check_name(self):
        for record in self:
            if len(record.name) >= 12:
                raise ValidationError(("Len of %s is greater than 7" % record.name))

    """function will call the 'sbutton' (smart button) execute"""
    def sbutton(self):
        print("Button clicked")

    """when user click on create button then here give data will generate on form
        by using create method."""
    @api.model
    def create(self, vals):
        # vals = {'name': 'dsrshD', 'email':'Abc@gmail.com', 'contact_no': 10}
        vals['name']="Abgt12"
        vals['email']="Abc@gmail.com"
        vals['contact_no']=123456789
        res = super(Smart_View, self).create(vals)
        # print("Res is: ", res)
        # print("Values is: ",vals)
        # print("Self is: ",self)
        return res

    """We can edit the data by using 'write' method"""
    def write(self,val):
        print("Write Vals: ",val)
        # val['name'] = "Adarsh12"
        # val['email'] = "Adarsh12@gmail.com"
        # val['contact_no'] = 999456789
        rtn = super(Smart_View, self).write(val)
        print("Return vals is: ",rtn)
        return rtn

    """For the deletion of data we have use unlink method"""
    def unlink(self):
        print("Unlink method is:-- ",self)
        rten = super(Smart_View, self).unlink()
        print("After return:-- ", rten)
        return rten

    # @api.returns('mail.message', lambda value: value.id)
    """'message_post' will generate log message of given parameters."""
    def msg_post(self):
        msg="Message Confirmed of,  "
        self.message_post(body=msg + self.name + "  E-mail is:  "+self.email + "Contact No: " + str(self.contact_no))
