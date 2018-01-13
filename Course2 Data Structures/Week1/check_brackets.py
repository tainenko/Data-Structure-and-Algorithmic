# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position
    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()
    opening_brackets_stack = []
    for index, item in enumerate(text):
        if item == '(' or item == '[' or item == '{':
            opening_brackets_stack.append(Bracket(item, index))
        elif item == ')' or item == ']' or item == '}':
            if not opening_brackets_stack:
                opening_brackets_stack.append(Bracket(item, index))
                break
            last_item = opening_brackets_stack.pop()
            if not last_item.Match(item):
                opening_brackets_stack.append(Bracket(item, index))
                break
    if not opening_brackets_stack:
        print("Success")
    else:
        print(opening_brackets_stack.pop().position + 1)