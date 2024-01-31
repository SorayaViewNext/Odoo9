from odoo import fields, models

class svrc_etiquetas_inmuebles(models.Model):
    _name = "etiquetas.inmuebles"
    _description = "Modelo (tabla) para las etiquetas que califican las propiedades inmobiliarias"

    name = fields.Char('Nombre', required=True)
