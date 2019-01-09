import argparse
import colorama

from modules import  Proof
#from tools.argstoredict import StoreDictKeyPair

class Main:
    """
     properties:
     active_module = list of modules.
    """

    def __init__(self):
        parser = argparse.ArgumentParser(description='Parse the arguments')
        parser.add_argument('-d','--domain_name',help='Define domain name', nargs='+')
        parser.add_argument('-dn','--dns',help='Enable DNS mopule', nargs='+')
        parser.add_argument('-cr','--crawler',help='Enable  crawler module', nargs='+')
        parser.add_argument('-bn','--banners',help='Enable  banner grabbing module', nargs='+')
        parser.add_argument('-geo','--geolocate',help='Enable  geolocation module', nargs='+')
        parser.add_argument('-hip','--haveibeenpwned',help='Enable  haveibeenpwned querys module', nargs='+')
        parser.add_argument('-nm','--nmap',help='Enable  nmap module', nargs='+')
        parser.add_argument('-p','--ping',help='Enable  ping module', nargs='+')
        parser.add_argument('-th','--theharvester',help='Enable the harvester module', nargs='+')
        parser.add_argument('-cc','--cert_and_cipher',help='Enable certified and cipher module', nargs='+')
        parser.add_argument('-wi','--whois',help='Enable whois module', nargs='+')
        parser.add_argument('-cve','--cve_detail',help='Enable CVE module', nargs='+')
        parser.add_argument('-cms','--cmsmap',help='Enable cmsmap module', nargs='+')
        parser.add_argument('-x','--xss',help='Enable xss module', nargs='+')
        parser.add_argument('-s','--sqli',help='Enable sqli module', nargs='+')
        #parser.add_argument('-prof','--prof',help='Just for devs', action=StoreDictKeyPair, nargs="+", metavar="KEY=VAL", dest="my_dict")
        parser.add_argument('-pp','--pref',help='Just for devs', nargs='+')
        #parser.add_argument('-prof','--prof',help='Just for devs')




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

        if( args.pref is not None): # Devs proof
            #self.active_modules.append(Proof("args.proof"))
            self.active_modules.append(Proof(args.pref))

            #print(keyvalues)
        else:
            print("adios")


    def run_all_modules(self):
        """
        Run all active modules
        """
        for i in self.active_modules:
            i.run_module()




a = Main()
a.run_all_modules()
