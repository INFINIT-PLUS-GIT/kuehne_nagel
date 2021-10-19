# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Survey(models.Model):
    _inherit = 'survey.survey'
    background_image = fields.Binary("Background Image", attachment=True)
    
    def get_url_img(self):

        attachment = self.env['ir.attachment'].search([('res_model', '=', 'survey.survey'), ('res_id', '=', self.id)], limit=1)
        img_url = "/web/image/ir.attachment/%s/datas" % attachment.id

        return img_url
        # For website/report
        #<img t-att-src="/web/image/ir.attachment/attachment.id/datas"/>
class survey_nps(models.Model):
    _inherit = 'survey.question'
    
    
    type_simple_question = fields.Selection(
        string='Type',
        selection=[('yesno', 'Yes or No'), ('rate', 'Rate'),('other','Other')],
        default='other'
    )
    triggering_answer_id = fields.Many2many(
        'survey.question.answer', string="Triggering Answer", copy=False, compute="_compute_triggering_answer_id",
        store=True, readonly=False, help="Answer that will trigger the display of the current question.",
        domain="[('question_id', '=', triggering_question_id)]")
    
    
    
