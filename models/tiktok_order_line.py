import requests
import base64

from odoo import fields, models, api

class OrderLine(models.Model):
    _name = "tiktok.order.line"
    _description = "Order Line"

    name = fields.Char("Product Name")
    order_line_id = fields.Char("Order Line ID")
    sku_image = fields.Binary("Product Image", compute="_compute_image_url")
    sku_image_url = fields.Char(string="SKU Image URL")
    currency_id = fields.Many2one("res.currency")
    sale_price = fields.Monetary("Sale Price", "currency_id")

    order_id = fields.Many2one("tiktok.order", required=True)
    product_id = fields.Many2one("tiktok.product")
    select_product = fields.Char("Select Product", related="product_id.product_type")
    select_color = fields.Char("Select Color", related="product_id.product_color")
    select_size = fields.Char("Select Size", related="product_id.product_size")

    @api.depends("sku_image_url")
    def _compute_image_url(self):
        image = False
        if self.sku_image_url:
            image = base64.b64encode(requests.get(self.sku_image_url).content)
        self.sku_image = image
