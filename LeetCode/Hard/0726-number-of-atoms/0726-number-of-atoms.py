class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # From GPT
        
        def parse_formula():
            n = len(formula)
            stack = deque([defaultdict(int)])
            i = 0

            while i < n:
                if formula[i] == '(':
                    stack.append(defaultdict(int))
                    i += 1
                elif formula[i] == ')':
                    top = stack.pop()
                    i += 1
                    i_start = i
                    while i < n and formula[i].isdigit():
                        i += 1
                    multiplicity = int(formula[i_start:i] or 1)
                    for elem, count in top.items():
                        stack[-1][elem] += count * multiplicity
                else:
                    i_start = i
                    i += 1
                    while i < n and formula[i].islower():
                        i += 1
                    elem = formula[i_start:i]
                    i_start = i
                    while i < n and formula[i].isdigit():
                        i += 1
                    multiplicity = int(formula[i_start:i] or 1)
                    stack[-1][elem] += multiplicity

            return stack.pop()
        
        atom_counts = parse_formula()
        sorted_atoms = sorted(atom_counts.items())
        result = []
        for atom, count in sorted_atoms:
            result.append(atom)
            if count > 1:
                result.append(str(count))

        return ''.join(result)