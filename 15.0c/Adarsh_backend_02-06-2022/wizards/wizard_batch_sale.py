from odoo import models, fields, api


class WizardBatchSale(models.TransientModel):

    _name = 'wizard.batch_sale'
    _description = 'wizard_batch_sale'

    o2m_so_line_id = fields.One2many('wizard.batch_sale2', 'wizard_id', string="Product One2Many", required=True)

    @api.model
    def default_get(self, o2m_so_line_id):
        """The default_get() will return the customized give data"""
        # current_id = self.env.context.get('active_model')

        print("\n\n\n ...........Default get RES -> ")
        active_id = self.env['batch_sale.workflow'].browse(self.env.context.get('active_id'))
        print("\n...........Rec active ID -> ", active_id)
        print("\n self.sale_order_ids -> ", active_id.sale_order_ids)
        print("self.sale_order_ids -> ", active_id.sale_order_ids.ids, "\n")
        print("self.Product_id -> ", active_id.sale_order_ids.order_line, "\n")
        products = active_id.sale_order_ids.order_line.product_id
        print("self.Product_id.order line -> ", products, "\n")
        # print("\n self.o2m_so_line_id.read -> ", self.o2m_so_line_id.customer, "\n")

        # print("\n   ** END ** ", result, "\n\n")
        # print("\n   ** END ** ", result, "\n\n")
        res = super(WizardBatchSale, self).default_get(o2m_so_line_id)
        order_list = []
        for data in products:
            print("\n\n------- Data -> ", data)

            order_list.append((0, 0, {
                    'sol_product': data.id,
                    'sol_description': data.name,
                    'sol_price_unit': data.lst_price,
                    # 'sol_price_unit': data.price_unit,
                    # 'sol_quantity': data.product_uom_qty
                }))

        res.update({
            'o2m_so_line_id': order_list,
        })
        return res

    # @api.onchange('o2m_so_line_id')
    # def wizards_price(self):
    #     active_id = self.env['batch_sale.workflow'].browse(self.env.context.get('active_id'))
    #     products = active_id.sale_order_ids.order_line
    #     print("\n\n On Change total_price ")
    #     # res = super(WizardBatchSale, self).wizards_price()
    #     total_price = products.sol_price_unit
    #     total_price *= products.product_uom_qty
    #     print("\n\n On Change total_price ", total_price, "\n\n")


class WizardBatchSale2(models.TransientModel):

    _name = 'wizard.batch_sale2'
    _description = 'wizard_batch_sale2'

    wizard_id = fields.Many2one('wizard.batch_sale')
    sol_product = fields.Many2one('product.product', string="Product")
    #customer = fields.Char(string="Customer")
    # sol_product = fields.Char(string="Product")
    sol_description = fields.Char(string="Description")
    sol_quantity = fields.Float(string="Quantity")
    sol_price_unit = fields.Float(string="Price")
    # sol_quantity = fields.One2many('sale.order.line', string="Quantity")

    # @api.model
    # def default_get(self, wizard_id):
    #     """The default_get() will return the customized give data"""
    #     # current_id = self.env.context.get('active_model')
    #     res = super(WizardBatchSale2, self).default_get(wizard_id)
    #     print("\n\n\n ...........Default get RES -> ", res)
    #     active_id = self.env['batch_sale.workflow'].browse(self.env.context.get('active_id'))
    #     print("\n...........Rec active ID -> ", active_id)
    #     print("\n self.sale_order_ids -> ", active_id.sale_order_ids)
    #     print("self.sale_order_ids -> ", active_id.sale_order_ids.ids)
    #
    #     for data in active_id.sale_order_ids:
    #         print("\n\n------- Data -> ", data)
    #         res.update({
    #             "sol_product": data.order_line.product_id,
    #             "sol_description": data.order_line.name,
    #             "sol_quantity": data.order_line.product_uom_qty,
    #         })
    #     print("\n   ** END **\n\n")
    #     return res





# res = super(WizardBatchSale, self).default_get(o2m_so_line_id)
#         print("\n\n\n ...........Default get RES -> ", res)
#         active_id = self.env['batch_sale.workflow'].browse(self.env.context.get('active_id'))
#         print("\n...........Rec active ID -> ", active_id)
#         print("\n self.sale_order_ids -> ", active_id.sale_order_ids)
#         print("self.sale_order_ids -> ", active_id.sale_order_ids.ids, "\n")
#         print("self.Product_id -> ", active_id.sale_order_ids.order_line, "\n")
#         products = active_id.sale_order_ids.order_line.product_id
#         print("self.Product_id.order line -> ", products, "\n")
#         # print("\n self.o2m_so_line_id.read -> ", self.o2m_so_line_id.customer, "\n")
#         result = []
#         wizards2 = self.env['wizard.batch_sale']
#         for data in products:
#             print("\n\n------- Data -> ", data)
#             result.append(
#                 [(0, 0, {
#                     'sol_product': data.default_code,
#                     'sol_description': data.name,
#                     'sol_price_unit': data.lst_price,
#                 })])
#
#             print("\n   ** IN LOOP ** ", res, "\n\n")
#             print("\n   ** IN LOOP ** ", result, "\n\n")
#         res.update({'o2m_so_line_id': result})
#         print("\n   ** TYPE END ** ", type(res), "\n\n")
#         print("\n   ** END ** ", res, "\n\n")
#         print("\n   ** END ** ", result, "\n\n")
#         return res