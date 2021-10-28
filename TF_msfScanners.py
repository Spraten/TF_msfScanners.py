#!/usr/bin/env python3
import sys
import re 
import glob, os


#these are the protos that tire fire has listed but are not in msfs ["WHOIS",43, ],["LDAP",389, 636, ],["Web",80, 443, ],["Ident",113, ] ,["Kerberos",88, ],["Java-RMI",1098, ],["Portmapper",43, ,["Oracle",1521,],

PL = [["IMAP",143, 993,], ["MySql",3306,],["NFS",2049, ],["DNS",53],["SMTP",25, 465, 587, ],["FTP", 21, ],["WinRM",5985, ],["MSSQL",1433, ],["Netbios",137, 138, 139],["SNMP",161, ],["Telnet",23, ], ["SMB",137, 138, 139, ],["POP3",110, ],["SSH",22, ],["NTP",123, ],["RDP",3389, ],]
list_rb = []

#proto = input("Enter search term")


def find_proto():
	for i in range(len(PL)):
		proto_port= PL[i][1]
		proto_name=PL[i][0]
		print(proto_name)
		print(proto_port)
		print("/usr/share/metasploit-framework/modules/auxiliary/scanner/"+ str.lower(proto_name))
		pattern_dir = "/usr/share/metasploit-framework/modules/auxiliary/scanner/"+str.lower(proto_name) #input("Enter pattern dir")


		if proto_name == proto_name:
			os.chdir(pattern_dir)

			list_proto = []
			for file in glob.glob("*.rb"):
				file = file[:-3]
				list_proto.append("msfconsole -q -x 'use " + file + "; set RHOSTS 192.168.152.132; set RPORT " + str(proto_port) +"; run; exit' &&")
				list_rb.append(file)
				listToStrProto = ' '.join([str(elem) for elem in list_proto]) 
				outfile = open("/re/Projects/enmu/"+ str.lower(proto_name), "w")
				outfile.write(listToStrProto)
				outfile.write("RE")
				outfile.close()
			list_proto = []



		


find_proto()
	