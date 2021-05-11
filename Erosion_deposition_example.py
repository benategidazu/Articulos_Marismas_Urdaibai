# Hacemos una prueba del modelo que tiene en cuenta la variación elevación-SLR al año

# Importamos los módulos necesarios
import arcpy
from arcpy import env
from arcpy.sa import *

# Introducimos el ráster de elevacíon necesario para establecer la zonación de la marisma:
raster_Marisma = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\ServiciosEcosistemicosUrdaibai.Overviews\SEU_prueba.gdb\raster_prueba"

# Pedimos al usuario que introduzca el límite mínimo donde empieza la marisma y el límite máximo (en nuestro caso el mínimo es 0,87 por ser la elevación donde empieza a habitar Spartina):
#limite_inferior_marisma = 0,87
#limite_superior_marisma = 2,47

#Pedimos al usuario que introduzca el valor de la concentración de sedimento en gramos por metro cubico:
concentracion = input("Introduce la concentracion de sedimento: ")

#Pedimos al usuario que introduzca el valor de la produccion de biomasa en gramos por metro cuadrado y año:
produccion_biomasa = input("Introduce la produccion de biomasa: ")

#Pedimos al usuario el escenario y fecha que quiere reproyectar:
choice = input("Introduce el escenario que quiere conocer: ")

