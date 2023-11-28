{
    'name': 'Controle de Tecidos - Bonamaison',
    'version': '15.0.0.1.0.0',
    'author':'Bruno Campos',     
    'category': 'Vendas',
    'summary': 'Controles de estoque dos tecidos',
    'description': """
O modulo deverá gerar os arquivos de comprovante e dar baixa no estoque dos tecidos
    """,
    'depends': ['product'],
    'data': [
            "security/ir.model.access.csv",
            "report/meu_primeiro_report_template.xml",
            "report/meu_primeiro_report.xml",
            'views/comprovante.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}