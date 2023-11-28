from odoo import models,fields

class ArquivoDeComprovante(models.Model):
    _name = "arquivo.comprovante"
    _description = "Gerador de arquivos de comprovantes"

    numero = fields.Char(string="Numero do comprovante", required=True)
        
    descricao = fields.Text(
        string="Descrição"  
    )

    transportadora = fields.Text(
        string="Descrição"  
    )


    product_id = fields.Many2one('product.template', string='Product')

    primeiro_modelo_ids = fields.One2many('produtos', 'product2_id', string="Primeiro Modelo Linhas")

class MeuPrimeiroModuloLinha(models.Model):
     _name = 'produtos'
    
     nome = fields.Char(string="Nome")
    
     product2_id = fields.Many2one('product.template', string='Product')
    