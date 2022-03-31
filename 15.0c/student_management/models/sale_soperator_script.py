from odoo import models, fields, api


class SaleInheritRank(models.Model):
    _inherit = "sale.order"

    sale_customer_rank = fields.Integer(string="Customer Rank", related="partner_id.contacts_customer_rank")

    def wiz_pids(self):
        print("---------Wizard---------")


    @api.model
    def create(self, vals):
        res = super(SaleInheritRank, self).create(vals)
        if res.partner_id.contacts_customer_rank > 5:
            best_cate_id = self.env.ref("student_management.res_partner_category_best_customer").id
            res.partner_id.write(
                {'category_id': [(4, best_cate_id)]})  # 4 - Link, best_cate_id - id of Best Customer tag
        return res
