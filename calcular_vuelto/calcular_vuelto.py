class CalcularVuelto:
    denominaciones = (1000, 500, 200, 100, 50, 20, 10, 5, 2, 1)

    @classmethod
    def run(cls, x: int, y: int) -> list:
        cls._validate_params(x, y)
        vuelto = x - y
        respuesta = []
        for billete in cls.denominaciones:
            if billete > vuelto:
                continue
            cantidad = int(vuelto / billete)
            for i in range(0, cantidad):
                respuesta.append(billete)
            vuelto = vuelto % billete
        if not respuesta:
            respuesta = [0]
        return respuesta

    @staticmethod
    def _validate_params(x: int, y: int):
        # Lo correcto es crear una custom except para este error y validar
        if not isinstance(x, int):
            raise Exception('x debe ser entero')
        if not isinstance(y, int):
            raise Exception('y debe ser entero')
        if y > x:
            raise Exception('El dinero no alcanza')
