# -*- coding: utf-8 -*-
# test_demo Database
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class StudentEmailDetails(models.Model):
    _inherit = 'student.management'

    def email_action_smart_btn(self):
        """TO send email of student information"""

        print("\n\nemail_action_smart_btn\n")
        template_id = self.env.ref('student_management.student_details_email').id
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)
        print("\n------ Func end----------\n")
        if template:
            raise UserError(_('Mail send successfully'))
