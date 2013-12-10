"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class twoSwTwoHostPerTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHost = self.addHost( 'h1' )
        leftHost1 = self.addHost( 'h2' )
        centerHost = self.addHost( 'h3' )
        centerHost1 = self.addHost( 'h4' )
#        rightHost = self.addHost( 'h5' )
#        rightHost1 = self.addHost( 'h6' )
        leftSwitch = self.addSwitch( 's1' )
        centerSwitch = self.addSwitch( 's2' )
#        rightSwitch = self.addSwitch( 's3' )

        # Add links
        self.addLink( leftHost, leftSwitch )
        self.addLink( leftHost1, leftSwitch )
        self.addLink( centerHost, centerSwitch)
        self.addLink( centerHost1, centerSwitch)
#        self.addLink( rightHost, rightSwitch)
#        self.addLink( rightHost1, rightSwitch)
        self.addLink( leftSwitch, centerSwitch )
#        self.addLink( rightSwitch, centerSwitch )


topos = { 'twoSwTwoHostPerTopo': ( lambda: twoSwTwoHostPerTopo() ) }
