
from odoo import models, fields, api

class OfficeToStudent(models.Model):

    _inherit = "project.project"

    sid = fields.Char(string="Student ID")
    sname = fields.Char(string="Student name")
    saddress = fields.Char(string="Student Address")





import xmlrpc.client

# Destination DB -
dest_db_url = 'http://localhost:9999'
dest_db_db = 'v15_test_02m'
dest_db_username = 'admin'
dest_db_password = 'admin'

dest_db_common = xmlrpc.client.ServerProxy(
    '{}/xmlrpc/2/common'.format(dest_db_url))
dest_db_common.version()
dest_db_uid = dest_db_common.authenticate(
    dest_db_db, dest_db_username, dest_db_password, {})
dest_db_models = xmlrpc.client.ServerProxy(
    '{}/xmlrpc/2/object'.format(dest_db_url))
print("\n\n Destination db Details: ", dest_db_common.version())

# Create Record
# sale_dict = {
#     'partner_id': 11,
#     'order_line': [(0, 0, {
#         'product_id': 31,
#         'product_uom_qty': 10
#     })]
# }
# sale_record = dest_db_models.execute_kw(
#     dest_db_db, dest_db_uid, dest_db_password, 'sale.order', 'create', [sale_dict])
# print ("\n\n sale_record>>>>>>>>>>>", sale_record)

# # Link line with main ID
# line_dict = {
#     'product_id': 24,
#     'product_uom_qty': 25,
#     # 'order_id': 21
# }
# line_record = dest_db_models.execute_kw(
#     dest_db_db, dest_db_uid, dest_db_password, 'sale.order.line', 'create', [line_dict])
# print ("\n\n line_record>>>>>>>>>>>", line_record)

# # Replace o2m lines
# order_dict_to_upate = {'order_line': [(6, 0, [50])]}
# line_record = dest_db_models.execute_kw(
#     dest_db_db, dest_db_uid, dest_db_password, 'sale.order', 'write', [21, order_dict_to_upate])

# line_list = [47]
# # Remove relation from main obejct but doesn't delete:
# order_dict_to_upate = {'order_line': [(3, l) for l in line_list]}
# line_record = dest_db_models.execute_kw(
#     dest_db_db, dest_db_uid, dest_db_password, 'sale.order', 'write', [21, order_dict_to_upate])
# # print("\n\n After line_ids>>>>>>>>>>>", line_ids)

line_list = [1]
 # Append ids to 02m and m2m fields
order_dict_to_upate = {'category_id': [(6, 0, line_list)]}
line_record = dest_db_models.execute_kw(
    dest_db_db, dest_db_uid, dest_db_password, 'res.partner', 'write', [11, order_dict_to_upate])


# # Update 02m field value
# order_dict_to_upate = {'order_line': [(1, 45, {'product_uom_qty': 25})]}
# line_record = dest_db_models.execute_kw(
#     dest_db_db, dest_db_uid, dest_db_password, 'sale.order', 'write', [21, order_dict_to_upate])
# # print ("\n\n After line_ids>>>>>>>>>>>", line_ids)


# # Unlink o2m line from db
# order_dict_to_upate = {'order_line': [(2, 45)]}
# line_record = dest_db_models.execute_kw(
#     dest_db_db, dest_db_uid, dest_db_password, 'sale.order', 'write', [21, order_dict_to_upate])

# Search Order Lines
# line_ids = dest_db_models.execute_kw(
#     dest_db_db, dest_db_uid, dest_db_password, 'sale.order.line', 'search', [[['order_id', '=', 21]]])
# print("\n\n line_ids>>>>>>>>>>>", line_ids)
