from odoo import api, fields, models
from datetime import timedelta, date

class svrc_ofertas_inmuebles(models.Model):
    _name = 'ofertas.inmuebles'
    _description = 'Modelo (tabla) para las ofertas de compra de propiedades inmobiliarias.'

    precio = fields.Float('Precio')
    estado = fields.Selection([('aceptada', 'Aceptada'), ('rechazada', 'Rechazada')], 'Estado', copy=False)
    comprador_id = fields.Many2one('res.partner', required=True, string="Comprador")
    inmueble_id = fields.Many2one('propiedades.inmuebles', required=True, string="Propiedad")
    validez = fields.Integer(default=7, string="Validez (días)")
    fecha_tope = fields.Date(compute="_calcular_fecha_tope", inverse="_inverso_fecha_tope", string="Fecha tope")

    @api.depends('validez')
    def _calcular_fecha_tope(self):
        for record in self:
            if record.create_date:
                record.fecha_tope = record.create_date + timedelta(days=record.validez)
            else:
                record.fecha_tope = date.today() + timedelta(days=record.validez)

    def _inverso_fecha_tope(self):
        for record in self:
            record.validez = (record.fecha_tope - date.today()).days
