import omni.ext
import omni.ui as ui

from .ui_components.navmesh_panel import NavmeshPanel
from .ui_components.settings_panel import SettingsPanel


class SiborgCreateNavmeshExtension(omni.ext.IExt):
    def on_startup(self, ext_id):
        print("[siborg.create.navmesh] siborg create navmesh startup")


        self.settings_panel = SettingsPanel()
        self.navmesh_panel = NavmeshPanel(self.settings_panel)
        

    def on_shutdown(self):
        print("[siborg.create.navmesh] siborg create navmesh shutdown")
        self.navmesh_panel = None
        self.settings_panel = None 
