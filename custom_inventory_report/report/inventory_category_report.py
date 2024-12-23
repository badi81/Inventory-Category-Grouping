from odoo import api, fields, models, tools

class InventoryCategoryReport(models.Model):
    _name = 'inventory.category.report'
    _description = 'Inventory Report by Product Category'
    _auto = False

    location_id = fields.Many2one('stock.location', string='Location', readonly=True)
    categ_id = fields.Many2one('product.category', string='Product Category', readonly=True)
    product_count = fields.Integer(string='Product Count', readonly=True)
    quantity_on_hand = fields.Float(string='Quantity on Hand', readonly=True)
    value = fields.Float(string='Total Value', readonly=True)

    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW %s AS (
                SELECT
                    ROW_NUMBER() OVER () AS id,
                    sq.location_id,
                    pt.categ_id,
                    COUNT(DISTINCT pp.id) as product_count,
                    SUM(sq.quantity) as quantity_on_hand,
                    SUM(sq.quantity * COALESCE(pt.list_price, 0)) as value
                FROM stock_quant sq
                JOIN product_product pp ON pp.id = sq.product_id
                JOIN product_template pt ON pt.id = pp.product_tmpl_id
                WHERE sq.location_id IS NOT NULL
                GROUP BY sq.location_id, pt.categ_id
            )
        """ % self._table)