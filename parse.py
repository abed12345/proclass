#!/usr/bin/python
import re
source_code = "start i = 19 j = i print (j) a = 5 end"
def Start():
	global source_code
	rcol()
	start = re.match(r'start', source_code)
	print "Start function ==:", start.group(0)
	source_code = source_code.lstrip(start.group(0))
	clear()
def clear():
	global source_code
	source_code = source_code[1:]
def rcol():
	global source_code
	if source_code[0] == ")":
		source_code = source_code.lstrip(")")
		clear ()
	
	
	

def Assign():
	global source_code
	rcol()
	while source_code[0:5]!= 'print':
		id = re.match(r'[a-zA-Z]+[a-zA-Z0-9]*', source_code) 
		source_code= source_code.lstrip(id.group(0))
		clear()
		eq = re.match(r'=', source_code)
		source_code = source_code.lstrip(eq.group(0))
		clear()
		var = re.match(r'[a-zA-Z1-9]+[a-zA-Z0-9]*', source_code)
		source_code = source_code.lstrip(var.group(0))
		clear()
		print "Assignment statement(s) ==:", id.group(0), eq.group(0), var.group(0)
		
		


def Output():
	global source_code
	rcol()
	while source_code[0] != ")":
		pnt = re.match(r"print", source_code)
		if pnt== None:
			return false   
		else:
			source_code = source_code.lstrip(pnt.group(0))
			clear()
		lcol = re.match(r"\(", source_code)
		source_code = source_code.lstrip(lcol.group(0))
		var = re.match(r'[a-zA-Z1-9]+[a-zA-Z0-9]*', source_code)
		source_code = source_code.lstrip(var.group(0))
		print "Output statement ==:", pnt.group(0), lcol.group(0), var.group(0), ")"
		rcol()
		


def End():
	global source_code
	rcol()
	end = re.match(r'end', source_code)
	print "End function ==:", end.group(0)


Start()
Assign()
Output()
Assign()
End()

	
	
	  