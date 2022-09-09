from enmapbox import EnMAPBox

from enmapbox.testing import start_app
from qgis.core import QgsProcessingParameterDefinition, QgsProcessingParameterFile, QgsProcessingContext
from qgis.gui import QgsProcessingAbstractParameterDefinitionWidget, QgsAbstractProcessingParameterWidgetWrapper, \
    QgsProcessingParameterWidgetContext, QgsGui

qgsApp = start_app()

class MyParameterDefinitionWidget(QgsProcessingAbstractParameterDefinitionWidget):

    def createParameter(self, name: str, description: str, flags: QgsProcessingParameterDefinition.Flags):
        param = QgsProcessingParameterFile(name, description)
        return param

class MyParameterWidgetWrapper(QgsAbstractProcessingParameterWidgetWrapper):

    def __init__(self, *args, **kwargs):
        QgsAbstractProcessingParameterWidgetWrapper.__init__(self, *args, **kwargs)

    def createParameterDefinitionWidget(
            self, context: QgsProcessingContext, widgetContext: QgsProcessingParameterWidgetContext
    ):
        return MyParameterDefinitionWidget(context, widgetContext)

myParameterWidgetWrapper = MyParameterWidgetWrapper()
QgsGui.processingGuiRegistry().addParameterWidgetFactory(myParameterWidgetWrapper)

enmapBox = EnMAPBox()
qgsApp.exec_()
