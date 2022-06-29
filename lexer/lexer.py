def lexer(line):
    lexeme_count = 0
    while lexeme_count < len(line):
        lexeme = line[lexeme_count]
        if lexeme.isdigit():
            typ, tok, consumed = lex_num(line[lexeme_count:])
            lexeme_count += consumed
        elif lexeme.isalpha():
            pass
        else:
            lexeme_count += 1


code = input()
lexer(code)
