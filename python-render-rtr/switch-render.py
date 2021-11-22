class Switch:
    device = "Switch"
    def __init__(self, mgmtip, hostname, serialnum):
        self.mgmtip = mgmtip
        self.hostname = hostname
        self.serialnum = serialnum
    def switch_info(self):
        #device = {}
        device = {"hostname" :self.hostname,
                  "management-ip" : self.mgmtip,
                  "serial-number": self.serialnum}
        return device
class Vlan:
    def __init__(self, vlanid, vlanname, vlannum):
        self.vlanid = vlanid
        self.vlanname = vlanname
        self.vlannum = vlannum
    