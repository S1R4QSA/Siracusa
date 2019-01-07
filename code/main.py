import argparse
from colorama import Back, Fore, init
init()
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

if __name__ == "__main__":
    domain_name = args.domain_name
    if (domain_name is None or domain_name == "" ):
        print(Fore.RED + "[-] Domain name is empty")
        raise argparse.ArgumentTypeError('Value cant be empty')
    else:
        print(Fore.GREEN +"[+] Domain name defined: "+domain_name)

print(str(args.domain_name))

if(args.dns_module is not None):
    pass
if(args.crawler is not None):
    pass
if(args.banners is not None):
    pass
if(args.geolocate is not None):
    pass
if(args.haveibeenpwned is not None):
    pass
if(args.nmap is not None):
    pass
if(args.ping is not None):
    pass
if(args.theharvester is not None):
    pass
if(args.cert_and_cipher is not None):
    pass
if(args.whois is not None):
    pass
if(args.cve_detail is not None):
    pass
if(args.cmsmap is not None):
    pass
if(args.xss is not None):
    pass
if(args.sqli is not None):
    pass






#ArgumentParser

#ExecuteOptions

#GetInfo

#ShowInfo
