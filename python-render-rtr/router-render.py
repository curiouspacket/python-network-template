
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



cnt =4
i=0
routers = []
while i<cnt:
    rtr = "rtr" + str(i+1)
    ip =  "10.100.1." + str(i+1)
    ser = str(i+1)
    create = Router(rtr, ip, ser)
    routers.append(create.router_info())
    i= i + 1
print(routers)
