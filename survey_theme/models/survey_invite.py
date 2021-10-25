# -*- coding: utf-8 -*-

import logging
import re
import werkzeug

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)



class SurveyInvite(models.TransientModel):
    _inherit = 'survey.invite'

    
    category_ids = fields.Many2many(
        string='Add by tags',
        comodel_name='res.partner.category',
    )
    exist_laggards = fields.Boolean(string="Send to laggards")
    show_laggards = fields.Boolean(string='Number of laggards',
        compute='_compute_laggards' )
    
    @api.depends('survey_id')
    def _compute_laggards(self):
        for record in self:
            user_inputs_ids = record.survey_id.user_input_ids.filtered(lambda r: r.state == 'new' and r.test_entry == False).mapped("partner_id.id")
            if len(user_inputs_ids):
                record.show_laggards = True
            else:
                record.show_laggards = False
    @api.onchange('survey_id')
    def _onchange_survey_id(self):
        self.template_id = self.env.ref('survey_theme.mail_template_user_input_invite_KN').id

    @api.onchange('exist_laggards')
    def load_user_incomplete(self):
        for r in self:
            contacts_ids = r.env['res.partner'].search([('category_id','in',r.category_ids.ids),('email','!=',''),('parent_id','!=',False)])
            if self.exist_laggards:
                laggards = self.env['res.partner'].browse(self.survey_id.user_input_ids.filtered(lambda r: r.state == 'new' and r.test_entry == False).mapped("partner_id.id"))
                for laggard in laggards:
                    if laggard not in contacts_ids:
                        contacts_ids += laggard
            r.write({'partner_ids':[(6, None, contacts_ids.ids)]})
        
        
        
    @api.onchange('category_ids')
    def _onchange_category(self):
        for r in self:
            contacts_ids = r.env['res.partner'].search([('category_id','in',r.category_ids.ids),('email','!=',''),('parent_id','!=',False)])
            if self.exist_laggards:
                laggards = self.env['res.partner'].browse(self.survey_id.user_input_ids.filtered(lambda r: r.state == 'new' and r.test_entry == False).mapped("partner_id.id"))
                for laggard in laggards:
                    if laggard not in contacts_ids:
                        contacts_ids += laggard
            r.write({'partner_ids':[(6, None, contacts_ids.ids)]})


