# -*- coding: utf-8 -*-

from odoo import models, fields, api


class adarsh(models.TransientModel):
    _name = 'adarsh.adarsh'
    _description = 'adarsh.adarsh'

    name = fields.Char(string="Name", required=True)
    email = fields.Char()
    contact_no = fields.Integer(size=20)
    address = fields.Char()
    today = fields.Selection(selection=[('draft', 'Draft'), ('to_approve', 'To approve'), ('posted', 'Posted'), ('cancel', 'Cancelled')], string='Status')
    refer = fields.Reference([('model.name', 'String_string')])
    html_wid = fields.Html() # to used as HTML Widget like it give some feature of html ie. bold, italic, underline, color etc.
    # refer = fields.Reference(selection=[('model.name', 'String_string')])
    dob = fields.Date(string="DOB", required=True, help="Date of Birth")
    description = fields.Text()
    Wizard = fields.Char()
    cancel = fields.Integer()

    @api.depends('email')
    def _email_pc(self):
        for record in self:
            record.contact_no = float(record.email)
