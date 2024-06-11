"""
test_smiley.py

Contains automatic test for Smiley.
Automatic tests are very important for large projects.
For smaller projects, automatic tests are also very important.
Usually, you would want to have multiple small tests
checking each individual part of your codebase.
But's even just having one "sanity check" test
also goes a long way.
"""

import unittest

import raimad as rai

from rai_smiley import Smiley

class TestSmiley(unittest.TestCase):

    def test_smiley(self):
        """
        Simple sanity check to make sure Smiley exports to CIF correctly.
        """
        compo = Smiley()
        cif_string = rai.export_cif(compo)

        # check the number of polygons
        self.assertEqual(
            cif_string.count('P'),
            4
            )


if __name__ == '__main__':
    unittest.main()

