from kivy.app import App
from kivy.lang import Builder


class ConvertMilesApp(App):
    """Kivy App to convert miles to kilometres."""
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
