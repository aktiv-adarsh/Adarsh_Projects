
from odoo import http
from odoo.http import request


class ContactController(http.Controller):

    @http.route('/contact_controller', type='http', auth='public', website=True)
    def contact_data(self, **kw):
        res = request.env['res.partner'].sudo().search([])
        return request.render('student_management.controller_file_data', {'contact': res})

    print("------------------Before dec------------------")

    @http.route(['/contact_controller/<model("res.partner"):record>/'], type='http', auth='public', website=True)
    def contact_data_link(self, record):
        print("----------------record--------[", record, "]----")
        return request.render('student_management.controller_file_data_link', {'link_record': record})
