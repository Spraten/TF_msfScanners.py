#!/usr/bin/env python3
import sys
import re 
import glob
import os

def main():
	proto_list = {
		"IMAP": [143, 993],
		"MySql": [3306],
		"NFS": [2049],
		"DNS": [53],
		"SMTP": [25,465,587],
		"FTP": [21],
		"WinRM": [5585],
		"MSSQL": [1433],
		"Netbios": [137,138, 139],
		"SMNP": [161],
		"Telnet": [23],
		"SMB": [137, 138, 139],
		"POP3": [110],
		"SSH": [22],
		"NTP": [123],
		"RDP": [3389]
	}

	find_proto(proto_list)
	test_proto(proto_list)

def find_proto(proto_list: dict) -> list:
	"""these are the protos that tire fire has listed but are not in msfs ["WHOIS",43, ],["LDAP",389, 636, ],["Web",80, 443, ],["Ident",113, ] ,["Kerberos",88, ],["Java-RMI",1098, ],["Portmapper",43, ,["Oracle",1521,]
	"""
	for proto_name, proto_ports in proto_list.items():
		command_list = []
		proto_dir = "/usr/share/metasploit-framework/modules/auxiliary/scanner/" + proto_name.lower() +"/"
		rb_files = glob.glob(proto_dir + "*.rb")
		counter = 1
		for f in rb_files:
			last_count = len(rb_files)					
			#print(proto_name)							#sorry I'm dumb and need to see whats going on
			#print("counter = "+ str(counter))			#sorry I'm dumb and need to see whats going on
			#print("last count = " + str(last_count)) 	#sorry I'm dumb and need to see whats going on
			if counter < last_count:
				for port in proto_ports:
					command = f"msfconsole -q -x 'use {f[32:-3]}; set RHOSTS 127.0.0.1; set RPORT {str(port)}; run; exit' &&" ##LoopBackTo {IP}
					command_list.append(command)
			elif counter == last_count:
				for port in proto_ports:
					command = f"msfconsole -q -x 'use {f[32:-3]}; set RHOSTS 127.0.0.1; set RPORT {str(port)}; run; exit'" ##LoopBackTo {IP}
					command_list.append(command)
			counter += 1

		with open("/tmp/" + proto_name, "w") as f:
			for i in command_list:
				f.write(i + "\n")

def test_proto(proto_list: dict) -> list:
	for proto_name, proto_ports in proto_list.items():
		print("testing :" +proto_name)
		with open("/tmp/"+ proto_name, "r") as f :
			line = f.readlines()
			listToStr = ' '.join([str(elem) for elem in line])
			print(listToStr)
			os.system(listToStr)





if __name__ == "__main__":
	main()
	
