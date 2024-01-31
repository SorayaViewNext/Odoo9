from odoo import fields, models

class svrc_tipos_inmuebles(models.Model):
    _name = "tipos.inmuebles"
    _description = "Modelo (tabla) para los tipos de propiedades inmobiliarias"

    name = fields.Char(string='Nombre', required=True)
