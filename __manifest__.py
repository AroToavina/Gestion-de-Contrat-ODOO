{
    'name': 'Gestion de Contrats',
    'version': '1.0',
    'summary': 'Module pour la gestion des contrats et la facturation',
    'sequence': 10,
    'description': "Gérer les contrats et générer des factures",
    'category': 'Accounting',
    'depends': ['base', 'account'],
    'data': [
        'views/contract_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
