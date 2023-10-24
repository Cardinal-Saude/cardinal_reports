from odoo import api, fields, models


class ProductMinQuantity(models.Model):
    _inherit = 'product.template'
    sales_monthly = fields.Integer(string="Vendas mensais", help="Quantidade de produtos vendidos por mês")
