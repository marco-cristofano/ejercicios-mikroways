class NumerosRomanos:
    equivalencias = {
        '1': ('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'),
        '10': ('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'),
        '100': ('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'),
        '1000': ('', 'M', 'MM', 'MMM', 'MMMM', 'MMMMM', 'MMMMMM', 'MMMMMMM', 'MMMMMMM', 'MMMMMMM')
    }

    @classmethod
    def run(cls, numero: int, minuscula=False) -> list:
        cls._validate_params(numero)
        respuesta = ''
        for divisor in (1000, 100, 10, 1):
            resultado = numero // divisor
            respuesta = respuesta + cls.equivalencias[str(divisor)][resultado]
            numero = numero % divisor
        if minuscula:
            respuesta = respuesta.lower()
        return respuesta

    @staticmethod
    def _validate_params(numero: int):
        # Lo correcto es crear una custom except para este error y validar
        if not isinstance(numero, int):
            raise Exception('numero debe ser entero')
