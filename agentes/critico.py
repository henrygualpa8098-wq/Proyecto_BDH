class SubagenteCritico:

    def revisar(self):
        return """
        Evalúa errores conceptuales,
        problemas metodológicos,
        fallos técnicos y propone mejoras
        para asegurar la calidad del proyecto.
        """


if __name__ == "__main__":
    agente = SubagenteCritico()
    print(agente.revisar())