from qgis.core import QgsRasterLayer

from colorspaceexplorerapp import ColorSpaceExplorerDialog
from enmapbox import initall
from enmapbox.gui.enmapboxgui import EnMAPBox

from enmapbox.exampledata import enmap
from enmapbox.testing import start_app

qgsApp = start_app()
initAll()

enmapBox = EnMAPBox(None)
layer = QgsRasterLayer(enmap, 'enmap_berlin.bsq')
mapDock = enmapBox.onDataDropped([layer])

widget = ColorSpaceExplorerDialog()
widget.show()
widget.mLayer.setLayer(layer)

qgsApp.exec_()
