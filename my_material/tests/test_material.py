from odoo.exceptions import UserError
from odoo.tests.common import TransactionCase


class TestMyMaterial(TransactionCase):
    def test_new_material(self):
        vals = {
            "name": "Material #1",
            "code": "MAT #1",
            "type": "fabric",
            "buy_price": 890.0,
        }

        material = self.env["my.material"].create(vals)

        self.assertEqual(material.name, "Material #1", "Nama harus sama!")

    def test_constraint_price(self):
        vals = {
            "name": "Material #2",
            "code": "MAT #2",
            "type": "cotton",
            "buy_price": 89.0,
        }

        material = self.env["my.material"].create(vals)

        self.assertEqual(material.name, "Material #2", "Nama harus sama!")
