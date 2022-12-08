# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Pricelist(models.Model):
    _inherit = "product.pricelist"

    partner_id = fields.Many2one('res.partner', string='Customer',domain=[('customer_rank','>',0)])

    def write(self, vals):
        res = super(Pricelist, self).write(vals)
        if vals.get('partner_id',False):
            partner = self.env['res.partner'].browse(vals.get('partner_id'))
            for each in self:
                for item in each.item_ids:
                    if item.applied_on == '1_product' and (not item.product_tmpl_id.partner_id or item.product_tmpl_id.partner_id.id != partner.id):
                        raise ValidationError(_("Some selected products partners are different from selected partner %s!")%partner.name)
                    if item.applied_on == '0_product_variant' and (not item.product_id.partner_id or item.product_id.partner_id.id != partner.id):
                        raise ValidationError(_("Some selected products partners are different from selected partner %s!")%partner.name)
        return res


