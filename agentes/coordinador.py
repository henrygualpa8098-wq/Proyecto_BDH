class AgenteCoordinador:

    def __init__(self):
        self.nombre = "Agente Coordinador"

    def ejecutar(self):
        return """
        Coordina el proyecto de política pública.
        Asigna tareas a los agentes especialistas.
        Revisa resultados y organiza decisiones.
        """


if __name__ == "__main__":
    agente = AgenteCoordinador()
    print(agente.ejecutar())