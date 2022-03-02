#
# from odoo import models, fields
#
# class RelationalFields(models.Model):
#
#     """Created one 'relational field' - 'rel.fld' name module"""
#
#     _name = 'rel.fld'
#     _description = 'rel.fld'
#
#     """Fetch all data from res.partner(Contact) to rel.fld by Many2one field"""
#     # m2o_field_id = fields.Many2one('res.partner', string="Name")
#
#     o2m_field_ids = fields.One2many('rel.fld', 'm2o_field_id', string="One2Many")
#     rid = fields.Integer(string="Id")
#     address = fields.Text(string="Address")
#     currency_id = fields.Many2one('res.currency')
#
#     m2o_field_id = fields.Many2one('res.partner', string="Many2One")
#     # user_id = fields.Many2one('User', related='resource_id.user_id', store=True, readonly=False)



from odoo import models, fields

class RelationalFields(models.Model):

    """Created one 'relational field' - 'rel.fld' name module"""

    _name = 'rel.fld'
    _description = 'rel.fld'

    """Fetch all data from res.partner(Contact) to rel.fld by Many2one field"""
    m2o_field_id1 = fields.Many2one('res.partner', string="Many2one")

    o2m_field_ids = fields.One2many('m2o.fld', 'm2o_field_id', string="One2Many")
    rid = fields.Integer(string="Id")
    address = fields.Text(string="Address")
    currency_id = fields.Many2one('res.currency')

class M2oField(models.Model):

    _name = 'm2o.fld'
    _description = 'm2o.fld'

    m2o_field_id = fields.Many2one('rel.fld', string="Many2One")
    # user_id = fields.Many2one('User', related='resource_id.user_id', store=True, readonly=False)
