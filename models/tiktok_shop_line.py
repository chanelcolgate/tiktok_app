import requests
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

    def button_refresh_token(self):
        for record in self:
            # Base URL for the API Get Fresh Token
            base_url = "https://28d7-171-232-185-180.ngrok-free.app/api/v1"
            url = base_url + f"/shop/authorization/{record.shop_id.shop_db_id}"
            try:
                # make  GET request with parameters
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    self.env.cr.commit()
                else:
                    return False
            except requests.exceptions.RequestException as e:
                return False

            # URL for API Update Access Token
            url = base_url + f"/authorization/update?id={record.shop_line_db_id}"
            try:
                # make  GET request with parameters
                response = requests.patch(url, json=data, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    self.env.cr.commit()
                    print(data)
                else:
                    return False
            except requests.exceptions.RequestException as e:
                return False
        return True
