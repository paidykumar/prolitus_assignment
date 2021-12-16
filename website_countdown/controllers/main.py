from odoo import http
from odoo.http import request


class ProductCountDown(http.Controller):

    @http.route('/get_product_config/<int:product_id>', type='json', auth='public')
    def get_product_config_details_for_timer(self, product_id):
        import logging
        logging.info("product id %s" % product_id)
        vals = {}
        prod_obj = request.env['product.template'].search([('id', '=', product_id)])
        if prod_obj.product_config:
            vals = {
                "active": prod_obj.product_config.active,
                "launch_date": prod_obj.product_config.launch_date,
                "is_launched": prod_obj.product_config.is_launched,
            }
        data = {'status': 200, 'response': vals, 'message': 'Product Returned'}
        return data

    @http.route('/auto_check_is_launched/<int:product_id>', type='json', auth='public')
    def auto_check_is_launched(self, product_id):
        prod_obj = request.env['product.template'].search([('id', '=', product_id)], limit=1)
        prod_obj.product_config.is_launched = True
