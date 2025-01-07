import logging

from odoo import fields, models, api, exceptions

_logger = logging.getLogger(__name__)

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

    fullfill_state_1 = fields.Selection(
        [
            ("not_fullfill", "Not Fullfill"),
            ("fullfilled", "Fullfilled"),
        ],
        default="not_fullfill"
    )
    design_state_1 = fields.Selection(
        [
            ("not_design", "Not Design"),
            ("designed", "Designed"),
        ],
        default="not_design"
    )

    def button_send(self):
        self.ensure_one()
        if not self.line_ids:
            raise exceptions.UserError("No Lines were selected")

        for line in self.line_ids:
            _logger.info(
                f"Order Line on {line.order_line_id}"
            )

        _logger.info(f"Order on {self.name}")
        return True
