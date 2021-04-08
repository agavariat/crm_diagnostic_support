# -*- coding: utf-8 -*-
{
    'name': 'CRM Diagnostic',
    'version': '0.1',
    'category': 'Crm',
    'summary': 'CRM Diagnostic',
    'description': """
CRM Diagnostic
==============
    """,
    'depends': [
        'base',
        'web',
        'crm',
        'crm_form_support'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/web_assets.xml',
        'data/email_template.xml',
        'data/ir_cron.xml',
        'views/crm_lead_view.xml',
        'views/crm_diagnostic_view.xml',      
        'report/crm_diagnostic_report_template.xml',
        'report/crm_diagnostic_report.xml',
        
    ],
    'installable': True,
    'auto_install': False,
}
