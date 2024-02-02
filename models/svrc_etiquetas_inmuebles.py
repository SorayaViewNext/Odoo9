from odoo import fields, models

class svrc_etiquetas_inmuebles(models.Model):
    _name = "etiquetas.inmuebles"
    _description = "Modelo (tabla) para las etiquetas que califican las propiedades inmobiliarias"
    _order = "name"

    name = fields.Char('Nombre', required=True)
    color = fields.Integer('color')

    _sql_constraints = [
        ('check_name', 'unique (name)', 'El nombre de la ETIQUETA DE PROPIEDAD debe ser único.')
    ]
