import json
import logging

from odoo import fields, models, api, exceptions
from odoo.addons.tiktok_app.utils.utils import name_to_abbreviation

_logger = logging.getLogger(__name__)

class Order(models.Model):
    _name = "tiktok.order"
    _description = "Order"

    @api.model
    def _default_stage(self):
        Stage = self.env["tiktok.order.stage"]
        return Stage.search([("state", "=", "awaiting shipment")], limit=1)

    name = fields.Char("Order ID") # id

    line_ids = fields.One2many(
        "tiktok.order.line",
        "order_id",
        string="Line Items"
    )

    # order_date = fields.Date(
    #     default=lambda s: fields.Date.today(),
    #     store=True,
    #     readonly=False,
    # ) # order_date
    order_date = fields.Datetime(
        default=lambda s: fields.Datetime.now(),
        store=True,
        readonly=False
    ) # order_date

    stage_id = fields.Many2one(
        "tiktok.order.stage",
        default=_default_stage,
        copy=False,
        group_expand="_group_expand_stage_id"
    ) # order_status
    state = fields.Selection(related="stage_id.state")

    currency_id = fields.Many2one("res.currency") # currency
    total_amount = fields.Monetary("Total Amount", "currency_id") # total_amount

    buyer_name = fields.Char("Buyer") # buyer_name
    buyer_phone = fields.Char("Phone") # buyer_phone
    buyer_address = fields.Char("Shipping Address") # buyer_address
    buyer_zipcode = fields.Char("Zip Code") # buyer_zipcode

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
        body = {}
        products = []

        self.ensure_one()
        if not self.line_ids:
            raise exceptions.UserError("No Lines were selected")


        for line in self.line_ids:
            _logger.info(
                f"Order Line on {line.order_line_id}"
            )
            product = {}
            product["variant_id"] = line.product_id.product_id;
            product["printer_design_front_url"] = line.design_front_image_url
            product["printer_design_back_url"]  = line.design_back_image_url
            product["printer_design_right_url"] = None
            product["printer_design_left_url"] = None
            product["printer_design_neck_url"] = None
            product["mockup_front_url"] = line.mockup_front_image_url
            product["mockup_back_url"]  = line.mockup_back_image_url
            product["mockup_right_url"] = None
            product["mockup_left_url"] = None
            product["mockup_neck_url"] = None
            product["quantity"] = 1  # Missing
            product["note"]     = "" # Missing
            products.append(product)


        body["order_id"] = self.name
        body["buyer_first_name"] = self.buyer_name
        body["buyer_email"] = None
        body["buyer_phone"] = self.buyer_phone
        _, province, city, _, address = self.buyer_address.split(",")
        body["buyer_address1"] = address.strip()
        body["buyer_address2"] = ""
        body["buyer_city"] = city.strip()
        body["buyer_provice_city"] = name_to_abbreviation[province.strip()]
        body["buyer_zip"] = self.buyer_zipcode
        body["buyer_country_code"] = "US"   # Missing
        body["shipment"] = "1"              # Missing
        body["link_label"] = None

        body["products"] = products

        payload = json.dumps(body)

        _logger.info(f"Order on {self.name}")
        _logger.info(payload)
        return True
