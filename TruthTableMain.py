
from Evaluator import Evaluator
class TruthTableGenerator:
    def __init__(self, exp):
        self.var_map = {}  # Variable to indexes in expression
        self.original_exp=exp
        self.table = []  # Truth table for result calculation
        self.pfix = []  # Expression in postfix
        self.var_count = 0  # Variable count
        self.evaluator = Evaluator()  # Evaluator object for evaluation
        self.var_set = []  # Variables present in string
        self.is_valid = False

        expression = self.process_expression(exp)
        if self.evaluator.is_valid(expression):
            self.is_valid = True
            self.pfix = list(self.evaluator.intopo(expression))  # Convert to postfix
            self.scan_input()
        else:
            self.is_valid = False

    def replace_expression(self, new_expression):
        """Replace the expression to avoid unnecessary object creation."""
        expression = self.process_expression(new_expression)
        if self.evaluator.is_valid(expression):
            self.is_valid = True
            self.pfix = list(self.evaluator.intopo(expression))  # Convert to postfix
            self.scan_input()
        else:
            self.is_valid = False

    def process_expression(self, exp):
        """Remove whitespace and handle different possible notations."""
        exp = exp.replace(" ", "")
        expression = ""
        i=0
        while i<len(exp)-1:
            curr = exp[i]
            next_char = exp[i + 1]
            if curr.isalpha() and (next_char.isalpha() or next_char == '(' or next_char in ('!','~')):
                expression += curr + "*"
            elif (curr == '|' and next_char == '|') or (curr == '&' and next_char == '&'):
                expression += curr
                i += 1
            else:
                expression += curr
            i+=1

        expression += exp[-1]
        return expression

    def scan_input(self):
        """Create a map of variables to their corresponding indexes in the string."""
        self.var_map = {}
        self.var_set = []

        for i, curr in enumerate(self.pfix):
            if curr.isalpha():
                if curr not in self.var_map:
                    self.var_set.append(curr)
                    self.var_map[curr] = [i]
                    self.var_count += 1
                else:
                    self.var_map[curr].append(i)
        self.table = [[0] * (self.var_count + 1) for _ in range(2 ** self.var_count)]

    def calculate_truth_table(self):
        """Fill the truth table with binary values and evaluate the expression."""

        for i in range(len(self.table)):
            temp = i
            for j in range(self.var_count):
                self.table[i][j] = temp % 2
                temp //= 2
                assigned_value = 't' if self.table[i][j] == 1 else 'f'

                for index in self.var_map[self.var_set[j]]:
                    self.pfix[index] = assigned_value

            self.table[i][self.var_count] = 1 if self.evaluator.evaluate(self.pfix) else 0

        return True
    @staticmethod
    def print_2d_array(arr):
        """Print a 2D array."""
        for row in arr:
            print(" ".join(map(str, row)))
    def toString_2d_array(self):
        """Print a 2D array with each row on a new line."""
        print(f'  {self.original_exp}')
        if self.var_count > 6 or not self.is_valid:
            return "Invalid expression"
        s=  '  '
        for row in self.table:
            for val in row:
                s+= str(val)+ " "
            s+="\n  "
        return s

    @staticmethod
    def main():
        """Main function to interact with the user."""
        exp = input("Please enter expression to evaluate: ")
        t_table = TruthTableGenerator(exp)

        while not t_table.calculate_truth_table():
            exp = input("Please re-enter expression to evaluate: ")
            t_table.replace_expression(exp)
        print(t_table.toString_2d_array())


if __name__ == "__main__":
    TruthTableGenerator.main()
