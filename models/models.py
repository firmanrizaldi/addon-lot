# -*- coding: utf-8 -*-

from odoo import models, fields, api

class stock_move_lot(models.Model):
    _name = 'stock.move'
    
    _inherit = 'stock.move'

    lot_id = fields.Many2one(
        'stock.production.lot', 'Lot/Serial Number', 
            compute='_create_lot' )
        
    @api.depends('lot_id')
    def _create_lot(self):
        for record in self:
            lot_id = record.lot_id.id
    
