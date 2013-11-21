## parser.py
## parses the tokens for lis.py

def parse(st):
    def parse_tokens(tokens, inner):
        res = []
        while len(tokens) > 0:
            current = tokens.pop(0)
            if current == '(':
                res.append(parse_tokens(tokens, True))
            elif current == ')':
                if inner: return res
                else:
                    error('Unmatched clse paren: ' + st)
                    return None
            else:
                res.append(current)

        if inner:
            error('Unmatched open paren: ' + st)
            return None
        else:
            return res

        return parse_tokens(tokenize(st), False)
