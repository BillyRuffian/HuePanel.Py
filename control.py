import logging
import discoverhue

from urllib.parse import urlparse
from touch_hue.status import Status

logger = logging.getLogger( __name__ )

def main():
    logger.debug( 'Discovering' )
    status = Status()
    found_bridges = discoverhue.find_bridges()
    if len( found_bridges ) < 1:
        logger.fatal( 'No Hue bridges found' )
        return
        
    for bridge in found_bridges:
        bridge_ip = urlparse( found_bridges[bridge] ).netloc
        logger.debug( 'Found a bridge at {ip}'.format( ip=bridge_ip ) )
        status.set_bridge( bridge_ip )
    status.rooms()


if __name__ == "__main__":
    logging.basicConfig( level=logging.DEBUG )
    logger = logging.getLogger( __name__ )
    
    main()
