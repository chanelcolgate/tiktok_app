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

    mockup_front_image = fields.Binary("Mockup Front Image", compute="_compute_mockup_front_image_url")
    mockup_back_image = fields.Binary("Mockup Back Image", compute="_compute_mockup_back_image_url")
    design_front_image = fields.Binary("Design Front Image", compute="_compute_design_front_image_url")
    design_back_image = fields.Binary("Design Back Image", compute="_compute_design_back_image_url")

    mockup_front_image_url = fields.Char(string="Mockup Front Image URL")
    mockup_back_image_url= fields.Char(string="Mockup Back Image URL")
    design_front_image_url = fields.Char(string="Design Front Image URL")
    design_back_image_url = fields.Char(string="Design Back Image URL")
    note = fields.Char("Notes")
    quantity = fields.Integer()
    shipment = fields.Selection(
        [
            ("1", "FirstClass"),
            ("2", "Priority"),
            ("3", "RushProduction"),
            ("4", "OverNight"),
            ("6", "Expedite")
        ],
        default="1"
    )

    # Product Image
    @api.depends("sku_image_url")
    def _compute_image_url(self):
        image = False
        if self.sku_image_url:
            image = base64.b64encode(requests.get(self.sku_image_url).content)
        self.sku_image = image

    # Mockup front image
    @api.depends("mockup_front_image_url")
    def _compute_mockup_front_image_url(self):
        image = False
        if self.mockup_front_image_url:
            image = base64.b64encode(requests.get(self.mockup_front_image_url).content)
        self.mockup_front_image = image

    @api.depends("mockup_back_image_url")
    def _compute_mockup_back_image_url(self):
        image = False
        if self.mockup_back_image_url:
            image = base64.b64encode(requests.get(self.mockup_back_image_url).content)
        self.mockup_back_image = image

    @api.depends("design_front_image_url")
    def _compute_design_front_image_url(self):
        image = False
        if self.design_front_image_url:
            image = base64.b64encode(requests.get(self.design_front_image_url).content)
        self.design_front_image = image

    @api.depends("design_back_image_url")
    def _compute_design_back_image_url(self):
        image = False
        if self.design_back_image_url:
            image = base64.b64encode(requests.get(self.design_back_image_url).content)
        self.design_back_image = image
