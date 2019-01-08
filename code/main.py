import argparse
from modules import *
class Main:
    def __init__(self):
        parser = argparse.ArgumentParser(description='Parse the arguments')
        parser.add_argument('-dn','--domain_name',help='Define domain name')
        parser.add_argument('-dns','--dns_module',help='Enable DNS mopule')
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
        args = parser.parse_args()
        self.active_modules=[]
        if(args.dns_module is not None):
            self.dns_module=args.dns_module
            self.active_modules.append("domain_name")
        else:
            self.dns_module=0
        if(args.crawler is not None):
            self.crawler=args.crawler
            self.active_modules.append("crawler")
        else:
            self.crawler=0
        if(args.banners is not None):
            self.banners=args.banners
            self.active_modules.append("banners")
        else:
            self.banners=0
        if(args.geolocate is not None):
            self.geolocate=args.geolocate
            self.active_modules.append("geolocate")
        else:
            self.geolocate=0
        if(args.haveibeenpwned is not None):
            self.haveibeenpwned=args.haveibeenpwned
            self.active_modules.append("haveibeenpwned")
        else:
            self.haveibeenpwned=0
        if(args.nmap is not None):
            self.nmap=args.nmap
            self.active_modules.append("nmap")
        else:
            self.nmap=0
        if(args.ping is not None):
            self.ping=args.ping
            self.active_modules.append("ping")
        else:
            self.ping=0
        if(args.theharvester is not None):
            self.theharvester=args.theharvester
            self.active_modules.append("theharvester")
        else:
            self.theharvester=0
        if(args.cert_and_cipher is not None):
            self.cert_and_cipher=args.cert_and_cipher
            self.active_modules.append("cert_and_cipher")
        else:
            self.cert_and_cipher=0
        if(args.whois is not None):
            self.whois=args.whois
            self.active_modules.append("whois")
        else:
            self.whois=0
        if(args.cve_detail is not None):
            self.cve_detail=args.cve_detail
            self.active_modules.append("cve_detail")
        else:
            self.cve_detail=0
        if(args.cmsmap is not None):
            self.cmsmap=args.cmsmap
            self.active_modules.append("cmsmap")
        else:
            self.cmsmap=0
        if(args.xss is not None):
            self.xss=args.xss
            self.active_modules.append("xss")
        else:
            self.xss=0
        if(args.sqli is not None):
            self.sqli=args.sqli
            self.active_modules.append("sqli")
        else:
            self.sqli=0



a = Main()
b = globals()["Main"]()
