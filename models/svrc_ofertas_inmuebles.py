from odoo import fields, models

class svrc_ofertas_inmuebles(models.Model):
    _name = 'ofertas.inmuebles'
    _description = 'Modelo (tabla) para las ofertas de compra de propiedades inmobiliarias.'

    precio = fields.Float('Precio')
    estado = fields.Selection([('aceptada', 'Aceptada'), ('rechazada', 'Rechazada')], 'Estado', copy=False)
    comprador_id = fields.Many2one('res.partner', required=True, string="Comprador")
    inmueble_id = fields.Many2one('propiedades.inmuebles', required=True, string="Propiedad")
