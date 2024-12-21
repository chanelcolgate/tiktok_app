from odoo import fields, models, api

class ShopLine(models.Model):
    _name = "tiktok.shop.line"
    _description = "Shop Line"

    name = fields.Char("Shop Name")
    shop_cipher = fields.Char("Shop Cipher")
    shop_num = fields.Char("Shop ID")
    active = fields.Boolean("Active?", default=True)
    state = fields.Char("State")

    shop_id = fields.Many2one("tiktok.shop", required=True)
    shop_line_db_id = fields.Integer(default=201)
