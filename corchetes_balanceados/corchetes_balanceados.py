class CorchetesBalanceados:

    @staticmethod
    def run(string: str) -> bool:
        corchetes_open = 0
        for char in string:
            if char == '[':
                corchetes_open += 1
            elif char == ']':
                corchetes_open -= 1
            if corchetes_open < 0:
                return False
        if corchetes_open != 0:
            return False
        return True
