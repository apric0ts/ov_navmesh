import omni.ui as ui
# from ..pyrecast import build_navmesh

import carb



class SettingsPanel:


    def __init__(self):
        
        print("Settings Panel started")
        
        self._window = ui.Window("Navmesh Settings", width=500, height=600, position_x = 1000, position_y = 100)    
        # Define the default settings in a dict
        self.default_settings = {
            "cellSize": 0.3,
            "cellHeight": 0.2,
            "agentHeight": 2.0,
            "agentRadius": 0.6,
            "agentMaxClimb": 0.9,
            "agentMaxSlope": 45.0,
            "regionMinSize": 8,
            "regionMergeSize": 20,
            "edgeMaxLen": 12.0,
            "edgeMaxError": 1.3,
            "vertsPerPoly": 3,
            "detailSampleDist": 6.0,
            "detailSampleMaxError": 1.0,
            "partitionType": 0
        }



        # Define bounds for custom settings sliders
        self.settings_bounds = {
            "cellSize": (0.01, 0.6, "float"),
            "cellHeight": (0.1, 0.3, "float"),
            "agentHeight": (1.0, 3.0, "float"),
            "agentRadius": (0.3,0.9, "float"),
            "agentMaxClimb": (0.3, 1.5, "float"),
            "agentMaxSlope": (15.0, 75.0, "float"),
            "regionMinSize": (4, 12, "int"),
            "regionMergeSize": (10, 30, "int"),
            "edgeMaxLen": (6.0, 18.0, "float"),
            "edgeMaxError": (0.6, 2.0, "float"),
            "vertsPerPoly": (3, 6, "int"),
            "detailSampleDist": (3.0, 9.0, "float"),
            "detailSampleMaxError": (0.5, 1.5, "float"),
            "partitionType": (0, 0, "int")
        }

        # Define custom settings in a dict, with default values equal to the default settings
        self.custom_settings = self.default_settings.copy()

        self.slider_value_model_list = [] # List of tuples (model, type) where type is either "int" or "float"

        def use_default_settings():
            self.custom_settings = self.default_settings.copy()
            print("Default settings used")

        def reset_custom_settings():
            self.custom_settings = self.default_settings.copy()
            print("Reset to default settings")


        def update_custom_settings():
            for model, key, t in self.slider_value_model_list:
                if t == "int":
                    self.custom_settings[key] = model.get_value_as_int()
                elif t == "float":
                    self.custom_settings[key] = model.get_value_as_float()
            print("Custom settings updated")

        def get_custom_settings():
            print("Custom settings retrieved")
            return self.custom_settings

        
        with self._window.frame:

            with ui.VStack():
                for key in self.default_settings:
                    with ui.HStack():
                        ui.Label(key)

                        bounds = self.settings_bounds[key]
                        min_bound, max_bound = bounds[0], bounds[1]

                        step_size = (max_bound - min_bound) / 150

                        if bounds[2] == "int":
                            int_model = ui.SimpleIntModel(self.default_settings[key], min=min_bound, max=max_bound)
                            slider = ui.IntSlider(int_model, 
                                                  width=150, 
                                                  min=min_bound, 
                                                  max=max_bound, 
                                                  step=step_size, 
                                                  default = self.default_settings[key])
                            self.slider_value_model_list.append((int_model, key, "int"))
                            

                        elif bounds[2] == "float":
                            float_model = ui.SimpleFloatModel(self.default_settings[key], min=min_bound, max=max_bound)
                            slider = ui.FloatSlider(float_model, width=150, min=min_bound, max=max_bound, step=step_size)
                            self.slider_value_model_list.append((float_model, key, "float"))


                        
                        

                
                with ui.HStack():
                    ui.Button("Use Default Settings", clicked_fn=use_default_settings)
                    ui.Button("Save Custom Settings", clicked_fn=update_custom_settings)
                    ui.Button("Reset to Default", clicked_fn=reset_custom_settings)

