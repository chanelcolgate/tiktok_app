from odoo import fields, models, api

class Shop(models.Model):
    _name = "tiktok.shop"
    _description = "Shop"
    
    name = fields.Char("Name")
    app_key = fields.Char("App Key")
    app_secret = fields.Char("App Secret")
    auth_code = fields.Char("Auth Code")
    auth_code_display = fields.Char("Auth Code", compute="_compute_auth_code_display")

    line_ids = fields.One2many(
        "tiktok.shop.line",
        "shop_id",
        string="Shops",
    )

    @api.depends("auth_code")
    def _compute_auth_code_display(self):
        for record in self:
            if record.auth_code:
                record.auth_code_display = record.auth_code[:10] + "..."
