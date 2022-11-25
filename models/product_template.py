# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    partner_id = fields.Many2one('res.partner',string='Customer',domain=[('customer_rank','>',0)])