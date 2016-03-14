# This file is part of the purchase_party module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool, PoolMeta

__all__ = ['Purchase']


class Purchase:
    __metaclass__ = PoolMeta
    __name__ = 'purchase.purchase'

    def on_change_party(self):
        super(Purchase, self).on_change_party()

        if self.party and self.party.purchase_currency:
            self.currency = self.party.purchase_currency
        else:
            Currency = Pool().get('currency.currency')
            self.currency = Currency(self.default_currency())
