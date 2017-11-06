import logging
import discoverhue
import qhue

logger = logging.getLogger( __name__ )

def main():
    logger.debug( 'Discovering' )
    found_bridges = discoverhue.find_bridges()
    for bridge in found_bridges:
        logger.debug( 'Found a bridge at {ip}'.format( ip=found_bridges[bridge] ) )

if __name__ == "__main__":
    logging.basicConfig( level=logging.DEBUG )
    logger = logging.getLogger( __name__ )
    
    main()
