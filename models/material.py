# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

class UserMaterial(models.Model):      
    _name  ='user.material'
    
    _description= 'Manage Material'
    
    _rec_name= 'material_name'
    
    #compute fields
    @api.constrains('material_price')
    def check_price(self):
        for rec in self:
            if rec.material_price < 100 :
                raise ValidationError(_("Price must be at least 100"))
    
    material_code = fields.Char('Material Code', required=True)
    
    material_name = fields.Char('Material Name', required=True)
    
    material_type = fields.Selection([('fabric','Fabric'),('jeans','Jeans'),('cotton','Cotton')], 'Material Type', required=True)
    
    material_price = fields.Integer('Material Price', required=True)
    
    related_supp = fields.Selection([('supplier_a','Supplier A'),('supplier_b','Supplier B'),('supplier_c','Supplier C')], 'Related Supplier', required=True)