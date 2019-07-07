# -*- coding: utf-8 -*-
{
    'name': "faculty_attendance",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Your Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','faculty_core'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'templates.xml',
        'views/register_sheet_view.xml',
        'views/attendance_sheet.xml',
        'wizard/barcode_view.xml',
        'report/student_profile.xml',
        'report/student_report.xml',
        'report/absence_report.xml',
        'report/absence_main.xml',
        'wizard/check_student_absent.xml',
        'report/monthly_report_oFstudent_attendance/monthlyReport.xml',
        'report/monthly_report_oFstudent_attendance/reportDetails.xml',
        'wizard/monthly_report_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}