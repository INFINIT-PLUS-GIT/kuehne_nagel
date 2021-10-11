# -*- coding: utf-8 -*-

from odoo import models, fields, api


class survey_nps(models.Model):
    _inherit = 'survey.question'
    
    
    type_simple_question = fields.Selection(
        string='Type',
        selection=[('yesno', 'Yes or No'), ('rate', 'Rate'),('other','Other')],
        default='other'
    )
    
    
    
