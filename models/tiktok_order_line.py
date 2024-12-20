from odoo import fields, models, api

class OrderLine(models.Model):
    _name = "tiktok.order.line"
    _description = "Order Line"

    name = fields.Char("Product Name")
    order_line_id = fields.Char("Order Line ID")
    sku_image = fields.Binary("Cover")
    currency_id = fields.Many2one("res.currency")
    sale_price = fields.Monetary("Sale Price", "currency_id")

    order_id = fields.Many2one("tiktok.order", required=True)
