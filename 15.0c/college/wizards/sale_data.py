
from odoo import models, fields

class WizardSale(models.TransientModel):

    _name = 'wizard.sales'
    _description = 'wizard.sales'

    def func(self):
        print("Hiiiiiii")
