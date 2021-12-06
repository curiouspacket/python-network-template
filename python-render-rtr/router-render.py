
#This is parent class that creates a Router Object
#Every Router has managementip, hostname and serialnumber
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
# Routing Class inherits from Router Class
#takes values for subnets to be included in routing
class Routing(Router):
    def __init__(self, mgmtip, hostname, serialnum, nets):
        super().__init__(mgmtip, hostname, serialnum)
        self.nets = nets
    def router_bgp(self):
        #print(nets)
        return f"RouterID:{self.mgmtip}, advertises these subnets {self.nets}"

cnt =4
i=0
routers = []
while i<cnt:
    rtr = "rtr" + str(i+1)
    ip =  "10.100.1." + str(i+1)
    ser = str(i+1)
    nets = ["10.20."+str(i+1)+".0"]
    create = Router( ip, rtr,ser)
    routers.append(create.router_info())
    i= i + 1
print(routers)

subs = ['10.10.1.0', "10.10.2.0", "10.10.3.0"]
rtr1 = Routing("10.10.1.1", "rtr1", "000000000001", subs)
print(rtr1.router_bgp())
print(rtr1.router_info())

