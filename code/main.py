import argparse

parser = argparse.ArgumentParser(description='Parse the arguments.')

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




//ArgumentParser

//ExecuteOptions

//GetInfo

//ShowInfo
