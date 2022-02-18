from odoo import models, fields, api

class director(models.Model):
    _name = 'odoo9.director'
    _description = 'model director'

    name = fields.Char('Nombre',required=True)
    edad = fields.Char(String='Edad',required=True)

    agencia_id = fields.One2many('odoo9.agencia','director_id',string='Agencias')

class instalaciones(models.Model):
    _name = 'odoo9.instalaciones'
    _description = 'model instalaciones'

    name = fields.Char('Nombre',required=True)
    lugar = fields.Char(String='Lugar',required=True)

    agencia_id = fields.Many2one('odoo9.agencia',string='Agencia')

class astronautas(models.Model):
    _name = 'odoo9.astronautas'
    _description = 'model astronautas'

    name = fields.Char('Nombre',required=True)
    edad = fields.Char(String='Edad',required=True)

    misiones_id = fields.Many2many('odoo9.misiones','astronautas_id',string='Misiones')

class planetas(models.Model):
    _name = 'odoo9.planetas'
    _description = 'model planetas'

    name = fields.Char('Nombre',required=True)

    misiones_id = fields.One2many('odoo9.misiones','planetas_id',string='Misiones')

class fabricacion(models.Model):
    _name = 'odoo9.fabricacion'
    _description = 'model fabricacion'

    name = fields.Char('Modelo',required=True)
    componentes = fields.Char(String='Componentes',required=True)

    robots_id = fields.One2many('odoo9.robots','fabricacion_id',string='Robots')

class naves(models.Model):
    _name = 'odoo9.naves'
    _description = 'model naves'

    name = fields.Char('Nombre',required=True)

    robots_id = fields.One2many('odoo9.robots','nave_id',string='Robots')
    misiones_id = fields.One2many('odoo9.misiones','naves_id',string='Misiones')

class robots(models.Model):
    _name = 'odoo9.robots'
    _description = 'model robots'

    name = fields.Char('Nombre',required=True)

    nave_id = fields.Many2one('odoo9.nave',string='Nave')
    fabricacion_id = fields.Many2one('odoo9.fabricacion',string='Modelo de fabricacion')

class misiones(models.Model):
    _name = 'odoo9.misiones'
    _description = 'model misiones'

    name = fields.Char('Nombre',required=True)

    naves_id = fields.Many2one('odoo9.naves',string='Naves')
    astronautas_id = fields.Many2many('odoo9.astronautas',string='Astronautas')
    planetas_id = fields.Many2one('odoo9.planetas',string='Planetas')
    agencia_id = fields.Many2one('odoo9.agencia',string='Agencia')

class agencia(models.Model):
    _name = 'odoo9.agencia'
    _description = 'model agencia'

    name = fields.Char('Nombre',required=True)
    pais = fields.Char(String='Pais',required=True)

    director_id = fields.Many2one('odoo9.director',string='Director')
    instalaciones_id = fields.One2many('odoo9.instalaciones','agencia_id',string='Instalaciones')
    misiones_id = fields.One2many('odoo9.misiones','agencia_id',string='Misiones')
