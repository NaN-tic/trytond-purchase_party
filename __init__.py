# This file is part of purchase_party module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from . import party
from . import purchase


def register():
    Pool.register(
        party.Party,
        purchase.Purchase,
        module='purchase_party', type_='model')
