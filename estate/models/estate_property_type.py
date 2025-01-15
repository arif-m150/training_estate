from odoo import _, api, fields, models

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Estate Property Type'
    
    name = fields.Char('Name')
    