## lis.py
## create a lisp implementation using python --> might be more scheme than lisp

def tokenize(string):
    current = ''                            # initialize to empty string
    tokens = []                             # initialize to empty list

    for char in string:                        # checks each character in the the string s
        if char.iispace():                     # if c is whitespace
            if len(current) > 0             # if current token is non-empty
                tokens.append(current)      # add it to the list
                current = ''                # reset current token to empty string
            elif char in '()':                 # otherwise, if c is a parenthesis
                if len(current) > 0:        # end the current token
                    tokens.append(current)  # add it to the list of tokens
                    current = ''            # reset current again
                tokens.append(char)            # add the parenthesis to the token list
            else:                           # else it is alphanumeric
                current = current + char       # add the character to the currrent token
        # end the for loop
        if len(current) > 0:                # if there is a current token
            tokens.append(current)          # add it to the token list
        return tokens                       # the result is the list of tokens

def parse(string):
    def parse_tokens(tokens, inner):
        res = []
        while len(tokens) > 0:
            current = tokens.pop(0)
            if current == '(':
                res.append(parse_tokens(tokens, True))
            elif current == ')':
                if inner: return res
                else:
                    error('Unmatched clse paren: ' + string)
                    return None
                else:
                    res.append(current)

        if inner:
            error('Unmatched open paren: ' + string)
            return None
        else:
            return res

    return parse_tokens(tokenize(string), False)
