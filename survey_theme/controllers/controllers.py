# -*- coding: utf-8 -*-
# from odoo import http


# class SurveyTheme(http.Controller):
#     @http.route('/survey_theme/survey_theme/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/survey_theme/survey_theme/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('survey_theme.listing', {
#             'root': '/survey_theme/survey_theme',
#             'objects': http.request.env['survey_theme.survey_theme'].search([]),
#         })

#     @http.route('/survey_theme/survey_theme/objects/<model("survey_theme.survey_theme"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('survey_theme.object', {
#             'object': obj
#         })
