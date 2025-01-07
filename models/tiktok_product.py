import requests
import base64

from odoo import fields, models, api

class Product(models.Model):
    _name = "tiktok.product"
    _description = "Product"

    name = fields.Char("Title")
    product_id = fields.Char(string="Product Id", required=True)
    product_type = fields.Char("Product Type", required=True)
    product_size = fields.Char("Product Size", required=True)
    product_color = fields.Char("Product Color", required=True)
    active = fields.Boolean("Active?", default=True)
    image = fields.Binary("Cover")
    # product_image = fields.Binary(string="Image", compute="_compute_image_url")
    # image_url = fields.Char(string="Image URL")

    def name_get(self):
        result = []
        for record in self:
            rec_name = f"{record.product_type}, {record.product_size}, {record.product_color}"
            result.append((record.id, rec_name))
        return result

    @api.model
    def create(self, vals):
        vals['name'] = f"{vals['product_type']}, {vals['product_size']}, {vals['product_color']}"
        new_record = super().create(vals)
        return new_record

    # @api.depends("image_url")
    # def _compute_image_url(self):
    #     """ function to load image from URL """
    #     image = False
    #     if self.image_url:
    #         image = base64.b64encode(requests.get(self.image_url).content)
    #     self.product_image = image

    @api.model
    def _name_search(
            self,
            name="",
            args=NOne,
            operator="ilike",
            limit=100,
            name_get_uid=None):
        args = [] if args is None else args.copy()
        if not(name == "" and operator == "ilike"):
            args += ["|", "|",
                     ("name", operator, name),
                     ("product_type", operator, name),
                     ("product_size", operator, name),
                     ("product_color", operator, name)]
        return super()._name_search(
                name=name,
                args=args,
                operator=operator,
                limit=limit,
                name_get_uid=name_get_uid)
