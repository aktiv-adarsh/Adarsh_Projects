from odoo import http
from odoo.http import request


class ContactController(http.Controller):

    @http.route('/contact_controller', type='http', auth='public', website=True)
    def contact_data(self, **kwargs):

        contact_data = request.env['res.partner'].sudo().search([])
        return request.render('contact_controller.contact_records', {'my_details': contact_data})
