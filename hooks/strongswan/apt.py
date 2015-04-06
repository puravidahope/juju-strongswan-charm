#!/usr/bin/env python3
"""
File containing wrapper and helpers functions
"""

import subprocess as sp
from charmhelpers.core import hookenv
from strongswan.hosts import update_hosts_file
import time


def ss_apt_pkgs( config ):
	avail_pkgs = ss_apt_cache() # this is not used.. yet.
	_pkgs = ["strongswan"]
	hookenv.log("Installing: {0}".format(_pkgs) )
	
	return [ "strongswan" ]

def ss_apt_cache():
	avail_pkgs = []

	cmd = ["apt-cache", "search", "strongswan"]
	try:
		handler = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE )
		data = handler.communicate()[0].decode('utf-8') 
	except (OSError, sp.TimeoutExpired, ValueError) as error : 
		hookenv.log(error)

	for s in ( data.split('\n') ):
		t = s.split(' ')
		avail_pkgs.append(t[0])

	return avail_pkgs

# call apt-get command
# if we have a problem with the network or contacting the 
# archive servers we will see it here first
def run_apt_command(cmd, timeout_interval ):
	hookenv.log("INFO:\tCalling {0}".format(cmd))

	apt_retry_count = 0
	apt_retry_max = 0
	apt_retry_wait = 10
	dpkg_lock_error = 100
	timed_out = False
	result = None

	while result is None or result == dpkg_lock_error :
		try:
			result = sp.check_call( cmd, timeout=timeout_interval )

		except sp.CalledProcessError as e:
			apt_retry_count += 1
			if apt_retry_count > apt_retry_max : 
				raise
			result = e.returncode
			hookenv.log("ERROR:\tCouldn't aquire DPKG lock trying again in {0}".format(apt_retry_wait) )
			time.sleep(apt_retry_wait)

		except sp.TimeoutExpired:
			hookenv.log("ERROR:\t{0} command has timed out.".format(cmd))
			if not timed_out :
				timed_out = True
				dns_entries = get_archive_ip_addrs()
				if not dns_entries:
					hookenv.log('ERROR:\tDo we have a DNS issue? Can\'t Resolve archive.ubuntu.com.')
					raise
			if not dns_entries:
				hookenv.log('ERROR:\tUnable to contact an archive server.')
				raise
			else:
				_ip = dns_entries.pop()
				update_hosts_file( _ip , "archive.ubuntu.com" )
				update_hosts_file( _ip , "security.ubuntu.com" )

	hookenv.log("INFO:\t{0} has completed. ".format(cmd) )

# returns a list with the result of dig archive.ubuntu.com			
def get_archive_ip_addrs():
	hookenv.log("INFO:\tObtaining IP addresses.")
	ip_list = []
	dig = sp.check_output(['dig', 'archive.ubuntu.com'])
	dig = dig.decode('utf-8').split('\n')
	for i in dig:
		i = i.split('\t')
		if i:
			if i[0] == 'archive.ubuntu.com.' :
				ip_list.append(i[4])
	return ip_list