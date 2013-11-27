## tokenize.py
## why is this my problem?


def tokenize(line):
    ret = list()


class Context:
    begin = 0
    accum = ''
    token_type = ''
    offset = 0
 
ctx = Context()
for i, char in enumerate(line):
def check_line(signature, given_type, ctx):
if char in signature:
if ctx.token_type != given_type:
if ctx.accum:
ret.append({"type": ctx.token_type, "value": ctx.accum,
"from": ctx.begin, "to": i + ctx.offset})
ctx.accum = ''
 
ctx.begin = i
 
ctx.accum += char
ctx.token_type = given_type
 
def check_numbers(ctx):
def numbers():
return [str(i) for i in range(10)]
 
check_line(numbers(), "number", ctx)
 
def check_operators(ctx):
possible_operators = ("+", "-", "/", "*", )
check_line(possible_operators, "operator", ctx)
 
def check_empty(ctx):
if char == " " and ctx.accum:
ret.append({"type": ctx.token_type, "value": ctx.accum,
"from": ctx.begin, "to": i})
 
ctx.begin = i + 1
ctx.offset += 1
ctx.accum = ''
 
check_numbers(ctx)
check_operators(ctx)
check_empty(ctx)
 
if ctx.accum:
ret.append({"type": ctx.token_type, "value": ctx.accum,
"from": ctx.begin, "to": len(line)})
 
return ret
 
def test_line(line, expected_type):
result = tokenize(line)[0]
 
def assert_line(attr, expected_value):
assert result[attr] == expected_value, attr.capitalize() + \
" failed for " + result + ". Expected " + expected_value + \
" but received " + result[attr] + "."
 
assert_line("type", expected_type)
assert_line("value", line)
assert_line("from", 0)
assert_line("to", len(line))
 
def test_lines(lines, expected_type):
[test_line(line, expected_type) for line in lines]
 
 
possible_numbers = ("1", "46", "123", )
test_lines(possible_numbers, expected_type="number")
 
possible_operators = ("+", "-", "/", "*", )
test_lines(possible_operators, expected_type="operator")
 
assert tokenize("1+2") == [{"type": "number",
"value": "1",
"from": 0,
"to": 1},
{"type": "operator",
"value": "+",
"from": 1,
"to": 2},
{"type": "number",
"value": "2",
"from": 2,
"to": 3},
]
 
assert tokenize("1 + 2") == [{"type": "number",
"value": "1",
"from": 0,
"to": 1},
{"type": "operator",
"value": "+",
"from": 2,
"to": 3},
{"type": "number",
"value": "2",
"from": 4,
"to": 5},
]
 
assert tokenize("1 + 2") == [{"type": "number",
"value": "1",
"from": 0,
"to": 1},
{"type": "operator",
"value": "+",
"from": 2,
"to": 3},
{"type": "number",
"value": "2",
"from": 6,
"to": 7},
]
 
assert tokenize("1 + 2 * 4") == [{"type": "number",
"value": "1",
"from": 0,
"to": 1},
{"type": "operator",
"value": "+",
"from": 2,
"to": 3},
{"type": "number",
"value": "2",
"from": 4,
"to": 5},
{"type": "operator",
"value": "*",
"from": 6,
"to": 7},
{"type": "number",
"value": "4",
"from": 8,
"to": 9},
]