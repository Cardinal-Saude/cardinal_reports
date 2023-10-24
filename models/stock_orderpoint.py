from odoo import api, fields, models


class StockWarehouseOrderpoint(models.Model):
    _inherit = 'stock.warehouse.orderpoint'

    stock_days = fields.Float('Dias Estoque', readonly=True, store=True, compute='_compute_stock_days')

    @api.depends('qty_forecast')
    def _compute_stock_days(self):
        for orderpoint in self:
            if orderpoint.product_id.sales_monthly == 0:
                orderpoint.stock_days = 0
            else:
                orderpoint.stock_days = orderpoint.qty_forecast/orderpoint.product_id.sales_monthly * 30
