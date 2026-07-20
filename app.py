# Proyecto Integrador Final
# Arquitectura Multiagéntica para Política Pública

from agentes.coordinador import AgenteCoordinador
from agentes.politica_publica import AgentePoliticaPublica
from agentes.datos_metodologia import AgenteDatos
from agentes.programacion_visualizacion import AgenteProgramacionVisualizacion
from agentes.verificador import SubagenteVerificador
from agentes.critico import SubagenteCritico


def ejecutar_proyecto():

    print("="*50)
    print("PROYECTO FINAL - POLÍTICA PÚBLICA")
    print("Arquitectura Multiagéntica")
    print("="*50)


    coordinador = AgenteCoordinador()
    politica = AgentePoliticaPublica()
    datos = AgenteDatos()
    programacion = AgenteProgramacionVisualizacion()
    verificador = SubagenteVerificador()
    critico = SubagenteCritico()


    print("\nAGENTE COORDINADOR:")
    print(coordinador.ejecutar())


    print("\nAGENTE POLÍTICAS PÚBLICAS:")
    print(politica.analizar())


    print("\nAGENTE DATOS Y METODOLOGÍA:")
    print(datos.analizar_datos())


    print("\nAGENTE PROGRAMACIÓN Y VISUALIZACIÓN:")
    print(programacion.desarrollar())


    print("\nSUBAGENTE VERIFICADOR:")
    print(verificador.verificar())


    print("\nSUBAGENTE CRÍTICO:")
    print(critico.revisar())



if __name__ == "__main__":
    ejecutar_proyecto()