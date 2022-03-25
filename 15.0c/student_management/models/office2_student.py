
from odoo import models, fields, api

class OfficeToStudent(models.Model):

    _inherit = "project.project"

    sid = fields.Char(string="Student ID")
    sname = fields.Char(string="Student name")
    saddress = fields.Char(string="Student Address")

