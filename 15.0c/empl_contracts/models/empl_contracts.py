from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers import portal


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


class ContractsCounts(portal.CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        """To display all records total at my account"""

        values = super()._prepare_home_portal_values(counters)
        counted = request.env['hr.contract'].search_count([('employee_id', '=', request.env.user.employee_id.id)])
        # print("\n\n--------counted-", counted, "\n\n")
        values.update({'contracts_count': counted})
        return values
