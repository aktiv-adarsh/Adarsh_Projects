# -*- coding: utf-8 -*-

from odoo import models, fields, api


class adarsh(models.Model):
    _name = 'adarsh.adarsh'
    _inherit = 'mail.thread','mail.activity.mixin'
    _description = 'adarsh.adarsh'

    name = fields.Char(string="Name", required=True)
    email = fields.Char()
    contact_no = fields.Integer(size=20)
    address = fields.Char()
    today = fields.Selection(selection=[('draft', 'Draft'), ('to_approve', 'To approve'), ('posted', 'Posted'), ('cancel', 'Cancelled')], string='Select Options')
    refer = fields.Reference([('model.name', 'String_string')])
    html_wid = fields.Html() # to used as HTML Widget like it give some feature of html ie. bold, italic, underline, color etc.
    # refer = fields.Reference(selection=[('model.name', 'String_string')])
    dob = fields.Date(string="DOB", help="Date of Birth")
    description = fields.Text()
    responsible_id = fields.Many2one('res.partner', string="Responsible") # string="Responsible", comodel_name='res.partener'
    # state = fields.Selection([('draft', 'Draft), ('confirm', 'Confirm'), ('done', 'Done'), ('cancel', 'Cancelled')], string='State')
    # @api.depends('email')
    # def _email_pc(self):
    #     for record in self:
    #         record.contact_no = float(record.email)
























    # today = fields.Char(string="Name", required=True, size=40) #Give input type Character for editing.
    # today = fields.Date(string="DOB", required=True, help="Date of Birth") #provide date selection option.
    # today = fields.Boolean(string="Active", default=True) # fields.Date()
    # today = fields.Text(string='Text_Filed') #text use for long text
    # today = fields.Integer(string='Integer') #use for gatting integer value only.
    #DDD today = fields.Float(string='Float', digits=(6,3)) #to grt or display pointing val. here (6,3)
    #ERROR today = fields.Date(timestamp=datetime.datetime.now())
    #ERROR today = fields.Datetime.context_timestamp(self,timestamp=datetime.datetime.now())
    # today = fields.Binary() # field stores the encoded file in base64 in column bytea.
    # today = fields.Selection(selection=[('a', 'A')])    #Give option for selection. It has only onr "A".
