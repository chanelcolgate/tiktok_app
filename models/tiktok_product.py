from odoo import fields, models

class Product(models.Model):
    _name = "tiktok.product"
    _description = "Product"

    name = fields.Char("Title")
    product_id = fields.Integer(string="Product Id", required=True)
    product_type = fields.Char("Product Type", required=True)
    product_size = fields.Char("Product Size", required=True)
    product_color = fields.Char("Product Color", required=True)
    active = fields.Boolean("Active?", default=True)
    image = fields.Binary("Cover")

    def name_get(self):
        result = []
        for record in self:
            rec_name = f"{record.product_type}, {record.product_size}, {record.product_color}"
            result.append((record.id, rec_name))
        return result
