from tokens import *

class Lexer:
    def __init__(self, source):
        self.source = source
        self.start = 0
        self.curr = 0
        self.line = 1
        self.tokens = []

    def advance(self):
        ch = self.source[self.curr]
        self.curr += 1
        return ch
    
    def peek(self):
        return self.source[self.curr]

    def lookahead(self, n=1):
        return self.source[self.curr + n]

    def match(self, expected):
        if self.curr >= len(self.source):
            return False
        if self.source[self.curr] != expected:
            return False
        self.curr = self.curr + 1
        return True

    def add_token(self, token_type):
        self.tokens.append(Token(token_type, self.source[self.start:self.curr], self.line)) 

    def tokenize(self):
        while self.curr < len(self.source):
            self.start = self.curr
            ch = self.advance()
            
            if ch == '\n': self.line += 1
            elif ch == ' ': pass
            elif ch == '\t': pass
            elif ch == '\r': pass

            elif ch == '#':
                while self.peek() != '\n':
                    self.advance()

            elif ch == '(': self.add_token(TOK_LPAREN)
            elif ch == ')': self.add_token(TOK_RPAREN)
            elif ch == '{': self.add_token(TOK_LCURLY)
            elif ch == '}': self.add_token(TOK_RCURLY)
            elif ch == '[': self.add_token(TOK_LSQUAR)
            elif ch == ']': self.add_token(TOK_RSQUAR)
            elif ch == '.': self.add_token(TOK_DOT)
            elif ch == ',': self.add_token(TOK_COMMA)
            elif ch == '+': self.add_token(TOK_PLUS)
            elif ch == '-': self.add_token(TOK_MINUS)
            elif ch == '*': self.add_token(TOK_STAR)
            elif ch == '^': self.add_token(TOK_CARET)
            elif ch == '/': self.add_token(TOK_SLASH)
            elif ch == ';': self.add_token(TOK_SEMICOLON)
            elif ch == '?': self.add_token(TOK_QUESTION)
            elif ch == '%': self.add_token(TOK_MOD)
        return self.tokens



"""
    tokens = estrutura de dados linear que armazena os tokens
    append = método que serve para adicionar um elemento tal a uma estrutura de dados
    Token() = classe de Tokens
    TOK_INTEGER = apenas o token type
    source[start:curr] = um lexema, que, no token, é uma string. 
    antes de tudo, verifica-se o tipo do lexema, se é um dígito, um operador etc.
    no caso, o lexema usa um algoritmo
    que verifica o inicio dele (start) e o curr, que seria um ponteiro que faz um lookahead 
    para verificar se o caractere subsequente é do mesmo tipo do anterior. se, por ex, start for 1 e
    curr passar por 2, 3 e 4, significa que o lexema é 1234, mas se o próximo objeto que o ponteiro
    encontrar for de outro tipo, significa que o lexema terminou e que era de um tipo dígito, por exemplo.
    resumindo: um lexema começa no start e termina onde ele vir que o tipo não é mais o mesmo 
    do start

    tokens.append(Token(TOK_INTEGER, source[start:curr]))
"""


