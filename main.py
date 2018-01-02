from kivy.app import App
from kivy.app import Widget
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.togglebutton import ToggleButton
from kivy.clock import Clock

from hue import Hue

import logging


class LightSwitch( ToggleButton ):
    pass


class HueControlApp( App ):
    
    
    def build( self ):
        Clock.schedule_once( self.connect_to_bridge, 3 )
        
    
    def connect_to_bridge( self, dt ):
        logging.info( 'Connecting to Hue bridge' )
        hue = Hue()
        self.bridge = hue.bridge()
        self.root.ids.screen_manager.current = 'discovering lights'
        Clock.schedule_once( self.discover_lights, 3 )
        
    
    def discover_lights( self, dt ):
        self.groups = self.bridge.groups()
        self.toggles = []
        for group in self.groups:
            toggle = LightSwitch( text=self.groups[group]['name'] )
            toggle.state = 'down' if self.groups[group]['state']['any_on'] == True else 'normal'
            toggle.bind( on_press=self.toggle_pressed )
            self.toggles.append( toggle )
            self.root.ids.lightswitch_layout.add_widget( toggle )
        self.root.ids.screen_manager.current = 'switches'
        Clock.schedule_interval( self.refresh_lights, 2.5 )
        
    
    def refresh_lights( self, dt ):
        # this is super ugly, there must be a better way
        self.groups = self.bridge.groups()
        for group in self.groups:
            for toggle in self.toggles:
                if self.groups[group]['name'] == toggle.text:
                    toggle.state = 'down' if self.groups[group]['state']['any_on'] == True else 'normal'
                    break
                    
    
    def toggle_pressed( self, instance ):
        # b.groups( 4, 'action', on=True )
        name = instance.text
        target_group = None
        for group in self.groups:
            if self.groups[group]['name'] == name:
                self.bridge.groups( group, 'action', on=( instance.state == 'down' ) )
                break

        
if __name__ == '__main__':
    app = HueControlApp()
    app.run()