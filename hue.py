import discoverhue
import os
from urllib.parse import urlparse
from qhue import Bridge

class Hue:
    def __init__( self ):
        self.username = os.environ['HUE_USER']
        self.hue_bridge = None
        
    def bridge( self ):
        if self.hue_bridge == None:
            found_bridges = discoverhue.find_bridges()
            if len( found_bridges ) > 0:
                bridge_ip = urlparse( list( found_bridges.values() )[0] ).netloc
                self.hue_bridge = Bridge( bridge_ip, self.username )
        return self.hue_bridge