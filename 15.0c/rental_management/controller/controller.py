
from odoo import http
from odoo.http import request


class RentalContactController(http.Controller):

    @http.route('/contacts_controller', type='http', auth='public', website=True)
    def contacts_data(self, **kw):
        res = request.env['res.partner'].sudo().search([])
        return request.render('rental_management.controllers_file_data', {'contact': res})

    print("------------------Before dec------------------")

    @http.route(['/contacts_controller/<model("res.partner"):record>/'], type='http', auth='public', website=True)
    def contacts_data_link(self, record):
        print("----------------record--------[", record, "]----")
        return request.render('rental_management.controllers_file_data_link', {'link_record': record})
