import argparse
import colorama

from modules.proof import  Proof
class Main:
    """
     properties:
     active_module = list of modules.
    """

    def __init__(self):
        parser = argparse.ArgumentParser(description='Parse the arguments')
        parser.add_argument('-d','--domain_name',help='Define domain name')
        parser.add_argument('-dn','--dns',help='Enable DNS mopule')
        parser.add_argument('-cr','--crawler',help='Enable  crawler module')
        parser.add_argument('-bn','--banners',help='Enable  banner grabbing module')
        parser.add_argument('-geo','--geolocate',help='Enable  geolocation module')
        parser.add_argument('-hip','--haveibeenpwned',help='Enable  haveibeenpwned querys module')
        parser.add_argument('-nm','--nmap',help='Enable  nmap module')
        parser.add_argument('-p','--ping',help='Enable  ping module')
        parser.add_argument('-th','--theharvester',help='Enable the harvester module')
        parser.add_argument('-cc','--cert_and_cipher',help='Enable certified and cipher module')
        parser.add_argument('-wi','--whois',help='Enable whois module')
        parser.add_argument('-cve','--cve_detail',help='Enable CVE module')
        parser.add_argument('-cms','--cmsmap',help='Enable cmsmap module')
        parser.add_argument('-x','--xss',help='Enable xss module')
        parser.add_argument('-s','--sqli',help='Enable sqli module')
        parser.add_argument('-proof','--proof',help='Just for devs')
        args = parser.parse_args()
        self.active_modules = [] #not need.
        if(args.dns is not None):
            #self.active_modules.append(Dns(args.dns))
            pass
        if(args.crawler is not None):
            #self.active_modules.append(Crawler(args.crawler))
            pass

        if(args.banners is not None):
            #self.active_modules.append(Banners(args.banners))
            pass

        if(args.geolocate is not None):
            #self.active_modules.append(Geolocate(args.geolocate))
            pass
        if(args.haveibeenpwned is not None):
            #self.active_modules.append(Haveibeenpwned(args.haveibeenpwned))
            pass
        if(args.nmap is not None):
            #self.active_modules.append(Nmap(args.nmap))
            pass

        if(args.ping is not None):
            #self.active_modules.append(Ping(args.ping))
            pass
        if(args.theharvester is not None):
            #self.active_modules.append(Theharvester(args.theharvester))
            pass
        if(args.cert_and_cipher is not None):
            #self.active_modules.append(Cert_and_cipher(args.cert_and_cipher))
            pass
        if(args.whois is not None):
            #self.active_modules.append(Whois(args.whois))
            pass
        if(args.cve_detail is not None):
            #self.active_modules.append(Cve_detail(args.cve_detail))
            pass

        if(args.cmsmap is not None):
            #self.active_modules.append(Cmsmap(args.cmsmap))
            pass

        if(args.xss is not None):
            #self.active_modules.append(Xss(args.xss))
            pass
        if(args.sqli is not None):
            #self.active_modules.append(Sqli(args.sqli))
            pass
        #Use this example to build more modules.
        if(args.proof is not None): # Devs proof
            self.active_modules.append(Proof(args.proof))


    def run_all_modules(self):
        """
        Run all active modules
        """
        for i in self.active_modules:
            i.run_module()




a = Main()
a.run_all_modules()
