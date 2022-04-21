# -*- coding: utf-8 -*-
# test_demo Database
from odoo import models, fields, api, _


class StudentEmail(models.Model):
    _inherit = 'student.management'

    """Send E-mail to the current customer when it has confirm state"""

    def student_email_send_action(self):
        print("\n------ Func In----------")
        template_id = self.env.ref('student_management.student_details_email').id
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)
        print("\n------ Func end----------\n")
