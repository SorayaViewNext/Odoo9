from odoo import fields, models
# from datetime import timedelta

class svrc_inmuebles(models.Model):
    _name = "propiedades.inmuebles"
    _description = "Propiedades Inmuebles"

    name = fields.Char(string='Nombre', required = True)
    descripcion = fields.Text(string='Descripcion')
    cliente_id = fields.Many2one("res.partner", string="Comprador", copy=False)
    agente_id = fields.Many2one("res.users", string="Vendedor", default=lambda self: self.env.user)
    tipos_id = fields.Many2one("tipos.inmuebles", string="Tipo")
    etiquetas_ids = fields.Many2many("etiquetas.inmuebles", string="Tipo")
    ofertas_ids = fields.One2many("ofertas.inmuebles", "inmueble_id", string="Ofertas")
    codigo_postal = fields.Char(string='Código postal')
    fecha_disponibilidad = fields.Date(string='Fecha de disponibilidad', copy=False, default=lambda self:fields.Date.today() + timedelta(days=90))
    precio_esperado = fields.Float(string='Precio esperado', required=True)
    precio_venta = fields.Float(string='Precio de venta', readonly=True, copy=False)
    dormitorios = fields.Integer(string='Nº dormitorios', default=2)
    salon = fields.Integer(string='Tamaño del salón')
    fachadas = fields.Integer(string='Nº fachadas')
    garaje = fields.Boolean(string='Garaje')
    jardin = fields.Boolean(string='Jardín')
    area_jardin = fields.Integer(string='Tamaño del jardín m2')
    orientacion_jardin = fields.Selection([('norte', 'Norte'), ('sur', 'Sur'), ('este', 'Este'), ('oeste', 'Oeste'),
                                           ], string='Orientación del jardín')
    active = fields.Boolean(string='Activo', default=True)
    state = fields.Selection([('nuevo', 'Nuevo'), ('oferta_recibida', 'Oferta recibida'), ('oferta_aceptada',
                                                                                           'Oferta aceptada'), ('vendido', 'Vendido'), ('cancelado', 'Cancelado')], string='Estado', required=True, copy=False, default='nuevo')

