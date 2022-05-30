from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers import portal
import base64
from odoo import http
from odoo.http import request


class ContactsControllers(http.Controller):

    @http.route('/contacts_controller', type='http', auth='user', website=True)
    def contact_data(self, **kw):
        """Display all the contact list"""
        res = request.env['res.partner'].sudo().search([])
        return request.render('rental_management.controllers_file_data', {'contact': res})

    @http.route(['/contacts_controller/<model("res.partner"):record>/'], type='http', auth='user', website=True)
    def contact_data_link(self, record):
        """Display clicked contact basics details"""
        print("\n\n\n----------------record--------[", record.name, "]----\n\n\n")
        return request.render('rental_management.controllers_file_data_link', {'link_record': record})

    @http.route(['/contacts_controller/link_record/<model("res.partner"):record>/'], type='http', auth='user', website=True)
    def contact_data_to_edit(self, record):
        """Display Edit view of above clicked contact."""
        print("\n\n\n----------------record--------[", record.name, "]----\n\n\n")
        return request.render('rental_management.controllers_record_to_edit', {'link_record': record})

    # @http.route('/replace_record', type='http', auth='public', website=True)
    # def replace_records_data(self, **kw):
    #     """it will Replace new contact record"""
    #     if record:
    #         result = request.env['res.partner'].sudo().write(record)
    #         print("\n\n\n ************** Result ************** \n\n\n")
    #         return request.render('rental_management.controllers_record_to_edit', {'link_record': result})
    #     else:
    #         # result = request.env['res.partner'].sudo().search([])
    #         print("\n\n******* Else 'replace_records_data' Func called *******\n")
    #         # return request.render('rental_management.controllers_record_to_edit', {'link_record': result})

    #
    #
    #
    #

    @http.route('/registration', type='http', auth='public', website=True)
    def contacts_data(self, **kw):
        """it will create new contact record"""
        if kw:
            result = request.env['res.partner'].sudo().create(kw)
            print("\n\n Result \n")
            return request.render('rental_management.controllers_new_user_registration', {'res_partner': result})
        else:
            result = request.env['res.partner'].sudo().search([])
            print("\n\n******* Else registration *******\n")
            return request.render('rental_management.controllers_new_user_registration', {'res_partner': result})

    @http.route('/controller/website', type='http', auth='public', website=True)
    def controller_website(self, **kw):
        """TEST func:- Call on registration"""
        # return "Hello world"
        return request.render('rental_management.controllers_website_views', {})


class AllContactsCount(portal.CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        """It will display total records at my account page."""

        print("\n\n--------IN Function-\n\n")
        values = super()._prepare_home_portal_values(counters)
        counted = request.env['res.partner'].search_count([])
        print("\n\n--------counted-", counted, "\n\n")
        values.update({'contact_count': counted})
        return values
