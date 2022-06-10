from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers import portal
import base64
from base64 import b64decode, b64encode
from odoo import http


class ContactsCreation(http.Controller):

    @http.route('/contacts_controller', type='http', auth='user', website=True)
    def contact_data(self, **kw):
        """Display all the contact list"""

        records = request.env['res.partner'].sudo().search([])
        return request.render('Adarsh_Exam_02-06-2022.display_all_contacts', {'contact': records})

    @http.route('/registration', type='http', auth='user', website=True)
    def contacts_data(self, **kw):
        """it will create new record on contact"""

        if kw:
            files = request.httprequest.files.getlist('image_1920')
            print("\n\n\n-------------------", files)

            for data in files:
                result = request.env['res.partner'].sudo().create({'name': kw.get('name'),
                                                                   'email': kw.get('email'),
                                                                   'phone': kw.get('phone'),
                                                                   'image_1920': base64.b64encode(data.read())})
                print("-------------------", result)
                print("\n\n Result \n")
            return request.render('Adarsh_Exam_02-06-2022.contacts_new_user_registration', {})
        else:
            result = request.env['res.partner'].sudo().search([])
            print("\n\n******* Else registration *******\n")
            return request.render('Adarsh_Exam_02-06-2022.contacts_new_user_registration', {'res_partner': result})

    # @http.route('/registration', type="http", auth="user", website=True)
    # def create_student(self, **kw):
    #     """It will pass the image from portal to contacts"""
    #
    #     files = request.httprequest.files.getlist('image')
    #
    #     for file in files:
    #
    #         partner_id = int(kw.get('partner_id'))
    #
    #         attachment = file.read()
    #
    #         partner = request.env['res.partner'].sudo().browse(partner_id)
    #
    #         if partner:
    #             partner.write({'image_1920': base64.encodestring(attachment)})
    #
    #             request.env.user.image_1920 = base64.encodestring(attachment)
    #
    #     return request.redirect('/home')


class CountAllContacts(portal.CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        """It will display total records at my account page."""

        print("\n\n--------IN Function-\n\n")
        values = super()._prepare_home_portal_values(counters)
        counted = request.env['res.partner'].search_count([])
        print("\n\n--------counted-", counted, "\n\n")
        values.update({'contact_count': counted})
        return values
