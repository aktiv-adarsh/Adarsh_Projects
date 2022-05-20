from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers import portal
import base64
from odoo import http
from odoo.http import request


class EmplContracts(http.Controller):

    @http.route('/my/emp_contracts', type='http', auth='user', website=True)
    def contracts_data(self, **kw):
        """This function will get the employees records"""

        res = request.env['hr.contract'].sudo().search([('employee_id', '=', request.env.user.employee_id.id)])
        # print("\n\n\n----------------emp_id", res.employee_id.id)

        # print("\n\n------FUNC--in empl_contracts-", res, "------\n\n\n")
        return request.render('empl_contracts.emp_contracts_list_view', {'contract': res})

    @http.route(['/my/emp_contracts/<model("hr.contract"):record>'], type='http', auth='user', website=True)
    def link_to_contract_details(self, record):
        # print("\n\n\n\n Function Executed \n\n\n")
        return request.render("empl_contracts.contracts_link_to_details", {'records': record})

    @http.route('/project/uploaded', type='http', auth="public", website=True)
    def contract_details_attachment_button(self, **post):
        # new_task = request.env['ir.attachment']
        print("----------------**POST--------------", post)
        Attachments = request.env['ir.attachment']
        print("------------------------------", Attachments)
        name = post.get('attachment').filename
        print("---===============NAME===============", name)
        file = post.get('attachment')
        print("---===============FILE================", file)
        project_id = post.get('project_id')
        print("---===============PROJECT_ID==========", project_id)

        attached_files = request.httprequest.files.getlist('attachment')
        for attachment in attached_files:
            request.env['ir.attachment'].sudo().create({
                'name': attachment.filename,
                'res_model': 'hr.contract',
                'res_id': project_id,
                'type': 'binary',
                'datas': base64.b64encode(attachment.read()),
            })

    # print("----------------**POST--------------", post)
    # Attachments = request.env['ir.attachment']
    # print("------------------------------", Attachments)
    # name = post.get('attachment').filename
    # print("---===============NAME===============", name)
    # file = post.get('attachment')
    # print("---===============FILE================", file)
    # project_id = post.get('project_id')
    # print("---===============PROJECT_ID==========", project_id)
    # attachment_id = Attachments.create({
    #     'name': name,
    #     'res_name': name,
    #     'type': 'binary',
    #     'res_model': 'hr.contract',
    #     'res_id': project_id,
    #     'datas': base64.b64encode(file.read()),
    #
    # })
    # print("---===============ATTACHMENT_ID=======", attachment_id, "\n\n\n\n")


class ContractsCounts(portal.CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        """To display all records total at my account"""

        values = super()._prepare_home_portal_values(counters)
        counted = request.env['hr.contract'].search_count([('employee_id', '=', request.env.user.employee_id.id)])
        # print("\n\n--------counted-", counted, "\n\n")
        values.update({'contracts_count': counted})
        return values
