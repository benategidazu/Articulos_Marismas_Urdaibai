# Hacemos una prueba del modelo que tiene en cuenta la variación elevacion-SLR al año

# Importamos los módulos necesarios
import arcpy
from arcpy import env
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")

env.overwriteOutput=True;
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(25830)

# Introducimos el ráster de elevacíon necesario para establecer la zonación de la marisma:
raster_Marisma = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\ServiciosEcosistemicosUrdaibai.Overviews\SEU_prueba.gdb\Raster_prueba_mm"

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
        nueva_elevacion_087 = elevaciones_087[-1] - expresion_087 + 0.0121875;
        elevaciones_087.append(nueva_elevacion_087);
        tasa_deposicion_087+= expresion_087;
    print("Tasa de deposición acumulada del rango 0.87-0.97 es: " + str(tasa_deposicion_087))

    #Volvemos a calcular las tasas de deposiciones pero ahora para todos los rangos de valores (desde 0.87 hasta 2.47 metros, cada
    #10 centimetros):
    tasa_deposicion_097 = 0;
    elevaciones_097 = [1.45];

    for tasa_dep_097 in range(2017,2050):
        expresion_097 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_097[-1];
        nueva_elevacion_097 = elevaciones_097[-1] - expresion_097 + 0.0121875;
        elevaciones_097.append(nueva_elevacion_097);
        tasa_deposicion_097+= expresion_097;
    print("Tasa de deposición acumulada del rango 0.97-1.07 es: " + str(tasa_deposicion_097))

    tasa_deposicion_107 = 0;
    elevaciones_107 = [1.35];

    for tasa_dep_107 in range(2017, 2050):
        expresion_107 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_107[-1];
        nueva_elevacion_107 = elevaciones_107[-1] - expresion_107 + 0.0121875;
        elevaciones_107.append(nueva_elevacion_107);
        tasa_deposicion_107 += expresion_107;
    print("Tasa de deposicion acumulada del rango 1.07-1.17 es: " + str(tasa_deposicion_107))

    tasa_deposicion_117 = 0;
    elevaciones_117 = [1.25];

    for tasa_dep_117 in range(2017, 2050):
        expresion_117 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_117[-1];
        nueva_elevacion_117 = elevaciones_117[-1] - expresion_117 + 0.0121875;
        elevaciones_117.append(nueva_elevacion_117);
        tasa_deposicion_117 += expresion_117;
    print("Tasa de deposicion acumulada del rango 1.17-1.27 es: " + str(tasa_deposicion_117))

    tasa_deposicion_127 = 0;
    elevaciones_127 = [1.15];

    for tasa_dep_127 in range(2017, 2050):
        expresion_127 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_127[-1];
        nueva_elevacion_127 = elevaciones_127[-1] - expresion_127 + 0.0121875;
        elevaciones_127.append(nueva_elevacion_127);
        tasa_deposicion_127 += expresion_127;
    print("Tasa de deposicion acumulada del rango 1.27-1.37 es: " + str(tasa_deposicion_127))

    tasa_deposicion_137 = 0;
    elevaciones_137 = [1.05];

    for tasa_dep_137 in range(2017, 2050):
        expresion_137 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_137[-1];
        nueva_elevacion_137 = elevaciones_137[-1] - expresion_137 + 0.0121875;
        elevaciones_137.append(nueva_elevacion_137);
        tasa_deposicion_137 += expresion_137;
    print("Tasa de deposicion acumulada del rango 1.37-1.47 es: " + str(tasa_deposicion_137))

    tasa_deposicion_147 = 0;
    elevaciones_147 = [0.95];

    for tasa_dep_147 in range(2017, 2050):
        expresion_147 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_147[-1];
        nueva_elevacion_147 = elevaciones_147[-1] - expresion_147 + 0.0121875;
        elevaciones_147.append(nueva_elevacion_147);
        tasa_deposicion_147 += expresion_147;
    print("Tasa de deposicion acumulada del rango 1.47-1.57 es: " + str(tasa_deposicion_147))

    tasa_deposicion_157 = 0;
    elevaciones_157 = [0.85];

    for tasa_dep_157 in range(2017, 2050):
        expresion_157 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_157[-1];
        nueva_elevacion_157 = elevaciones_157[-1] - expresion_157 + 0.0121875;
        elevaciones_157.append(nueva_elevacion_157);
        tasa_deposicion_157 += expresion_157;
    print("Tasa de deposicion acumulada del rango 1.57-1.67 es: " + str(tasa_deposicion_157))

    tasa_deposicion_167 = 0;
    elevaciones_167 = [0.75];

    for tasa_dep_167 in range(2017, 2050):
        expresion_167 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_167[-1];
        nueva_elevacion_167 = elevaciones_167[-1] - expresion_167 + 0.0121875;
        elevaciones_167.append(nueva_elevacion_167);
        tasa_deposicion_167 += expresion_167;
    print("Tasa de deposicion acumulada del rango 1.67-1.77 es: " + str(tasa_deposicion_167))

    tasa_deposicion_177 = 0;
    elevaciones_177 = [0.65];

    for tasa_dep_177 in range(2017, 2050):
        expresion_177 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_177[-1];
        nueva_elevacion_177 = elevaciones_177[-1] - expresion_177 + 0.0121875;
        elevaciones_177.append(nueva_elevacion_177);
        tasa_deposicion_177 += expresion_177;
    print("Tasa de deposicion acumulada del rango 1.77-1.87 es: " + str(tasa_deposicion_177))

    tasa_deposicion_187 = 0;
    elevaciones_187 = [0.55];

    for tasa_dep_187 in range(2017, 2050):
        expresion_187 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_187[-1];
        nueva_elevacion_187 = elevaciones_187[-1] - expresion_187 + 0.0121875;
        elevaciones_187.append(nueva_elevacion_187);
        tasa_deposicion_187 += expresion_187;
    print("Tasa de deposicion acumulada del rango 1.87-1.97 es: " + str(tasa_deposicion_187))

    tasa_deposicion_197 = 0;
    elevaciones_197 = [0.45];

    for tasa_dep_197 in range(2017, 2050):
        expresion_197 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_197[-1];
        nueva_elevacion_197 = elevaciones_197[-1] - expresion_197 + 0.0121875;
        elevaciones_197.append(nueva_elevacion_197);
        tasa_deposicion_197 += expresion_197;
    print("Tasa de deposicion acumulada del rango 1.97-2.07 es: "+ str(tasa_deposicion_197))

    tasa_deposicion_207 = 0;
    elevaciones_207 = [0.35];

    for tasa_dep_207 in range(2017, 2050):
        expresion_207 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_207[-1];
        nueva_elevacion_207 = elevaciones_207[-1] - expresion_207 + 0.0121875;
        elevaciones_207.append(nueva_elevacion_207);
        tasa_deposicion_207 += expresion_207;
    print("Tasa de deposicion acumulada del rango 2.07-2.17 es: " + str(tasa_deposicion_207))

    tasa_deposicion_217 = 0;
    elevaciones_217 = [0.25];

    for tasa_dep_217 in range(2017, 2050):
        expresion_217 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_217[-1];
        nueva_elevacion_217 = elevaciones_217[-1] - expresion_217 + 0.0121875;
        elevaciones_217.append(nueva_elevacion_217);
        tasa_deposicion_217 += expresion_217;
    print("Tasa de deposicion acumulada del rango 2.17-2.27 es: " + str(tasa_deposicion_217))

    tasa_deposicion_227 = 0;
    elevaciones_227 = [0.15];

    for tasa_dep_227 in range(2017, 2050):
        expresion_227 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_227[-1];
        nueva_elevacion_227 = elevaciones_227[-1] - expresion_227 + 0.0121875;
        elevaciones_227.append(nueva_elevacion_227);
        tasa_deposicion_227 += expresion_227;
    print("Tasa de deposicion acumulada del rango 2.27-2.37 es: " + str(tasa_deposicion_227))

    tasa_deposicion_237 = 0;
    elevaciones_237 = [0.05];

    for tasa_dep_237 in range(2017, 2050):
        expresion_237 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_237[-1];
        nueva_elevacion_237 = elevaciones_237[-1] - expresion_237 + 0.0121875;
        elevaciones_237.append(nueva_elevacion_237);
        tasa_deposicion_237 += expresion_237;
    print("Tasa de deposicion acumulada del rango 2.37-2.47 es: " + str(tasa_deposicion_237))

    #Reclasificamos el raster con los datos de la tasa de deposicion, por rangos, para representar la tasa de deposicion (aumento de
    # la elevacion en mm para el año 2050 en la zona de estudio para el escenario RCP4.5 y el año 2050:
    deposicion_RCP45_2050 = Reclassify(raster_Marisma, "VALUE", RemapRange([[-10000, 870,"NODATA"],[870, 970, round(tasa_deposicion_087*1000)],
                                 [970, 1070, round(tasa_deposicion_097*1000)], [1070, 1170, round(tasa_deposicion_107*1000)], [1170, 1270, round(tasa_deposicion_117*1000)],
                                 [1270, 1370, round(tasa_deposicion_127*1000)], [1370, 1470, round(tasa_deposicion_137*1000)], [1470, 1570, round(tasa_deposicion_147*1000)],
                                 [1570, 1670, round(tasa_deposicion_157*1000)], [1670, 1770, round(tasa_deposicion_167*1000)], [1770, 1870, round(tasa_deposicion_177*1000)],
                                 [1870, 1970, round(tasa_deposicion_187*1000)], [1970, 2070, round(tasa_deposicion_197*1000)], [2070, 2170, round(tasa_deposicion_207*1000)],
                                 [2170, 2270, round(tasa_deposicion_217*1000)], [2270, 2370, round(tasa_deposicion_227*1000)], [2370, 2470, round(tasa_deposicion_237*1000)],
                                                                           [2470, 1000000, "NODATA"]]))
    deposicion_RCP45_2050.save(r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\ServiciosEcosistemicosUrdaibai.Overviews\SEU_prueba.gdb\Deposicion_RCP45_2050")
    direcc_depo_RCP45_2050 = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\ServiciosEcosistemicosUrdaibai.Overviews\SEU_prueba.gdb\Deposicion_RCP45_2050"

    #Ahora ya tenemos el raster con la deposicion que habra en la zona de estudio segun el escenario RCP4.5 y para el año 2050,
    #asumiendo que desde el limite inferior hasta el superior donde se encuentran las marismas de Urdaibai de acuerdo a distintos
    #estudios, son las potenciales zonas de las marismas (aunque en realidad no haya por distintos factores y suponiendo que serían
    #marismas consolidadas con unas tasas de deposicion acorde a su elevacion.

    #Pues bien, sumamos los dos rasteres (elevacion en mm y deposicion en mm) para obtener la nueva altura que tendra la marisma.
    elevacion_RCP45_2050 = RasterCalculator([raster_Marisma, direcc_depo_RCP45_2050], ["marisma", "depo"],
                                            "(marisma+depo)")
    elevacion_RCP45_2050.save(
       r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\ServiciosEcosistemicosUrdaibai.Overviews\SEU_prueba.gdb\Elevacion_RCP45_2050")
    direc_elevacion_RCP45_2050 = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\ServiciosEcosistemicosUrdaibai.Overviews\SEU_prueba.gdb\Elevacion_RCP45_2050"

    #Una vez que tenemos la elevacion nueva de la zona de estudio debido a la deposicion fusionamos los rasteres de la nueva
    #elevacion de la marisma con el raster de elevaciones original para que tenga las nuevas elevaciones y tenga en cuenta los
    #valores del raster original en las zonas donde no hay marisma (y asi no ponga "NODATA").
    comb_elevacion_RCP45_2050 = arcpy.management.MosaicToNewRaster([direc_elevacion_RCP45_2050, raster_Marisma], r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\ServiciosEcosistemicosUrdaibai.Overviews\SEU_prueba.gdb",
                                    "Elevacion_Combi_Terreno_RCP45_2050", 25830, "32_BIT_FLOAT", 1, 1, "FIRST")

    #Ya tenemos el la elevacion que habra en la zona de estudio en 2050 segun el escenario 2050, ahora volvemos a reclasificar dicho
    #raster para obtener la potencial distribucion de la marisma en dicho escenario y año:
    pot_distribucion_RCP45_2050 = Reclassify(comb_elevacion_RCP45_2050, "VALUE", RemapRange([[-100000,1260,"NODATA"], [1260,2860,0],[2860, 1000000,"NODATA"]]))
    pot_distribucion_RCP45_2050.save(r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\ServiciosEcosistemicosUrdaibai.Overviews\SEU_prueba.gdb\Pot_Distribucion_RCP45_2050")

#Ahora vamos a hacer lo mismo pero para el escenario RCP8.5 y el año 2050:
if choice == "RCP8.5_2050":
    #Variable que almacena la elevación que tendrá la marisma en ese rango para el año especificado:
    tasa_deposicion_087 = 0;
    #Variable que almacena la profundidad de la zona de la marisma respecto al límite superior de la marisma (highest astronomical
    #tide):
    elevaciones_087 = [1.55];

    #Ahora hacemos un bucle para iterar las variaciones de la tasa de deposición por la diferencia entre el aumento del nivel
    #del mar y la tasa de deposicion para el rango de elevaciones [0.87-0.97]:
    for tasa_dep_087 in range(2017,2050):
        expresion_087 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_087[-1];
        nueva_elevacion_087 = elevaciones_087[-1] - expresion_087 + 0.0134375;
        elevaciones_087.append(nueva_elevacion_087);
        tasa_deposicion_087+= expresion_087;
    print("Tasa de deposición acumulada del rango 0.87-0.97 es: " + str(tasa_deposicion_087))

    #Volvemos a calcular las tasas de deposiciones pero ahora para todos los rangos de valores (desde 0.87 hasta 2.47 metros, cada
    #10 centimetros):
    tasa_deposicion_097 = 0;
    elevaciones_097 = [1.45];

    for tasa_dep_097 in range(2017,2050):
        expresion_097 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_097[-1];
        nueva_elevacion_097 = elevaciones_097[-1] - expresion_097 + 0.0134375;
        elevaciones_097.append(nueva_elevacion_097);
        tasa_deposicion_097+= expresion_097;
    print("Tasa de deposición acumulada del rango 0.97-1.07 es: " + str(tasa_deposicion_097))

    tasa_deposicion_107 = 0;
    elevaciones_107 = [1.35];

    for tasa_dep_107 in range(2017, 2050):
        expresion_107 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_107[-1];
        nueva_elevacion_107 = elevaciones_107[-1] - expresion_107 + 0.0134375;
        elevaciones_107.append(nueva_elevacion_107);
        tasa_deposicion_107 += expresion_107;
    print("Tasa de deposicion acumulada del rango 1.07-1.17 es: " + str(tasa_deposicion_107))

    tasa_deposicion_117 = 0;
    elevaciones_117 = [1.25];

    for tasa_dep_117 in range(2017, 2050):
        expresion_117 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_117[-1];
        nueva_elevacion_117 = elevaciones_117[-1] - expresion_117 + 0.0134375;
        elevaciones_117.append(nueva_elevacion_117);
        tasa_deposicion_117 += expresion_117;
    print("Tasa de deposicion acumulada del rango 1.17-1.27 es: " + str(tasa_deposicion_117))

    tasa_deposicion_127 = 0;
    elevaciones_127 = [1.15];

    for tasa_dep_127 in range(2017, 2050):
        expresion_127 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_127[-1];
        nueva_elevacion_127 = elevaciones_127[-1] - expresion_127 + 0.0134375;
        elevaciones_127.append(nueva_elevacion_127);
        tasa_deposicion_127 += expresion_127;
    print("Tasa de deposicion acumulada del rango 1.27-1.37 es: " + str(tasa_deposicion_127))

    tasa_deposicion_137 = 0;
    elevaciones_137 = [1.05];

    for tasa_dep_137 in range(2017, 2050):
        expresion_137 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_137[-1];
        nueva_elevacion_137 = elevaciones_137[-1] - expresion_137 + 0.0134375;
        elevaciones_137.append(nueva_elevacion_137);
        tasa_deposicion_137 += expresion_137;
    print("Tasa de deposicion acumulada del rango 1.37-1.47 es: " + str(tasa_deposicion_137))

    tasa_deposicion_147 = 0;
    elevaciones_147 = [0.95];

    for tasa_dep_147 in range(2017, 2050):
        expresion_147 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_147[-1];
        nueva_elevacion_147 = elevaciones_147[-1] - expresion_147 + 0.0134375;
        elevaciones_147.append(nueva_elevacion_147);
        tasa_deposicion_147 += expresion_147;
    print("Tasa de deposicion acumulada del rango 1.47-1.57 es: " + str(tasa_deposicion_147))

    tasa_deposicion_157 = 0;
    elevaciones_157 = [0.85];

    for tasa_dep_157 in range(2017, 2050):
        expresion_157 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_157[-1];
        nueva_elevacion_157 = elevaciones_157[-1] - expresion_157 + 0.0134375;
        elevaciones_157.append(nueva_elevacion_157);
        tasa_deposicion_157 += expresion_157;
    print("Tasa de deposicion acumulada del rango 1.57-1.67 es: " + str(tasa_deposicion_157))

    tasa_deposicion_167 = 0;
    elevaciones_167 = [0.75];

    for tasa_dep_167 in range(2017, 2050):
        expresion_167 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_167[-1];
        nueva_elevacion_167 = elevaciones_167[-1] - expresion_167 + 0.0134375;
        elevaciones_167.append(nueva_elevacion_167);
        tasa_deposicion_167 += expresion_167;
    print("Tasa de deposicion acumulada del rango 1.67-1.77 es: " + str(tasa_deposicion_167))

    tasa_deposicion_177 = 0;
    elevaciones_177 = [0.65];

    for tasa_dep_177 in range(2017, 2050):
        expresion_177 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_177[-1];
        nueva_elevacion_177 = elevaciones_177[-1] - expresion_177 + 0.0134375;
        elevaciones_177.append(nueva_elevacion_177);
        tasa_deposicion_177 += expresion_177;
    print("Tasa de deposicion acumulada del rango 1.77-1.87 es: " + str(tasa_deposicion_177))

    tasa_deposicion_187 = 0;
    elevaciones_187 = [0.55];

    for tasa_dep_187 in range(2017, 2050):
        expresion_187 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_187[-1];
        nueva_elevacion_187 = elevaciones_187[-1] - expresion_187 + 0.0134375;
        elevaciones_187.append(nueva_elevacion_187);
        tasa_deposicion_187 += expresion_187;
    print("Tasa de deposicion acumulada del rango 1.87-1.97 es: " + str(tasa_deposicion_187))

    tasa_deposicion_197 = 0;
    elevaciones_197 = [0.45];

    for tasa_dep_197 in range(2017, 2050):
        expresion_197 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_197[-1];
        nueva_elevacion_197 = elevaciones_197[-1] - expresion_197 + 0.0134375;
        elevaciones_197.append(nueva_elevacion_197);
        tasa_deposicion_197 += expresion_197;
    print("Tasa de deposicion acumulada del rango 1.97-2.07 es: "+ str(tasa_deposicion_197))

    tasa_deposicion_207 = 0;
    elevaciones_207 = [0.35];

    for tasa_dep_207 in range(2017, 2050):
        expresion_207 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_207[-1];
        nueva_elevacion_207 = elevaciones_207[-1] - expresion_207 + 0.0134375;
        elevaciones_207.append(nueva_elevacion_207);
        tasa_deposicion_207 += expresion_207;
    print("Tasa de deposicion acumulada del rango 2.07-2.17 es: " + str(tasa_deposicion_207))

    tasa_deposicion_217 = 0;
    elevaciones_217 = [0.25];

    for tasa_dep_217 in range(2017, 2050):
        expresion_217 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_217[-1];
        nueva_elevacion_217 = elevaciones_217[-1] - expresion_217 + 0.0134375;
        elevaciones_217.append(nueva_elevacion_217);
        tasa_deposicion_217 += expresion_217;
    print("Tasa de deposicion acumulada del rango 2.17-2.27 es: " + str(tasa_deposicion_217))

    tasa_deposicion_227 = 0;
    elevaciones_227 = [0.15];

    for tasa_dep_227 in range(2017, 2050):
        expresion_227 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_227[-1];
        nueva_elevacion_227 = elevaciones_227[-1] - expresion_227 + 0.0134375;
        elevaciones_227.append(nueva_elevacion_227);
        tasa_deposicion_227 += expresion_227;
    print("Tasa de deposicion acumulada del rango 2.27-2.37 es: " + str(tasa_deposicion_227))

    tasa_deposicion_237 = 0;
    elevaciones_237 = [0.05];

    for tasa_dep_237 in range(2017, 2050):
        expresion_237 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_237[-1];
        nueva_elevacion_237 = elevaciones_237[-1] - expresion_237 + 0.0134375;
        elevaciones_237.append(nueva_elevacion_237);
        tasa_deposicion_237 += expresion_237;
    print("Tasa de deposicion acumulada del rango 2.37-2.47 es: " + str(tasa_deposicion_237))

    #Reclasificamos el raster con los datos de la tasa de deposicion, por rangos, para representar la tasa de deposicion (aumento de
    # la elevacion en mm para el año 2050 en la zona de estudio para el escenario RCP8.5 y el año 2050:
    deposicion_RCP85_2050 = Reclassify(raster_Marisma, "VALUE", RemapRange([[-10000, 870,"NODATA"],[870, 970, round(tasa_deposicion_087*1000)],
                                 [970, 1070, round(tasa_deposicion_097*1000)], [1070, 1170, round(tasa_deposicion_107*1000)], [1170, 1270, round(tasa_deposicion_117*1000)],
                                 [1270, 1370, round(tasa_deposicion_127*1000)], [1370, 1470, round(tasa_deposicion_137*1000)], [1470, 1570, round(tasa_deposicion_147*1000)],
                                 [1570, 1670, round(tasa_deposicion_157*1000)], [1670, 1770, round(tasa_deposicion_167*1000)], [1770, 1870, round(tasa_deposicion_177*1000)],
                                 [1870, 1970, round(tasa_deposicion_187*1000)], [1970, 2070, round(tasa_deposicion_197*1000)], [2070, 2170, round(tasa_deposicion_207*1000)],
                                 [2170, 2270, round(tasa_deposicion_217*1000)], [2270, 2370, round(tasa_deposicion_227*1000)], [2370, 2470, round(tasa_deposicion_237*1000)],
                                                                           [2470, 1000000, "NODATA"]]))
    deposicion_RCP85_2050.save(r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\ServiciosEcosistemicosUrdaibai.Overviews\SEU_prueba.gdb\Deposicion_RCP85_2050")
    direcc_depo_RCP85_2050 = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\ServiciosEcosistemicosUrdaibai.Overviews\SEU_prueba.gdb\Deposicion_RCP85_2050"

    #Ahora ya tenemos el raster con la deposicion que habra en la zona de estudio segun el escenario RCP8.5 y para el año 2050,
    #asumiendo que desde el limite inferior hasta el superior donde se encuentran las marismas de Urdaibai de acuerdo a distintos
    #estudios, son las potenciales zonas de las marismas (aunque en realidad no haya por distintos factores y suponiendo que serían
    #marismas consolidadas con unas tasas de deposicion acorde a su elevacion.

    #Pues bien, sumamos los dos rasteres (elevacion en mm y deposicion en mm) para obtener la nueva altura que tendra la marisma.
    elevacion_RCP85_2050 = RasterCalculator([raster_Marisma, direcc_depo_RCP85_2050], ["marisma", "depo"],
                                            "(marisma+depo)")
    elevacion_RCP85_2050.save(
       r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\ServiciosEcosistemicosUrdaibai.Overviews\SEU_prueba.gdb\Elevacion_RCP85_2050")
    direc_elevacion_RCP85_2050 = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\ServiciosEcosistemicosUrdaibai.Overviews\SEU_prueba.gdb\Elevacion_RCP85_2050"

    #Una vez que tenemos la elevacion nueva de la zona de estudio debido a la deposicion fusionamos los rasteres de la nueva
    #elevacion de la marisma con el raster de elevaciones original para que tenga las nuevas elevaciones y tenga en cuenta los
    #valores del raster original en las zonas donde no hay marisma (y asi no ponga "NODATA").
    comb_elevacion_RCP85_2050 = arcpy.management.MosaicToNewRaster([direc_elevacion_RCP85_2050, raster_Marisma], r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\ServiciosEcosistemicosUrdaibai.Overviews\SEU_prueba.gdb",
                                    "Elevacion_Combi_Terreno_RCP85_2050", 25830, "32_BIT_FLOAT", 1, 1, "FIRST")

    #Ya tenemos el la elevacion que habra en la zona de estudio en 2050 segun el escenario RCP8.5, ahora volvemos a reclasificar dicho
    #raster para obtener la potencial distribucion de la marisma en dicho escenario y año:
    pot_distribucion_RCP85_2050 = Reclassify(comb_elevacion_RCP85_2050, "VALUE", RemapRange([[-100000,1300,"NODATA"], [1300,2900,0],[2900, 1000000,"NODATA"]]))
    pot_distribucion_RCP85_2050.save(r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\ServiciosEcosistemicosUrdaibai.Overviews\SEU_prueba.gdb\Pot_Distribucion_RCP85_2050")
if choice == "RCP4.5_2100":
    #Variable que almacena la elevación que tendrá la marisma en ese rango para el año especificado:
    tasa_deposicion_087 = 0;
    #Variable que almacena la profundidad de la zona de la marisma respecto al límite superior de la marisma (highest astronomical
    #tide):
    elevaciones_087 = [1.55];

    #Ahora hacemos un bucle para iterar las variaciones de la tasa de deposición por la diferencia entre el aumento del nivel
    #del mar y la tasa de deposicion para el rango de elevaciones [0.87-0.97]:
    for tasa_dep_087 in range(2017,2050):
        expresion_087 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_087[-1];
        nueva_elevacion_087 = elevaciones_087[-1] - expresion_087 + 0.0121875;
        elevaciones_087.append(nueva_elevacion_087);
        tasa_deposicion_087+= expresion_087;

    for tasa_dep_087 in range(2050,2100):
        expresion_087 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_087[-1];
        nueva_elevacion_087 = elevaciones_087[-1] - expresion_087 + 0.0112;
        elevaciones_087.append(nueva_elevacion_087);
        tasa_deposicion_087+= expresion_087;
    print("Tasa de deposición acumulada del rango 0.87-0.97 es: " + str(tasa_deposicion_087))

    #Volvemos a calcular las tasas de deposiciones pero ahora para todos los rangos de valores (desde 0.87 hasta 2.47 metros, cada
    #10 centimetros):
    tasa_deposicion_097 = 0;
    elevaciones_097 = [1.45];

    for tasa_dep_097 in range(2017,2050):
        expresion_097 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_097[-1];
        nueva_elevacion_097 = elevaciones_097[-1] - expresion_097 + 0.0121875;
        elevaciones_097.append(nueva_elevacion_097);
        tasa_deposicion_097+= expresion_097;

    for tasa_dep_097 in range(2050,2100):
        expresion_097 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_097[-1];
        nueva_elevacion_097 = elevaciones_097[-1] - expresion_097 + 0.0112;
        elevaciones_097.append(nueva_elevacion_097);
        tasa_deposicion_097+= expresion_097;
    print("Tasa de deposición acumulada del rango 0.97-1.07 es: " + str(tasa_deposicion_097))

    tasa_deposicion_107 = 0;
    elevaciones_107 = [1.35];

    for tasa_dep_107 in range(2017, 2050):
        expresion_107 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_107[-1];
        nueva_elevacion_107 = elevaciones_107[-1] - expresion_107 + 0.0121875;
        elevaciones_107.append(nueva_elevacion_107);
        tasa_deposicion_107 += expresion_107;

    for tasa_dep_107 in range(2050, 2100):
        expresion_107 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_107[-1];
        nueva_elevacion_107 = elevaciones_107[-1] - expresion_107 + 0.0112;
        elevaciones_107.append(nueva_elevacion_107);
        tasa_deposicion_107 += expresion_107;
    print("Tasa de deposicion acumulada del rango 1.07-1.17 es: " + str(tasa_deposicion_107))

    tasa_deposicion_117 = 0;
    elevaciones_117 = [1.25];

    for tasa_dep_117 in range(2017, 2050):
        expresion_117 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_117[-1];
        nueva_elevacion_117 = elevaciones_117[-1] - expresion_117 + 0.0121875;
        elevaciones_117.append(nueva_elevacion_117);
        tasa_deposicion_117 += expresion_117;

    for tasa_dep_117 in range(2050, 2100):
        expresion_117 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_117[-1];
        nueva_elevacion_117 = elevaciones_117[-1] - expresion_117 + 0.0112;
        elevaciones_117.append(nueva_elevacion_117);
        tasa_deposicion_117 += expresion_117;
    print("Tasa de deposicion acumulada del rango 1.17-1.27 es: " + str(tasa_deposicion_117))

    tasa_deposicion_127 = 0;
    elevaciones_127 = [1.15];

    for tasa_dep_127 in range(2017, 2050):
        expresion_127 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_127[-1];
        nueva_elevacion_127 = elevaciones_127[-1] - expresion_127 + 0.0121875;
        elevaciones_127.append(nueva_elevacion_127);
        tasa_deposicion_127 += expresion_127;

    for tasa_dep_127 in range(2050, 2100):
        expresion_127 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_127[-1];
        nueva_elevacion_127 = elevaciones_127[-1] - expresion_127 + 0.0112;
        elevaciones_127.append(nueva_elevacion_127);
        tasa_deposicion_127 += expresion_127;
    print("Tasa de deposicion acumulada del rango 1.27-1.37 es: " + str(tasa_deposicion_127))

    tasa_deposicion_137 = 0;
    elevaciones_137 = [1.05];

    for tasa_dep_137 in range(2017, 2050):
        expresion_137 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_137[-1];
        nueva_elevacion_137 = elevaciones_137[-1] - expresion_137 + 0.0121875;
        elevaciones_137.append(nueva_elevacion_137);
        tasa_deposicion_137 += expresion_137;

    for tasa_dep_137 in range(2050, 2100):
        expresion_137 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_137[-1];
        nueva_elevacion_137 = elevaciones_137[-1] - expresion_137 + 0.0112;
        elevaciones_137.append(nueva_elevacion_137);
        tasa_deposicion_137 += expresion_137;
    print("Tasa de deposicion acumulada del rango 1.37-1.47 es: " + str(tasa_deposicion_137))

    tasa_deposicion_147 = 0;
    elevaciones_147 = [0.95];

    for tasa_dep_147 in range(2017, 2050):
        expresion_147 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_147[-1];
        nueva_elevacion_147 = elevaciones_147[-1] - expresion_147 + 0.0121875;
        elevaciones_147.append(nueva_elevacion_147);
        tasa_deposicion_147 += expresion_147;

    for tasa_dep_147 in range(2050, 2100):
        expresion_147 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_147[-1];
        nueva_elevacion_147 = elevaciones_147[-1] - expresion_147 + 0.0112;
        elevaciones_147.append(nueva_elevacion_147);
        tasa_deposicion_147 += expresion_147;
    print("Tasa de deposicion acumulada del rango 1.47-1.57 es: " + str(tasa_deposicion_147))

    tasa_deposicion_157 = 0;
    elevaciones_157 = [0.85];

    for tasa_dep_157 in range(2017, 2050):
        expresion_157 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_157[-1];
        nueva_elevacion_157 = elevaciones_157[-1] - expresion_157 + 0.0121875;
        elevaciones_157.append(nueva_elevacion_157);
        tasa_deposicion_157 += expresion_157;

    for tasa_dep_157 in range(2050, 2100):
        expresion_157 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_157[-1];
        nueva_elevacion_157 = elevaciones_157[-1] - expresion_157 + 0.0112;
        elevaciones_157.append(nueva_elevacion_157);
        tasa_deposicion_157 += expresion_157;
    print("Tasa de deposicion acumulada del rango 1.57-1.67 es: " + str(tasa_deposicion_157))

    tasa_deposicion_167 = 0;
    elevaciones_167 = [0.75];

    for tasa_dep_167 in range(2017, 2050):
        expresion_167 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_167[-1];
        nueva_elevacion_167 = elevaciones_167[-1] - expresion_167 + 0.0121875;
        elevaciones_167.append(nueva_elevacion_167);
        tasa_deposicion_167 += expresion_167;

    for tasa_dep_167 in range(2050, 2100):
        expresion_167 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_167[-1];
        nueva_elevacion_167 = elevaciones_167[-1] - expresion_167 + 0.0112;
        elevaciones_167.append(nueva_elevacion_167);
        tasa_deposicion_167 += expresion_167;
    print("Tasa de deposicion acumulada del rango 1.67-1.77 es: " + str(tasa_deposicion_167))

    tasa_deposicion_177 = 0;
    elevaciones_177 = [0.65];

    for tasa_dep_177 in range(2017, 2050):
        expresion_177 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_177[-1];
        nueva_elevacion_177 = elevaciones_177[-1] - expresion_177 + 0.0121875;
        elevaciones_177.append(nueva_elevacion_177);
        tasa_deposicion_177 += expresion_177;

    for tasa_dep_177 in range(2050, 2100):
        expresion_177 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_177[-1];
        nueva_elevacion_177 = elevaciones_177[-1] - expresion_177 + 0.0112;
        elevaciones_177.append(nueva_elevacion_177);
        tasa_deposicion_177 += expresion_177;
    print("Tasa de deposicion acumulada del rango 1.77-1.87 es: " + str(tasa_deposicion_177))

    tasa_deposicion_187 = 0;
    elevaciones_187 = [0.55];

    for tasa_dep_187 in range(2017, 2050):
        expresion_187 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_187[-1];
        nueva_elevacion_187 = elevaciones_187[-1] - expresion_187 + 0.0121875;
        elevaciones_187.append(nueva_elevacion_187);
        tasa_deposicion_187 += expresion_187;

    for tasa_dep_187 in range(2050, 2100):
        expresion_187 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_187[-1];
        nueva_elevacion_187 = elevaciones_187[-1] - expresion_187 + 0.0112;
        elevaciones_187.append(nueva_elevacion_187);
        tasa_deposicion_187 += expresion_187;
    print("Tasa de deposicion acumulada del rango 1.87-1.97 es: " + str(tasa_deposicion_187))

    tasa_deposicion_197 = 0;
    elevaciones_197 = [0.45];

    for tasa_dep_197 in range(2017, 2050):
        expresion_197 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_197[-1];
        nueva_elevacion_197 = elevaciones_197[-1] - expresion_197 + 0.0121875;
        elevaciones_197.append(nueva_elevacion_197);
        tasa_deposicion_197 += expresion_197;

    for tasa_dep_197 in range(2050, 2100):
        expresion_197 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_197[-1];
        nueva_elevacion_197 = elevaciones_197[-1] - expresion_197 + 0.0112;
        elevaciones_197.append(nueva_elevacion_197);
        tasa_deposicion_197 += expresion_197;
    print("Tasa de deposicion acumulada del rango 1.97-2.07 es: "+ str(tasa_deposicion_197))

    tasa_deposicion_207 = 0;
    elevaciones_207 = [0.35];

    for tasa_dep_207 in range(2017, 2050):
        expresion_207 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_207[-1];
        nueva_elevacion_207 = elevaciones_207[-1] - expresion_207 + 0.0121875;
        elevaciones_207.append(nueva_elevacion_207);
        tasa_deposicion_207 += expresion_207;

    for tasa_dep_207 in range(2050, 2100):
        expresion_207 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_207[-1];
        nueva_elevacion_207 = elevaciones_207[-1] - expresion_207 + 0.0112;
        elevaciones_207.append(nueva_elevacion_207);
        tasa_deposicion_207 += expresion_207;
    print("Tasa de deposicion acumulada del rango 2.07-2.17 es: " + str(tasa_deposicion_207))

    tasa_deposicion_217 = 0;
    elevaciones_217 = [0.25];

    for tasa_dep_217 in range(2017, 2050):
        expresion_217 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_217[-1];
        nueva_elevacion_217 = elevaciones_217[-1] - expresion_217 + 0.0121875;
        elevaciones_217.append(nueva_elevacion_217);
        tasa_deposicion_217 += expresion_217;

    for tasa_dep_217 in range(2050, 2100):
        expresion_217 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_217[-1];
        nueva_elevacion_217 = elevaciones_217[-1] - expresion_217 + 0.0112;
        elevaciones_217.append(nueva_elevacion_217);
        tasa_deposicion_217 += expresion_217;
    print("Tasa de deposicion acumulada del rango 2.17-2.27 es: " + str(tasa_deposicion_217))

    tasa_deposicion_227 = 0;
    elevaciones_227 = [0.15];

    for tasa_dep_227 in range(2017, 2050):
        expresion_227 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_227[-1];
        nueva_elevacion_227 = elevaciones_227[-1] - expresion_227 + 0.0121875;
        elevaciones_227.append(nueva_elevacion_227);
        tasa_deposicion_227 += expresion_227;

    for tasa_dep_227 in range(2050, 2100):
        expresion_227 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_227[-1];
        nueva_elevacion_227 = elevaciones_227[-1] - expresion_227 + 0.0112;
        elevaciones_227.append(nueva_elevacion_227);
        tasa_deposicion_227 += expresion_227;
    print("Tasa de deposicion acumulada del rango 2.27-2.37 es: " + str(tasa_deposicion_227))

    tasa_deposicion_237 = 0;
    elevaciones_237 = [0.05];

    for tasa_dep_237 in range(2017, 2050):
        expresion_237 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_237[-1];
        nueva_elevacion_237 = elevaciones_237[-1] - expresion_237 + 0.0121875;
        elevaciones_237.append(nueva_elevacion_237);
        tasa_deposicion_237 += expresion_237;

    for tasa_dep_237 in range(2050, 2100):
        expresion_237 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_237[-1];
        nueva_elevacion_237 = elevaciones_237[-1] - expresion_237 + 0.0112;
        elevaciones_237.append(nueva_elevacion_237);
        tasa_deposicion_237 += expresion_237;
    print("Tasa de deposicion acumulada del rango 2.37-2.47 es: " + str(tasa_deposicion_237))

    #Reclasificamos el raster con los datos de la tasa de deposicion, por rangos, para representar la tasa de deposicion (aumento de
    # la elevacion en mm para el año 2100 en la zona de estudio para el escenario RCP4.5 y el año 2100:
    deposicion_RCP45_2100 = Reclassify(raster_Marisma, "VALUE", RemapRange([[-10000, 870,"NODATA"],[870, 970, round(tasa_deposicion_087*1000)],
                                 [970, 1070, round(tasa_deposicion_097*1000)], [1070, 1170, round(tasa_deposicion_107*1000)], [1170, 1270, round(tasa_deposicion_117*1000)],
                                 [1270, 1370, round(tasa_deposicion_127*1000)], [1370, 1470, round(tasa_deposicion_137*1000)], [1470, 1570, round(tasa_deposicion_147*1000)],
                                 [1570, 1670, round(tasa_deposicion_157*1000)], [1670, 1770, round(tasa_deposicion_167*1000)], [1770, 1870, round(tasa_deposicion_177*1000)],
                                 [1870, 1970, round(tasa_deposicion_187*1000)], [1970, 2070, round(tasa_deposicion_197*1000)], [2070, 2170, round(tasa_deposicion_207*1000)],
                                 [2170, 2270, round(tasa_deposicion_217*1000)], [2270, 2370, round(tasa_deposicion_227*1000)], [2370, 2470, round(tasa_deposicion_237*1000)],
                                                                           [2470, 1000000, "NODATA"]]))
    deposicion_RCP45_2100.save(r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\ServiciosEcosistemicosUrdaibai.Overviews\SEU_prueba.gdb\Deposicion_RCP45_2100")
    direcc_depo_RCP45_2100 = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\ServiciosEcosistemicosUrdaibai.Overviews\SEU_prueba.gdb\Deposicion_RCP45_2100"

    #Ahora ya tenemos el raster con la deposicion que habra en la zona de estudio segun el escenario RCP4.5 y para el año 2100,
    #asumiendo que desde el limite inferior hasta el superior donde se encuentran las marismas de Urdaibai de acuerdo a distintos
    #estudios, son las potenciales zonas de las marismas (aunque en realidad no haya por distintos factores y suponiendo que serían
    #marismas consolidadas con unas tasas de deposicion acorde a su elevacion.

    #Pues bien, sumamos los dos rasteres (elevacion en mm y deposicion en mm) para obtener la nueva altura que tendra la marisma.
    elevacion_RCP45_2100 = RasterCalculator([raster_Marisma, direcc_depo_RCP45_2100], ["marisma", "depo"],
                                            "(marisma+depo)")
    elevacion_RCP45_2100.save(
       r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\ServiciosEcosistemicosUrdaibai.Overviews\SEU_prueba.gdb\Elevacion_RCP45_2100")
    direc_elevacion_RCP45_2100 = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\ServiciosEcosistemicosUrdaibai.Overviews\SEU_prueba.gdb\Elevacion_RCP45_2100"

    #Una vez que tenemos la elevacion nueva de la zona de estudio debido a la deposicion fusionamos los rasteres de la nueva
    #elevacion de la marisma con el raster de elevaciones original para que tenga las nuevas elevaciones y tenga en cuenta los
    #valores del raster original en las zonas donde no hay marisma (y asi no ponga "NODATA").
    comb_elevacion_RCP45_2100 = arcpy.management.MosaicToNewRaster([direc_elevacion_RCP45_2100, raster_Marisma], r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\ServiciosEcosistemicosUrdaibai.Overviews\SEU_prueba.gdb",
                                    "Elevacion_Combi_Terreno_RCP45_2100", 25830, "32_BIT_FLOAT", 1, 1, "FIRST")

    #Ya tenemos el la elevacion que habra en la zona de estudio en 2050 segun el escenario RCP4.5, ahora volvemos a reclasificar dicho
    #raster para obtener la potencial distribucion de la marisma en dicho escenario y año:
    pot_distribucion_RCP45_2100 = Reclassify(comb_elevacion_RCP45_2100, "VALUE", RemapRange([[-100000,1820,"NODATA"], [1820,3420,0],[3420, 1000000,"NODATA"]]))
    pot_distribucion_RCP45_2100.save(r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\ServiciosEcosistemicosUrdaibai.Overviews\SEU_prueba.gdb\Pot_Distribucion_RCP45_2100")

if choice == "RCP8.5_2100":
    #Variable que almacena la elevación que tendrá la marisma en ese rango para el año especificado:
    tasa_deposicion_087 = 0;
    #Variable que almacena la profundidad de la zona de la marisma respecto al límite superior de la marisma (highest astronomical
    #tide):
    elevaciones_087 = [1.55];

    #Ahora hacemos un bucle para iterar las variaciones de la tasa de deposición por la diferencia entre el aumento del nivel
    #del mar y la tasa de deposicion para el rango de elevaciones [0.87-0.97]:
    for tasa_dep_087 in range(2017,2050):
        expresion_087 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_087[-1];
        nueva_elevacion_087 = elevaciones_087[-1] - expresion_087 + 0.0134375;
        elevaciones_087.append(nueva_elevacion_087);
        tasa_deposicion_087+= expresion_087;

    for tasa_dep_087 in range(2050,2100):
        expresion_087 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_087[-1];
        nueva_elevacion_087 = elevaciones_087[-1] - expresion_087 + 0.0148;
        elevaciones_087.append(nueva_elevacion_087);
        tasa_deposicion_087+= expresion_087;
    print("Tasa de deposición acumulada del rango 0.87-0.97 es: " + str(tasa_deposicion_087))

    #Volvemos a calcular las tasas de deposiciones pero ahora para todos los rangos de valores (desde 0.87 hasta 2.47 metros, cada
    #10 centimetros):
    tasa_deposicion_097 = 0;
    elevaciones_097 = [1.45];

    for tasa_dep_097 in range(2017,2050):
        expresion_097 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_097[-1];
        nueva_elevacion_097 = elevaciones_097[-1] - expresion_097 + 0.0134375;
        elevaciones_097.append(nueva_elevacion_097);
        tasa_deposicion_097+= expresion_097;

    for tasa_dep_097 in range(2050,2100):
        expresion_097 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_097[-1];
        nueva_elevacion_097 = elevaciones_097[-1] - expresion_097 + 0.0148;
        elevaciones_097.append(nueva_elevacion_097);
        tasa_deposicion_097+= expresion_097;
    print("Tasa de deposición acumulada del rango 0.97-1.07 es: " + str(tasa_deposicion_097))

    tasa_deposicion_107 = 0;
    elevaciones_107 = [1.35];

    for tasa_dep_107 in range(2017, 2050):
        expresion_107 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_107[-1];
        nueva_elevacion_107 = elevaciones_107[-1] - expresion_107 + 0.0134375;
        elevaciones_107.append(nueva_elevacion_107);
        tasa_deposicion_107 += expresion_107;

    for tasa_dep_107 in range(2050, 2100):
        expresion_107 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_107[-1];
        nueva_elevacion_107 = elevaciones_107[-1] - expresion_107 + 0.0148;
        elevaciones_107.append(nueva_elevacion_107);
        tasa_deposicion_107 += expresion_107;
    print("Tasa de deposicion acumulada del rango 1.07-1.17 es: " + str(tasa_deposicion_107))

    tasa_deposicion_117 = 0;
    elevaciones_117 = [1.25];

    for tasa_dep_117 in range(2017, 2050):
        expresion_117 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_117[-1];
        nueva_elevacion_117 = elevaciones_117[-1] - expresion_117 + 0.0134375;
        elevaciones_117.append(nueva_elevacion_117);
        tasa_deposicion_117 += expresion_117;

    for tasa_dep_117 in range(2050, 2100):
        expresion_117 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_117[-1];
        nueva_elevacion_117 = elevaciones_117[-1] - expresion_117 + 0.0148;
        elevaciones_117.append(nueva_elevacion_117);
        tasa_deposicion_117 += expresion_117;
    print("Tasa de deposicion acumulada del rango 1.17-1.27 es: " + str(tasa_deposicion_117))

    tasa_deposicion_127 = 0;
    elevaciones_127 = [1.15];

    for tasa_dep_127 in range(2017, 2050):
        expresion_127 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_127[-1];
        nueva_elevacion_127 = elevaciones_127[-1] - expresion_127 + 0.0134375;
        elevaciones_127.append(nueva_elevacion_127);
        tasa_deposicion_127 += expresion_127;

    for tasa_dep_127 in range(2050, 2100):
        expresion_127 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_127[-1];
        nueva_elevacion_127 = elevaciones_127[-1] - expresion_127 + 0.0148;
        elevaciones_127.append(nueva_elevacion_127);
        tasa_deposicion_127 += expresion_127;
    print("Tasa de deposicion acumulada del rango 1.27-1.37 es: " + str(tasa_deposicion_127))

    tasa_deposicion_137 = 0;
    elevaciones_137 = [1.05];

    for tasa_dep_137 in range(2017, 2050):
        expresion_137 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_137[-1];
        nueva_elevacion_137 = elevaciones_137[-1] - expresion_137 + 0.0134375;
        elevaciones_137.append(nueva_elevacion_137);
        tasa_deposicion_137 += expresion_137;

    for tasa_dep_137 in range(2050, 2100):
        expresion_137 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_137[-1];
        nueva_elevacion_137 = elevaciones_137[-1] - expresion_137 + 0.0148;
        elevaciones_137.append(nueva_elevacion_137);
        tasa_deposicion_137 += expresion_137;
    print("Tasa de deposicion acumulada del rango 1.37-1.47 es: " + str(tasa_deposicion_137))

    tasa_deposicion_147 = 0;
    elevaciones_147 = [0.95];

    for tasa_dep_147 in range(2017, 2050):
        expresion_147 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_147[-1];
        nueva_elevacion_147 = elevaciones_147[-1] - expresion_147 + 0.0134375;
        elevaciones_147.append(nueva_elevacion_147);
        tasa_deposicion_147 += expresion_147;

    for tasa_dep_147 in range(2050, 2100):
        expresion_147 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_147[-1];
        nueva_elevacion_147 = elevaciones_147[-1] - expresion_147 + 0.0148;
        elevaciones_147.append(nueva_elevacion_147);
        tasa_deposicion_147 += expresion_147;
    print("Tasa de deposicion acumulada del rango 1.47-1.57 es: " + str(tasa_deposicion_147))

    tasa_deposicion_157 = 0;
    elevaciones_157 = [0.85];

    for tasa_dep_157 in range(2017, 2050):
        expresion_157 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_157[-1];
        nueva_elevacion_157 = elevaciones_157[-1] - expresion_157 + 0.0134375;
        elevaciones_157.append(nueva_elevacion_157);
        tasa_deposicion_157 += expresion_157;

    for tasa_dep_157 in range(2050, 2100):
        expresion_157 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_157[-1];
        nueva_elevacion_157 = elevaciones_157[-1] - expresion_157 + 0.0148;
        elevaciones_157.append(nueva_elevacion_157);
        tasa_deposicion_157 += expresion_157;
    print("Tasa de deposicion acumulada del rango 1.57-1.67 es: " + str(tasa_deposicion_157))

    tasa_deposicion_167 = 0;
    elevaciones_167 = [0.75];

    for tasa_dep_167 in range(2017, 2050):
        expresion_167 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_167[-1];
        nueva_elevacion_167 = elevaciones_167[-1] - expresion_167 + 0.0134375;
        elevaciones_167.append(nueva_elevacion_167);
        tasa_deposicion_167 += expresion_167;

    for tasa_dep_167 in range(2050, 2100):
        expresion_167 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_167[-1];
        nueva_elevacion_167 = elevaciones_167[-1] - expresion_167 + 0.0148;
        elevaciones_167.append(nueva_elevacion_167);
        tasa_deposicion_167 += expresion_167;
    print("Tasa de deposicion acumulada del rango 1.67-1.77 es: " + str(tasa_deposicion_167))

    tasa_deposicion_177 = 0;
    elevaciones_177 = [0.65];

    for tasa_dep_177 in range(2017, 2050):
        expresion_177 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_177[-1];
        nueva_elevacion_177 = elevaciones_177[-1] - expresion_177 + 0.0134375;
        elevaciones_177.append(nueva_elevacion_177);
        tasa_deposicion_177 += expresion_177;

    for tasa_dep_177 in range(2050, 2100):
        expresion_177 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_177[-1];
        nueva_elevacion_177 = elevaciones_177[-1] - expresion_177 + 0.0148;
        elevaciones_177.append(nueva_elevacion_177);
        tasa_deposicion_177 += expresion_177;
    print("Tasa de deposicion acumulada del rango 1.77-1.87 es: " + str(tasa_deposicion_177))

    tasa_deposicion_187 = 0;
    elevaciones_187 = [0.55];

    for tasa_dep_187 in range(2017, 2050):
        expresion_187 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_187[-1];
        nueva_elevacion_187 = elevaciones_187[-1] - expresion_187 + 0.0134375;
        elevaciones_187.append(nueva_elevacion_187);
        tasa_deposicion_187 += expresion_187;

    for tasa_dep_187 in range(2050, 2100):
        expresion_187 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_187[-1];
        nueva_elevacion_187 = elevaciones_187[-1] - expresion_187 + 0.0148;
        elevaciones_187.append(nueva_elevacion_187);
        tasa_deposicion_187 += expresion_187;
    print("Tasa de deposicion acumulada del rango 1.87-1.97 es: " + str(tasa_deposicion_187))

    tasa_deposicion_197 = 0;
    elevaciones_197 = [0.45];

    for tasa_dep_197 in range(2017, 2050):
        expresion_197 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_197[-1];
        nueva_elevacion_197 = elevaciones_197[-1] - expresion_197 + 0.0134375;
        elevaciones_197.append(nueva_elevacion_197);
        tasa_deposicion_197 += expresion_197;

    for tasa_dep_197 in range(2050, 2100):
        expresion_197 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_197[-1];
        nueva_elevacion_197 = elevaciones_197[-1] - expresion_197 + 0.0148;
        elevaciones_197.append(nueva_elevacion_197);
        tasa_deposicion_197 += expresion_197;
    print("Tasa de deposicion acumulada del rango 1.97-2.07 es: "+ str(tasa_deposicion_197))

    tasa_deposicion_207 = 0;
    elevaciones_207 = [0.35];

    for tasa_dep_207 in range(2017, 2050):
        expresion_207 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_207[-1];
        nueva_elevacion_207 = elevaciones_207[-1] - expresion_207 + 0.0134375;
        elevaciones_207.append(nueva_elevacion_207);
        tasa_deposicion_207 += expresion_207;

    for tasa_dep_207 in range(2050, 2100):
        expresion_207 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_207[-1];
        nueva_elevacion_207 = elevaciones_207[-1] - expresion_207 + 0.0148;
        elevaciones_207.append(nueva_elevacion_207);
        tasa_deposicion_207 += expresion_207;
    print("Tasa de deposicion acumulada del rango 2.07-2.17 es: " + str(tasa_deposicion_207))

    tasa_deposicion_217 = 0;
    elevaciones_217 = [0.25];

    for tasa_dep_217 in range(2017, 2050):
        expresion_217 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_217[-1];
        nueva_elevacion_217 = elevaciones_217[-1] - expresion_217 + 0.0134375;
        elevaciones_217.append(nueva_elevacion_217);
        tasa_deposicion_217 += expresion_217;

    for tasa_dep_217 in range(2050, 2100):
        expresion_217 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_217[-1];
        nueva_elevacion_217 = elevaciones_217[-1] - expresion_217 + 0.0148;
        elevaciones_217.append(nueva_elevacion_217);
        tasa_deposicion_217 += expresion_217;
    print("Tasa de deposicion acumulada del rango 2.17-2.27 es: " + str(tasa_deposicion_217))

    tasa_deposicion_227 = 0;
    elevaciones_227 = [0.15];

    for tasa_dep_227 in range(2017, 2050):
        expresion_227 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_227[-1];
        nueva_elevacion_227 = elevaciones_227[-1] - expresion_227 + 0.0134375;
        elevaciones_227.append(nueva_elevacion_227);
        tasa_deposicion_227 += expresion_227;

    for tasa_dep_227 in range(2050, 2100):
        expresion_227 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_227[-1];
        nueva_elevacion_227 = elevaciones_227[-1] - expresion_227 + 0.0148;
        elevaciones_227.append(nueva_elevacion_227);
        tasa_deposicion_227 += expresion_227;
    print("Tasa de deposicion acumulada del rango 2.27-2.37 es: " + str(tasa_deposicion_227))

    tasa_deposicion_237 = 0;
    elevaciones_237 = [0.05];

    for tasa_dep_237 in range(2017, 2050):
        expresion_237 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_237[-1];
        nueva_elevacion_237 = elevaciones_237[-1] - expresion_237 + 0.0134375;
        elevaciones_237.append(nueva_elevacion_237);
        tasa_deposicion_237 += expresion_237;

    for tasa_dep_237 in range(2050, 2100):
        expresion_237 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_237[-1];
        nueva_elevacion_237 = elevaciones_237[-1] - expresion_237 + 0.0148;
        elevaciones_237.append(nueva_elevacion_237);
        tasa_deposicion_237 += expresion_237;
    print("Tasa de deposicion acumulada del rango 2.37-2.47 es: " + str(tasa_deposicion_237))

    #Reclasificamos el raster con los datos de la tasa de deposicion, por rangos, para representar la tasa de deposicion (aumento de
    # la elevacion en mm para el año 2050 en la zona de estudio para el escenario RCP8.5 y el año 2100:
    deposicion_RCP85_2100 = Reclassify(raster_Marisma, "VALUE", RemapRange([[-10000, 870,"NODATA"],[870, 970, round(tasa_deposicion_087*1000)],
                                 [970, 1070, round(tasa_deposicion_097*1000)], [1070, 1170, round(tasa_deposicion_107*1000)], [1170, 1270, round(tasa_deposicion_117*1000)],
                                 [1270, 1370, round(tasa_deposicion_127*1000)], [1370, 1470, round(tasa_deposicion_137*1000)], [1470, 1570, round(tasa_deposicion_147*1000)],
                                 [1570, 1670, round(tasa_deposicion_157*1000)], [1670, 1770, round(tasa_deposicion_167*1000)], [1770, 1870, round(tasa_deposicion_177*1000)],
                                 [1870, 1970, round(tasa_deposicion_187*1000)], [1970, 2070, round(tasa_deposicion_197*1000)], [2070, 2170, round(tasa_deposicion_207*1000)],
                                 [2170, 2270, round(tasa_deposicion_217*1000)], [2270, 2370, round(tasa_deposicion_227*1000)], [2370, 2470, round(tasa_deposicion_237*1000)],
                                                                           [2470, 1000000, "NODATA"]]))
    deposicion_RCP85_2100.save(r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\ServiciosEcosistemicosUrdaibai.Overviews\SEU_prueba.gdb\Deposicion_RCP85_2100")
    direcc_depo_RCP85_2100 = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\ServiciosEcosistemicosUrdaibai.Overviews\SEU_prueba.gdb\Deposicion_RCP85_2100"

    #Ahora ya tenemos el raster con la deposicion que habra en la zona de estudio segun el escenario RCP8.5 y para el año 2100,
    #asumiendo que desde el limite inferior hasta el superior donde se encuentran las marismas de Urdaibai de acuerdo a distintos
    #estudios, son las potenciales zonas de las marismas (aunque en realidad no haya por distintos factores y suponiendo que serían
    #marismas consolidadas con unas tasas de deposicion acorde a su elevacion.

    #Pues bien, sumamos los dos rasteres (elevacion en mm y deposicion en mm) para obtener la nueva altura que tendra la marisma.
    elevacion_RCP85_2100 = RasterCalculator([raster_Marisma, direcc_depo_RCP85_2100], ["marisma", "depo"],
                                            "(marisma+depo)")
    elevacion_RCP85_2100.save(
       r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\ServiciosEcosistemicosUrdaibai.Overviews\SEU_prueba.gdb\Elevacion_RCP85_2100")
    direc_elevacion_RCP85_2100 = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\ServiciosEcosistemicosUrdaibai.Overviews\SEU_prueba.gdb\Elevacion_RCP85_2100"

    #Una vez que tenemos la elevacion nueva de la zona de estudio debido a la deposicion fusionamos los rasteres de la nueva
    #elevacion de la marisma con el raster de elevaciones original para que tenga las nuevas elevaciones y tenga en cuenta los
    #valores del raster original en las zonas donde no hay marisma (y asi no ponga "NODATA").
    comb_elevacion_RCP85_2100 = arcpy.management.MosaicToNewRaster([direc_elevacion_RCP85_2100, raster_Marisma], r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\ServiciosEcosistemicosUrdaibai.Overviews\SEU_prueba.gdb",
                                    "Elevacion_Combi_Terreno_RCP85_2100", 25830, "32_BIT_FLOAT", 1, 1, "FIRST")

    #Ya tenemos la elevacion que habra en la zona de estudio en 2100 segun el escenario RCP8.5, ahora volvemos a reclasificar dicho
    #raster para obtener la potencial distribucion de la marisma en dicho escenario y año:
    pot_distribucion_RCP85_2100 = Reclassify(comb_elevacion_RCP85_2100, "VALUE", RemapRange([[-100000,2040,"NODATA"], [2040,3640,0],[3640, 1000000,"NODATA"]]))
    pot_distribucion_RCP85_2100.save(r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\ServiciosEcosistemicosUrdaibai.Overviews\SEU_prueba.gdb\Pot_Distribucion_RCP85_2100")