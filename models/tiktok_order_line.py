import requests
import base64

from odoo import fields, models, api

class OrderLine(models.Model):
    _name = "tiktok.order.line"
    _description = "Order Line"

    name = fields.Char("Product Name") # order.product_name
    order_line_id = fields.Char("Order Line ID") # order.id
    sku_name = fields.Char("Sku Name")
    sku_image = fields.Binary("Product Image", compute="_compute_image_url")
    sku_image_url = fields.Char(string="SKU Image URL") # order.sku_image
    currency_id = fields.Many2one("res.currency")
    sale_price = fields.Monetary("Sale Price", "currency_id") # order.sale_price

    order_id = fields.Many2one("tiktok.order", required=True) # order.order_line_list_id
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
    quantity = fields.Integer() # order.quantity

    # Product Image
    @api.depends("sku_image_url")
    def _compute_image_url(self):
        for record in self:
            image = False
            if record.sku_image_url:
                image = base64.b64encode(requests.get(record.sku_image_url).content)
            record.sku_image = image

    # Mockup front image
    @api.depends("mockup_front_image_url")
    def _compute_mockup_front_image_url(self):
        for record in self:
            image = False
            if record.mockup_front_image_url:
                image = base64.b64encode(requests.get(record.mockup_front_image_url).content)
            record.mockup_front_image = image

    @api.depends("mockup_back_image_url")
    def _compute_mockup_back_image_url(self):
        for record in self:
            image = False
            if record.mockup_back_image_url:
                image = base64.b64encode(requests.get(record.mockup_back_image_url).content)
            record.mockup_back_image = image

    @api.depends("design_front_image_url")
    def _compute_design_front_image_url(self):
        for record in self:
            image = False
            if record.design_front_image_url:
                image = base64.b64encode(requests.get(record.design_front_image_url).content)
            record.design_front_image = image

    @api.depends("design_back_image_url")
    def _compute_design_back_image_url(self):
        for record in self:
            image = False
            if record.design_back_image_url:
                image = base64.b64encode(requests.get(record.design_back_image_url).content)
            record.design_back_image = image
