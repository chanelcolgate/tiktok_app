from odoo import fields, models, api

class Shop(models.Model):
    _name = "tiktok.shop"
    _description = "Shop"
    
    name = fields.Char("Name")
    app_key = fields.Char("App Key")
    app_secret = fields.Char("App Secret")
    auth_code = fields.Char("Auth Code", password="True")

    line_ids = fields.One2many(
        "tiktok.shop.line",
        "shop_id",
        string="Shops",
    )
