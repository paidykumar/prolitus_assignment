from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Countdown(models.Model):
    _name = 'product.countdown.config'

    product = fields.Many2one('product.product', 'Product', required=True)
    name = fields.Char(string="Name", related="product.name")
    launch_date = fields.Date("Date", required=True)
    is_launched = fields.Boolean("Is Launched?")
    active = fields.Boolean("Active")

    _sql_constraints = [
        ('product_uniq', 'unique(product)', 'product must be unique!'),
    ]

    @api.constrains('launch_date')
    def validate_launch_date(self):
        today = fields.Date.today()
        if self.launch_date <= today:
            raise ValidationError("date should be more than todays date..")

    def write(self, vals):
        res = super().write(vals)
        product = self.env['product.product'].browse(self.product.id)
        product.product_config = self.id
        return res

    @api.model
    def create(self, vals):
        res = super().create(vals)
        product = self.env['product.product'].browse(res.product.id)
        product.product_config = res.id
        return res


class ProductProduct(models.Model):
    _inherit = 'product.template'

    product_config = fields.Many2one('product.countdown.config', 'Product Config')
