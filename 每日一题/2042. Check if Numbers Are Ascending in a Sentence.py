def areNumbersAscending(self, s: str) -> bool:
    stack = []
    for w in s.split(' '):
        if w.isdigit():
            w_i = int(w)
            if stack and w_i <= stack[-1]:
                print(stack, w_i)
                return False
            stack.append(w_i)
    return True