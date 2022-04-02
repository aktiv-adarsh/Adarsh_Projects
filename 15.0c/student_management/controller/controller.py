
from odoo import http
from odoo.http import request


class ContactController(http.Controller):

    @http.route('/contact_controller', type='http', auth='public', website=True)
    def contact_data(self, **kw):
        res = request.env['res.partner'].sudo().search([])
        return request.render('student_management.controller_file_data', {'student':res})
        # return "Hellow word"
        # contact = request.env['res.partner'].sudo().search([])
        # return request.render('student_management.controller_file_data', {'my_details': contact})
