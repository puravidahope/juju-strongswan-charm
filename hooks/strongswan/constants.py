
from charmhelpers.core import hookenv
from strongswan.errors import ExportDirDoesNotExist
from os.path import exists

# Raise an exception is /home/ubuntu doesn't exist.
if not exists('/home/ubuntu/'):
	raise ExportDirDoesNotExist("/home/ubuntu does not exist")

EXPORT_DIR 			= 	'/home/ubuntu/'
CONFIG 				= 	hookenv.config()
DL_BASE_URL 		= 	"http://download.strongswan.org/"
DPKG_LOCK_ERROR 	= 	100
IPV4_FORWARD 		= 	"net.ipv4.ip_forward"
IPV6_FORWARD 		= 	"net.ipv6.conf.all.forwarding"
SYSCTL_PATH 		= 	"/etc/sysctl.conf"
IPSEC_D_PRIVATE 	= 	'/etc/ipsec.d/private/'
IPSEC_D_CACERTS 	= 	'/etc/ipsec.d/cacerts/'
IPSEC_D_CERTS 		= 	'/etc/ipsec.d/certs/'
IPSEC_D_CRLS		= 	'/etc/ipsec.d/crls/'
CA_KEY				= 	'caKey.pem'
CA_CERT				= 	'caCert.pem'
SERVER_CERT_NAME	= 	'SERVER'
INSERT 				= 	'INSERT'
APPEND 				= 	'APPEND'
DELETE				= 	'DELETE'
FILTER				=	'FILTER'
NAT 				= 	'NAT'
ACCEPT 				= 	"ACCEPT"
DROP 				= 	"DROP"
SSH 				=	"22"
IKE					= 	"500"
NAT_T				=	"4500"


APT_DEPENDENCIES = [
	"build-essential",
	"libssl-dev",
	"libffi-dev",
	"python-dev",
	"python3-pip"
]
PIP_DEPENDENCIES = [
	"python-iptables",
	"pyOpenSSL"
]

BUILD_DEPENDENCIES = [
	"libgmp3-dev",
	"gcc",
	"make"
]



	



ALLOW_APT_OUT	= 	['-p', TCP, '--dport', '80', '--sport', '49152:65535', '-j', ACCEPT ]
ALLOW_APT_IN	= 	['-p', TCP, '--dport', '49152:65535', '--sport', '80', '-j', ACCEPT ]
ALLOW_DHCP		=	['-p', UDP, '--dport', DHCP, '--sport', DHCP, '-j', ACCEPT ]
ALLOW_EST_CONN_IN 	= 	['-m', 'conntrack', '--ctstate', 'ESTABLISHED,RELATED', '-j', ACCEPT ]
ALLOW_EST_CONN_OUT 	= 	['-m', 'conntrack', '--ctstate', 'ESTABLISHED,RELATED,NEW', '-j', ACCEPT ]

ALLOW_DNS_UDP_OUT	=	[
	'-p',  UDP, 
	'--dport', DNS,  
	'-m', 'conntrack', '--ctstate', 'NEW,ESTABLISHED', 
	'-j', ACCEPT 
]
ALLOW_DNS_UDP_IN	=	[
	'-p', UDP,
	'--sport', DNS,
	'-m', 'conntrack', '--ctstate', 'ESTABLISHED,RELATED',
	'-j', ACCEPT
]
ALLOW_DNS_TCP_OUT	=	[
	'-p',  TCP, 
	'--dport', DNS,  
	'-m', 'conntrack', '--ctstate', 'NEW,ESTABLISHED', 
	'-j', ACCEPT 
]
ALLOW_DNS_TCP_IN	=	[
	'-p', TCP,
	'--sport', DNS,
	'-m', 'conntrack', '--ctstate', 'ESTABLISHED,RELATED',
	'-j', ACCEPT
]




