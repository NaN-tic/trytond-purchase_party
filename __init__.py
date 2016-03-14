# This file is part of purchase_party module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .party import *
from .purchase import *

def register():
    Pool.register(
        Party,
        Purchase,
        module='purchase_party', type_='model')
