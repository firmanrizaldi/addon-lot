# -*- coding: utf-8 -*-

from odoo import models, fields, api

class stock_move_lot(models.Model):
    _name = 'stock.move'
    _inherit = 'stock.move'

    lot = fields.Many2one(
        'stock.production.lot', 'Lot/Serial Number', 
            compute='_create_lot' )
        
    @api.depends('lot_id')
    def _create_lot(self):
        for x in self:
            data = self.env('stock.production.lot').search([ 
            	('product_id','=', x.product_id.id),
            	('name','=', x.picking_id.origin) 
            	])
            x.lot = data.id


