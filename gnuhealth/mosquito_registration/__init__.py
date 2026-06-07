# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 10:44:06 2024

@author: vdberghepi
"""

from trytond.pool import Pool
from . import mosquito

def register():
    Pool.register(
        mosquito.Mosquito,
        module='mosquito_registration', type_='model')
