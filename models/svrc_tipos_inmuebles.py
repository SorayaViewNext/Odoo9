from odoo import fields, models

class svrc_tipos_inmuebles(models.Model):
    _name = "tipos.inmuebles"
    _description = "Modelo (tabla) para los tipos de propiedades inmobiliarias"
    _order = "name"

    name = fields.Char(string='Nombre', required=True)
    inmuebles_ids = fields.One2many("propiedades.inmuebles", "tipos_id", string = "Propiedades inmuebles")
    secuencia = fields.Integer('Secuencia')
    ofertas_ids = fields.One2many("ofertas.inmuebles", "tipo_propiedad_id")
    contador_ofertas = fields.Integer(compute="_calcular_numero_ofertas")

    _sql_constraints = [
        ('check_name', 'unique(name)', 'El nombre del tipo de propiedad debe ser único')
    ]

    @api.depends("ofertas_ids")
    def _calcular_numero_ofertas(self):
        for record in self:
            if record.ofertas_ids:
                record.contador_ofertas = len(record.ofertas_ids)
            else:
                record.contador_ofertas = 0

