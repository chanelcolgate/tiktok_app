from odoo import fields, models

class Saler(models.Model):
    _name = "tiktok.seller"
    _description = "Seller"
    _inherits = {"res.partner": "partner_id"}

    partner_id = fields.Many2one(
        "res.partner",
        delegate=True,
        ondelete="cascade",
        required=True
    )
