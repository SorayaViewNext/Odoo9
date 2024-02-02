from odoo import api, fields, models
from datetime import timedelta, date
from odoo.exceptions import ValidationError

class svrc_ofertas_inmuebles(models.Model):
    _name = 'ofertas.inmuebles'
    _description = 'Modelo (tabla) para las ofertas de compra de propiedades inmobiliarias.'
    _order = "precio desc"

    precio = fields.Float('Precio')
    estado = fields.Selection([('aceptada', 'Aceptada'), ('rechazada', 'Rechazada')], 'Estado', copy=False)
    comprador_id = fields.Many2one('res.partner', required=True, string="Comprador")
    inmueble_id = fields.Many2one('propiedades.inmuebles', required=True, string="Propiedad")
    validez = fields.Integer(default=7, string="Validez (días)")
    fecha_tope = fields.Date(compute="_calcular_fecha_tope", inverse="_inverso_fecha_tope", string="Fecha tope")
    tipo_propiedad_id = fields.Many2one(related="inmueble_id.tipos_id", store=True)

    _sql_constraints = [
        ('check_precio', 'CHECK(precio > 0)', 'El valor del PRECIO DE LA OFERTA debe ser estrictamente positivo.')
    ]

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

    def action_aceptar_oferta(self):
        for record in self:
            record.estado = "aceptada"
            record.inmueble_id.precio_venta = record.precio
            record.inmueble_id.cliente_id = record.comprador_id
            record.inmueble_id.state = "oferta_aceptada"
        return True

    def action_rechazar_oferta(self):
        for record in self:
            record.estado = "rechazada"
        return True
