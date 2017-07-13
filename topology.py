from mininet.topo import Topo
from mininet.cli import CLI
from mininet.node import Link
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.term import makeTerm
from functools import partial
from mininet.log import setLogLevel
from mininet.node import OVSSwitch


class MyTopo( Topo ):
    def __init__( self ):
        "Create custom topo."
        Topo.__init__( self )
        h1 = self.addHost('h1', mac='00:00:00:00:00:01')
        h2 = self.addHost('h2', mac='00:00:00:00:00:02')
        s1 = self.addSwitch('s1', protocols='OpenFlow13')
        s2 = self.addSwitch('s2', protocols='OpenFlow13')
        s3 = self.addSwitch('s3', protocols='OpenFlow13')
        s4 = self.addSwitch('s4', protocols='OpenFlow13')
        s5 = self.addSwitch('s5', protocols='OpenFlow13')
        s6 = self.addSwitch('s6', protocols='OpenFlow13')
        s7 = self.addSwitch('s7', protocols='OpenFlow13')
        self.addLink(h1, s1)
        self.addLink(s1, s2)
        self.addLink(s1, s3)
        self.addLink(s2, s4)
        self.addLink(s3, s4)
        self.addLink(s4, s5)
        self.addLink(s4, s6)
        self.addLink(s5, s7)
        self.addLink(s6, s7)
        self.addLink(s7, h2)


def ofp_version(switch, protocols):
    # protocols_str = ','.join(protocols)
    command = 'ovs-vsctl set bridge %s protocols=%s' % (switch, protocols)
    # print command
    # print command.split(' ')
    switch.cmd(command)


if '__main__' == __name__:
    setLogLevel('info')
    topo = MyTopo()
    switch = partial(OVSSwitch, protocols='OpenFlow13')
    net = Mininet(topo=topo, controller=None, autoStaticArp=True, autoSetMacs=True)
    c0 = net.addController('Ryu', controller=RemoteController, ip='127.0.0.1', protocols='OpenFlow13', port=6633)
    net.start()
    # net.start()
    s1, s2, s3, s4, s5, s6, s7 = net.get('s1', 's2', 's3', 's4', 's5', 's6', 's7')

    ofp_version(s1, 'OpenFlow13')
    ofp_version(s2, 'OpenFlow13')
    ofp_version(s3, 'OpenFlow13')
    ofp_version(s4, 'OpenFlow13')
    ofp_version(s5, 'OpenFlow13')
    ofp_version(s6, 'OpenFlow13')
    ofp_version(s7, 'OpenFlow13')
    CLI(net)
    net.stop()
