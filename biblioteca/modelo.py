# -*- coding: utf-8 -*-

# Importamos las clases necesarias
from openerp import models, fields, api, exceptions, osv

#Clase para crear países
class biblioteca_pais(models.Model):
    _name = 'biblioteca.pais' #Nombre del modelo
    nombrePais = fields.Char(string="País", required=True)
    _rec_name = 'nombrePais' #Nombre de la clave primaria

#Clase para crear categorías
class biblioteca_categoria(models.Model):
    _name = 'biblioteca.categoria' #Nombre del modelo
    categoria = fields.Char(string="Categoría", required=True)
    _rec_name = 'categoria' #Nombre de la clave primaria

#Clase para crear autores
class biblioteca_autor(models.Model):
    _name = 'biblioteca.autor' #Nombre del modelo
    nombre = fields.Char(string='Nombre', required=True)
    paisN = fields.Many2one('biblioteca.pais',string='País')
    _rec_name = 'nombre' #Nombre de la clave primaria


#Clase para crear libros
class biblioteca_libro(models.Model):
    _name = 'biblioteca.libro' #Nombre del modelo
    titulo = fields.Char(string="Título", required=True)
    autorN = fields.Many2one('biblioteca.autor', string="Autor" ,required=True) #Relación Many2one
    categoria = fields.Many2one('biblioteca.categoria', string="Categoría", required=True)
    fecha = fields.Date(string = 'Fecha de publicación')
    _rec_name = 'titulo' #Nombre de la clave primaria



