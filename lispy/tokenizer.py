## tokenizer.py
## tokenizer for lisp implementation

def tokenize(st):
    current = ''                            # initialize to empty string
    tokens = []                             # initialize to empty list
    for ch in st:                     # checks each character in the the string s
        if ch.isspace():                   # if char is whitespace
            if len(current) > 0:             # if current token is non-empty
                tokens.append(current)      # add it to the list
                current = ''                # reset current token to empty string
        elif ch in '()':                 # otherwise, if c is a parenthesis
            if len(current) > 0:        # end the current token
                tokens.append(current)  # add it to the list of tokens
                current = ''            # reset current again
            tokens.append(ch)            # add the parenthesis to the token list
        else:                           # else it is alphanumeric
            current = current + ch   # add the character to the currrent token
        # end the for loop
        
    if len(current) > 0:                # if there is a current token
        tokens.append(current)          # add it to the token list
    return tokens                       # the result is the list of tokens
