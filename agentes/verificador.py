class SubagenteVerificador:

    def verificar(self):
        return """
        Verifica fuentes oficiales,
        cifras utilizadas,
        referencias bibliográficas,
        normas y calidad de la información.
        """


if __name__ == "__main__":
    agente = SubagenteVerificador()
    print(agente.verificar())