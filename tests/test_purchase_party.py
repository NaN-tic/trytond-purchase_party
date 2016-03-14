# This file is part of purchase_party module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest


from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import suite as test_suite


class PurchasePartyTestCase(ModuleTestCase):
    'Test Purchase Party module'
    module = 'purchase_party'


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            PurchasePartyTestCase))
    return suite
