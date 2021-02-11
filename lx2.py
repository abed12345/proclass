#!/usr/bin/python
import re

source_code = "start i = 19 j = i print(j) end"



lexics = [('WHITE_SPACE' , r"^\s+"),('start' , r"^start"), ('end', r"^end"), ('prints', r"^print"), ('equals', r"^="),('number',r"^[1-9]+[0-9]*"), ('identifer' , r"^[a-zA-Z]+[a-zA-Z0-9]*"),('leftCol', r"^\("),('rightCol', r"^\)"), ('unregionezed', r".+")]
while len(source_code) > 0:
	for token,regex in lexics:
		lex = re.match(regex, source_code)
		
		if lex != None:
			source_code = source_code.lstrip(lex.group(0))
			if token != "WHITE_SPACE":
				print "TOKEN: ", token, ",", "LEXEME:", lex.group(0)
			break

		
			
		
	