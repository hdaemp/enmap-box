"""
Some scripts to setup the EnMAP-Box for figures

"""

import unittest

from enmapbox.gui.enmapboxgui import EnMAPBox


class TestCasesFigures(unittest.TestCase):

    def test_fig_main_gui(self):
        emb = EnMAPBox()
