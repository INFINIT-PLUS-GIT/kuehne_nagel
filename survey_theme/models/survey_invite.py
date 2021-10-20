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
    
    @api.onchange('category_ids')
    def _onchange_category(self):
        for r in self:
            r.write({'partner_ids':[(6, None, r.env['res.partner'].search([('category_id','in',r.category_ids.ids),('email','!=',''),('parent_id','!=',False)]).ids)]})
            