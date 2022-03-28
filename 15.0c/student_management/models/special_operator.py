from odoo import models, fields, api

class SpecialOperator(models.Model):

    _inherit = "res.partner"

    dest_db_url = 'http://localhost:9999'
    dest_db_db = 'v15_test_02m'
    dest_db_username = 'admin'
    dest_db_password = 'admin'

    def calc_tags(self):
        count = 1
        for rec in self.tag_ids:
            count += 1
            if count >= 5:
                order_dict_to_upate = {'category_id': [(1, 0, line_list)]}
                line_record = dest_db_models.execute_kw(
                    dest_db_db, dest_db_uid, dest_db_password, 'res.partner', 'write', [+6, order_dict_to_upate])