if choice == "RCP4.5_2050":
    #Variable que almacena la elevación que tendrá la marisma en ese rango para el año especificado:
    tasa_deposicion_087 = 0;
    #Variable que almacena la profundidad de la zona de la marisma respecto al límite superior de la marisma (highest astronomical
    #tide):
    elevaciones_087 = [1.55];

    #Ahora hacemos un bucle para iterar las variaciones de la tasa de deposición por la diferencia entre el aumento del nivel
    #del mar y la tasa de deposicion para el rango de elevaciones [0.87-0.97]:
    for tasa_dep_087 in range(2017,2050):
        expresion_087 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_087[-1];
        nueva_elevacion_087 = elevaciones_087[-1] - expresion_087 + 0.0071875;
        elevaciones_087.append(nueva_elevacion_087);
        tasa_deposicion_087+= expresion_087;
    print("Tasa de deposición acumulada del rango 0.87-0.97 es: " + str(tasa_deposicion_087))

    #Volvemos a calcular las tasas de deposiciones pero ahora para todos los rangos de valores (desde 0.87 hasta 2.47 metros, cada
    #10 centimetros):
    tasa_deposicion_097 = 0;
    elevaciones_097 = [1.45];

    for tasa_dep_097 in range(2017,2050):
        expresion_097 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_097[-1];
        nueva_elevacion_097 = elevaciones_097[-1] - expresion_097 + 0.0071875;
        elevaciones_097.append(nueva_elevacion_097);
        tasa_deposicion_097+= expresion_097;
    print("Tasa de deposición acumulada del rango 0.97-1.07 es: " + str(tasa_deposicion_097))

    tasa_deposicion_107 = 0;
    elevaciones_107 = [1.35];

    for tasa_dep_107 in range(2017, 2050):
        expresion_107 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_107[-1];
        nueva_elevacion_107 = elevaciones_107[-1] - expresion_107 + 0.0071875;
        elevaciones_107.append(nueva_elevacion_107);
        tasa_deposicion_107 += expresion_107;
    print("Tasa de deposicion acumulada del rango 1.07-1.17 es: " + str(tasa_deposicion_107))

    tasa_deposicion_117 = 0;
    elevaciones_117 = [1.25];

    for tasa_dep_117 in range(2017, 2050):
        expresion_117 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_117[-1];
        nueva_elevacion_117 = elevaciones_117[-1] - expresion_117 + 0.0071875;
        elevaciones_117.append(nueva_elevacion_117);
        tasa_deposicion_117 += expresion_117;
    print("Tasa de deposicion acumulada del rango 1.17-1.27 es: " + str(tasa_deposicion_117))

    tasa_deposicion_127 = 0;
    elevaciones_127 = [1.15];

    for tasa_dep_127 in range(2017, 2050):
        expresion_127 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_127[-1];
        nueva_elevacion_127 = elevaciones_127[-1] - expresion_127 + 0.0071875;
        elevaciones_127.append(nueva_elevacion_127);
        tasa_deposicion_127 += expresion_127;
    print("Tasa de deposicion acumulada del rango 1.27-1.37 es: " + str(tasa_deposicion_127))

    tasa_deposicion_137 = 0;
    elevaciones_137 = [1.05];

    for tasa_dep_137 in range(2017, 2050):
        expresion_137 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_137[-1];
        nueva_elevacion_137 = elevaciones_137[-1] - expresion_137 + 0.0071875;
        elevaciones_137.append(nueva_elevacion_137);
        tasa_deposicion_137 += expresion_137;
    print("Tasa de deposicion acumulada del rango 1.37-1.47 es: " + str(tasa_deposicion_137))

    tasa_deposicion_147 = 0;
    elevaciones_147 = [0.95];

    for tasa_dep_147 in range(2017, 2050):
        expresion_147 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_147[-1];
        nueva_elevacion_147 = elevaciones_147[-1] - expresion_147 + 0.0071875;
        elevaciones_147.append(nueva_elevacion_147);
        tasa_deposicion_147 += expresion_147;
    print("Tasa de deposicion acumulada del rango 1.47-1.57 es: " + str(tasa_deposicion_147))

    tasa_deposicion_157 = 0;
    elevaciones_157 = [0.85];

    for tasa_dep_157 in range(2017, 2050):
        expresion_157 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_157[-1];
        nueva_elevacion_157 = elevaciones_157[-1] - expresion_157 + 0.0071875;
        elevaciones_157.append(nueva_elevacion_157);
        tasa_deposicion_157 += expresion_157;
    print("Tasa de deposicion acumulada del rango 1.57-1.67 es: " + str(tasa_deposicion_157))

    tasa_deposicion_167 = 0;
    elevaciones_167 = [0.75];

    for tasa_dep_167 in range(2017, 2050):
        expresion_167 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_167[-1];
        nueva_elevacion_167 = elevaciones_167[-1] - expresion_167 + 0.0071875;
        elevaciones_167.append(nueva_elevacion_167);
        tasa_deposicion_167 += expresion_167;
    print("Tasa de deposicion acumulada del rango 1.67-1.77 es: " + str(tasa_deposicion_167))

    tasa_deposicion_177 = 0;
    elevaciones_177 = [0.65];

    for tasa_dep_177 in range(2017, 2050):
        expresion_177 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_177[-1];
        nueva_elevacion_177 = elevaciones_177[-1] - expresion_177 + 0.0071875;
        elevaciones_177.append(nueva_elevacion_177);
        tasa_deposicion_177 += expresion_177;
    print("Tasa de deposicion acumulada del rango 1.77-1.87 es: " + str(tasa_deposicion_177))

    tasa_deposicion_187 = 0;
    elevaciones_187 = [0.55];

    for tasa_dep_187 in range(2017, 2050):
        expresion_187 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_187[-1];
        nueva_elevacion_187 = elevaciones_187[-1] - expresion_187 + 0.0071875;
        elevaciones_187.append(nueva_elevacion_187);
        tasa_deposicion_187 += expresion_187;
    print("Tasa de deposicion acumulada del rango 1.87-1.97 es: " + str(tasa_deposicion_187))

    tasa_deposicion_197 = 0;
    elevaciones_197 = [0.45];

    for tasa_dep_197 in range(2017, 2050):
        expresion_197 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_197[-1];
        nueva_elevacion_197 = elevaciones_197[-1] - expresion_197 + 0.0071875;
        elevaciones_197.append(nueva_elevacion_197);
        tasa_deposicion_197 += expresion_197;
    print("Tasa de deposicion acumulada del rango 1.97-2.07 es: "+ str(tasa_deposicion_197))

    tasa_deposicion_207 = 0;
    elevaciones_207 = [0.35];

    for tasa_dep_207 in range(2017, 2050):
        expresion_207 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_207[-1];
        nueva_elevacion_207 = elevaciones_207[-1] - expresion_207 + 0.0071875;
        elevaciones_207.append(nueva_elevacion_207);
        tasa_deposicion_207 += expresion_207;
    print("Tasa de deposicion acumulada del rango 2.07-2.17 es: " + str(tasa_deposicion_207))

    tasa_deposicion_217 = 0;
    elevaciones_217 = [0.25];

    for tasa_dep_217 in range(2017, 2050):
        expresion_217 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_217[-1];
        nueva_elevacion_217 = elevaciones_217[-1] - expresion_217 + 0.0071875;
        elevaciones_217.append(nueva_elevacion_217);
        tasa_deposicion_217 += expresion_217;
    print("Tasa de deposicion acumulada del rango 2.17-2.27 es: " + str(tasa_deposicion_217))

    tasa_deposicion_227 = 0;
    elevaciones_227 = [0.15];

    for tasa_dep_227 in range(2017, 2050):
        expresion_227 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_227[-1];
        nueva_elevacion_227 = elevaciones_227[-1] - expresion_227 + 0.0071875;
        elevaciones_227.append(nueva_elevacion_227);
        tasa_deposicion_227 += expresion_227;
    print("Tasa de deposicion acumulada del rango 2.27-2.37 es: " + str(tasa_deposicion_227))

    tasa_deposicion_237 = 0;
    elevaciones_237 = [0.05];

    for tasa_dep_237 in range(2017, 2050):
        expresion_237 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_237[-1];
        nueva_elevacion_237 = elevaciones_237[-1] - expresion_237 + 0.0071875;
        elevaciones_237.append(nueva_elevacion_237);
        tasa_deposicion_237 += expresion_237;
    print("Tasa de deposicion acumulada del rango 2.37-2.47 es: " + str(tasa_deposicion_237))
