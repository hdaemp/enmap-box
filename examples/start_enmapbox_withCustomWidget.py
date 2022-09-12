from enmapbox import EnMAPBox

from enmapbox.testing import start_app
from qgis._core import QgsProcessingAlgorithm, QgsProcessingRegistry, QgsApplication
from qgis._gui import QgsProcessingParameterWidgetFactoryInterface
from qgis.core import QgsProcessingParameterDefinition, QgsProcessingParameterFile, QgsProcessingContext
from qgis.gui import QgsProcessingAbstractParameterDefinitionWidget, QgsAbstractProcessingParameterWidgetWrapper, \
    QgsProcessingParameterWidgetContext, QgsGui

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


class MyInterface(QgsProcessingParameterWidgetFactoryInterface):
    def parameterType(self):
        return 'MyParameterWidgetWrapper'


qgsApp = start_app()
myIface = MyInterface()
QgsGui.processingGuiRegistry().addParameterWidgetFactory(myIface)


class MyAlgorithm(QgsProcessingAlgorithm):

    def displayName(self):
        return 'Issue 1366 Algorithm'

    def name(self):
        return 'Issue1366Algorithm'

    def shortDescription(self):
        return 'dummy'

    def group(self):
        return 'Debugging'

    def groupId(self):
        return 'Debugging'

    def createInstance(self):
        return type(self)()

    def initAlgorithm(self, configuration):
        # add a parameter with custom widget
        param = QgsProcessingParameterFile('file', 'Custom File')
        param.setMetadata({'widget_wrapper': {'class': MyParameterWidgetWrapper}})
        self.addParameter(param)

    def processAlgorithm(self, parameters, context, feedback):
        return {}


enmapBox = EnMAPBox()
registry: QgsProcessingRegistry = QgsApplication.instance().processingRegistry()
provider = registry.providerById('enmapbox')
provider.addAlgorithm(MyAlgorithm())

enmapBox.showProcessingAlgorithmDialog(MyAlgorithm())

qgsApp.exec_()
