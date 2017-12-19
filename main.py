from kivy.app import App
from kivy.app import Widget
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.stacklayout import StackLayout

from hue import Hue

import logging

logger = logging.getLogger( __name__ )

class Lights( StackLayout ):
    bridge = ObjectProperty( None )
    group = ObjectProperty( None )
    
    def on_group( self, instance, pos ):
        pass

class GroupPanel( RelativeLayout ):
    pass

class GroupListPanel( BoxLayout ):
    bridge = ObjectProperty( None )
    groups = ListProperty([])
    group = ObjectProperty( None )
    
    def on_bridge( self, instance, pos ):
        groups = self.bridge.groups()
        for group in list( groups.values() ):
            self.groups.append( group )
        self.group = self.groups[0]
    
    def on_groups( self, instance, pos ):
        print( self.groups )

class ControlPanel( Widget ):
    bridge = ObjectProperty( None )
    
    def connect_to_bridge( self ):
        hue = Hue()
        self.bridge = hue.bridge()
        logging.info( self.bridge )

class HueControlApp( App ):
    """Kivy main class."""
    
    def build( self ):
        control_panel = ControlPanel()
        control_panel.connect_to_bridge()
        return control_panel
        
if __name__ == '__main__':
    HueControlApp().run()