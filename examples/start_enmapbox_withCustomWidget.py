from enmapbox import EnMAPBox

from enmapbox.testing import start_app
from qgis._core import QgsProcessingParameterDefinition, QgsProcessingParameterFile, QgsProcessingContext
from qgis._gui import QgsProcessingAbstractParameterDefinitionWidget, QgsAbstractProcessingParameterWidgetWrapper, \
    QgsProcessingParameterWidgetContext, QgsGui

qgsApp = start_app()

class MyParameterDefinitionWidget(QgsProcessingAbstractParameterDefinitionWidget):

    def createParameter(self, name: str, description: str, flags: QgsProcessingParameterDefinition.Flags):
        param = QgsProcessingParameterFile(name, description)
        return param

class MyParameterWidgetWrapper(QgsAbstractProcessingParameterWidgetWrapper):

    def createParameterDefinitionWidget(
            self, context: QgsProcessingContext, widgetContext: QgsProcessingParameterWidgetContext
    ):
        return MyParameterDefinitionWidget(context, widgetContext)

QgsGui.processingGuiRegistry().addParameterWidgetFactory(MyParameterWidgetWrapper())


enmapBox = EnMAPBox()
qgsApp.exec_()
