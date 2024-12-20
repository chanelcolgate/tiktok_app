from odoo import fields, models, api

class Shop(models.Model):
    _name = "tiktok.shop"
    _description = "Shop"
    
    name = fields.Char("Shop Name")
    app_key = fields.Char("App Key")
    app_secret = fields.Char("App Secret")
    auth_code = fields.Char("Auth Code", password="True")
    shop_id = fields.Char("Shop ID")
    shop_cipher = field.Char("Shop Cipher")
    state = fields.Char("State")

    active = fields.Boolean("Active?", default=True)
