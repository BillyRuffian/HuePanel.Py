import logging
import os
import yaml
from qhue import Bridge


logger = logging.getLogger( __name__ )

class Status:
    def __init__( self ):
        self.username = os.environ['HUE_USER']
        
    def set_bridge( self, ip=None ):
        self.bridge = Bridge( ip, self.username )
        
    def rooms( self ):
        print( yaml.safe_dump( self.bridge.groups(), indent=2 ) )