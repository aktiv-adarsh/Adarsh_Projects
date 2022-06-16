from odoo import models, fields, api


class WizardBatchSale(models.TransientModel):

    _name = 'wizard.batch_sale'
    _description = 'wizard_batch_sale'

    o2m_so_line_id = fields.One2many('wizard.batch_sale2', 'wizard_id', string="Product One2Many", required=True)

    @api.model
    def default_get(self):
        """The default_get() will return the customized give data"""
        # current_id = self.env.context.get('active_model')
        res = super(WizardBatchSale, self).default_get()
        print("\n\n\n ...........Default get RES -> ", res)
        active_id = self.env['batch_sale.workflow'].browse(self.env.context.get('active_id'))
        print("\n...........Rec active ID -> ", active_id)
        print("\nself.sale_order_ids -> ", active_id.sale_order_ids)
        print("self.sale_order_ids -> ", active_id.sale_order_ids.ids)

        for data in active_id.sale_order_ids:
            print("\n\n------- Data -> ", data)
            res.update({
                "sol_product": data.order_line.product_id,
                "sol_description": data.order_line.name,
                "sol_quantity": data.order_line.product_uom_qty,
            })
        print("\n   ** END **\n\n")
        return res


class WizardBatchSale2(models.TransientModel):

    _name = 'wizard.batch_sale2'
    _description = 'wizard_batch_sale2'

    wizard_id = fields.Many2one('wizard.batch_sale')
    customer = fields.Many2one('sale.order.line', string="Sale Order")
    sol_product = fields.Char(string="Product")
    sol_description = fields.Char(string="Description")
    sol_quantity = fields.Char(string="Quantity")

    # @api.model
    # def default_get(self):
    #     """The default_get() will return the customized give data"""
    #     # current_id = self.env.context.get('active_model')
    #     res = super(WizardBatchSale2, self).default_get()
    #     print("\n\n\n ...........Default get RES -> ", res)
    #     active_id = self.env['batch_sale.workflow'].browse(self.env.context.get('active_id'))
    #     print("\n...........Rec active ID -> ", active_id)
    #     print("\nself.sale_order_ids -> ", active_id.sale_order_ids)
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
