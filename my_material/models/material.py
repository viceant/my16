# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class MyMaterial(models.Model):
    _name = "my.material"
    _description = "My Material"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(
        tracking=True,
    )

    code = fields.Char(
        tracking=True,
    )

    type = fields.Selection(
        [
            ("fabric", "Fabric"),
            ("jeans", "Jeans"),
            ("cotton", "Cotton"),
        ],
        string="Type",
        tracking=True,
    )

    buy_price = fields.Float(
        tracking=True,
    )

    supplier_id = fields.Many2one(
        "res.partner",
        string="Supplier",
        tracking=True,
    )

    @api.constrains("buy_price")
    def _constrains_buy_price(self):
        if self.buy_price < 100:
            raise UserError("Tidak boleh kurang dari seratus")


class MySupplier(models.Model):
    _inherit = "res.partner"
