
class Router:
    device = "Router"
    def __init__(self, mgmtip, hostname, serialnum):
        self.mgmtip = mgmtip
        self.hostname = hostname
        self.serialnum = serialnum
    def router_info(self):
        #device = {}
        device = {"hostname" :self.hostname,
                  "management-ip" : self.mgmtip,
                  "serial-number": self.serialnum}
        return device

class Routing(Router):
    def router_bgp(self, nets):
        #print(nets)
        return f"RouterID:{self.mgmtip}, advertises these subnets {nets}"

cnt =4
i=0
routers = []
while i<cnt:
    rtr = "rtr" + str(i+1)
    ip =  "10.100.1." + str(i+1)
    ser = str(i+1)
    nets = ["10.20."+str(i+1)+".0"]
    create = Routing( ip, rtr,ser)
    print(create.router_bgp(nets))
    routers.append(create.router_info())
    i= i + 1
print(routers)
