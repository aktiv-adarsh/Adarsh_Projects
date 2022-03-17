# -*- coding: utf-8 -*-

"""1) ValidationError means that type of error which is always fix,
        ie, contact num must have 10 digit length."""

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class RentalType(models.Model):

    _name = 'rental.type'
    _description = 'rental_type'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", tracking=True, required=True) # Tracking field will display who has which content changed
    code = fields.Char(string="Code", tracking=True)
    description = fields.Char(string="Description", tracking=True)

    """'message_post' will generate log message of given parameters."""
    def msg_post(self):
        msg="Message Confirmed of,  "
        self.message_post(body=msg + self.name + "code: " + self.code + "Description  "+self.description)



    """@api constrains are use when user wants to give multiple condition which
        can not give to 'sql constrains' at that place we use api constrain"""
    @api.constrains('code')
    def check_code(self):
        for record in self:
            if len(record.code) >= 5:
                raise ValidationError(("Len of %s is greater than 5" % record.code))


    """ when user click on create button then here give data will generate on form
        by using create method.
        When user has fill or not filled the code and description then vals['code']=123 and 
        vals['description']="Aabc12" is auto override"""
    @api.model
    def create(self, vals):
        vals['code']=123
        vals['description']="Aabc12"
        res = super(RentalType, self).create(vals)
        # print("Res is: ", res)
        # print("Values is: ",vals)
        # print("Self is: ",self)
        return res
