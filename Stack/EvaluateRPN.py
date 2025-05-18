class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        val = []

        for num_op in tokens:

            if num_op == "+":
                val.append(val.pop() + val.pop())
            elif num_op == "-":
                first = val.pop()
                second = val.pop()
                val.append(second - first)
            elif num_op == "*":
                val.append(val.pop() * val.pop())
            elif num_op == "/":
                first = val.pop()
                second = val.pop()
                val.append(int(float(second) / first))
            else:
                val.append(int(num_op))
        
        return val[-1]
