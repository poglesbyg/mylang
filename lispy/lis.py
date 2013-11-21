## lis.py
## create a lisp implementation using python --> might be more scheme than lisp

import tokenizer
import parser

def meval(expr, env):
    if is_primitive(expr): return eval_primitive(expr)
    elif is_if(expr):return eval_if(expr, env)
    elif is_definition(expr): eval_definition(expr, env)
    elif is_name(expr):return eval_name
    elif is_lambda(expr):return eval_lambda(expr, env)
    elif is_application(expr): return eval_application(expr, env)
    else: error('Unknown expression type:' + str(expr))

def is_primitive(expr):                     # RULE: Primitives, evaluates to its predefined value
    return is_number(expr) or is_primitive_procedure(expr)

def is_number(expr):
    return isinstance(expr, str) and expr.isdigit()

def is_primitive_procedure(expr):
    return callable(expr)

def eval_primitive(expr):
    if is_number(expr): return int(expr)
    else: return expr

def primitive_plus(operands):
    if (len(operands)==0):return 0
    else: return operands[0] + primitive_plus(operands[1:])

def primitive_times(operands):
    if(len(operands)==0):return 1
    else: return operands[0] * primitive_times(operands[1:])

def primitive_minus(operands):
    if(len(operands)==1):return -1 * operands[0]
    elif len(operands)==2:return operands[0] - operands[1]
    else:
        eval_error('- expects 1 or 2 operands, given %s: %s'
                   %(len(operands), str(operands)))

def primitive_equals(operands):
    check_operands(operands, 2, '=')
    return operands[0] < operands[1]

def primitive_lessthan(operands):
    check_operands(operands, 2, '<')
    return operands[0]<operands[1]

def check_operands(operands, num, prim):
    if(len(operands) != num):
        eval_error('Primitive %s expected %s operands, given %s: %s'
                   % (prim, num, len(operands), str(operands)))

def is_special_form(expr, keyword):
    return isinstance(expr, list) and len(expr) > 0 and expr[0] == keyword

def is_if(expr):                    # RULE: If, COND THEN ELSE
    return is_special_form(expr, 'if')

def eval_if(expr, env):
    if meval(expr[1], env) != False: return meval(expr[2], env)
    else: return meval(expr[3], env)

class Environment:
    def __init__(self, parent):
        self._parent = parent
        self._frame = {}

    def add_variable(self, name, value):
        self._frame[name] = value

    def lookup_variable(self, name):
        if self._fram.has_key(name): return self._fram[name]
        elif (self._parent): return self._parent.lookup_variable(name)
        else: eval_error('Undefined name: %s' %(name))

def is_definition(expr):return is_special_form(expr, 'define')
def eval_definition(expr, env):
    name = expr[1]
    value = meval(expr[2], env)
    env.add_variable(name, value)

def is_name(expr): return isinstance(expr, str)
def eval_name(expr, env):
    return env.loopup_variable(expr)

class Procedure:
    def __init__(self, params, body, env):
        self._params = params
        self._body = body
        self._env = env

    def getParams(self): return self._params
    def getBody(self): return self._body
    def getEnvironment(self): return self._env

def is_lambda(expr): return is_special_form(expr, 'lambda')

def eval_lambda(expr, env):
    return Procedure(expr[1], expr[2], env)

def is_application(expr):
    return isinstance(expr, list)

def eval_application(expr, env):
    subexprs = expr
    subexprvals = map(lambda sexpr: meval(sexpr, env),subexprs)
    return mapply(subexprvals[0], subexprvals[1:])

# RULE: to apply procedure, construct new environment
# whose parent is the environment of the applied procedure.
# For each procedure parameter, create a place in the frame of the new environment
# Evaluate each operand expression in the environment or the application and initialize
# the value in each place to the value
# of the corresponding operand expression
# Evaluate the body of the procedure in the newly created environment
# The resulting value is the value of the application

def mapply(proc, operands):
    if (is_primitive_procedure(proc)): return proc(operands)
    elif isinstance(proc, Procedure):
        params = proc.getParams()
        newenv = Environment(proc.getEnvironment())
        if len(params) != len(operands):
            eval_error ('Parameter length mismatch: %s given operands %s'
                        % (str(proc), str(operands)))
            for i in range(0, len(params)):
                newenv.add_variable(params[i], operands[i])
            return meval(proc.getBody(), newenv)
    else: eval_error('Application of non-procedure: %s' % (proc))


def evalLoop():
    genv = Environment(None)
    genv.add_variable('true', True)
    genv.add_variable('false', False)
    genv.add_variable('+', primitive_plus)
    genv.add_variable('-', primitive_minus)
    genv.add_variable('*', primitive_times)
    genv.add_variable('=', primitive_equals)
    genv.add_variable('<', primitive_lessthan)
    while True:
        inv = raw_input('Lispy-> ')
        if inv == 'quit': break
        if inv == 'exit': break
        for expr in parse(inv):
            print str(meval(expr, genv))


