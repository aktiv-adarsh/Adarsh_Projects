from odoo import http
from odoo.http import request


class ContactsControllers(http.Controller):

    @http.route('/contacts_controller', type='http', auth='user', website=True)
    def contact_data(self, **kw):
        res = request.env['res.partner'].sudo().search([])
        return request.render('rental_management.controllers_file_data', {'contact': res})

    print("------------------Before dec------------------")

    @http.route(['/contacts_controller/<model("res.partner"):record>/'], type='http', auth='user', website=True)
    def contact_data_link(self, record):
        print("----------------record--------[", record, "]----")
        return request.render('rental_management.controllers_file_data_link', {'link_record': record})

    @http.route('/registration', type='http', auth='public', website=True)
    def contacts_data(self, **kw):
        if kw:
            result = request.env['res.partner'].sudo().create(kw)
            print("\n\n Result \n")
            return request.render('rental_management.controllers_new_user_registration', {'res_partner': result})
        else:
            result = request.env['res.partner'].sudo().search([])
            print("\n\n******* Else registration \n")
            return request.render('rental_management.controllers_new_user_registration', {'res_partner': result})

    @http.route('/controller/website', type='http', auth='public', website=True)
    def controller_website(self, **kw):
        # return "Hello world"
        return request.render('rental_management.controllers_website_views', {})

    def _prepare_home_portal_values(self, counters):
        print("\n\n--------IN Function-\n\n")
        values = super()._prepare_home_portal_values(counters)
        counted = request.env['res.partner'].search_count([])
        print("\n\n--------counted-", counted, "\n\n")
        # values.update = {'count': counted}
        values['counted']= counted
        return values
