from collections import deque

class Evaluator:
    def __init__(self):
        pass


    def get_corresponding_char(self, exp, curr, i):
        if i + 1 < len(exp):
            operand = exp[i + 1]
            if operand.isalpha() or operand == '(' or operand == '!' or operand == '~':
                return True
            else:
                return False
        return False

    def is_valid(self, exp):
        operator_stack = deque()
        variable_stack = deque()

        for i, curr in enumerate(exp):
            if curr.isalpha():
                variable_stack.append(curr)
            elif self.is_operator(curr):
                if curr in ('!', '~'):
                    if not self.get_corresponding_char(exp, curr, i):
                        return False
                else:
                    if not (self.get_corresponding_char(exp, curr, i) and len(variable_stack) >= 1):
                        return False
                    variable_stack.pop()
            elif curr == '(':
                operator_stack.append(curr)
            elif curr == ')':
                while True:
                    if not operator_stack:
                        return False
                    operator = operator_stack.pop()
                    if operator == '(':
                        break
            else:
                return False

        return not operator_stack and len(variable_stack) <= 1

    def intopo(self, exp):
        res = ""
        stack = deque()

        for curr in exp:
            if curr.isalpha():
                res += curr
            elif curr == '(':
                stack.append(curr)
            elif curr == ')':
                while stack[-1] != '(':
                    res += stack.pop()
                stack.pop()
            elif self.is_operator(curr):
                if curr == '!':
                    stack.append(curr)
                else:
                 while stack and not (self.precedence(stack[-1]) < self.precedence(curr)):
                     if stack[-1] != '(':
                        res += stack.pop()
                     else:
                         break
                 stack.append(curr)

        while stack:
            res += stack.pop()

        return res

    def precedence(self, c):
        if c in ('!', '~'):
            return 3
        elif c in ('*', '&'):
            return 2
        else:
            return 1

    def is_operator(self, c):
        return c in ('!', '*', '+', '&', '|', '~')

    def evaluate(self, pfix):
        stack = deque()

        for curr in pfix:
            if curr.isalpha():
                stack.append(curr)
            elif self.is_operator(curr):
                stack.append(curr)
                self.operation(stack)

        return stack[-1] == 't'

    def operation(self, stack):
        operator = stack.pop()
        res = '?'

        if operator in ('*', '&'):
            operand2 = stack.pop()
            operand1 = stack.pop()
            res = 't' if operand1 == 't' and operand2 == 't' else 'f'
        elif operator in ('+', '|'):
            operand2 = stack.pop()
            operand1 = stack.pop()
            res = 't' if operand1 == 't' or operand2 == 't' else 'f'
        else:
            operand1 = stack.pop()
            res = 't' if operand1 == 'f' else 'f'

        stack.append(res)
