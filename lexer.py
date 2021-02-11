class Controller(object):
	enter = argument[0]
	in_comment = False
	def __init__(lexeme_count, current_index):
		self.lexeme_count = lexeme_count
		self.current_index = current_index 
	def match_reserved_words():
		lexeme = enter
		if lexeme == "print": 	
			return "PRINT"
		if lexeme == "start": 	
			return "START"
		if lexeme == "end": 
			return "END"
		return "UNRECOGNIZED"
	def match_identifier():
		lexeme = enter 
		#char = string_char_at(lexeme,1)
		if char != len(char):
			return "UNRECOGNIZED"
		#lexeme = string_delete(lexeme, 1, 1)
	def get_lexeme():
		advance = argument[]
		with Controller.lexer:
			if current_index >= lexeme_count:
				current_index = 0
				return None
			if !advance:
				return lexemes[current_index]
			current_index = current_index + 1
			return lexemes[current_index - 1]
		while len(lexeme) > 0:
			#char = string_char_at(lexeme, 1)
			#lexeme = string_delete(lexeme, 1, 1)
			if char != string_letters(char) and char != string_digits(char) and char != "_":
				return "UNRECOGNIZED"
			return "IDENTIFIER"
	def extract_next_lexeme():
		enter  = argument[0]
		lexeme = ""
		#WHITE_SPACE = " " + ansi_char(9) + ansi_char(10) + ansi_char(13)
		#STOP_CHARS = WHITE_SPACE + "()=*/\"
		#while (string_pos(string_char_at(input, 1), WHITE_SPACE) != 0):
			#enter = string_delete(input, 1, 1)
		while len(enter) > 0:
			#next_char = string_char_at(enter, 1)
		
		if (string_pos(next_char, STOP_CHARS) != 0): 
			if lexeme == "":
				lexeme = lexeme + next_char
			second_char = string_char_at(enter, 2)
			if lexeme == "/" and second_char == "*"  or lexeme == "*" and second_char == "/":
				lexeme = lexeme + second_char
			return lexeme
		lexeme = lexeme + next_char   
		input = string_delete(input, 1, 1)
		return lexeme
	while True:
		lexeme = Controller(0,0)
		lexeme.source = extract_next_lexeme(enter)
		#show_debug_message("lexeme source: " + string(lexeme.source))
		if len(lexeme) == 0:
			break
		#input = string_delete(input, 1, string_pos(lexeme.source, input) + string_length(lexeme.source) - 1)
		#next_char = string_char_at(lexeme.source, 1)    
        
        
        #if (next_char == string_letters(next_char)):
            lexeme.token = match_reserved_words(lexeme.source)
                
        if lexeme.token == "UNRECOGNIZED": 
			lexeme.token = match_identifier(lexeme.source);
        elif lexeme.source == "(": 
			lexeme.token = "OPEN_PAREN"
        elif lexeme.source == ")": 
			lexeme.token = "CLOSE_PAREN"
        elif lexeme.source == "=": 
			lexeme.token = "ASSIGNMENT"
        elif lexeme.source == "/*" : 
			lexeme.token = "OPEN_COMMENT"
        elif lexeme.source == "*/":  
			lexeme.token = "CLOSE_COMMENT"
        #elif lexeme.source == string_digits(lexeme.source): 
			lexeme.token = "NUMERIC"
        else: 
			lexeme.token = "UNRECOGNIZED"
        
        
        if lexeme.token == "OPEN_COMMENT": 
			in_comment = true
        
        if (!in_comment) 
            self.lexemes[self.lexeme_count++] = lexeme
            print "Token: " + lexeme.token + ". Lexeme: " + lexeme.source
        
        if lexeme.token == "CLOSE_COMMENT": 
			in_comment = false;
		