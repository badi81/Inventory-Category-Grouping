from odoo import fields, models

class StockQuant(models.Model):
    _inherit = 'stock.quant'
    
    categ_id = fields.Many2one(
        comodel_name='product.category',
        related='product_id.categ_id',
        string='Product Category',
        store=True,
        readonly=True,
    )