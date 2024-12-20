from odoo import fields, models

class OrderStage(models.Model):
    _name = "tiktok.order.stage"
    _description = "Order Stage"
    _order = "sequence"

    name = fields.Char()
    sequence = fields.Integer(default=10)
    fold = fields.Boolean()
    active = fields.Boolean(default=True)
    state = fields.Selection(
        [
            ("awaiting shipment", "Awaiting Shipment"),
            ("awaiting collection", "Awaiting Collection"),
            ("in transit", "In Transit"),
            ("delivered", "Delivered"),
            ("completed", "Completed"),
            ("cancelled", "Cancelled"),
            ("unpaid", "Unpaid"),
            ("on hold", "On Hold"),
        ],
        default="awaiting shipment"
    )
