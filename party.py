# This file is part of the purchase_party module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.model import fields

__all__ = ['Party']


class Party(metaclass=PoolMeta):
    __name__ = 'party.party'
    purchase_currency = fields.Many2One('currency.currency',
            'Purchase Currency')
