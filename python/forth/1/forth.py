class StackUnderflowError(Exception): pass


# Returns a function that applies a sequence of operations or values
# to a given stack, using the snapshot of known operations at creation.
def make_composite_op(ops_sequence: list[str], ops_snapshot: dict[str, callable]):
    def composite(stack: list[int]) -> list[int]:
        for op in ops_sequence:
            if op in ops_snapshot:
                stack = ops_snapshot[op](stack)
            elif is_integer(op):
                stack = stack + [int(op)]
        return stack
    return composite


# Returns True if the string can be converted to an integer, otherwise False
def is_integer(val: str) -> bool:
    try:
        int(val)
        return True
    except:
        return False # Non-integer string or invalid type


# Evaluates a list of Forth-like source code lines and returns the final stack state
def evaluate(src: list[str]) -> list[int]:
    # Dictionary of operations: functions that apply to the stack and return a new stack
    # Defined locally to avoid re-initialization issues on Exercism's multiple test runs
    Ops = {"+" : lambda x: x[:-2] + [x[-2] + x[-1]],
           "-" : lambda x: x[:-2] + [x[-2] - x[-1]],
           "/" : lambda x: x[:-2] + [x[-2] // x[-1]],
           "*" : lambda x: x[:-2] + [x[-2] * x[-1]],
           "dup" : lambda x: x + [x[-1]],
           "drop" : lambda x: x[:-1] if x else x[1], # triggers IndexError if stack empty
           "swap" : lambda x: x[:-2] + [x[-1]] + [x[-2]],
           "over" : lambda x: x + [x[-2]]}
    
    # Flatten all operation tokens from non-definition lines
    src_list = [t for line in src if ";" not in line for t in line.lower().split()]
    
    # Process all new operation definitions
    def_new = [d.lstrip(": ").rstrip(" ;").lower().split() for d in src if ";" in d]
    for op in def_new:
        if is_integer(op[0]):
            raise ValueError("illegal operation")
        Ops[op[0]] = make_composite_op(op[1:], Ops.copy())
    
    # Evaluate the list of tokens
    numbers = []
    for i, string in enumerate(src_list):
        if is_integer(string):
            numbers.append(int(string))
        elif string in Ops:
            try:
                numbers = Ops[string](numbers)
            except(IndexError):
                raise StackUnderflowError("Insufficient number of items in stack")
            except(ZeroDivisionError):
                raise ZeroDivisionError("divide by zero")
        else:
            raise ValueError("undefined operation")
    return numbers