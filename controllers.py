# -*- coding: utf-8 -*-
from openerp import http

# class FacultyAttendance(http.Controller):
#     @http.route('/faculty_attendance/faculty_attendance/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/faculty_attendance/faculty_attendance/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('faculty_attendance.listing', {
#             'root': '/faculty_attendance/faculty_attendance',
#             'objects': http.request.env['faculty_attendance.faculty_attendance'].search([]),
#         })

#     @http.route('/faculty_attendance/faculty_attendance/objects/<model("faculty_attendance.faculty_attendance"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('faculty_attendance.object', {
#             'object': obj
#         })