class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        val = []

        for value in tokens:

            if value == "+":
                val.append(val.pop() + val.pop())
            
            elif value == "-":
                first, second = val.pop(), val.pop()
                val.append(second - first)

            elif value == "*":
                val.append(val.pop() * val.pop())

            elif value == "/":
                first, second = val.pop(), val.pop()
                val.append(int((float(second) / first)))
            else:
                val.append(int(value))

        return val.pop()