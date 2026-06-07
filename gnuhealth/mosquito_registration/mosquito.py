# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 10:43:39 2024

@author: vdberghepi
"""

from trytond.model import ModelSQL, ModelView, fields

class Mosquito(ModelSQL, ModelView):
    "Mosquito"
    __name__ = 'gnuhealth.mosquito'
    _rec_name = 'species'

    #Trap information
    trap_id = fields.Char("Trap ID", required=True)
    location = fields.Char("Location", required=True)
    latitude = fields.Float("Latitude")
    longitude = fields.Float("Longitude")
    altitude = fields.Float("Altitude")
    comment = fields.Text("Comment")
    
    #Sample information
    sample_id = fields.Char("Sample ID", required=True)
    observation_date = fields.Date("Date", required=True)
    observer = fields.Many2One('party.party', "Observer", required=True)
    
    #Lab information
    number_per_species = fields.Integer("Number per species")
    species = fields.Selection([
        (None, ''),
        ('aae', 'Aedes aegypti'),
        ('aal', 'Aedes albopictus'),
        ('ag', 'Anopheles gambiae'),
        ('af', 'Anopheles funestus'),
        ('as', 'Anopheles stephensi'),
        ('cp', 'Culex pipiens'),
        ('cta', 'Culex tarsalis'),
        ('ctr', 'Culex tritaeniorhynchus'),
        ('mu', 'Mansoni uniformis'),
        ('ma', 'Mansoni africana'),
        ('hj', 'Haemagogus janthinomys'),
        ('sc', 'Sabethes cyaneus'),
    ], "Species", required=True)
    life_stage = fields.Selection([
        (None, ''),
        ('a', 'Adult'),
        ('l', 'Larva'),
        ('e', 'Egg'),
    ], "Stage", required=True)
    num_male = fields.Numeric ("Number of males")
    num_female = fields.Numeric ("Number of females")
    id_method= fields.Selection([
        (None,''),
        ('m', 'Morphological'),
        ('mt', 'Maldi-TOF'),
        ('p', 'PCR'),
    ], "Identification Method", required=True)
