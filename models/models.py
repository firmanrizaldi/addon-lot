
from odoo import api, fields, models, _



class stockMoveLine(models.Model):
	_name ='stock.move'
	_inherit = 'stock.move'

	lot_id = fields.Many2one('stock.production.lot','Lot/Serial number', compute='create_data')

	def create_data(self):
		for ress in self:
			data = self.env['stock.production.lot'].search([
				('product_id','=', ress.product_id.id),
				('name', '=', ress.picking_id.origin)
				])
			ress.lot_id = data.id

