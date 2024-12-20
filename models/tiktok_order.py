from odoo import fields, models, api

class Order(models.Model):
    _name = "tiktok.order"
    _description = "Order"

    @api.model
    def _default_stage(self):
        Stage = self.env["tiktok.order.stage"]
        return Stage.search([("state", "=", "awaiting shipment")], limit=1)

    name = fields.Char("Order ID")

    line_ids = fields.One2many(
        "tiktok.order.line",
        "order_id",
        string="Line Items"
    )

    order_date = fields.Date(
        default=lambda s: fields.Date.today(),
        store=True,
        readonly=False,
    )

    stage_id = fields.Many2one(
        "tiktok.order.stage",
        default=_default_stage,
        copy=False,
        group_expand="_group_expand_stage_id"
    )
    state = fields.Selection(related="stage_id.state")

    currency_id = fields.Many2one("res.currency")
    total_amount = fields.Monetary("Total Amount", "currency_id")

    buyer_name = fields.Char("Buyer")
    buyer_phone = fields.Char("Phone")
    buyer_address = fields.Char("Shipping Address")
    buyer_zipcode = fields.Char("Zip Code")
