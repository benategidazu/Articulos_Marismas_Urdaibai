# Hacemos una prueba del modelo que tiene en cuenta la variacion elevacion-SLR al año

# Importamos los modulos necesarios
import arcpy
from arcpy import env
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")

env.overwriteOutput=True;
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(25830)

# Introducimos el ráster de elevacíon necesario para establecer la zonación de la marisma:
raster_Marisma = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Raster_marisma_natural"
raster_zonas_cultivo = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Raster_campos_inundables_SLR";
raster_marisma_regeneracion = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Raster_marisma_regenerandose";
raster_marisma_reclamada_errota = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Raster_marismas_reclamadas";

# Pedimos al usuario que introduzca el límite mínimo donde empieza la marisma y el límite máximo (en nuestro caso el mínimo es 0,87 por ser la elevación donde empieza a habitar Spartina):
#limite_inferior_marisma = 0,87
#limite_superior_marisma = 2,47

#Pedimos al usuario que introduzca el valor de la concentración de sedimento en gramos por metro cubico:
concentracion = input("Introduce la concentracion de sedimento: ")

#Pedimos al usuario que introduzca el valor de la produccion de biomasa en gramos por metro cuadrado y año:
produccion_biomasa = input("Introduce la produccion de biomasa: ")

#Pedimos al usuario el escenario y fecha que quiere reproyectar:
choice = input("Introduce el escenario que quiere conocer: ")

#Tasas de aumento del nivel del mar estimadas para los años 2050 y 2100 según los escenarios RCP4.5 y RCP8.5 obtenidas a partir
#del Modelo Browniano Geometrico (GBM) con base de referencia en el año 2000 y atendiendo al percentil 95 de la distribucion de
#probabilidades:
tasa_SLR_RCP45_2000_2050 = 0.0078;
tasa_SLR_RCP45_2050_2100 = 0.0112;
tasa_SLR_RCP85_2000_2050 = 0.0086;
tasa_SLR_RCP85_2050_2100 = 0.0148;

deposicion_marisma_regeneracion = 0.016;

if choice == "RCP4.5_2050":

    #Tasas de deposición para marismas naturales:
    #Variable que almacena la elevación que tendrá la marisma en ese rango para el año especificado:
    tasa_deposicion_087 = 0;
    #Variable que almacena la profundidad de la zona de la marisma respecto al límite superior de la marisma (highest astronomical
    #tide). Estamos cogiendo la media del rango de elevaciones, es decir, si el rango es entre 0.87 y 0.97, cogemos que su elevacion
    # es 0.92 metros:
    elevaciones_087 = [1.55];

    #Ahora hacemos un bucle para iterar las variaciones de la tasa de deposición por la diferencia entre el aumento del nivel
    #del mar y la tasa de deposicion para el rango de elevaciones [0.87-0.97]:
    for tasa_dep_087 in range(2017,2050):
        expresion_087 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_087[-1];
        nueva_elevacion_087 = elevaciones_087[-1] - expresion_087 + tasa_SLR_RCP45_2000_2050;
        elevaciones_087.append(nueva_elevacion_087);
        tasa_deposicion_087+= expresion_087;
    print("Tasa de deposición acumulada del rango 0.87-0.97 es: " + str(tasa_deposicion_087))

    #Volvemos a calcular las tasas de deposiciones pero ahora para todos los rangos de valores (desde 0.87 hasta 2.47 metros, cada
    #10 centimetros):
    tasa_deposicion_097 = 0;
    elevaciones_097 = [1.45];

    for tasa_dep_097 in range(2017,2050):
        expresion_097 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_097[-1];
        nueva_elevacion_097 = elevaciones_097[-1] - expresion_097 + tasa_SLR_RCP45_2000_2050;
        elevaciones_097.append(nueva_elevacion_097);
        tasa_deposicion_097+= expresion_097;
    print("Tasa de deposición acumulada del rango 0.97-1.07 es: " + str(tasa_deposicion_097))

    tasa_deposicion_107 = 0;
    elevaciones_107 = [1.35];

    for tasa_dep_107 in range(2017, 2050):
        expresion_107 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_107[-1];
        nueva_elevacion_107 = elevaciones_107[-1] - expresion_107 + tasa_SLR_RCP45_2000_2050;
        elevaciones_107.append(nueva_elevacion_107);
        tasa_deposicion_107 += expresion_107;
    print("Tasa de deposicion acumulada del rango 1.07-1.17 es: " + str(tasa_deposicion_107))

    tasa_deposicion_117 = 0;
    elevaciones_117 = [1.25];

    for tasa_dep_117 in range(2017, 2050):
        expresion_117 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_117[-1];
        nueva_elevacion_117 = elevaciones_117[-1] - expresion_117 + tasa_SLR_RCP45_2000_2050;
        elevaciones_117.append(nueva_elevacion_117);
        tasa_deposicion_117 += expresion_117;
    print("Tasa de deposicion acumulada del rango 1.17-1.27 es: " + str(tasa_deposicion_117))

    tasa_deposicion_127 = 0;
    elevaciones_127 = [1.15];

    for tasa_dep_127 in range(2017, 2050):
        expresion_127 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_127[-1];
        nueva_elevacion_127 = elevaciones_127[-1] - expresion_127 + tasa_SLR_RCP45_2000_2050;
        elevaciones_127.append(nueva_elevacion_127);
        tasa_deposicion_127 += expresion_127;
    print("Tasa de deposicion acumulada del rango 1.27-1.37 es: " + str(tasa_deposicion_127))

    tasa_deposicion_137 = 0;
    elevaciones_137 = [1.05];

    for tasa_dep_137 in range(2017, 2050):
        expresion_137 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_137[-1];
        nueva_elevacion_137 = elevaciones_137[-1] - expresion_137 + tasa_SLR_RCP45_2000_2050;
        elevaciones_137.append(nueva_elevacion_137);
        tasa_deposicion_137 += expresion_137;
    print("Tasa de deposicion acumulada del rango 1.37-1.47 es: " + str(tasa_deposicion_137))

    tasa_deposicion_147 = 0;
    elevaciones_147 = [0.95];

    for tasa_dep_147 in range(2017, 2050):
        expresion_147 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_147[-1];
        nueva_elevacion_147 = elevaciones_147[-1] - expresion_147 + tasa_SLR_RCP45_2000_2050;
        elevaciones_147.append(nueva_elevacion_147);
        tasa_deposicion_147 += expresion_147;
    print("Tasa de deposicion acumulada del rango 1.47-1.57 es: " + str(tasa_deposicion_147))

    tasa_deposicion_157 = 0;
    elevaciones_157 = [0.85];

    for tasa_dep_157 in range(2017, 2050):
        expresion_157 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_157[-1];
        nueva_elevacion_157 = elevaciones_157[-1] - expresion_157 + tasa_SLR_RCP45_2000_2050;
        elevaciones_157.append(nueva_elevacion_157);
        tasa_deposicion_157 += expresion_157;
    print("Tasa de deposicion acumulada del rango 1.57-1.67 es: " + str(tasa_deposicion_157))

    tasa_deposicion_167 = 0;
    elevaciones_167 = [0.75];

    for tasa_dep_167 in range(2017, 2050):
        expresion_167 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_167[-1];
        nueva_elevacion_167 = elevaciones_167[-1] - expresion_167 + tasa_SLR_RCP45_2000_2050;
        elevaciones_167.append(nueva_elevacion_167);
        tasa_deposicion_167 += expresion_167;
    print("Tasa de deposicion acumulada del rango 1.67-1.77 es: " + str(tasa_deposicion_167))

    tasa_deposicion_177 = 0;
    elevaciones_177 = [0.65];

    for tasa_dep_177 in range(2017, 2050):
        expresion_177 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_177[-1];
        nueva_elevacion_177 = elevaciones_177[-1] - expresion_177 + tasa_SLR_RCP45_2000_2050;
        elevaciones_177.append(nueva_elevacion_177);
        tasa_deposicion_177 += expresion_177;
    print("Tasa de deposicion acumulada del rango 1.77-1.87 es: " + str(tasa_deposicion_177))

    tasa_deposicion_187 = 0;
    elevaciones_187 = [0.55];

    for tasa_dep_187 in range(2017, 2050):
        expresion_187 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_187[-1];
        nueva_elevacion_187 = elevaciones_187[-1] - expresion_187 + tasa_SLR_RCP45_2000_2050;
        elevaciones_187.append(nueva_elevacion_187);
        tasa_deposicion_187 += expresion_187;
    print("Tasa de deposicion acumulada del rango 1.87-1.97 es: " + str(tasa_deposicion_187))

    tasa_deposicion_197 = 0;
    elevaciones_197 = [0.45];

    for tasa_dep_197 in range(2017, 2050):
        expresion_197 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_197[-1];
        nueva_elevacion_197 = elevaciones_197[-1] - expresion_197 + tasa_SLR_RCP45_2000_2050;
        elevaciones_197.append(nueva_elevacion_197);
        tasa_deposicion_197 += expresion_197;
    print("Tasa de deposicion acumulada del rango 1.97-2.07 es: "+ str(tasa_deposicion_197))

    tasa_deposicion_207 = 0;
    elevaciones_207 = [0.35];

    for tasa_dep_207 in range(2017, 2050):
        expresion_207 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_207[-1];
        nueva_elevacion_207 = elevaciones_207[-1] - expresion_207 + tasa_SLR_RCP45_2000_2050;
        elevaciones_207.append(nueva_elevacion_207);
        tasa_deposicion_207 += expresion_207;
    print("Tasa de deposicion acumulada del rango 2.07-2.17 es: " + str(tasa_deposicion_207))

    tasa_deposicion_217 = 0;
    elevaciones_217 = [0.25];

    for tasa_dep_217 in range(2017, 2050):
        expresion_217 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_217[-1];
        nueva_elevacion_217 = elevaciones_217[-1] - expresion_217 + tasa_SLR_RCP45_2000_2050;
        elevaciones_217.append(nueva_elevacion_217);
        tasa_deposicion_217 += expresion_217;
    print("Tasa de deposicion acumulada del rango 2.17-2.27 es: " + str(tasa_deposicion_217))

    tasa_deposicion_227 = 0;
    elevaciones_227 = [0.15];

    for tasa_dep_227 in range(2017, 2050):
        expresion_227 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_227[-1];
        nueva_elevacion_227 = elevaciones_227[-1] - expresion_227 + tasa_SLR_RCP45_2000_2050;
        elevaciones_227.append(nueva_elevacion_227);
        tasa_deposicion_227 += expresion_227;
    print("Tasa de deposicion acumulada del rango 2.27-2.37 es: " + str(tasa_deposicion_227))

    tasa_deposicion_237 = 0;
    elevaciones_237 = [0.05];

    for tasa_dep_237 in range(2017, 2050):
        expresion_237 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_237[-1];
        nueva_elevacion_237 = elevaciones_237[-1] - expresion_237 + tasa_SLR_RCP45_2000_2050;
        elevaciones_237.append(nueva_elevacion_237);
        tasa_deposicion_237 += expresion_237;
    print("Tasa de deposicion acumulada del rango 2.37-2.47 es: " + str(tasa_deposicion_237))

    #Ahora calculamos la tasa de deposición de las elevaciones inundables superiores al límite superior de la marisma,
    #teniendo en cuenta que la deposición comienza cuando se inunde todo el rango, es decir, cuando se inunde la elevación
    #2,57 metros empezará la deposicion en todo el rango. Asi pues, tiene en cuenta que la deposicion se dara de manera
    #instantanea, no cuando la vegetacion terrestre sea 'cambiada' por vegetacion halofita.
    depo_247 = 0;
    elevaciones_247 = [0.0514];

    for deposicion_247 in range(2030, 2050):
        expr_247 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_247[-1];
        nueva_elevacion_247 = elevaciones_247[-1] - expr_247 + tasa_SLR_RCP45_2000_2050;
        elevaciones_247.append(nueva_elevacion_247);
        depo_247 += expr_247;
    print("Tasa de deposicion acumulada del rango 2.47-2.57 es: " + str(depo_247))

    #Tasa deposicion marismas en regeneracion:
    deposicion_marisma_regeneracion = 0.016;

    depo_257 = 0;
    elevaciones_257 = [0.0528];

    for deposicion_257 in range(2043, 2050):
        expr_257 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_257[-1];
        nueva_elevacion_257 = elevaciones_257[-1] - expr_257 + tasa_SLR_RCP45_2000_2050;
        elevaciones_257.append(nueva_elevacion_257);
        depo_257 += expr_257;
    print("Tasa de deposicion acumulada del rango 2.57-2.67 es: " + str(depo_257))

    #Ahora tratamos las marismas en regeneracion. En este caso, la elevacion mas frecuente de las marismas colindantes es de 2,2 metros
    #por lo que las marismas en regeneracion tendran una tasa de acrecion de 16mm por año hasta igualar dicha elevacion. No se tiene
    #en cuenta lo que aumenta la marisma natural colindante en el periodo en que las que estan en regeneracion alcanzan 2,2 metros
    #porque no hay datos suficientemente fiables de la productividad de las especies de esa zona de marisma y concentracion de sedimento.
    deposicion_087_167 = 0;
    for dep_087_167 in range(2017,2050):
        expr_087_167 = deposicion_marisma_regeneracion
        deposicion_087_167 += expr_087_167;
    print("La deposición acumulada del rango 0.87-1.67 de la marisma en regeneracion es:" + str(deposicion_087_167))

    deposicion_167_177 = 0;
    elev_regen_167 = [0.504];  # Diferencia entre el nivel de marea alta (2.47) mas el SLR para ese año y la elevacion del
    # rango mas la deposicion hasta que llegue a los 2,2 metros aprox.
    for dep_167_177 in range(2017, 2047):
        deposicion_167_177 += deposicion_marisma_regeneracion
    for dep_167_177 in range(2047, 2050):
        expresion_167_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_167[
            -1];
        nueva_ele_167 = elev_regen_167[-1] - expresion_167_bis + tasa_SLR_RCP45_2000_2050;
        elev_regen_167.append(nueva_ele_167);
        deposicion_167_177 += expresion_167_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 1.67-1.77 es:" + str(deposicion_167_177));

    deposicion_177_187 = 0;
    elev_regen_177 = [0.453];  # Diferencia entre el nivel de marea alta (2.47) mas el SLR para ese año y la elevacion del
    # rango mas la deposicion hasta que llegue a los 2,2 metros aprox.
    for dep_177_187 in range(2017, 2041):
        deposicion_177_187 += deposicion_marisma_regeneracion
    for dep_177_187 in range(2041, 2050):
        expresion_177_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_177[-1];
        nueva_ele_177 = elev_regen_177[-1] - expresion_177_bis + tasa_SLR_RCP45_2000_2050;
        elev_regen_177.append(nueva_ele_177);
        deposicion_177_187 += expresion_177_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 1.77-1.87 es:" + str(deposicion_177_187));

    deposicion_187_197 = 0;
    elev_regen_187 = [0.402];  # Diferencia entre el nivel de marea alta (2.47) mas el SLR para ese año y la elevacion del
    # rango mas la deposicion hasta que llegue a los 2,2 metros aprox.
    for dep_187_197 in range(2017, 2035):
        deposicion_187_197 += deposicion_marisma_regeneracion
    for dep_187_197 in range(2035, 2050):
        expresion_187_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_187[-1];
        nueva_ele_187 = elev_regen_187[-1] - expresion_187_bis + tasa_SLR_RCP45_2000_2050;
        elev_regen_187.append(nueva_ele_187);
        deposicion_187_197 += expresion_187_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 1.87-1.97 es:" + str(deposicion_187_197));

    deposicion_197_207 = 0;
    elev_regen_197 = [0.351];  # Diferencia entre el nivel de marea alta (2.47) mas el SLR para ese año y la elevacion del
    # rango mas la deposicion hasta que llegue a los 2,2 metros aprox.
    for dep_197_207 in range(2017, 2029):
        deposicion_197_207 += deposicion_marisma_regeneracion
    for dep_197_207 in range(2029, 2050):
        expresion_197_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_197[-1];
        nueva_ele_197 = elev_regen_197[-1] - expresion_197_bis + tasa_SLR_RCP45_2000_2050;
        elev_regen_197.append(nueva_ele_197);
        deposicion_197_207 += expresion_197_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 1.97-2.07 es:" + str(deposicion_197_207));

    deposicion_207_217 = 0;
    elev_regen_207 = [0.300];  # Diferencia entre el nivel de marea alta (2.47) mas el SLR para ese año y la elevacion del
    # rango mas la deposicion hasta que llegue a los 2,2 metros aprox.
    for dep_207_217 in range(2017, 2023):
        deposicion_207_217 += deposicion_marisma_regeneracion
    for dep_207_217 in range(2023, 2050):
        expresion_207_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_207[-1];
        nueva_ele_207 = elev_regen_207[-1] - expresion_207_bis + tasa_SLR_RCP45_2000_2050;
        elev_regen_207.append(nueva_ele_207);
        deposicion_207_217 += expresion_207_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 2.07-2.17 es:" + str(deposicion_207_217));

    #A partir de 2,17 metros hasta 2,47 tendran un comportamiento de marisma natural.
    #A partir de 2,47 metros hasta 2,727 metros seran tratados como zonas inundables con el SLR.

    #Ahora calculamos la deposicion que tendran las marismas reclamadas que no se inundan por la presencia de una barrera (natural o artificial)
    #que impide el flujo de agua de mar por su mayor altura (mas de 2,47). Obteniendo la elevacion mas frecuente mediante un histograma del raster
    #que da informacion a cerca de la elevacion de la barrera, se ha obtenido una elevacion de 2,6 metros (2'5-2'7), por lo que ahora, se calcula
    #cuando el SLR, en este caso referido al escenario RCP4.5 proyectado a 2050. Se obtiene que se inundara el año 2034, por lo que se aplicara una
    #acrecion de 16 mm por año (marisma en regeneracion) hasta que iguale su elevacion con la marisma colindante, que en este caso esta aproximadamente
    #a 2 metros de altura.Una vez que alcance esos 2 metros se aplica una tasa de acrecion de marisma natural y si esta a mas de 2,47 metros, una
    #deposicion igual a las zonas inundables por el SLR.

    #El rango 0.87-0.97m se ha descartado del calculo porque en 17 años, cuando el NM supere la barrera, el NM habra aumentado
    #0.132 metros y por tanto dicho rango (el valor medio que utilizamos para el calculo) estara por debajo del limite inferior
    #a la que existe marisma.

    tas_deposicion_MReclamada_097_177 = 0;

    for t_097_177 in range(2034,2050):
        tas_deposicion_MReclamada_097_177 += deposicion_marisma_regeneracion;
    print("La deposicion de la marisma reclamada en el rango 0.87-1.77 sera de: " +str(tas_deposicion_MReclamada_097_177))

    tas_deposicion_MReclamada_177_187 = 0;
    el_MReclamada_177 = [0.684];#Las elevaciones se han obtenido calculando 2,47m + (0.0078 * (2046-2017))- elevacion cuando alcance el equilibrio

    for t_177_187 in range (2034, 2046):
        tas_deposicion_MReclamada_177_187 += deposicion_marisma_regeneracion;
    for t_177_187 in range(2046,2050):
        expr_MR_177 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_177[-1];
        nuev_el_MR_177 = el_MReclamada_177 [-1] - expr_MR_177 + tasa_SLR_RCP45_2000_2050;
        el_MReclamada_177.append(nuev_el_MR_177);
        tas_deposicion_MReclamada_177_187 += expr_MR_177;
    print("La deposicion de la marisma reclamada en el rango 1.77-1.87 sera de: " +str(tas_deposicion_MReclamada_177_187))

    tas_deposicion_MReclamada_187_197 = 0;
    el_MReclamada_187 = [
        0.641];  # Las elevaciones se han obtenido calculando 2,47m + (0.0078 * (2046-2017))- elevacion cuando alcance el equilibrio

    for t_187_197 in range(2034, 2039):
        tas_deposicion_MReclamada_187_197 += deposicion_marisma_regeneracion;
    for t_187_197 in range(2039, 2050):
        expr_MR_187 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_187[-1];
        nuev_el_MR_187 = el_MReclamada_187[-1] - expr_MR_187 + tasa_SLR_RCP45_2000_2050;
        el_MReclamada_187.append(nuev_el_MR_187);
        tas_deposicion_MReclamada_187_197 += expr_MR_187;
    print("La deposicion de la marisma reclamada en el rango 1.87-1.97 sera de: " + str(
        tas_deposicion_MReclamada_187_197))

    tas_deposicion_MReclamada_197_207 = 0;
    el_MReclamada_197 = [
        0.582];  # Las elevaciones se han obtenido calculando 2,47m + (0.0078 * (2046-2017))- elevacion cuando alcance el equilibrio

    for t_197_207 in range(2034, 2050):
        expr_MR_197 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_197[-1];
        nuev_el_MR_197 = el_MReclamada_197[-1] - expr_MR_197 + tasa_SLR_RCP45_2000_2050;
        el_MReclamada_197.append(nuev_el_MR_197);
        tas_deposicion_MReclamada_197_207 += expr_MR_197;
    print("La deposicion de la marisma reclamada en el rango 1.97-2.07 sera de: " + str(tas_deposicion_MReclamada_197_207));

    tas_deposicion_MReclamada_207_217 = 0;
    el_MReclamada_207 = [
        0.482];  # Las elevaciones se han obtenido calculando 2,47m + (0.0078 * (2046-2017))- elevacion cuando alcance el equilibrio

    for t_207_217 in range(2034, 2050):
        expr_MR_207 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_207[-1];
        nuev_el_MR_207 = el_MReclamada_207[-1] - expr_MR_207 + tasa_SLR_RCP45_2000_2050;
        el_MReclamada_207.append(nuev_el_MR_207);
        tas_deposicion_MReclamada_207_217 += expr_MR_207;
    print("La deposicion de la marisma reclamada en el rango 2.07-2.17 sera de: " + str(
        tas_deposicion_MReclamada_207_217))

    tas_deposicion_MReclamada_217_227 = 0;
    el_MReclamada_217 = [
        0.382];  # Las elevaciones se han obtenido calculando 2,47m + (0.0078 * (2046-2017))- elevacion cuando alcance el equilibrio

    for t_217_227 in range(2034, 2050):
        expr_MR_217 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_217[-1];
        nuev_el_MR_217 = el_MReclamada_217[-1] - expr_MR_217 + tasa_SLR_RCP45_2000_2050;
        el_MReclamada_217.append(nuev_el_MR_217);
        tas_deposicion_MReclamada_217_227 += expr_MR_217;
    print("La deposicion de la marisma reclamada en el rango 2.17-2.27 sera de: " + str(
        tas_deposicion_MReclamada_217_227))

    tas_deposicion_MReclamada_227_237 = 0;
    el_MReclamada_227 = [
        0.282];  # Las elevaciones se han obtenido calculando 2,47m + (0.0078 * (2046-2017))- elevacion cuando alcance el equilibrio

    for t_227_237 in range(2034, 2050):
        expr_MR_227 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_227[-1];
        nuev_el_MR_227 = el_MReclamada_227[-1] - expr_MR_227 + tasa_SLR_RCP45_2000_2050;
        el_MReclamada_227.append(nuev_el_MR_227);
        tas_deposicion_MReclamada_227_237 += expr_MR_227;
    print("La deposicion de la marisma reclamada en el rango 2.27-2.37 sera de: " + str(
        tas_deposicion_MReclamada_227_237))

    tas_deposicion_MReclamada_237_247 = 0;
    el_MReclamada_237 = [
        0.182];  # Las elevaciones se han obtenido calculando 2,47m + (0.0078 * (2046-2017))- elevacion cuando alcance el equilibrio

    for t_237_247 in range(2034, 2050):
        expr_MR_237 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_237[-1];
        nuev_el_MR_237 = el_MReclamada_237[-1] - expr_MR_237 + tasa_SLR_RCP45_2000_2050;
        el_MReclamada_237.append(nuev_el_MR_237);
        tas_deposicion_MReclamada_237_247 += expr_MR_237;
    print("La deposicion de la marisma reclamada en el rango 2.37-2.47 sera de: " + str(
        tas_deposicion_MReclamada_237_247))

    #Las elevaciones superiores a 2,47 metros se harán con los calculos de las zonas inundables hasta el limite donde vaya a llegar el NM en 2050.

    #Reclasificamos el raster de la marisma reclamada que se volvera a inundar con el SLR con la sedimentacion que tendra
    #cada rango de elevaciones:
    depo_maris_reclamada_RCP45_2050 = Reclassify(raster_marisma_reclamada_errota, "VALUE", RemapRange([[-1000000, 970, "NODATA"],
                                    [970,1770,round(tas_deposicion_MReclamada_097_177*1000)],[1770,1870, round(tas_deposicion_MReclamada_177_187*1000)],
                                    [1870,1970, round(tas_deposicion_MReclamada_187_197*1000)],[1970,2070,round(tas_deposicion_MReclamada_197_207*1000)],
                                    [2070,2170, round(tas_deposicion_MReclamada_207_217*1000)],[2170,2270, round(tas_deposicion_MReclamada_217_227*1000)],
                                    [2270,2370, round(tas_deposicion_MReclamada_227_237*1000)], [2370,2470,round(tas_deposicion_MReclamada_237_247*1000)],
                                    [2470, 2570, round(depo_247*1000)], [2570,2670, round(depo_257*1000)], [2670, 2727, 0], [2727, 100000000, "NODATA"]]))
    depo_maris_reclamada_RCP45_2050.save(r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Deposicion_marisma_Reclamada_RCP45_2050");
    direc_depo_marisma_reclamada_RCP45_2050 = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Deposicion_marisma_Reclamada_RCP45_2050";

    #Reclasificamos el raster de las marismas en regeneracion para tener la deposicion por rangos que tendra dicha zona:
    depo_maris_regeneracion_RCP45_2050 = Reclassify(raster_marisma_regeneracion, "VALUE", RemapRange([[-10000,870, "NODATA"],
                                            [870, 1670, round(deposicion_087_167*1000)], [1670,1770, round(deposicion_167_177*1000)],
                                            [1770,1870,round(deposicion_177_187*1000)],[1870,1970, round(deposicion_187_197*1000)],
                                            [1970,2070, round(deposicion_197_207*1000)], [2070,2170, round(deposicion_207_217*1000)],
                                            [2170, 2270,round(tasa_deposicion_217 * 1000)],[2270, 2370,round(tasa_deposicion_227 * 1000)],
                                            [2370, 2470,round(tasa_deposicion_237 * 1000)], [2470, 2570, round(depo_247*1000)],
                                            [2570,2670, round(depo_257*1000)], [2670, 2727, 0], [2727, 100000000, "NODATA"]]))
    depo_maris_regeneracion_RCP45_2050.save(r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Deposicion_marisma_regen_RCP45_2050")
    direc_depo_maris_regeneracion_RCP45_2050 = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Deposicion_marisma_regen_RCP45_2050";

    #Reclasificamos el raster con los datos de la tasa de deposicion, por rangos, para representar la tasa de deposicion (aumento de
    # la elevacion en mm para el año 2050 en la zona de estudio para el escenario RCP4.5 y el año 2050:
    deposicion_RCP45_2050 = Reclassify(raster_Marisma, "VALUE", RemapRange([[-10000, 870,"NODATA"],[870, 970, round(tasa_deposicion_087*1000)],
                                 [970, 1070, round(tasa_deposicion_097*1000)], [1070, 1170, round(tasa_deposicion_107*1000)], [1170, 1270, round(tasa_deposicion_117*1000)],
                                 [1270, 1370, round(tasa_deposicion_127*1000)], [1370, 1470, round(tasa_deposicion_137*1000)], [1470, 1570, round(tasa_deposicion_147*1000)],
                                 [1570, 1670, round(tasa_deposicion_157*1000)], [1670, 1770, round(tasa_deposicion_167*1000)], [1770, 1870, round(tasa_deposicion_177*1000)],
                                 [1870, 1970, round(tasa_deposicion_187*1000)], [1970, 2070, round(tasa_deposicion_197*1000)], [2070, 2170, round(tasa_deposicion_207*1000)],
                                 [2170, 2270, round(tasa_deposicion_217*1000)], [2270, 2370, round(tasa_deposicion_227*1000)], [2370, 2470, round(tasa_deposicion_237*1000)],
                                 [2470, 2570, round(depo_247*1000)], [2570,2670, round(depo_257*1000)], [2670, 2727, 0], [2727, 100000000, "NODATA"]]))
    deposicion_RCP45_2050.save(r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Deposicion_RCP45_2050")
    direcc_depo_RCP45_2050 = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Deposicion_RCP45_2050"

    #Reclasificamos el raster de marismas de zonas inundables por el SLR (zonas de cultivo) para tener en cuenta la interaccion
    #deposicion-SLR en las zonas que se inundarán con el SLR:
    depo_RCP45_2050_zonas_inundables = Reclassify(raster_zonas_cultivo, "VALUE", RemapRange([[870, 2570, round(depo_247*1000)],
                                            [2570, 2670, round(depo_257*1000)], [2670, 2727, 0], [2727, 1000000000, "NODATA"]]));
    depo_RCP45_2050_zonas_inundables.save(r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Deposicion_RCP45_2050_zonas_inundables")
    direcc_depo_RCP45_2050_zonas_inundables = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Deposicion_RCP45_2050_zonas_inundables"

    #Ahora ya tenemos el raster con la deposicion que habra en la zona de estudio segun el escenario RCP4.5 y para el año 2050,

    #Pues bien, sumamos los dos rasteres para obtener la nueva altura que tendra la marisma.
    elevacion_RCP45_2050 = RasterCalculator([raster_Marisma, direcc_depo_RCP45_2050], ["marisma", "depo"],
                                            "(marisma+depo)")
    elevacion_RCP45_2050.save(
       r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Elevacion_RCP45_2050")
    direc_elevacion_RCP45_2050 = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Elevacion_RCP45_2050"

    elevacion_marisma_regener_RCP45_2050 = RasterCalculator([raster_marisma_regeneracion, direc_depo_maris_regeneracion_RCP45_2050],
                                                            ["mar_reg","deposi_regen"], "(mar_reg + deposi_regen)")
    elevacion_marisma_regener_RCP45_2050.save(r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Elevacion_marism_regener_RCP45_2050")
    direc_elevacion_marisma_regener_RCP45_2050 = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Elevacion_marism_regener_RCP45_2050";

    elevacion_RCP45_2050_zonas_inundables = RasterCalculator ([raster_zonas_cultivo, direcc_depo_RCP45_2050_zonas_inundables],
                                                              ["zonas_inundables", "depo_inundables"], "(zonas_inundables+depo_inundables)")
    elevacion_RCP45_2050_zonas_inundables.save(r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Elevacion_RCP45_2050_zonas_inundables");
    direc_elevacion_RCP45_2050_zonas_inundables = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Elevacion_RCP45_2050_zonas_inundables";

    #Calculamos la elevacion que tendra la marisma reclamada el año 2050 y teniendo en cuenta el escenario RCP 4.5 sumando las elevaciones
    #que en el año 2017 tenia dicha zona mas la deposicion acumulada desde dicho año hasta 2050.
    elev_RCP45_2050_marisma_reclamada = RasterCalculator ([raster_marisma_reclamada_errota, direc_depo_marisma_reclamada_RCP45_2050],
                                                          ["MR", "dep_MR"], "(MR + dep_MR)");
    elev_RCP45_2050_marisma_reclamada.save(r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Elevacion_RCP45_2050_mari_reclamada");
    direc_elev_RCP45_2050_marisma_reclamada = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Elevacion_RCP45_2050_mari_reclamada"

    #Una vez que tenemos la elevacion nueva de la zona de estudio debido a la deposicion fusionamos los rasteres de la nueva
    #elevacion de la marisma.
    comb_elevacion_RCP45_2050 = arcpy.management.MosaicToNewRaster([direc_elevacion_RCP45_2050, direc_elevacion_RCP45_2050_zonas_inundables,
                                    direc_elevacion_marisma_regener_RCP45_2050, direc_elev_RCP45_2050_marisma_reclamada], r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb",
                                    "Elevacion_Combi_Terreno_RCP45_2050", 25830, "32_BIT_FLOAT", 1, 1, "FIRST")

    #Ya tenemos el la elevacion que habra en la zona de estudio en 2050 segun el escenario 2050, ahora volvemos a reclasificar dicho
    #raster para obtener la potencial distribucion de la marisma en dicho escenario y año:
    pot_distribucion_RCP45_2050 = Reclassify(comb_elevacion_RCP45_2050, "VALUE", RemapRange([[-100000,1127,"NODATA"], [1127,2727,0],[2727, 1000000,"NODATA"]]))
    pot_distribucion_RCP45_2050.save(r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Pot_Distribucion_RCP45_2050")

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
        nueva_elevacion_087 = elevaciones_087[-1] - expresion_087 + tasa_SLR_RCP85_2000_2050;
        elevaciones_087.append(nueva_elevacion_087);
        tasa_deposicion_087+= expresion_087;
    print("Tasa de deposición acumulada del rango 0.87-0.97 es: " + str(tasa_deposicion_087))

    #Volvemos a calcular las tasas de deposiciones pero ahora para todos los rangos de valores (desde 0.87 hasta 2.47 metros, cada
    #10 centimetros):
    tasa_deposicion_097 = 0;
    elevaciones_097 = [1.45];

    for tasa_dep_097 in range(2017,2050):
        expresion_097 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_097[-1];
        nueva_elevacion_097 = elevaciones_097[-1] - expresion_097 + tasa_SLR_RCP85_2000_2050;
        elevaciones_097.append(nueva_elevacion_097);
        tasa_deposicion_097+= expresion_097;
    print("Tasa de deposición acumulada del rango 0.97-1.07 es: " + str(tasa_deposicion_097))

    tasa_deposicion_107 = 0;
    elevaciones_107 = [1.35];

    for tasa_dep_107 in range(2017, 2050):
        expresion_107 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_107[-1];
        nueva_elevacion_107 = elevaciones_107[-1] - expresion_107 + tasa_SLR_RCP85_2000_2050;
        elevaciones_107.append(nueva_elevacion_107);
        tasa_deposicion_107 += expresion_107;
    print("Tasa de deposicion acumulada del rango 1.07-1.17 es: " + str(tasa_deposicion_107))

    tasa_deposicion_117 = 0;
    elevaciones_117 = [1.25];

    for tasa_dep_117 in range(2017, 2050):
        expresion_117 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_117[-1];
        nueva_elevacion_117 = elevaciones_117[-1] - expresion_117 + tasa_SLR_RCP85_2000_2050;
        elevaciones_117.append(nueva_elevacion_117);
        tasa_deposicion_117 += expresion_117;
    print("Tasa de deposicion acumulada del rango 1.17-1.27 es: " + str(tasa_deposicion_117))

    tasa_deposicion_127 = 0;
    elevaciones_127 = [1.15];

    for tasa_dep_127 in range(2017, 2050):
        expresion_127 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_127[-1];
        nueva_elevacion_127 = elevaciones_127[-1] - expresion_127 + tasa_SLR_RCP85_2000_2050;
        elevaciones_127.append(nueva_elevacion_127);
        tasa_deposicion_127 += expresion_127;
    print("Tasa de deposicion acumulada del rango 1.27-1.37 es: " + str(tasa_deposicion_127))

    tasa_deposicion_137 = 0;
    elevaciones_137 = [1.05];

    for tasa_dep_137 in range(2017, 2050):
        expresion_137 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_137[-1];
        nueva_elevacion_137 = elevaciones_137[-1] - expresion_137 + tasa_SLR_RCP85_2000_2050;
        elevaciones_137.append(nueva_elevacion_137);
        tasa_deposicion_137 += expresion_137;
    print("Tasa de deposicion acumulada del rango 1.37-1.47 es: " + str(tasa_deposicion_137))

    tasa_deposicion_147 = 0;
    elevaciones_147 = [0.95];

    for tasa_dep_147 in range(2017, 2050):
        expresion_147 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_147[-1];
        nueva_elevacion_147 = elevaciones_147[-1] - expresion_147 + tasa_SLR_RCP85_2000_2050;
        elevaciones_147.append(nueva_elevacion_147);
        tasa_deposicion_147 += expresion_147;
    print("Tasa de deposicion acumulada del rango 1.47-1.57 es: " + str(tasa_deposicion_147))

    tasa_deposicion_157 = 0;
    elevaciones_157 = [0.85];

    for tasa_dep_157 in range(2017, 2050):
        expresion_157 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_157[-1];
        nueva_elevacion_157 = elevaciones_157[-1] - expresion_157 + tasa_SLR_RCP85_2000_2050;
        elevaciones_157.append(nueva_elevacion_157);
        tasa_deposicion_157 += expresion_157;
    print("Tasa de deposicion acumulada del rango 1.57-1.67 es: " + str(tasa_deposicion_157))

    tasa_deposicion_167 = 0;
    elevaciones_167 = [0.75];

    for tasa_dep_167 in range(2017, 2050):
        expresion_167 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_167[-1];
        nueva_elevacion_167 = elevaciones_167[-1] - expresion_167 + tasa_SLR_RCP85_2000_2050;
        elevaciones_167.append(nueva_elevacion_167);
        tasa_deposicion_167 += expresion_167;
    print("Tasa de deposicion acumulada del rango 1.67-1.77 es: " + str(tasa_deposicion_167))

    tasa_deposicion_177 = 0;
    elevaciones_177 = [0.65];

    for tasa_dep_177 in range(2017, 2050):
        expresion_177 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_177[-1];
        nueva_elevacion_177 = elevaciones_177[-1] - expresion_177 + tasa_SLR_RCP85_2000_2050;
        elevaciones_177.append(nueva_elevacion_177);
        tasa_deposicion_177 += expresion_177;
    print("Tasa de deposicion acumulada del rango 1.77-1.87 es: " + str(tasa_deposicion_177))

    tasa_deposicion_187 = 0;
    elevaciones_187 = [0.55];

    for tasa_dep_187 in range(2017, 2050):
        expresion_187 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_187[-1];
        nueva_elevacion_187 = elevaciones_187[-1] - expresion_187 + tasa_SLR_RCP85_2000_2050;
        elevaciones_187.append(nueva_elevacion_187);
        tasa_deposicion_187 += expresion_187;
    print("Tasa de deposicion acumulada del rango 1.87-1.97 es: " + str(tasa_deposicion_187))

    tasa_deposicion_197 = 0;
    elevaciones_197 = [0.45];

    for tasa_dep_197 in range(2017, 2050):
        expresion_197 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_197[-1];
        nueva_elevacion_197 = elevaciones_197[-1] - expresion_197 + tasa_SLR_RCP85_2000_2050;
        elevaciones_197.append(nueva_elevacion_197);
        tasa_deposicion_197 += expresion_197;
    print("Tasa de deposicion acumulada del rango 1.97-2.07 es: "+ str(tasa_deposicion_197))

    tasa_deposicion_207 = 0;
    elevaciones_207 = [0.35];

    for tasa_dep_207 in range(2017, 2050):
        expresion_207 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_207[-1];
        nueva_elevacion_207 = elevaciones_207[-1] - expresion_207 + tasa_SLR_RCP85_2000_2050;
        elevaciones_207.append(nueva_elevacion_207);
        tasa_deposicion_207 += expresion_207;
    print("Tasa de deposicion acumulada del rango 2.07-2.17 es: " + str(tasa_deposicion_207))

    tasa_deposicion_217 = 0;
    elevaciones_217 = [0.25];

    for tasa_dep_217 in range(2017, 2050):
        expresion_217 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_217[-1];
        nueva_elevacion_217 = elevaciones_217[-1] - expresion_217 + tasa_SLR_RCP85_2000_2050;
        elevaciones_217.append(nueva_elevacion_217);
        tasa_deposicion_217 += expresion_217;
    print("Tasa de deposicion acumulada del rango 2.17-2.27 es: " + str(tasa_deposicion_217))

    tasa_deposicion_227 = 0;
    elevaciones_227 = [0.15];

    for tasa_dep_227 in range(2017, 2050):
        expresion_227 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_227[-1];
        nueva_elevacion_227 = elevaciones_227[-1] - expresion_227 + tasa_SLR_RCP85_2000_2050;
        elevaciones_227.append(nueva_elevacion_227);
        tasa_deposicion_227 += expresion_227;
    print("Tasa de deposicion acumulada del rango 2.27-2.37 es: " + str(tasa_deposicion_227))

    tasa_deposicion_237 = 0;
    elevaciones_237 = [0.05];

    for tasa_dep_237 in range(2017, 2050):
        expresion_237 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_237[-1];
        nueva_elevacion_237 = elevaciones_237[-1] - expresion_237 + tasa_SLR_RCP85_2000_2050;
        elevaciones_237.append(nueva_elevacion_237);
        tasa_deposicion_237 += expresion_237;
    print("Tasa de deposicion acumulada del rango 2.37-2.47 es: " + str(tasa_deposicion_237))

    depo_247 = 0;
    elevaciones_247 = [0.0532];

    for deposicion_247 in range(2029, 2050):
        expr_247 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_247[-1];
        nueva_elevacion_247 = elevaciones_247[-1] - expr_247 + tasa_SLR_RCP85_2000_2050;
        elevaciones_247.append(nueva_elevacion_247);
        depo_247 += expr_247;
    print("Tasa de deposicion acumulada del rango 2.47-2.57 es: " + str(depo_247))

    depo_257 = 0;
    elevaciones_257 = [0.0564];

    for deposicion_257 in range(2041, 2050):
        expr_257 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_257[-1];
        nueva_elevacion_257 = elevaciones_257[-1] - expr_257 + tasa_SLR_RCP85_2000_2050;
        elevaciones_257.append(nueva_elevacion_257);
        depo_257 += expr_257;
    print("Tasa de deposicion acumulada del rango 2.57-2.67 es: " + str(depo_257))

    deposicion_087_167 = 0;

    for dep_087_167 in range(2017,2050):
        expr_087_167 = deposicion_marisma_regeneracion
        deposicion_087_167 += expr_087_167;
    print("La deposición acumulada del rango 0.87-1.67 de la marisma en regeneracion es:" + str(deposicion_087_167))

    deposicion_167_177 = 0;
    elev_regen_167 = [0.504];  # Diferencia entre el nivel de marea alta (2.47) mas el SLR para ese año y la elevacion del
    # rango mas la deposicion hasta que llegue a los 2,2 metros aprox.
    for dep_167_177 in range(2017, 2047):
        deposicion_167_177 += deposicion_marisma_regeneracion
    for dep_167_177 in range(2047, 2050):
        expresion_167_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_167[
            -1];
        nueva_ele_167 = elev_regen_167[-1] - expresion_167_bis + tasa_SLR_RCP85_2000_2050;
        elev_regen_167.append(nueva_ele_167);
        deposicion_167_177 += expresion_167_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 1.67-1.77 es:" + str(deposicion_167_177));

    deposicion_177_187 = 0;
    elev_regen_177 = [0.453];  # Diferencia entre el nivel de marea alta (2.47) mas el SLR para ese año y la elevacion del
    # rango mas la deposicion hasta que llegue a los 2,2 metros aprox.
    for dep_177_187 in range(2017, 2041):
        deposicion_177_187 += deposicion_marisma_regeneracion
    for dep_177_187 in range(2041, 2050):
        expresion_177_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_177[-1];
        nueva_ele_177 = elev_regen_177[-1] - expresion_177_bis + tasa_SLR_RCP85_2000_2050;
        elev_regen_177.append(nueva_ele_177);
        deposicion_177_187 += expresion_177_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 1.77-1.87 es:" + str(deposicion_177_187));

    deposicion_187_197 = 0;
    elev_regen_187 = [0.402];  # Diferencia entre el nivel de marea alta (2.47) mas el SLR para ese año y la elevacion del
    # rango mas la deposicion hasta que llegue a los 2,2 metros aprox.
    for dep_187_197 in range(2017, 2035):
        deposicion_187_197 += deposicion_marisma_regeneracion
    for dep_187_197 in range(2035, 2050):
        expresion_187_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_187[-1];
        nueva_ele_187 = elev_regen_187[-1] - expresion_187_bis + tasa_SLR_RCP85_2000_2050;
        elev_regen_187.append(nueva_ele_187);
        deposicion_187_197 += expresion_187_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 1.87-1.97 es:" + str(deposicion_187_197));

    deposicion_197_207 = 0;
    elev_regen_197 = [0.351];  # Diferencia entre el nivel de marea alta (2.47) mas el SLR para ese año y la elevacion del
    # rango mas la deposicion hasta que llegue a los 2,2 metros aprox.
    for dep_197_207 in range(2017, 2029):
        deposicion_197_207 += deposicion_marisma_regeneracion
    for dep_197_207 in range(2029, 2050):
        expresion_197_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_197[-1];
        nueva_ele_197 = elev_regen_197[-1] - expresion_197_bis + tasa_SLR_RCP85_2000_2050;
        elev_regen_197.append(nueva_ele_197);
        deposicion_197_207 += expresion_197_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 1.97-2.07 es:" + str(deposicion_197_207));

    deposicion_207_217 = 0;
    elev_regen_207 = [0.300];  # Diferencia entre el nivel de marea alta (2.47) mas el SLR para ese año y la elevacion del
    # rango mas la deposicion hasta que llegue a los 2,2 metros aprox.
    for dep_207_217 in range(2017, 2023):
        deposicion_207_217 += deposicion_marisma_regeneracion
    for dep_207_217 in range(2023, 2050):
        expresion_207_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_207[-1];
        nueva_ele_207 = elev_regen_207[-1] - expresion_207_bis + tasa_SLR_RCP85_2000_2050;
        elev_regen_207.append(nueva_ele_207);
        deposicion_207_217 += expresion_207_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 2.07-2.17 es:" + str(deposicion_207_217));

    tas_deposicion_MReclamada_097_177 = 0;

    for t_097_177 in range(2033, 2050):
        tas_deposicion_MReclamada_097_177 += deposicion_marisma_regeneracion;
    print("La deposicion de la marisma reclamada en el rango 0.97-1.77 sera de: " + str(
        tas_deposicion_MReclamada_097_177))

    tas_deposicion_MReclamada_177_187 = 0;
    el_MReclamada_177 = [
        0.707];  # Las elevaciones se han obtenido calculando 2,47m + (0.0078 * (2046-2017))- elevacion cuando alcance el equilibrio

    for t_177_187 in range(2033, 2045):
        tas_deposicion_MReclamada_177_187 += deposicion_marisma_regeneracion;
    for t_177_187 in range(2045, 2050):
        expr_MR_177 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_177[-1];
        nuev_el_MR_177 = el_MReclamada_177[-1] - expr_MR_177 + tasa_SLR_RCP85_2000_2050;
        el_MReclamada_177.append(nuev_el_MR_177);
        tas_deposicion_MReclamada_177_187 += expr_MR_177;
    print("La deposicion de la marisma reclamada en el rango 1.77-1.87 sera de: " + str(
        tas_deposicion_MReclamada_177_187))

    tas_deposicion_MReclamada_187_197 = 0;
    el_MReclamada_187 = [
        0.659];  # Las elevaciones se han obtenido calculando 2,47m + (0.0078 * (2046-2017))- elevacion cuando alcance el equilibrio

    for t_187_197 in range(2033, 2038):
        tas_deposicion_MReclamada_187_197 += deposicion_marisma_regeneracion;
    for t_187_197 in range(2038, 2050):
        expr_MR_187 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_187[-1];
        nuev_el_MR_187 = el_MReclamada_187[-1] - expr_MR_187 + tasa_SLR_RCP85_2000_2050;
        el_MReclamada_187.append(nuev_el_MR_187);
        tas_deposicion_MReclamada_187_197 += expr_MR_187;
    print("La deposicion de la marisma reclamada en el rango 1.87-1.97 sera de: " + str(
        tas_deposicion_MReclamada_187_197))

    tas_deposicion_MReclamada_197_207 = 0;
    el_MReclamada_197 = [
        0.596];  # Las elevaciones se han obtenido calculando 2,47m + (0.0078 * (2046-2017))- elevacion cuando alcance el equilibrio

    for t_197_207 in range(2033, 2050):
        expr_MR_197 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_197[-1];
        nuev_el_MR_197 = el_MReclamada_197[-1] - expr_MR_197 + tasa_SLR_RCP85_2000_2050;
        el_MReclamada_197.append(nuev_el_MR_197);
        tas_deposicion_MReclamada_197_207 += expr_MR_197;
    print("La deposicion de la marisma reclamada en el rango 1.97-2.07 sera de: " + str(
        tas_deposicion_MReclamada_197_207));

    tas_deposicion_MReclamada_207_217 = 0;
    el_MReclamada_207 = [
        0.496];  # Las elevaciones se han obtenido calculando 2,47m + (0.0078 * (2046-2017))- elevacion cuando alcance el equilibrio

    for t_207_217 in range(2033, 2050):
        expr_MR_207 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_207[-1];
        nuev_el_MR_207 = el_MReclamada_207[-1] - expr_MR_207 + tasa_SLR_RCP85_2000_2050;
        el_MReclamada_207.append(nuev_el_MR_207);
        tas_deposicion_MReclamada_207_217 += expr_MR_207;
    print("La deposicion de la marisma reclamada en el rango 2.07-2.17 sera de: " + str(
        tas_deposicion_MReclamada_207_217))

    tas_deposicion_MReclamada_217_227 = 0;
    el_MReclamada_217 = [
        0.396];  # Las elevaciones se han obtenido calculando 2,47m + (0.0078 * (2046-2017))- elevacion cuando alcance el equilibrio

    for t_217_227 in range(2033, 2050):
        expr_MR_217 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_217[-1];
        nuev_el_MR_217 = el_MReclamada_217[-1] - expr_MR_217 + tasa_SLR_RCP85_2000_2050;
        el_MReclamada_217.append(nuev_el_MR_217);
        tas_deposicion_MReclamada_217_227 += expr_MR_217;
    print("La deposicion de la marisma reclamada en el rango 2.17-2.27 sera de: " + str(
        tas_deposicion_MReclamada_217_227))

    tas_deposicion_MReclamada_227_237 = 0;
    el_MReclamada_227 = [
        0.296];  # Las elevaciones se han obtenido calculando 2,47m + (0.0078 * (2046-2017))- elevacion cuando alcance el equilibrio

    for t_227_237 in range(2033, 2050):
        expr_MR_227 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_227[-1];
        nuev_el_MR_227 = el_MReclamada_227[-1] - expr_MR_227 + tasa_SLR_RCP85_2000_2050;
        el_MReclamada_227.append(nuev_el_MR_227);
        tas_deposicion_MReclamada_227_237 += expr_MR_227;
    print("La deposicion de la marisma reclamada en el rango 2.27-2.37 sera de: " + str(
        tas_deposicion_MReclamada_227_237))

    tas_deposicion_MReclamada_237_247 = 0;
    el_MReclamada_237 = [
        0.196];  # Las elevaciones se han obtenido calculando 2,47m + (0.0078 * (2046-2017))- elevacion cuando alcance el equilibrio

    for t_237_247 in range(2033, 2050):
        expr_MR_237 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_237[-1];
        nuev_el_MR_237 = el_MReclamada_237[-1] - expr_MR_237 + tasa_SLR_RCP85_2000_2050;
        el_MReclamada_237.append(nuev_el_MR_237);
        tas_deposicion_MReclamada_237_247 += expr_MR_237;
    print("La deposicion de la marisma reclamada en el rango 2.37-2.47 sera de: " + str(
        tas_deposicion_MReclamada_237_247))

    # Las elevaciones superiores a 2,47 metros se harán con los calculos de las zonas inundables hasta el limite donde vaya a llegar el NM en 2050.

    # Reclasificamos el raster de la marisma reclamada que se volvera a inundar con el SLR con la sedimentacion que tendra
    # cada rango de elevaciones:
    depo_maris_reclamada_RCP85_2050 = Reclassify(raster_marisma_reclamada_errota, "VALUE", RemapRange([[-1000000, 970, "NODATA"],
                                      [970, 1770,round(tas_deposicion_MReclamada_097_177 * 1000)],[1770, 1870,round(tas_deposicion_MReclamada_177_187 * 1000)],
                                      [1870, 1970,round(tas_deposicion_MReclamada_187_197 * 1000)],[1970, 2070,round(tas_deposicion_MReclamada_197_207 * 1000)],
                                      [2070, 2170,round(tas_deposicion_MReclamada_207_217 * 1000)],[2170, 2270,round(tas_deposicion_MReclamada_217_227 * 1000)],
                                      [2270, 2370,round(tas_deposicion_MReclamada_227_237 * 1000)],[2370, 2470,round(tas_deposicion_MReclamada_237_247 * 1000)],
                                      [2470, 2570, round(depo_247 * 1000)],[2570, 2670, round(depo_257 * 1000)], [2670, 2753, 0],[2753, 100000000, "NODATA"]]))
    depo_maris_reclamada_RCP85_2050.save(r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Deposicion_marisma_Reclamada_RCP85_2050");
    direc_depo_marisma_reclamada_RCP85_2050 = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Deposicion_marisma_Reclamada_RCP85_2050";

    # Reclasificamos el raster de las marismas en regeneracion para tener la deposicion por rangos que tendra dicha zona:
    depo_maris_regeneracion_RCP85_2050 = Reclassify(raster_marisma_regeneracion, "VALUE",RemapRange([[-10000, 870, "NODATA"],
                                        [870, 1670, round(deposicion_087_167 * 1000)],[1670, 1770, round(deposicion_167_177 * 1000)],
                                        [1770, 1870, round(deposicion_177_187 * 1000)], [1870, 1970, round(deposicion_187_197 * 1000)],
                                        [1970, 2070, round(deposicion_197_207 * 1000)],[2070, 2170, round(deposicion_207_217 * 1000)],
                                        [2170, 2270, round(tasa_deposicion_217 * 1000)],[2270, 2370, round(tasa_deposicion_227 * 1000)],
                                        [2370, 2470, round(tasa_deposicion_237 * 1000)],[2470, 2570, round(depo_247 * 1000)],
                                        [2570, 2670, round(depo_257 * 1000)], [2670, 2753, 0],[2753, 100000000, "NODATA"]]))
    depo_maris_regeneracion_RCP85_2050.save(r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Deposicion_marisma_regen_RCP85_2050")
    direc_depo_maris_regeneracion_RCP85_2050 = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Deposicion_marisma_regen_RCP85_2050";

    #Reclasificamos el raster con los datos de la tasa de deposicion, por rangos, para representar la tasa de deposicion (aumento de
    # la elevacion en mm para el año 2050 en la zona de estudio para el escenario RCP4.5 y el año 2050:
    deposicion_RCP85_2050 = Reclassify(raster_Marisma, "VALUE", RemapRange([[-10000, 870,"NODATA"],[870, 970, round(tasa_deposicion_087*1000)],
                                 [970, 1070, round(tasa_deposicion_097*1000)], [1070, 1170, round(tasa_deposicion_107*1000)], [1170, 1270, round(tasa_deposicion_117*1000)],
                                 [1270, 1370, round(tasa_deposicion_127*1000)], [1370, 1470, round(tasa_deposicion_137*1000)], [1470, 1570, round(tasa_deposicion_147*1000)],
                                 [1570, 1670, round(tasa_deposicion_157*1000)], [1670, 1770, round(tasa_deposicion_167*1000)], [1770, 1870, round(tasa_deposicion_177*1000)],
                                 [1870, 1970, round(tasa_deposicion_187*1000)], [1970, 2070, round(tasa_deposicion_197*1000)], [2070, 2170, round(tasa_deposicion_207*1000)],
                                 [2170, 2270, round(tasa_deposicion_217*1000)], [2270, 2370, round(tasa_deposicion_227*1000)], [2370, 2470, round(tasa_deposicion_237*1000)],
                                                                           [2470, 2570, round(depo_247*1000)], [2570,2670, round (depo_257*1000)], [2670,2753,0], [2753, 10000000, "NODATA"]]))
    deposicion_RCP85_2050.save(r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Deposicion_RCP85_2050")
    direcc_depo_RCP85_2050 = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Deposicion_RCP85_2050"

    #Reclasificamos el raster de marismas de zonas inundables por el SLR (zonas de cultivo) para tener en cuenta la interaccion
    #deposicion-SLR en las zonas que se inundarán con el SLR:
    depo_RCP85_2050_zonas_inundables = Reclassify(raster_zonas_cultivo, "VALUE", RemapRange([[870, 2570, round(depo_247*1000)],
                                            [2570, 2670, round(depo_257*1000)], [2670, 2753,0], [2753, 1000000000, "NODATA"]]));
    depo_RCP85_2050_zonas_inundables.save(r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Deposicion_RCP85_2050_zonas_inundables")
    direcc_depo_RCP85_2050_zonas_inundables = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Deposicion_RCP85_2050_zonas_inundables"

    #Ahora ya tenemos el raster con la deposicion que habra en la zona de estudio segun el escenario RCP4.5 y para el año 2050,
    #asumiendo que desde el limite inferior hasta el superior donde se encuentran las marismas de Urdaibai de acuerdo a distintos
    #estudios, son las potenciales zonas de las marismas (aunque en realidad no haya por distintos factores y suponiendo que serían
    #marismas consolidadas con unas tasas de deposicion acorde a su elevacion.

    #Pues bien, sumamos los dos rasteres (elevacion en mm y deposicion en mm) para obtener la nueva altura que tendra la marisma.
    elevacion_RCP85_2050 = RasterCalculator([raster_Marisma, direcc_depo_RCP85_2050], ["marisma", "depo"],
                                            "(marisma+depo)")
    elevacion_RCP85_2050.save(
       r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Elevacion_RCP85_2050")
    direc_elevacion_RCP85_2050 = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Elevacion_RCP85_2050"

    elevacion_RCP85_2050_zona_inundable = RasterCalculator([raster_zonas_cultivo, direcc_depo_RCP85_2050_zonas_inundables],
                                                           ["zonas_inun", "depo_inun"], "(zonas_inun+depo_inun)")
    elevacion_RCP85_2050_zona_inundable.save(r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Elevacion_RCP85_2050_zonas_inundables");
    direc_elevacion_RCP85_2050_zonas_inundables = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Elevacion_RCP85_2050_zonas_inundables";

    elevacion_marisma_regener_RCP85_2050 = RasterCalculator(
        [raster_marisma_regeneracion, direc_depo_maris_regeneracion_RCP85_2050],
        ["mar_reg", "deposi_regen"], "(mar_reg + deposi_regen)")
    elevacion_marisma_regener_RCP85_2050.save(
        r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Elevacion_marism_regener_RCP85_2050")
    direc_elevacion_marisma_regener_RCP85_2050 = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Elevacion_marism_regener_RCP85_2050";

    elevac_marisma_reclamada_RCP85_2050 = RasterCalculator([raster_marisma_reclamada_errota, direc_depo_marisma_reclamada_RCP85_2050],
                                                           ["MR", "depo_MR"], "(MR + depo_MR)")
    elevac_marisma_reclamada_RCP85_2050.save (r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Elevacion_marism_reclamada_RCP85_2050")
    direc_elevac_marisma_raclamada_RCP85_2050 = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Elevacion_marism_reclamada_RCP85_2050";

    #Una vez que tenemos la elevacion nueva de la zona de estudio debido a la deposicion fusionamos los rasteres de la nueva
    #elevacion de la marisma con el raster de elevaciones original para que tenga las nuevas elevaciones y tenga en cuenta los
    #valores del raster original en las zonas donde no hay marisma (y asi no ponga "NODATA").
    comb_elevacion_RCP85_2050 = arcpy.management.MosaicToNewRaster([direc_elevacion_RCP85_2050, direc_elevacion_RCP85_2050_zonas_inundables,direc_elevac_marisma_raclamada_RCP85_2050,
                                    direc_elevacion_marisma_regener_RCP85_2050], r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb",
                                    "Elevacion_Combi_Terreno_RCP85_2050", 25830, "32_BIT_FLOAT", 1, 1, "FIRST")

    #Ya tenemos el la elevacion que habra en la zona de estudio en 2050 segun el escenario 2050, ahora volvemos a reclasificar dicho
    #raster para obtener la potencial distribucion de la marisma en dicho escenario y año:
    pot_distribucion_RCP85_2050 = Reclassify(comb_elevacion_RCP85_2050, "VALUE", RemapRange([[-100000,1153,"NODATA"], [1153,2753,0],[2753, 1000000,"NODATA"]]))
    pot_distribucion_RCP85_2050.save(r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Pot_Distribucion_RCP85_2050")
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
        nueva_elevacion_087 = elevaciones_087[-1] - expresion_087 + tasa_SLR_RCP45_2000_2050;
        elevaciones_087.append(nueva_elevacion_087);
        tasa_deposicion_087+= expresion_087;

    for tasa_dep_087 in range(2050,2100):
        expresion_087 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_087[-1];
        nueva_elevacion_087 = elevaciones_087[-1] - expresion_087 + tasa_SLR_RCP45_2050_2100;
        elevaciones_087.append(nueva_elevacion_087);
        tasa_deposicion_087+= expresion_087;
    print("Tasa de deposición acumulada del rango 0.87-0.97 es: " + str(tasa_deposicion_087))

    #Volvemos a calcular las tasas de deposiciones pero ahora para todos los rangos de valores (desde 0.87 hasta 2.47 metros, cada
    #10 centimetros):
    tasa_deposicion_097 = 0;
    elevaciones_097 = [1.45];

    for tasa_dep_097 in range(2017,2050):
        expresion_097 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_097[-1];
        nueva_elevacion_097 = elevaciones_097[-1] - expresion_097 + tasa_SLR_RCP45_2000_2050;
        elevaciones_097.append(nueva_elevacion_097);
        tasa_deposicion_097+= expresion_097;

    for tasa_dep_097 in range(2050,2100):
        expresion_097 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_097[-1];
        nueva_elevacion_097 = elevaciones_097[-1] - expresion_097 + tasa_SLR_RCP45_2050_2100;
        elevaciones_097.append(nueva_elevacion_097);
        tasa_deposicion_097+= expresion_097;
    print("Tasa de deposición acumulada del rango 0.97-1.07 es: " + str(tasa_deposicion_097))

    tasa_deposicion_107 = 0;
    elevaciones_107 = [1.35];

    for tasa_dep_107 in range(2017, 2050):
        expresion_107 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_107[-1];
        nueva_elevacion_107 = elevaciones_107[-1] - expresion_107 + tasa_SLR_RCP45_2000_2050;
        elevaciones_107.append(nueva_elevacion_107);
        tasa_deposicion_107 += expresion_107;

    for tasa_dep_107 in range(2050, 2100):
        expresion_107 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_107[-1];
        nueva_elevacion_107 = elevaciones_107[-1] - expresion_107 + tasa_SLR_RCP45_2050_2100;
        elevaciones_107.append(nueva_elevacion_107);
        tasa_deposicion_107 += expresion_107;
    print("Tasa de deposicion acumulada del rango 1.07-1.17 es: " + str(tasa_deposicion_107))

    tasa_deposicion_117 = 0;
    elevaciones_117 = [1.25];

    for tasa_dep_117 in range(2017, 2050):
        expresion_117 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_117[-1];
        nueva_elevacion_117 = elevaciones_117[-1] - expresion_117 + tasa_SLR_RCP45_2000_2050;
        elevaciones_117.append(nueva_elevacion_117);
        tasa_deposicion_117 += expresion_117;

    for tasa_dep_117 in range(2050, 2100):
        expresion_117 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_117[-1];
        nueva_elevacion_117 = elevaciones_117[-1] - expresion_117 + tasa_SLR_RCP45_2050_2100;
        elevaciones_117.append(nueva_elevacion_117);
        tasa_deposicion_117 += expresion_117;
    print("Tasa de deposicion acumulada del rango 1.17-1.27 es: " + str(tasa_deposicion_117))

    tasa_deposicion_127 = 0;
    elevaciones_127 = [1.15];

    for tasa_dep_127 in range(2017, 2050):
        expresion_127 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_127[-1];
        nueva_elevacion_127 = elevaciones_127[-1] - expresion_127 + tasa_SLR_RCP45_2000_2050;
        elevaciones_127.append(nueva_elevacion_127);
        tasa_deposicion_127 += expresion_127;

    for tasa_dep_127 in range(2050, 2100):
        expresion_127 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_127[-1];
        nueva_elevacion_127 = elevaciones_127[-1] - expresion_127 + tasa_SLR_RCP45_2050_2100;
        elevaciones_127.append(nueva_elevacion_127);
        tasa_deposicion_127 += expresion_127;
    print("Tasa de deposicion acumulada del rango 1.27-1.37 es: " + str(tasa_deposicion_127))

    tasa_deposicion_137 = 0;
    elevaciones_137 = [1.05];

    for tasa_dep_137 in range(2017, 2050):
        expresion_137 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_137[-1];
        nueva_elevacion_137 = elevaciones_137[-1] - expresion_137 + tasa_SLR_RCP45_2000_2050;
        elevaciones_137.append(nueva_elevacion_137);
        tasa_deposicion_137 += expresion_137;

    for tasa_dep_137 in range(2050, 2100):
        expresion_137 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_137[-1];
        nueva_elevacion_137 = elevaciones_137[-1] - expresion_137 + tasa_SLR_RCP45_2050_2100;
        elevaciones_137.append(nueva_elevacion_137);
        tasa_deposicion_137 += expresion_137;
    print("Tasa de deposicion acumulada del rango 1.37-1.47 es: " + str(tasa_deposicion_137))

    tasa_deposicion_147 = 0;
    elevaciones_147 = [0.95];

    for tasa_dep_147 in range(2017, 2050):
        expresion_147 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_147[-1];
        nueva_elevacion_147 = elevaciones_147[-1] - expresion_147 + tasa_SLR_RCP45_2000_2050;
        elevaciones_147.append(nueva_elevacion_147);
        tasa_deposicion_147 += expresion_147;

    for tasa_dep_147 in range(2050, 2100):
        expresion_147 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_147[-1];
        nueva_elevacion_147 = elevaciones_147[-1] - expresion_147 + tasa_SLR_RCP45_2050_2100;
        elevaciones_147.append(nueva_elevacion_147);
        tasa_deposicion_147 += expresion_147;
    print("Tasa de deposicion acumulada del rango 1.47-1.57 es: " + str(tasa_deposicion_147))

    tasa_deposicion_157 = 0;
    elevaciones_157 = [0.85];

    for tasa_dep_157 in range(2017, 2050):
        expresion_157 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_157[-1];
        nueva_elevacion_157 = elevaciones_157[-1] - expresion_157 + tasa_SLR_RCP45_2000_2050;
        elevaciones_157.append(nueva_elevacion_157);
        tasa_deposicion_157 += expresion_157;

    for tasa_dep_157 in range(2050, 2100):
        expresion_157 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_157[-1];
        nueva_elevacion_157 = elevaciones_157[-1] - expresion_157 + tasa_SLR_RCP45_2050_2100;
        elevaciones_157.append(nueva_elevacion_157);
        tasa_deposicion_157 += expresion_157;
    print("Tasa de deposicion acumulada del rango 1.57-1.67 es: " + str(tasa_deposicion_157))

    tasa_deposicion_167 = 0;
    elevaciones_167 = [0.75];

    for tasa_dep_167 in range(2017, 2050):
        expresion_167 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_167[-1];
        nueva_elevacion_167 = elevaciones_167[-1] - expresion_167 + tasa_SLR_RCP45_2000_2050;
        elevaciones_167.append(nueva_elevacion_167);
        tasa_deposicion_167 += expresion_167;

    for tasa_dep_167 in range(2050, 2100):
        expresion_167 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_167[-1];
        nueva_elevacion_167 = elevaciones_167[-1] - expresion_167 + tasa_SLR_RCP45_2050_2100;
        elevaciones_167.append(nueva_elevacion_167);
        tasa_deposicion_167 += expresion_167;
    print("Tasa de deposicion acumulada del rango 1.67-1.77 es: " + str(tasa_deposicion_167))

    tasa_deposicion_177 = 0;
    elevaciones_177 = [0.65];

    for tasa_dep_177 in range(2017, 2050):
        expresion_177 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_177[-1];
        nueva_elevacion_177 = elevaciones_177[-1] - expresion_177 + tasa_SLR_RCP45_2000_2050;
        elevaciones_177.append(nueva_elevacion_177);
        tasa_deposicion_177 += expresion_177;

    for tasa_dep_177 in range(2050, 2100):
        expresion_177 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_177[-1];
        nueva_elevacion_177 = elevaciones_177[-1] - expresion_177 + tasa_SLR_RCP45_2050_2100;
        elevaciones_177.append(nueva_elevacion_177);
        tasa_deposicion_177 += expresion_177;
    print("Tasa de deposicion acumulada del rango 1.77-1.87 es: " + str(tasa_deposicion_177))

    tasa_deposicion_187 = 0;
    elevaciones_187 = [0.55];

    for tasa_dep_187 in range(2017, 2050):
        expresion_187 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_187[-1];
        nueva_elevacion_187 = elevaciones_187[-1] - expresion_187 + tasa_SLR_RCP45_2000_2050;
        elevaciones_187.append(nueva_elevacion_187);
        tasa_deposicion_187 += expresion_187;

    for tasa_dep_187 in range(2050, 2100):
        expresion_187 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_187[-1];
        nueva_elevacion_187 = elevaciones_187[-1] - expresion_187 + tasa_SLR_RCP45_2050_2100;
        elevaciones_187.append(nueva_elevacion_187);
        tasa_deposicion_187 += expresion_187;
    print("Tasa de deposicion acumulada del rango 1.87-1.97 es: " + str(tasa_deposicion_187))

    tasa_deposicion_197 = 0;
    elevaciones_197 = [0.45];

    for tasa_dep_197 in range(2017, 2050):
        expresion_197 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_197[-1];
        nueva_elevacion_197 = elevaciones_197[-1] - expresion_197 + tasa_SLR_RCP45_2000_2050;
        elevaciones_197.append(nueva_elevacion_197);
        tasa_deposicion_197 += expresion_197;

    for tasa_dep_197 in range(2050, 2100):
        expresion_197 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_197[-1];
        nueva_elevacion_197 = elevaciones_197[-1] - expresion_197 + tasa_SLR_RCP45_2050_2100;
        elevaciones_197.append(nueva_elevacion_197);
        tasa_deposicion_197 += expresion_197;
    print("Tasa de deposicion acumulada del rango 1.97-2.07 es: "+ str(tasa_deposicion_197))

    tasa_deposicion_207 = 0;
    elevaciones_207 = [0.35];

    for tasa_dep_207 in range(2017, 2050):
        expresion_207 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_207[-1];
        nueva_elevacion_207 = elevaciones_207[-1] - expresion_207 + tasa_SLR_RCP45_2000_2050;
        elevaciones_207.append(nueva_elevacion_207);
        tasa_deposicion_207 += expresion_207;

    for tasa_dep_207 in range(2050, 2100):
        expresion_207 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_207[-1];
        nueva_elevacion_207 = elevaciones_207[-1] - expresion_207 + tasa_SLR_RCP45_2050_2100;
        elevaciones_207.append(nueva_elevacion_207);
        tasa_deposicion_207 += expresion_207;
    print("Tasa de deposicion acumulada del rango 2.07-2.17 es: " + str(tasa_deposicion_207))

    tasa_deposicion_217 = 0;
    elevaciones_217 = [0.25];

    for tasa_dep_217 in range(2017, 2050):
        expresion_217 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_217[-1];
        nueva_elevacion_217 = elevaciones_217[-1] - expresion_217 + tasa_SLR_RCP45_2000_2050;
        elevaciones_217.append(nueva_elevacion_217);
        tasa_deposicion_217 += expresion_217;

    for tasa_dep_217 in range(2050, 2100):
        expresion_217 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_217[-1];
        nueva_elevacion_217 = elevaciones_217[-1] - expresion_217 + tasa_SLR_RCP45_2050_2100;
        elevaciones_217.append(nueva_elevacion_217);
        tasa_deposicion_217 += expresion_217;
    print("Tasa de deposicion acumulada del rango 2.17-2.27 es: " + str(tasa_deposicion_217))

    tasa_deposicion_227 = 0;
    elevaciones_227 = [0.15];

    for tasa_dep_227 in range(2017, 2050):
        expresion_227 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_227[-1];
        nueva_elevacion_227 = elevaciones_227[-1] - expresion_227 + tasa_SLR_RCP45_2000_2050;
        elevaciones_227.append(nueva_elevacion_227);
        tasa_deposicion_227 += expresion_227;

    for tasa_dep_227 in range(2050, 2100):
        expresion_227 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_227[-1];
        nueva_elevacion_227 = elevaciones_227[-1] - expresion_227 + tasa_SLR_RCP45_2050_2100;
        elevaciones_227.append(nueva_elevacion_227);
        tasa_deposicion_227 += expresion_227;
    print("Tasa de deposicion acumulada del rango 2.27-2.37 es: " + str(tasa_deposicion_227))

    tasa_deposicion_237 = 0;
    elevaciones_237 = [0.05];

    for tasa_dep_237 in range(2017, 2050):
        expresion_237 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_237[-1];
        nueva_elevacion_237 = elevaciones_237[-1] - expresion_237 + tasa_SLR_RCP45_2000_2050;
        elevaciones_237.append(nueva_elevacion_237);
        tasa_deposicion_237 += expresion_237;

    for tasa_dep_237 in range(2050, 2100):
        expresion_237 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_237[-1];
        nueva_elevacion_237 = elevaciones_237[-1] - expresion_237 + tasa_SLR_RCP45_2050_2100;
        elevaciones_237.append(nueva_elevacion_237);
        tasa_deposicion_237 += expresion_237;
    print("Tasa de deposicion acumulada del rango 2.37-2.47 es: " + str(tasa_deposicion_237))

    depo_247 = 0;
    elevaciones_247 = [0.0514];

    for deposicion_247 in range(2030, 2050):
        expr_247 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_247[-1];
        nueva_elevacion_247 = elevaciones_247[-1] - expr_247 + tasa_SLR_RCP45_2000_2050;
        elevaciones_247.append(nueva_elevacion_247);
        depo_247 += expr_247;

    for deposicion_247 in range(2050, 2100):
        expr_247 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_247[-1];
        nueva_elevacion_247 = elevaciones_247[-1] - expr_247 + tasa_SLR_RCP45_2050_2100;
        elevaciones_247.append(nueva_elevacion_247);
        depo_247 += expr_247;
    print("Tasa de deposicion acumulada del rango 2.47-2.57 es: " + str(depo_247))

    depo_257 = 0;
    elevaciones_257 = [0.0528];

    for deposicion_257 in range(2043, 2050):
        expr_257 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_257[-1];
        nueva_elevacion_257 = elevaciones_257[-1] - expr_257 + tasa_SLR_RCP45_2000_2050;
        elevaciones_257.append(nueva_elevacion_257);
        depo_257 += expr_257;

    for deposicion_257 in range(2050, 2100):
        expr_257 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_257[-1];
        nueva_elevacion_257 = elevaciones_257[-1] - expr_257 + tasa_SLR_RCP45_2050_2100;
        elevaciones_257.append(nueva_elevacion_257);
        depo_257 += expr_257;
    print("Tasa de deposicion acumulada del rango 2.57-2.67 es: " + str(depo_257))

    depo_267 = 0;
    elevaciones_267 = [0.0522];

    for deposicion_267 in range(2054, 2100):
        expr_267 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_267[-1];
        nueva_elevacion_267 = elevaciones_267[-1] - expr_267 + tasa_SLR_RCP45_2050_2100;
        elevaciones_267.append(nueva_elevacion_267);
        depo_267 += expr_267;
    print("Tasa de deposicion acumulada del rango 2.67-2.77 es: " + str(depo_267))

    depo_277 = 0;
    elevaciones_277 = [0.053];

    for deposicion_277 in range(2063,2100):
        expr_277 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_277[-1];
        nueva_elevacion_277 = elevaciones_277[-1] - expr_277 + tasa_SLR_RCP45_2050_2100;
        elevaciones_277.append(nueva_elevacion_277);
        depo_277 += expr_277;
    print("Tasa de deposicion acumulada del rango 2.77-2.87 es: " + str(depo_277))

    depo_287 = 0;
    elevaciones_287 = [0.0538];

    for deposicion_287 in range(2072,2100):
        expr_287 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_287[-1];
        nueva_elevacion_287 = elevaciones_287[-1] - expr_287 + tasa_SLR_RCP45_2050_2100;
        elevaciones_287.append(nueva_elevacion_287);
        depo_287 += expr_287;
    print("Tasa de deposicion acumulada del rango 2.87-2.97 es: " + str(depo_287))

    depo_297 = 0;
    elevaciones_297 = [0.0546];

    for deposicion_297 in range(2081,2100):
        expr_297 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_297[-1];
        nueva_elevacion_297 = elevaciones_297[-1] - expr_297 + tasa_SLR_RCP45_2050_2100;
        elevaciones_297.append(nueva_elevacion_297);
        depo_297 += expr_297;
    print("Tasa de deposicion acumulada del rango 2.97-3.07 es: " + str(depo_297))

    depo_307 = 0;
    elevaciones_307 = [0.0554];

    for deposicion_307 in range(2090, 2100):
        expr_307 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_307[-1];
        nueva_elevacion_307 = elevaciones_307[-1] - expr_307 + tasa_SLR_RCP45_2050_2100;
        elevaciones_307.append(nueva_elevacion_307);
        depo_307 += expr_307;
    print("Tasa de deposicion acumulada del rango 3.07-3.17 es: " + str(depo_307))

    depo_317 = 0;
    elevaciones_317 = [0.0562];

    for deposicion_317 in range(2099,2100):
        expr_317 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_317[-1];
        nueva_elevacion_317 = elevaciones_317[-1] - expr_317 + tasa_SLR_RCP45_2050_2100;
        elevaciones_317.append(nueva_elevacion_317);
        depo_317 += expr_317;
    print("Tasa de deposicion acumulada del rango 3.17-3.27 es: " + str(depo_317))

    deposicion_087_097 = 0;
    elev_regen_087 = [1.053];
    for dep_087_097 in range(2017, 2097):
        deposicion_087_097 += deposicion_marisma_regeneracion;
    for dep_087_097 in range(2097,2100):
        expresion_087_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_087[-1];
        nueva_ele_087 = elev_regen_087[-1]-expresion_087_bis+tasa_SLR_RCP45_2050_2100;
        elev_regen_087.append(nueva_ele_087);
        deposicion_087_097 += expresion_087_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 0.87-0.97 es:" + str(deposicion_087_097));

    deposicion_097_107 = 0;
    elev_regen_097 = [0.982];
    for dep_097_107 in range(2017, 2091):
        deposicion_097_107 += deposicion_marisma_regeneracion;
    for dep_097_107 in range(2091, 2100):
        expresion_097_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_097[
            -1];
        nueva_ele_097 = elev_regen_097[-1] - expresion_097_bis + tasa_SLR_RCP45_2050_2100;
        elev_regen_097.append(nueva_ele_097);
        deposicion_097_107 += expresion_097_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 0.97-1.07 es:" + str(deposicion_097_107));

    deposicion_107_117 = 0;
    elev_regen_107 = [0.911];
    for dep_107_117 in range(2017, 2085):
        deposicion_107_117 += deposicion_marisma_regeneracion;
    for dep_107_117 in range(2085, 2100):
        expresion_107_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_107[
            -1];
        nueva_ele_107 = elev_regen_107[-1] - expresion_107_bis + tasa_SLR_RCP45_2050_2100;
        elev_regen_107.append(nueva_ele_107);
        deposicion_107_117 += expresion_107_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 1.07-1.17 es:" + str(deposicion_107_117));

    deposicion_117_127 = 0;
    elev_regen_117 = [0.840];
    for dep_117_127 in range(2017, 2079):
        deposicion_117_127 += deposicion_marisma_regeneracion;
    for dep_117_127 in range(2079, 2100):
        expresion_117_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_117[
            -1];
        nueva_ele_117 = elev_regen_117[-1] - expresion_117_bis + tasa_SLR_RCP45_2050_2100;
        elev_regen_117.append(nueva_ele_117);
        deposicion_117_127 += expresion_117_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 1.17-1.27 es:" + str(deposicion_117_127));

    deposicion_127_137 = 0;
    elev_regen_127 = [0.773];
    for dep_127_137 in range(2017, 2072):
        deposicion_127_137 += deposicion_marisma_regeneracion;
    for dep_127_137 in range(2072, 2100):
        expresion_127_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_127[
            -1];
        nueva_ele_127 = elev_regen_127[-1] - expresion_127_bis + tasa_SLR_RCP45_2050_2100;
        elev_regen_127.append(nueva_ele_127);
        deposicion_127_137 += expresion_127_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 1.27-1.37 es:" + str(deposicion_127_137));

    deposicion_137_147 = 0;
    elev_regen_137 = [0.702];
    for dep_137_147 in range(2017, 2066):
        deposicion_137_147 += deposicion_marisma_regeneracion;
    for dep_137_147 in range(2066, 2100):
        expresion_137_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_137[
            -1];
        nueva_ele_137 = elev_regen_137[-1] - expresion_137_bis + tasa_SLR_RCP45_2050_2100;
        elev_regen_137.append(nueva_ele_137);
        deposicion_137_147 += expresion_137_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 1.37-1.47 es:" + str(deposicion_137_147));

    deposicion_147_157 = 0;
    elev_regen_147 = [0.631];
    for dep_147_157 in range(2017, 2060):
        deposicion_147_157 += deposicion_marisma_regeneracion;
    for dep_147_157 in range(2060, 2100):
        expresion_147_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_147[
            -1];
        nueva_ele_147 = elev_regen_147[-1] - expresion_147_bis + tasa_SLR_RCP45_2050_2100;
        elev_regen_147.append(nueva_ele_147);
        deposicion_147_157 += expresion_147_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 1.47-1.57 es:" + str(deposicion_147_157));

    deposicion_157_167 = 0;
    elev_regen_157 = [0.560];
    for dep_157_167 in range(2017, 2054):
        deposicion_157_167 += deposicion_marisma_regeneracion;
    for dep_157_167 in range(2054, 2100):
        expresion_157_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_157[
            -1];
        nueva_ele_157 = elev_regen_157[-1] - expresion_157_bis + tasa_SLR_RCP45_2050_2100;
        elev_regen_157.append(nueva_ele_157);
        deposicion_157_167 += expresion_157_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 1.57-1.67 es:" + str(deposicion_157_167));

    deposicion_167_177 = 0;
    elev_regen_167 = [
        0.504];  # Diferencia entre el nivel de marea alta (2.47) mas el SLR para ese año y la elevacion del
    # rango mas la deposicion hasta que llegue a los 2,2 metros aprox.
    for dep_167_177 in range(2017, 2047):
        deposicion_167_177 += deposicion_marisma_regeneracion
    for dep_167_177 in range(2047, 2050):
        expresion_167_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_167[
            -1];
        nueva_ele_167 = elev_regen_167[-1] - expresion_167_bis + tasa_SLR_RCP45_2000_2050;
        elev_regen_167.append(nueva_ele_167);
        deposicion_167_177 += expresion_167_bis;
    for dep_167_177 in range(2050, 2100):
        expresion_167_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_167[
            -1];
        nueva_ele_167 = elev_regen_167[-1] - expresion_167_bis + tasa_SLR_RCP45_2050_2100;
        elev_regen_167.append(nueva_ele_167);
        deposicion_167_177 += expresion_167_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 1.67-1.77 es:" + str(deposicion_167_177));

    deposicion_177_187 = 0;
    elev_regen_177 = [
        0.453];  # Diferencia entre el nivel de marea alta (2.47) mas el SLR para ese año y la elevacion del
    # rango mas la deposicion hasta que llegue a los 2,2 metros aprox.
    for dep_177_187 in range(2017, 2041):
        deposicion_177_187 += deposicion_marisma_regeneracion
    for dep_177_187 in range(2041, 2050):
        expresion_177_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_177[
            -1];
        nueva_ele_177 = elev_regen_177[-1] - expresion_177_bis + tasa_SLR_RCP45_2000_2050;
        elev_regen_177.append(nueva_ele_177);
        deposicion_177_187 += expresion_177_bis;
    for dep_177_187 in range(2050, 2100):
        expresion_177_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_177[
            -1];
        nueva_ele_177 = elev_regen_177[-1] - expresion_177_bis + tasa_SLR_RCP45_2050_2100;
        elev_regen_177.append(nueva_ele_177);
        deposicion_177_187 += expresion_177_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 1.77-1.87 es:" + str(deposicion_177_187));

    deposicion_187_197 = 0;
    elev_regen_187 = [
        0.402];  # Diferencia entre el nivel de marea alta (2.47) mas el SLR para ese año y la elevacion del
    # rango mas la deposicion hasta que llegue a los 2,2 metros aprox.
    for dep_187_197 in range(2017, 2035):
        deposicion_187_197 += deposicion_marisma_regeneracion
    for dep_187_197 in range(2035, 2050):
        expresion_187_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_187[
            -1];
        nueva_ele_187 = elev_regen_187[-1] - expresion_187_bis + tasa_SLR_RCP45_2000_2050;
        elev_regen_187.append(nueva_ele_187);
        deposicion_187_197 += expresion_187_bis;
    for dep_187_197 in range(2050, 2100):
        expresion_187_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_187[
            -1];
        nueva_ele_187 = elev_regen_187[-1] - expresion_187_bis + tasa_SLR_RCP45_2050_2100;
        elev_regen_187.append(nueva_ele_187);
        deposicion_187_197 += expresion_187_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 1.87-1.97 es:" + str(deposicion_187_197));

    deposicion_197_207 = 0;
    elev_regen_197 = [
        0.351];  # Diferencia entre el nivel de marea alta (2.47) mas el SLR para ese año y la elevacion del
    # rango mas la deposicion hasta que llegue a los 2,2 metros aprox.
    for dep_197_207 in range(2017, 2029):
        deposicion_197_207 += deposicion_marisma_regeneracion
    for dep_197_207 in range(2029, 2050):
        expresion_197_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_197[
            -1];
        nueva_ele_197 = elev_regen_197[-1] - expresion_197_bis + tasa_SLR_RCP45_2000_2050;
        elev_regen_197.append(nueva_ele_197);
        deposicion_197_207 += expresion_197_bis;
    for dep_197_207 in range(2050, 2100):
        expresion_197_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_197[
            -1];
        nueva_ele_197 = elev_regen_197[-1] - expresion_197_bis + tasa_SLR_RCP45_2050_2100;
        elev_regen_197.append(nueva_ele_197);
        deposicion_197_207 += expresion_197_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 1.97-2.07 es:" + str(deposicion_197_207));

    deposicion_207_217 = 0;
    elev_regen_207 = [
        0.300];  # Diferencia entre el nivel de marea alta (2.47) mas el SLR para ese año y la elevacion del
    # rango mas la deposicion hasta que llegue a los 2,2 metros aprox.
    for dep_207_217 in range(2017, 2023):
        deposicion_207_217 += deposicion_marisma_regeneracion
    for dep_207_217 in range(2023, 2050):
        expresion_207_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_207[
            -1];
        nueva_ele_207 = elev_regen_207[-1] - expresion_207_bis + tasa_SLR_RCP45_2000_2050;
        elev_regen_207.append(nueva_ele_207);
        deposicion_207_217 += expresion_207_bis;
    for dep_207_217 in range(2050, 2100):
        expresion_207_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_207[
            -1];
        nueva_ele_207 = elev_regen_207[-1] - expresion_207_bis + tasa_SLR_RCP45_2050_2100;
        elev_regen_207.append(nueva_ele_207);
        deposicion_207_217 += expresion_207_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 2.07-2.17 es:" + str(deposicion_207_217));

    # Ahora calculamos la deposicion que tendran las marismas reclamadas que no se inundan por la presencia de una barrera (natural o artificial)
    # que impide el flujo de agua de mar por su mayor altura (mas de 2,47). Obteniendo la elevacion mas frecuente mediante un histograma del raster
    # que da informacion a cerca de la elevacion de la barrera, se ha obtenido una elevacion de 2,6 metros (2'5-2'7), por lo que ahora, se calcula
    # cuando el SLR, en este caso referido al escenario RCP4.5 proyectado a 2100. Se obtiene que se inundara el año 2034, por lo que se aplicara una
    # acrecion de 16 mm por año (marisma en regeneracion) hasta que iguale su elevacion con la marisma colindante, que en este caso esta aproximadamente
    # a 2 metros de altura.Una vez que alcance esos 2 metros se aplica una tasa de acrecion de marisma natural y si esta a mas de 2,47 metros, una
    # deposicion igual a las zonas inundables por el SLR.

    tas_deposicion_MR_097_107 = 0;
    el_MReclamada_097 = [1.230];

    for t_097_107 in range(2034, 2096):
        tas_deposicion_MR_097_107 += deposicion_marisma_regeneracion;
    for t_097_107 in range(2096,2100):
        expr_MR_097 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_097[-1];
        nuev_el_MR_097 = el_MReclamada_097[-1] - expr_MR_097 + tasa_SLR_RCP45_2050_2100;
        el_MReclamada_097.append(nuev_el_MR_097);
        tas_deposicion_MR_097_107+=expr_MR_097;
    print("La deposicion de la marisma reclamada en el rango 0.97-1.07 sera de: " + str(tas_deposicion_MR_097_107))

    tas_deposicion_MR_107_117 = 0;
    el_MReclamada_107 = [1.164];

    for t_107_117 in range(2034, 2089):
        tas_deposicion_MR_107_117 += deposicion_marisma_regeneracion;
    for t_107_117 in range(2089, 2100):
        expr_MR_107 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_107[-1];
        nuev_el_MR_107 = el_MReclamada_107[-1] - expr_MR_107 + tasa_SLR_RCP45_2050_2100;
        el_MReclamada_107.append(nuev_el_MR_107);
        tas_deposicion_MR_107_117 += expr_MR_107;
    print("La deposicion de la marisma reclamada en el rango 1.07-1.17 sera de: " + str(tas_deposicion_MR_107_117))

    tas_deposicion_MR_117_127 = 0;
    el_MReclamada_117 = [1.093];

    for t_117_127 in range(2034, 2083):
        tas_deposicion_MR_117_127 += deposicion_marisma_regeneracion;
    for t_117_127 in range(2083, 2100):
        expr_MR_117 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_117[-1];
        nuev_el_MR_117 = el_MReclamada_117[-1] - expr_MR_117 + tasa_SLR_RCP45_2050_2100;
        el_MReclamada_117.append(nuev_el_MR_117);
        tas_deposicion_MR_117_127 += expr_MR_117;
    print("La deposicion de la marisma reclamada en el rango 1.17-1.27 sera de: " + str(tas_deposicion_MR_117_127))

    tas_deposicion_MR_127_137 = 0;
    el_MReclamada_127 = [1.021];

    for t_127_137 in range(2034, 2077):
        tas_deposicion_MR_127_137 += deposicion_marisma_regeneracion;
    for t_127_137 in range(2077, 2100):
        expr_MR_127 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_127[-1];
        nuev_el_MR_127 = el_MReclamada_127[-1] - expr_MR_127 + tasa_SLR_RCP45_2050_2100;
        el_MReclamada_127.append(nuev_el_MR_127);
        tas_deposicion_MR_127_137 += expr_MR_127;
    print("La deposicion de la marisma reclamada en el rango 1.27-1.37 sera de: " + str(tas_deposicion_MR_127_137))

    tas_deposicion_MR_137_147 = 0;
    el_MReclamada_137 = [0.950];

    for t_137_147 in range(2034, 2071):
        tas_deposicion_MR_137_147 += deposicion_marisma_regeneracion;
    for t_137_147 in range(2071, 2100):
        expr_MR_137 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_137[-1];
        nuev_el_MR_137 = el_MReclamada_137[-1] - expr_MR_137 + tasa_SLR_RCP45_2050_2100;
        el_MReclamada_137.append(nuev_el_MR_137);
        tas_deposicion_MR_137_147 += expr_MR_137;
    print("La deposicion de la marisma reclamada en el rango 1.37-1.47 sera de: " + str(tas_deposicion_MR_137_147))

    tas_deposicion_MR_147_157 = 0;
    el_MReclamada_147 = [0.884];

    for t_147_157 in range(2034, 2064):
        tas_deposicion_MR_147_157 += deposicion_marisma_regeneracion;
    for t_147_157 in range(2064, 2100):
        expr_MR_147 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_147[-1];
        nuev_el_MR_147 = el_MReclamada_147[-1] - expr_MR_147 + tasa_SLR_RCP45_2050_2100;
        el_MReclamada_147.append(nuev_el_MR_147);
        tas_deposicion_MR_147_157 += expr_MR_147;
    print("La deposicion de la marisma reclamada en el rango 1.47-1.57 sera de: " + str(tas_deposicion_MR_147_157))

    tas_deposicion_MR_157_167 = 0;
    el_MReclamada_157 = [0.813];

    for t_157_167 in range(2034, 2058):
        tas_deposicion_MR_157_167 += deposicion_marisma_regeneracion;
    for t_157_167 in range(2058, 2100):
        expr_MR_157 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_157[-1];
        nuev_el_MR_157 = el_MReclamada_157[-1] - expr_MR_157 + tasa_SLR_RCP45_2050_2100;
        el_MReclamada_157.append(nuev_el_MR_157);
        tas_deposicion_MR_157_167 += expr_MR_157;
    print("La deposicion de la marisma reclamada en el rango 1.57-1.67 sera de: " + str(tas_deposicion_MR_157_167))

    tas_deposicion_MR_167_177 = 0;
    el_MReclamada_167 = [0.741];

    for t_167_177 in range(2034, 2052):
        tas_deposicion_MR_167_177 += deposicion_marisma_regeneracion;
    for t_167_177 in range(2052, 2100):
        expr_MR_167 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_167[-1];
        nuev_el_MR_167 = el_MReclamada_167[-1] - expr_MR_167 + tasa_SLR_RCP45_2050_2100;
        el_MReclamada_167.append(nuev_el_MR_167);
        tas_deposicion_MR_167_177 += expr_MR_167;
    print("La deposicion de la marisma reclamada en el rango 1.67-1.77 sera de: " + str(tas_deposicion_MR_167_177))

    tas_deposicion_MReclamada_177_187 = 0;
    el_MReclamada_177 = [
        0.684];  # Las elevaciones se han obtenido calculando 2,47m + (0.0078 * (2046-2017))- elevacion cuando alcance el equilibrio

    for t_177_187 in range(2034, 2046):
        tas_deposicion_MReclamada_177_187 += deposicion_marisma_regeneracion;
    for t_177_187 in range(2046, 2050):
        expr_MR_177 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_177[-1];
        nuev_el_MR_177 = el_MReclamada_177[-1] - expr_MR_177 + tasa_SLR_RCP45_2000_2050;
        el_MReclamada_177.append(nuev_el_MR_177);
        tas_deposicion_MReclamada_177_187 += expr_MR_177;
    for t_177_187 in range(2050, 2100):
        expr_MR_177 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_177[-1];
        nuev_el_MR_177 = el_MReclamada_177[-1] - expr_MR_177 + tasa_SLR_RCP45_2050_2100;
        el_MReclamada_177.append(nuev_el_MR_177);
        tas_deposicion_MReclamada_177_187 += expr_MR_177;
    print("La deposicion de la marisma reclamada en el rango 1.77-1.87 sera de: " + str(
        tas_deposicion_MReclamada_177_187))

    tas_deposicion_MReclamada_187_197 = 0;
    el_MReclamada_187 = [
        0.641];  # Las elevaciones se han obtenido calculando 2,47m + (0.0078 * (2046-2017))- elevacion cuando alcance el equilibrio

    for t_187_197 in range(2034, 2039):
        tas_deposicion_MReclamada_187_197 += deposicion_marisma_regeneracion;
    for t_187_197 in range(2039, 2050):
        expr_MR_187 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_187[-1];
        nuev_el_MR_187 = el_MReclamada_187[-1] - expr_MR_187 + tasa_SLR_RCP45_2000_2050;
        el_MReclamada_187.append(nuev_el_MR_187);
        tas_deposicion_MReclamada_187_197 += expr_MR_187;
    for t_187_197 in range(2050, 2100):
        expr_MR_187 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_187[-1];
        nuev_el_MR_187 = el_MReclamada_187[-1] - expr_MR_187 + tasa_SLR_RCP45_2050_2100;
        el_MReclamada_187.append(nuev_el_MR_187);
        tas_deposicion_MReclamada_187_197 += expr_MR_187;
    print("La deposicion de la marisma reclamada en el rango 1.87-1.97 sera de: " + str(
        tas_deposicion_MReclamada_187_197))

    tas_deposicion_MReclamada_197_207 = 0;
    el_MReclamada_197 = [
        0.582];  # Las elevaciones se han obtenido calculando 2,47m + (0.0078 * (2046-2017))- elevacion cuando alcance el equilibrio

    for t_197_207 in range(2034, 2050):
        expr_MR_197 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_197[-1];
        nuev_el_MR_197 = el_MReclamada_197[-1] - expr_MR_197 + tasa_SLR_RCP45_2000_2050;
        el_MReclamada_197.append(nuev_el_MR_197);
        tas_deposicion_MReclamada_197_207 += expr_MR_197;
    for t_197_207 in range(2050, 2100):
        expr_MR_197 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_197[-1];
        nuev_el_MR_197 = el_MReclamada_197[-1] - expr_MR_197 + tasa_SLR_RCP45_2050_2100;
        el_MReclamada_197.append(nuev_el_MR_197);
        tas_deposicion_MReclamada_197_207 += expr_MR_197;
    print("La deposicion de la marisma reclamada en el rango 1.97-2.07 sera de: " + str(
        tas_deposicion_MReclamada_197_207));


    tas_deposicion_MReclamada_207_217 = 0;
    el_MReclamada_207 = [
        0.482];  # Las elevaciones se han obtenido calculando 2,47m + (0.0078 * (2046-2017))- elevacion cuando alcance el equilibrio

    for t_207_217 in range(2034, 2050):
        expr_MR_207 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_207[-1];
        nuev_el_MR_207 = el_MReclamada_207[-1] - expr_MR_207 + tasa_SLR_RCP45_2000_2050;
        el_MReclamada_207.append(nuev_el_MR_207);
        tas_deposicion_MReclamada_207_217 += expr_MR_207;
    for t_207_217 in range(2050, 2100):
        expr_MR_207 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_207[-1];
        nuev_el_MR_207 = el_MReclamada_207[-1] - expr_MR_207 + tasa_SLR_RCP45_2050_2100;
        el_MReclamada_207.append(nuev_el_MR_207);
        tas_deposicion_MReclamada_207_217 += expr_MR_207;
    print("La deposicion de la marisma reclamada en el rango 2.07-2.17 sera de: " + str(
        tas_deposicion_MReclamada_207_217))

    tas_deposicion_MReclamada_217_227 = 0;
    el_MReclamada_217 = [
        0.382];  # Las elevaciones se han obtenido calculando 2,47m + (0.0078 * (2046-2017))- elevacion cuando alcance el equilibrio

    for t_217_227 in range(2034, 2050):
        expr_MR_217 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_217[-1];
        nuev_el_MR_217 = el_MReclamada_217[-1] - expr_MR_217 + tasa_SLR_RCP45_2000_2050;
        el_MReclamada_217.append(nuev_el_MR_217);
        tas_deposicion_MReclamada_217_227 += expr_MR_217;
    for t_217_227 in range(2050, 2100):
        expr_MR_217 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_217[-1];
        nuev_el_MR_217 = el_MReclamada_217[-1] - expr_MR_217 + tasa_SLR_RCP45_2050_2100;
        el_MReclamada_217.append(nuev_el_MR_217);
        tas_deposicion_MReclamada_217_227 += expr_MR_217;
    print("La deposicion de la marisma reclamada en el rango 2.17-2.27 sera de: " + str(
        tas_deposicion_MReclamada_217_227))

    tas_deposicion_MReclamada_227_237 = 0;
    el_MReclamada_227 = [
        0.282];  # Las elevaciones se han obtenido calculando 2,47m + (0.0078 * (2046-2017))- elevacion cuando alcance el equilibrio

    for t_227_237 in range(2034, 2050):
        expr_MR_227 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_227[-1];
        nuev_el_MR_227 = el_MReclamada_227[-1] - expr_MR_227 + tasa_SLR_RCP45_2000_2050;
        el_MReclamada_227.append(nuev_el_MR_227);
        tas_deposicion_MReclamada_227_237 += expr_MR_227;
    for t_227_237 in range(2050, 2100):
        expr_MR_227 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_227[-1];
        nuev_el_MR_227 = el_MReclamada_227[-1] - expr_MR_227 + tasa_SLR_RCP45_2050_2100;
        el_MReclamada_227.append(nuev_el_MR_227);
        tas_deposicion_MReclamada_227_237 += expr_MR_227;
    print("La deposicion de la marisma reclamada en el rango 2.27-2.37 sera de: " + str(
        tas_deposicion_MReclamada_227_237))

    tas_deposicion_MReclamada_237_247 = 0;
    el_MReclamada_237 = [
        0.182];  # Las elevaciones se han obtenido calculando 2,47m + (0.0078 * (2046-2017))- elevacion cuando alcance el equilibrio

    for t_237_247 in range(2034, 2050):
        expr_MR_237 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_237[-1];
        nuev_el_MR_237 = el_MReclamada_237[-1] - expr_MR_237 + tasa_SLR_RCP45_2000_2050;
        el_MReclamada_237.append(nuev_el_MR_237);
        tas_deposicion_MReclamada_237_247 += expr_MR_237;
    for t_237_247 in range(2050, 2100):
        expr_MR_237 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_237[-1];
        nuev_el_MR_237 = el_MReclamada_237[-1] - expr_MR_237 + tasa_SLR_RCP45_2050_2100;
        el_MReclamada_237.append(nuev_el_MR_237);
        tas_deposicion_MReclamada_237_247 += expr_MR_237;
    print("La deposicion de la marisma reclamada en el rango 2.37-2.47 sera de: " + str(
        tas_deposicion_MReclamada_237_247))

    # Reclasificamos el raster de la marisma reclamada que se volvera a inundar con el SLR con la sedimentacion que tendra
    # cada rango de elevaciones:
    depo_maris_reclamada_RCP45_2100 = Reclassify(raster_marisma_reclamada_errota, "VALUE",RemapRange([[-1000000, 970, "NODATA"],
                                        [970,1070, round(tas_deposicion_MR_097_107*1000)],[1070,1170, round(tas_deposicion_MR_107_117*1000)],
                                        [1170,1270, round(tas_deposicion_MR_117_127*1000)],[1270,1370, round(tas_deposicion_MR_127_137*1000)],
                                        [1370,1470, round(tas_deposicion_MR_137_147*1000)], [1470,1570, round(tas_deposicion_MR_147_157*1000)],
                                        [1570,1670, round(tas_deposicion_MR_157_167*1000)], [1670,1770, round(tas_deposicion_MR_167_177*1000)],
                                        [1770,1870, round(tas_deposicion_MReclamada_177_187*1000)], [1870,1970, round(tas_deposicion_MReclamada_187_197*1000)],
                                        [1970,2070, round(tas_deposicion_MReclamada_197_207*1000)], [2070,2170, round(tas_deposicion_MReclamada_207_217*1000)],
                                        [2170,2270, round(tas_deposicion_MReclamada_217_227*1000)], [2270,2370, round(tas_deposicion_MReclamada_227_237*1000)],
                                        [2370,2470, round(tas_deposicion_MReclamada_237_247*1000)], [2470, 2570, round(depo_247*1000)], [2570, 2670, round(depo_257*1000)], [2670, 2770, round(depo_267*1000)],
                                        [2770, 2870, round(depo_277*1000)], [2870,2970, round(depo_287*1000)],[2970, 3070, round(depo_297*1000)], [3070, 3170, round(depo_307*1000)],
                                        [3170, 3270, round(depo_317*1000)], [3270, 3287,0],  [3287, 10000000, "NODATA"]]))
    depo_maris_reclamada_RCP45_2100.save(
        r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Deposicion_marisma_Reclamada_RCP45_2100");
    direc_depo_marisma_reclamada_RCP45_2100 = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Deposicion_marisma_Reclamada_RCP45_2100";

    # Reclasificamos el raster de las marismas en regeneracion para tener la deposicion por rangos que tendra dicha zona:
    depo_maris_regeneracion_RCP45_2100 = Reclassify(raster_marisma_regeneracion, "VALUE",RemapRange([[-10000, 870, "NODATA"],
                                            [870,970, round(deposicion_087_097*1000)],[970,1070, round(deposicion_097_107*1000)],
                                            [1070,1170, round(deposicion_107_117*1000)],[1170,1270, round(deposicion_117_127*1000)],
                                            [1270,1370, round(deposicion_127_137*1000)],[1370, 1470, round(deposicion_137_147*1000)],
                                            [1470,1570, round(deposicion_147_157*1000)],[1570,1670, round(deposicion_157_167*1000)],
                                            [1670, 1770, round(deposicion_167_177 * 1000)],
                                            [1770, 1870, round(deposicion_177_187 * 1000)],[1870, 1970, round(deposicion_187_197 * 1000)],
                                            [1970, 2070, round(deposicion_197_207 * 1000)], [2070, 2170, round(deposicion_207_217 * 1000)],
                                            [2170, 2270, round(tasa_deposicion_217 * 1000)],[2270, 2370, round(tasa_deposicion_227 * 1000)],
                                            [2370, 2470, round(tasa_deposicion_237 * 1000)], [2470, 2570, round(depo_247 * 1000)],
                                            [2570, 2670, round(depo_257 * 1000)], [2670, 2770, round(depo_267*1000)],[2770,2870, round(depo_277*1000)],
                                            [2870,2970, round(depo_287*1000)],[2970,3070, round(depo_297*1000)],[3070,3170, round(depo_307*1000)],
                                            [3170,3270,round(depo_317*1000)], [3270, 3287,0], [3287, 100000000, "NODATA"]]))
    depo_maris_regeneracion_RCP45_2100.save(
        r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Deposicion_marisma_regen_RCP45_2100")
    direc_depo_maris_regeneracion_RCP45_2100 = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Deposicion_marisma_regen_RCP45_2100";

    #Reclasificamos el raster con los datos de la tasa de deposicion, por rangos, para representar la tasa de deposicion (aumento de
    # la elevacion en mm para el año 2050 en la zona de estudio para el escenario RCP4.5 y el año 2050:
    deposicion_RCP45_2100 = Reclassify(raster_Marisma, "VALUE", RemapRange([[-10000, 870,"NODATA"],[870, 970, round(tasa_deposicion_087*1000)],
                                 [970, 1070, round(tasa_deposicion_097*1000)], [1070, 1170, round(tasa_deposicion_107*1000)], [1170, 1270, round(tasa_deposicion_117*1000)],
                                 [1270, 1370, round(tasa_deposicion_127*1000)], [1370, 1470, round(tasa_deposicion_137*1000)], [1470, 1570, round(tasa_deposicion_147*1000)],
                                 [1570, 1670, round(tasa_deposicion_157*1000)], [1670, 1770, round(tasa_deposicion_167*1000)], [1770, 1870, round(tasa_deposicion_177*1000)],
                                 [1870, 1970, round(tasa_deposicion_187*1000)], [1970, 2070, round(tasa_deposicion_197*1000)], [2070, 2170, round(tasa_deposicion_207*1000)],
                                 [2170, 2270, round(tasa_deposicion_217*1000)], [2270, 2370, round(tasa_deposicion_227*1000)], [2370, 2470, round(tasa_deposicion_237*1000)],
                                 [2470, 2570, round(depo_247*1000)], [2570, 2670, round(depo_257*1000)], [2670, 2770, round(depo_267*1000)],
                                 [2770, 2870, round(depo_277*1000)], [2870,2970, round(depo_287*1000)],[2970, 3070, round(depo_297*1000)], [3070, 3170, round(depo_307*1000)],
                                 [3170, 3270, round(depo_317*1000)], [3270, 3287,0],  [3287, 10000000, "NODATA"]]))
    deposicion_RCP45_2100.save(r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Deposicion_RCP45_2100")
    direcc_depo_RCP45_2100 = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Deposicion_RCP45_2100"

    # Reclasificamos el raster de marismas de zonas inundables por el SLR (zonas de cultivo) para tener en cuenta la interaccion
    # deposicion-SLR en las zonas que se inundarán con el SLR:
    depo_RCP45_2100_zonas_inundables = Reclassify(raster_zonas_cultivo, "VALUE",RemapRange([[870, 2570, round(depo_247 * 1000)],
                                            [2570, 2670, round(depo_257 * 1000)],[2670, 2770, round(depo_267 * 1000)],[2770, 2870, round(depo_277 * 1000)],
                                            [2870, 2970,round(depo_287 * 1000)], [2970, 3070,round(depo_297 * 1000)],[3070, 3170,round(depo_307 * 1000)],
                                            [3170, 3270,round(depo_317 * 1000)],[3270,3287,0], [3287, 10000000, "NODATA"]]));
    depo_RCP45_2100_zonas_inundables.save(
        r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Deposicion_RCP45_2100_zonas_inundables")
    direcc_depo_RCP45_2100_zonas_inundables = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Deposicion_RCP45_2100_zonas_inundables"

    #Ahora ya tenemos el raster con la deposicion que habra en la zona de estudio segun el escenario RCP4.5 y para el año 2100,
    #asumiendo que desde el limite inferior hasta el superior donde se encuentran las marismas de Urdaibai de acuerdo a distintos
    #estudios, son las potenciales zonas de las marismas (aunque en realidad no haya por distintos factores y suponiendo que serían
    #marismas consolidadas con unas tasas de deposicion acorde a su elevacion.

    #Pues bien, sumamos los dos rasteres (elevacion en mm y deposicion en mm) para obtener la nueva altura que tendra la marisma.
    elevacion_RCP45_2100 = RasterCalculator([raster_Marisma, direcc_depo_RCP45_2100], ["marisma", "depo"],
                                            "(marisma+depo)")
    elevacion_RCP45_2100.save(
       r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Elevacion_RCP45_2100")
    direc_elevacion_RCP45_2100 = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Elevacion_RCP45_2100"

    elevacion_RCP45_2100_zona_inundable = RasterCalculator([raster_zonas_cultivo, direcc_depo_RCP45_2100_zonas_inundables],["zonas_inun", "depo_inun"], "(zonas_inun+depo_inun)")
    elevacion_RCP45_2100_zona_inundable.save(
        r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Elevacion_RCP45_2100_zonas_inundables");
    direc_elevacion_RCP45_2100_zonas_inundables = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Elevacion_RCP45_2100_zonas_inundables";

    elevacion_marisma_regener_RCP45_2100 = RasterCalculator([raster_marisma_regeneracion, direc_depo_maris_regeneracion_RCP45_2100],
        ["mar_reg", "deposi_regen"], "(mar_reg + deposi_regen)")
    elevacion_marisma_regener_RCP45_2100.save(
        r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Elevacion_marism_regener_RCP45_2100")
    direc_elevacion_marisma_regener_RCP45_2100 = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Elevacion_marism_regener_RCP45_2100";

    elevacion_marisma_reclamada_RCP45_2100 = RasterCalculator ([raster_marisma_reclamada_errota, direc_depo_marisma_reclamada_RCP45_2100],
                                                               ["MR", "dep_MR"], "(MR + dep_MR)")
    elevacion_marisma_reclamada_RCP45_2100.save(r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Elevacion_mari_reclamada_RCP45_2100");
    direc_elevacion_marisma_reclamada_RCP45_2100 = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Elevacion_mari_reclamada_RCP45_2100";

    #Una vez que tenemos la elevacion nueva de la zona de estudio debido a la deposicion fusionamos los rasteres de la nueva
    #elevacion de la marisma con el raster de elevaciones original para que tenga las nuevas elevaciones y tenga en cuenta los
    #valores del raster original en las zonas donde no hay marisma (y asi no ponga "NODATA").
    comb_elevacion_RCP45_2100 = arcpy.management.MosaicToNewRaster([direc_elevacion_RCP45_2100, direc_elevacion_RCP45_2100_zonas_inundables, direc_elevacion_marisma_regener_RCP45_2100,direc_elevacion_marisma_reclamada_RCP45_2100], r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb",
                                    "Elevacion_Combi_Terreno_RCP45_2100", 25830, "32_BIT_FLOAT", 1, 1, "FIRST")

    #Ya tenemos el la elevacion que habra en la zona de estudio en 2050 segun el escenario 2050, ahora volvemos a reclasificar dicho
    #raster para obtener la potencial distribucion de la marisma en dicho escenario y año:
    pot_distribucion_RCP45_2100 = Reclassify(comb_elevacion_RCP45_2100, "VALUE", RemapRange([[-100000,1687,"NODATA"], [1687,3287,0],[3287, 1000000,"NODATA"]]))
    pot_distribucion_RCP45_2100.save(r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Pot_Distribucion_RCP45_2100")

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
        nueva_elevacion_087 = elevaciones_087[-1] - expresion_087 + tasa_SLR_RCP85_2000_2050;
        elevaciones_087.append(nueva_elevacion_087);
        tasa_deposicion_087+= expresion_087;

    for tasa_dep_087 in range(2050,2100):
        expresion_087 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_087[-1];
        nueva_elevacion_087 = elevaciones_087[-1] - expresion_087 + tasa_SLR_RCP85_2050_2100;
        elevaciones_087.append(nueva_elevacion_087);
        tasa_deposicion_087+= expresion_087;
    print("Tasa de deposición acumulada del rango 0.87-0.97 es: " + str(tasa_deposicion_087))

    #Volvemos a calcular las tasas de deposiciones pero ahora para todos los rangos de valores (desde 0.87 hasta 2.47 metros, cada
    #10 centimetros):
    tasa_deposicion_097 = 0;
    elevaciones_097 = [1.45];

    for tasa_dep_097 in range(2017,2050):
        expresion_097 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_097[-1];
        nueva_elevacion_097 = elevaciones_097[-1] - expresion_097 + tasa_SLR_RCP85_2000_2050;
        elevaciones_097.append(nueva_elevacion_097);
        tasa_deposicion_097+= expresion_097;

    for tasa_dep_097 in range(2050,2100):
        expresion_097 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_097[-1];
        nueva_elevacion_097 = elevaciones_097[-1] - expresion_097 + tasa_SLR_RCP85_2050_2100;
        elevaciones_097.append(nueva_elevacion_097);
        tasa_deposicion_097+= expresion_097;
    print("Tasa de deposición acumulada del rango 0.97-1.07 es: " + str(tasa_deposicion_097))

    tasa_deposicion_107 = 0;
    elevaciones_107 = [1.35];

    for tasa_dep_107 in range(2017, 2050):
        expresion_107 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_107[-1];
        nueva_elevacion_107 = elevaciones_107[-1] - expresion_107 + tasa_SLR_RCP85_2000_2050;
        elevaciones_107.append(nueva_elevacion_107);
        tasa_deposicion_107 += expresion_107;

    for tasa_dep_107 in range(2050, 2100):
        expresion_107 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_107[-1];
        nueva_elevacion_107 = elevaciones_107[-1] - expresion_107 + tasa_SLR_RCP85_2050_2100;
        elevaciones_107.append(nueva_elevacion_107);
        tasa_deposicion_107 += expresion_107;
    print("Tasa de deposicion acumulada del rango 1.07-1.17 es: " + str(tasa_deposicion_107))

    tasa_deposicion_117 = 0;
    elevaciones_117 = [1.25];

    for tasa_dep_117 in range(2017, 2050):
        expresion_117 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_117[-1];
        nueva_elevacion_117 = elevaciones_117[-1] - expresion_117 + tasa_SLR_RCP85_2000_2050;
        elevaciones_117.append(nueva_elevacion_117);
        tasa_deposicion_117 += expresion_117;

    for tasa_dep_117 in range(2050, 2100):
        expresion_117 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_117[-1];
        nueva_elevacion_117 = elevaciones_117[-1] - expresion_117 + tasa_SLR_RCP85_2050_2100;
        elevaciones_117.append(nueva_elevacion_117);
        tasa_deposicion_117 += expresion_117;
    print("Tasa de deposicion acumulada del rango 1.17-1.27 es: " + str(tasa_deposicion_117))

    tasa_deposicion_127 = 0;
    elevaciones_127 = [1.15];

    for tasa_dep_127 in range(2017, 2050):
        expresion_127 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_127[-1];
        nueva_elevacion_127 = elevaciones_127[-1] - expresion_127 + tasa_SLR_RCP85_2000_2050;
        elevaciones_127.append(nueva_elevacion_127);
        tasa_deposicion_127 += expresion_127;

    for tasa_dep_127 in range(2050, 2100):
        expresion_127 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_127[-1];
        nueva_elevacion_127 = elevaciones_127[-1] - expresion_127 + tasa_SLR_RCP85_2050_2100;
        elevaciones_127.append(nueva_elevacion_127);
        tasa_deposicion_127 += expresion_127;
    print("Tasa de deposicion acumulada del rango 1.27-1.37 es: " + str(tasa_deposicion_127))

    tasa_deposicion_137 = 0;
    elevaciones_137 = [1.05];

    for tasa_dep_137 in range(2017, 2050):
        expresion_137 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_137[-1];
        nueva_elevacion_137 = elevaciones_137[-1] - expresion_137 + tasa_SLR_RCP85_2000_2050;
        elevaciones_137.append(nueva_elevacion_137);
        tasa_deposicion_137 += expresion_137;

    for tasa_dep_137 in range(2050, 2100):
        expresion_137 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_137[-1];
        nueva_elevacion_137 = elevaciones_137[-1] - expresion_137 + tasa_SLR_RCP85_2050_2100;
        elevaciones_137.append(nueva_elevacion_137);
        tasa_deposicion_137 += expresion_137;
    print("Tasa de deposicion acumulada del rango 1.37-1.47 es: " + str(tasa_deposicion_137))

    tasa_deposicion_147 = 0;
    elevaciones_147 = [0.95];

    for tasa_dep_147 in range(2017, 2050):
        expresion_147 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_147[-1];
        nueva_elevacion_147 = elevaciones_147[-1] - expresion_147 + tasa_SLR_RCP85_2000_2050;
        elevaciones_147.append(nueva_elevacion_147);
        tasa_deposicion_147 += expresion_147;

    for tasa_dep_147 in range(2050, 2100):
        expresion_147 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_147[-1];
        nueva_elevacion_147 = elevaciones_147[-1] - expresion_147 + tasa_SLR_RCP85_2050_2100;
        elevaciones_147.append(nueva_elevacion_147);
        tasa_deposicion_147 += expresion_147;
    print("Tasa de deposicion acumulada del rango 1.47-1.57 es: " + str(tasa_deposicion_147))

    tasa_deposicion_157 = 0;
    elevaciones_157 = [0.85];

    for tasa_dep_157 in range(2017, 2050):
        expresion_157 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_157[-1];
        nueva_elevacion_157 = elevaciones_157[-1] - expresion_157 + tasa_SLR_RCP85_2000_2050;
        elevaciones_157.append(nueva_elevacion_157);
        tasa_deposicion_157 += expresion_157;

    for tasa_dep_157 in range(2050, 2100):
        expresion_157 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_157[-1];
        nueva_elevacion_157 = elevaciones_157[-1] - expresion_157 + tasa_SLR_RCP85_2050_2100;
        elevaciones_157.append(nueva_elevacion_157);
        tasa_deposicion_157 += expresion_157;
    print("Tasa de deposicion acumulada del rango 1.57-1.67 es: " + str(tasa_deposicion_157))

    tasa_deposicion_167 = 0;
    elevaciones_167 = [0.75];

    for tasa_dep_167 in range(2017, 2050):
        expresion_167 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_167[-1];
        nueva_elevacion_167 = elevaciones_167[-1] - expresion_167 + tasa_SLR_RCP85_2000_2050;
        elevaciones_167.append(nueva_elevacion_167);
        tasa_deposicion_167 += expresion_167;

    for tasa_dep_167 in range(2050, 2100):
        expresion_167 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_167[-1];
        nueva_elevacion_167 = elevaciones_167[-1] - expresion_167 + tasa_SLR_RCP85_2050_2100;
        elevaciones_167.append(nueva_elevacion_167);
        tasa_deposicion_167 += expresion_167;
    print("Tasa de deposicion acumulada del rango 1.67-1.77 es: " + str(tasa_deposicion_167))

    tasa_deposicion_177 = 0;
    elevaciones_177 = [0.65];

    for tasa_dep_177 in range(2017, 2050):
        expresion_177 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_177[-1];
        nueva_elevacion_177 = elevaciones_177[-1] - expresion_177 + tasa_SLR_RCP85_2000_2050;
        elevaciones_177.append(nueva_elevacion_177);
        tasa_deposicion_177 += expresion_177;

    for tasa_dep_177 in range(2050, 2100):
        expresion_177 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_177[-1];
        nueva_elevacion_177 = elevaciones_177[-1] - expresion_177 + tasa_SLR_RCP85_2050_2100;
        elevaciones_177.append(nueva_elevacion_177);
        tasa_deposicion_177 += expresion_177;
    print("Tasa de deposicion acumulada del rango 1.77-1.87 es: " + str(tasa_deposicion_177))

    tasa_deposicion_187 = 0;
    elevaciones_187 = [0.55];

    for tasa_dep_187 in range(2017, 2050):
        expresion_187 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_187[-1];
        nueva_elevacion_187 = elevaciones_187[-1] - expresion_187 + tasa_SLR_RCP85_2000_2050;
        elevaciones_187.append(nueva_elevacion_187);
        tasa_deposicion_187 += expresion_187;

    for tasa_dep_187 in range(2050, 2100):
        expresion_187 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_187[-1];
        nueva_elevacion_187 = elevaciones_187[-1] - expresion_187 + tasa_SLR_RCP85_2050_2100;
        elevaciones_187.append(nueva_elevacion_187);
        tasa_deposicion_187 += expresion_187;
    print("Tasa de deposicion acumulada del rango 1.87-1.97 es: " + str(tasa_deposicion_187))

    tasa_deposicion_197 = 0;
    elevaciones_197 = [0.45];

    for tasa_dep_197 in range(2017, 2050):
        expresion_197 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_197[-1];
        nueva_elevacion_197 = elevaciones_197[-1] - expresion_197 + tasa_SLR_RCP85_2000_2050;
        elevaciones_197.append(nueva_elevacion_197);
        tasa_deposicion_197 += expresion_197;

    for tasa_dep_197 in range(2050, 2100):
        expresion_197 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_197[-1];
        nueva_elevacion_197 = elevaciones_197[-1] - expresion_197 + tasa_SLR_RCP85_2050_2100;
        elevaciones_197.append(nueva_elevacion_197);
        tasa_deposicion_197 += expresion_197;
    print("Tasa de deposicion acumulada del rango 1.97-2.07 es: "+ str(tasa_deposicion_197))

    tasa_deposicion_207 = 0;
    elevaciones_207 = [0.35];

    for tasa_dep_207 in range(2017, 2050):
        expresion_207 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_207[-1];
        nueva_elevacion_207 = elevaciones_207[-1] - expresion_207 + tasa_SLR_RCP85_2000_2050;
        elevaciones_207.append(nueva_elevacion_207);
        tasa_deposicion_207 += expresion_207;

    for tasa_dep_207 in range(2050, 2100):
        expresion_207 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_207[-1];
        nueva_elevacion_207 = elevaciones_207[-1] - expresion_207 + tasa_SLR_RCP85_2050_2100;
        elevaciones_207.append(nueva_elevacion_207);
        tasa_deposicion_207 += expresion_207;
    print("Tasa de deposicion acumulada del rango 2.07-2.17 es: " + str(tasa_deposicion_207))

    tasa_deposicion_217 = 0;
    elevaciones_217 = [0.25];

    for tasa_dep_217 in range(2017, 2050):
        expresion_217 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_217[-1];
        nueva_elevacion_217 = elevaciones_217[-1] - expresion_217 + tasa_SLR_RCP85_2000_2050;
        elevaciones_217.append(nueva_elevacion_217);
        tasa_deposicion_217 += expresion_217;

    for tasa_dep_217 in range(2050, 2100):
        expresion_217 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_217[-1];
        nueva_elevacion_217 = elevaciones_217[-1] - expresion_217 + tasa_SLR_RCP85_2050_2100;
        elevaciones_217.append(nueva_elevacion_217);
        tasa_deposicion_217 += expresion_217;
    print("Tasa de deposicion acumulada del rango 2.17-2.27 es: " + str(tasa_deposicion_217))

    tasa_deposicion_227 = 0;
    elevaciones_227 = [0.15];

    for tasa_dep_227 in range(2017, 2050):
        expresion_227 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_227[-1];
        nueva_elevacion_227 = elevaciones_227[-1] - expresion_227 + tasa_SLR_RCP85_2000_2050;
        elevaciones_227.append(nueva_elevacion_227);
        tasa_deposicion_227 += expresion_227;

    for tasa_dep_227 in range(2050, 2100):
        expresion_227 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_227[-1];
        nueva_elevacion_227 = elevaciones_227[-1] - expresion_227 + tasa_SLR_RCP85_2050_2100;
        elevaciones_227.append(nueva_elevacion_227);
        tasa_deposicion_227 += expresion_227;
    print("Tasa de deposicion acumulada del rango 2.27-2.37 es: " + str(tasa_deposicion_227))

    tasa_deposicion_237 = 0;
    elevaciones_237 = [0.05];

    for tasa_dep_237 in range(2017, 2050):
        expresion_237 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_237[-1];
        nueva_elevacion_237 = elevaciones_237[-1] - expresion_237 + tasa_SLR_RCP85_2000_2050;
        elevaciones_237.append(nueva_elevacion_237);
        tasa_deposicion_237 += expresion_237;

    for tasa_dep_237 in range(2050, 2100):
        expresion_237 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_237[-1];
        nueva_elevacion_237 = elevaciones_237[-1] - expresion_237 + tasa_SLR_RCP85_2050_2100;
        elevaciones_237.append(nueva_elevacion_237);
        tasa_deposicion_237 += expresion_237;
    print("Tasa de deposicion acumulada del rango 2.37-2.47 es: " + str(tasa_deposicion_237))

    #ZONAS INUNDABLES:
    depo_247 = 0;
    elevaciones_247 = [0.0532];

    for deposicion_247 in range(2029, 2050):
        expr_247 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_247[-1];
        nueva_elevacion_247 = elevaciones_247[-1] - expr_247 + tasa_SLR_RCP85_2000_2050;
        elevaciones_247.append(nueva_elevacion_247);
        depo_247 += expr_247;
    for deposicion_247 in range(2050, 2100):
        expr_247 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_247[-1];
        nueva_elevacion_247 = elevaciones_247[-1] - expr_247 + tasa_SLR_RCP85_2050_2100;
        elevaciones_247.append(nueva_elevacion_247);
        depo_247 += expr_247;
    print("Tasa de deposicion acumulada del rango 2.47-2.57 es: " + str(depo_247))

    depo_257 = 0;
    elevaciones_257 = [0.0564];

    for deposicion_257 in range(2041, 2050):
        expr_257 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_257[-1];
        nueva_elevacion_257 = elevaciones_257[-1] - expr_257 + tasa_SLR_RCP85_2000_2050;
        elevaciones_257.append(nueva_elevacion_257);
        depo_257 += expr_257;
    for deposicion_257 in range(2050, 2100):
        expr_257 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_257[-1];
        nueva_elevacion_257 = elevaciones_257[-1] - expr_257 + tasa_SLR_RCP85_2050_2100;
        elevaciones_257.append(nueva_elevacion_257);
        depo_257 += expr_257;
    print("Tasa de deposicion acumulada del rango 2.57-2.67 es: " + str(depo_257))

    depo_267 = 0;
    elevaciones_267 = [0.0634];

    for deposicion_267 in range(2052, 2100):
        expr_267 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_267[-1];
        nueva_elevacion_267 = elevaciones_267[-1] - expr_267 + tasa_SLR_RCP85_2050_2100;
        elevaciones_267.append(nueva_elevacion_267);
        depo_267 += expr_267;
    print("Tasa de deposicion acumulada del rango 2.67-2.77 es: " + str(depo_267))

    depo_277 = 0;
    elevaciones_277 = [0.0522];

    for deposicion_277 in range (2058,2100):
        expr_277 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_277[-1];
        nueva_elevacion_277 = elevaciones_277[-1] - expr_277 + tasa_SLR_RCP85_2050_2100;
        elevaciones_277.append(nueva_elevacion_277);
        depo_277 += expr_277;
    print ("Tasa de deposicion acumulada del rango de 2.77-2.87 es: " + str(depo_277))

    depo_287 = 0;
    elevaciones_287 = [0.0558];

    for deposicion_287 in range(2065, 2100):
        expr_287 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_287[-1];
        nueva_elevacion_287 = elevaciones_287[-1] - expr_287 + tasa_SLR_RCP85_2050_2100;
        elevaciones_287.append(nueva_elevacion_287);
        depo_287 += expr_287;
    print ("Tasa de deposicion acumulada del rango de 2.87-2.97 es: " + str(depo_287))

    depo_297 = 0;
    elevaciones_297 = [0.0594];

    for deposicion_297 in range(2072, 2100):
        expr_297 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_297[-1];
        nueva_elevacion_297 = elevaciones_297[-1] - expr_297 + tasa_SLR_RCP85_2050_2100;
        elevaciones_297.append(nueva_elevacion_297);
        depo_297 += expr_297;
    print ("Tasa de deposicion acumulada del rango de 2.97-3.07 es: " + str(depo_297))

    depo_307 = 0;
    elevaciones_307 = [0.063];

    for deposicion_307 in range(2079, 2100):
        expr_307 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_307[-1];
        nueva_elevacion_307 = elevaciones_307[-1] - expr_307 + tasa_SLR_RCP85_2050_2100;
        elevaciones_307.append(nueva_elevacion_307);
        depo_307 += expr_307;
    print ("Tasa de deposicion acumulada del rango de 3.07-3.17 es: " + str(depo_307))

    depo_317 = 0;
    elevaciones_317 = [0.0518];

    for deposicion_317 in range(2085, 2100):
        expr_317 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_317[-1];
        nueva_elevacion_317 = elevaciones_317[-1] - expr_317 + tasa_SLR_RCP85_2050_2100;
        elevaciones_317.append(nueva_elevacion_317);
        depo_317 += expr_317;
    print ("Tasa de deposicion acumulada del rango de 3.17-3.27 es: " + str(depo_317))

    depo_327 = 0;
    elevaciones_327 = [0.0554];

    for deposicion_327 in range(2092, 2100):
        expr_327 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_327[-1];
        nueva_elevacion_327 = elevaciones_327[-1] - expr_327 + tasa_SLR_RCP85_2050_2100;
        elevaciones_327.append(nueva_elevacion_327);
        depo_327 += expr_327;
    print ("Tasa de deposicion acumulada del rango de 3.27-3.37 es: " + str(depo_327))

    depo_337 = 0;
    elevaciones_337 = [0.059];

    for deposicion_337 in range(2099, 2100):
        expr_337 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elevaciones_337[-1];
        nueva_elevacion_337 = elevaciones_337[-1] - expr_337 + tasa_SLR_RCP85_2050_2100;
        elevaciones_337.append(nueva_elevacion_337);
        depo_337 += expr_337;
    print ("Tasa de deposicion acumulada del rango de 3.37-3.47 es: " + str(depo_337))

    #MARISMA EN REGENERACION:
    deposicion_087_097 = 0;
    elev_regen_087 = [1.249];
    for dep_087_097 in range(2017, 2097):
        deposicion_087_097 += deposicion_marisma_regeneracion;
    for dep_087_097 in range(2097, 2100):
        expresion_087_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_087[
            -1];
        nueva_ele_087 = elev_regen_087[-1] - expresion_087_bis + tasa_SLR_RCP85_2050_2100;
        elev_regen_087.append(nueva_ele_087);
        deposicion_087_097 += expresion_087_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 0.87-0.97 es:" + str(deposicion_087_097));

    deposicion_097_107 = 0;
    elev_regen_097 = [1.156];
    for dep_097_107 in range(2017, 2091):
        deposicion_097_107 += deposicion_marisma_regeneracion;
    for dep_097_107 in range(2091, 2100):
        expresion_097_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_097[
            -1];
        nueva_ele_097 = elev_regen_097[-1] - expresion_097_bis + tasa_SLR_RCP85_2050_2100;
        elev_regen_097.append(nueva_ele_097);
        deposicion_097_107 += expresion_097_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 0.97-1.07 es:" + str(deposicion_097_107));

    deposicion_107_117 = 0;
    elev_regen_107 = [1.063];
    for dep_107_117 in range(2017, 2085):
        deposicion_107_117 += deposicion_marisma_regeneracion;
    for dep_107_117 in range(2085, 2100):
        expresion_107_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_107[
            -1];
        nueva_ele_107 = elev_regen_107[-1] - expresion_107_bis + tasa_SLR_RCP85_2050_2100;
        elev_regen_107.append(nueva_ele_107);
        deposicion_107_117 += expresion_107_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 1.07-1.17 es:" + str(deposicion_107_117));

    deposicion_117_127 = 0;
    elev_regen_117 = [0.971];
    for dep_117_127 in range(2017, 2079):
        deposicion_117_127 += deposicion_marisma_regeneracion;
    for dep_117_127 in range(2079, 2100):
        expresion_117_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_117[
            -1];
        nueva_ele_117 = elev_regen_117[-1] - expresion_117_bis + tasa_SLR_RCP85_2050_2100;
        elev_regen_117.append(nueva_ele_117);
        deposicion_117_127 += expresion_117_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 1.17-1.27 es:" + str(deposicion_117_127));

    deposicion_127_137 = 0;
    elev_regen_127 = [0.879];
    for dep_127_137 in range(2017, 2072):
        deposicion_127_137 += deposicion_marisma_regeneracion;
    for dep_127_137 in range(2072, 2100):
        expresion_127_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_127[
            -1];
        nueva_ele_127 = elev_regen_127[-1] - expresion_127_bis + tasa_SLR_RCP85_2050_2100;
        elev_regen_127.append(nueva_ele_127);
        deposicion_127_137 += expresion_127_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 1.27-1.37 es:" + str(deposicion_127_137));

    deposicion_137_147 = 0;
    elev_regen_137 = [0.786];
    for dep_137_147 in range(2017, 2066):
        deposicion_137_147 += deposicion_marisma_regeneracion;
    for dep_137_147 in range(2066, 2100):
        expresion_137_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_137[
            -1];
        nueva_ele_137 = elev_regen_137[-1] - expresion_137_bis + tasa_SLR_RCP85_2050_2100;
        elev_regen_137.append(nueva_ele_137);
        deposicion_137_147 += expresion_137_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 1.37-1.47 es:" + str(deposicion_137_147));

    deposicion_147_157 = 0;
    elev_regen_147 = [0.693];
    for dep_147_157 in range(2017, 2060):
        deposicion_147_157 += deposicion_marisma_regeneracion;
    for dep_147_157 in range(2060, 2100):
        expresion_147_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_147[
            -1];
        nueva_ele_147 = elev_regen_147[-1] - expresion_147_bis + tasa_SLR_RCP85_2050_2100;
        elev_regen_147.append(nueva_ele_147);
        deposicion_147_157 += expresion_147_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 1.47-1.57 es:" + str(deposicion_147_157));

    deposicion_157_167 = 0;
    elev_regen_157 = [0.601];
    for dep_157_167 in range(2017, 2054):
        deposicion_157_167 += deposicion_marisma_regeneracion;
    for dep_157_167 in range(2054, 2100):
        expresion_157_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_157[
            -1];
        nueva_ele_157 = elev_regen_157[-1] - expresion_157_bis + tasa_SLR_RCP85_2050_2100;
        elev_regen_157.append(nueva_ele_157);
        deposicion_157_167 += expresion_157_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 1.57-1.67 es:" + str(deposicion_157_167));

    deposicion_167_177 = 0;
    elev_regen_167 = [
        0.528];  # Diferencia entre el nivel de marea alta (2.47) mas el SLR para ese año y la elevacion del
    # rango mas la deposicion hasta que llegue a los 2,2 metros aprox.
    for dep_167_177 in range(2017, 2047):
        deposicion_167_177 += deposicion_marisma_regeneracion
    for dep_167_177 in range(2047, 2050):
        expresion_167_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_167[
            -1];
        nueva_ele_167 = elev_regen_167[-1] - expresion_167_bis + tasa_SLR_RCP85_2000_2050;
        elev_regen_167.append(nueva_ele_167);
        deposicion_167_177 += expresion_167_bis;
    for dep_167_177 in range(2050, 2100):
        expresion_167_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_167[
            -1];
        nueva_ele_167 = elev_regen_167[-1] - expresion_167_bis + tasa_SLR_RCP85_2050_2100;
        elev_regen_167.append(nueva_ele_167);
        deposicion_167_177 += expresion_167_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 1.67-1.77 es:" + str(deposicion_167_177));

    deposicion_177_187 = 0;
    elev_regen_177 = [
        0.472];  # Diferencia entre el nivel de marea alta (2.47) mas el SLR para ese año y la elevacion del
    # rango mas la deposicion hasta que llegue a los 2,2 metros aprox.
    for dep_177_187 in range(2017, 2041):
        deposicion_177_187 += deposicion_marisma_regeneracion
    for dep_177_187 in range(2041, 2050):
        expresion_177_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_177[
            -1];
        nueva_ele_177 = elev_regen_177[-1] - expresion_177_bis + tasa_SLR_RCP85_2000_2050;
        elev_regen_177.append(nueva_ele_177);
        deposicion_177_187 += expresion_177_bis;
    for dep_177_187 in range(2050, 2100):
        expresion_177_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_177[
            -1];
        nueva_ele_177 = elev_regen_177[-1] - expresion_177_bis + tasa_SLR_RCP85_2050_2100;
        elev_regen_177.append(nueva_ele_177);
        deposicion_177_187 += expresion_177_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 1.77-1.87 es:" + str(deposicion_177_187));

    deposicion_187_197 = 0;
    elev_regen_187 = [
        0.416];  # Diferencia entre el nivel de marea alta (2.47) mas el SLR para ese año y la elevacion del
    # rango mas la deposicion hasta que llegue a los 2,2 metros aprox.
    for dep_187_197 in range(2017, 2035):
        deposicion_187_197 += deposicion_marisma_regeneracion
    for dep_187_197 in range(2035, 2050):
        expresion_187_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_187[
            -1];
        nueva_ele_187 = elev_regen_187[-1] - expresion_187_bis + tasa_SLR_RCP85_2000_2050;
        elev_regen_187.append(nueva_ele_187);
        deposicion_187_197 += expresion_187_bis;
    for dep_187_197 in range(2050, 2100):
        expresion_187_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_187[
            -1];
        nueva_ele_187 = elev_regen_187[-1] - expresion_187_bis + tasa_SLR_RCP85_2050_2100;
        elev_regen_187.append(nueva_ele_187);
        deposicion_187_197 += expresion_187_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 1.87-1.97 es:" + str(deposicion_187_197));

    deposicion_197_207 = 0;
    elev_regen_197 = [
        0.361];  # Diferencia entre el nivel de marea alta (2.47) mas el SLR para ese año y la elevacion del
    # rango mas la deposicion hasta que llegue a los 2,2 metros aprox.
    for dep_197_207 in range(2017, 2029):
        deposicion_197_207 += deposicion_marisma_regeneracion
    for dep_197_207 in range(2029, 2050):
        expresion_197_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_197[
            -1];
        nueva_ele_197 = elev_regen_197[-1] - expresion_197_bis + tasa_SLR_RCP85_2000_2050;
        elev_regen_197.append(nueva_ele_197);
        deposicion_197_207 += expresion_197_bis;
    for dep_197_207 in range(2050, 2100):
        expresion_197_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_197[
            -1];
        nueva_ele_197 = elev_regen_197[-1] - expresion_197_bis + tasa_SLR_RCP85_2050_2100;
        elev_regen_197.append(nueva_ele_197);
        deposicion_197_207 += expresion_197_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 1.97-2.07 es:" + str(deposicion_197_207));

    deposicion_207_217 = 0;
    elev_regen_207 = [
        0.305];  # Diferencia entre el nivel de marea alta (2.47) mas el SLR para ese año y la elevacion del
    # rango mas la deposicion hasta que llegue a los 2,2 metros aprox.
    for dep_207_217 in range(2017, 2023):
        deposicion_207_217 += deposicion_marisma_regeneracion
    for dep_207_217 in range(2023, 2050):
        expresion_207_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_207[
            -1];
        nueva_ele_207 = elev_regen_207[-1] - expresion_207_bis + tasa_SLR_RCP85_2000_2050;
        elev_regen_207.append(nueva_ele_207);
        deposicion_207_217 += expresion_207_bis;
    for dep_207_217 in range(2050, 2100):
        expresion_207_bis = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * elev_regen_207[
            -1];
        nueva_ele_207 = elev_regen_207[-1] - expresion_207_bis + tasa_SLR_RCP85_2050_2100;
        elev_regen_207.append(nueva_ele_207);
        deposicion_207_217 += expresion_207_bis;
    print("La deposicion acumulada de la marisma en regeneracion en el rango 2.07-2.17 es:" + str(deposicion_207_217));

    # Ahora calculamos la deposicion que tendran las marismas reclamadas que no se inundan por la presencia de una barrera (natural o artificial)
    # que impide el flujo de agua de mar por su mayor altura (mas de 2,47). Obteniendo la elevacion mas frecuente mediante un histograma del raster
    # que da informacion a cerca de la elevacion de la barrera, se ha obtenido una elevacion de 2,6 metros (2'5-2'7), por lo que ahora, se calcula
    # cuando el SLR, en este caso referido al escenario RCP4.5 proyectado a 2100. Se obtiene que se inundara el año 2034, por lo que se aplicara una
    # acrecion de 16 mm por año (marisma en regeneracion) hasta que iguale su elevacion con la marisma colindante, que en este caso esta aproximadamente
    # a 2 metros de altura.Una vez que alcance esos 2 metros se aplica una tasa de acrecion de marisma natural y si esta a mas de 2,47 metros, una
    # deposicion igual a las zonas inundables por el SLR.

    tas_deposicion_MR_097_107 = 0;
    el_MReclamada_097 = [1.422];

    for t_097_107 in range(2033, 2095):
        tas_deposicion_MR_097_107 += deposicion_marisma_regeneracion;
    for t_097_107 in range(2095, 2100):
        expr_MR_097 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_097[-1];
        nuev_el_MR_097 = el_MReclamada_097[-1] - expr_MR_097 + tasa_SLR_RCP85_2050_2100;
        el_MReclamada_097.append(nuev_el_MR_097);
        tas_deposicion_MR_097_107 += expr_MR_097;
    print("La deposicion de la marisma reclamada en el rango 0.97-1.07 sera de: " + str(tas_deposicion_MR_097_107))

    tas_deposicion_MR_107_117 = 0;
    el_MReclamada_107 = [1.331];

    for t_107_117 in range(2033, 2088):
        tas_deposicion_MR_107_117 += deposicion_marisma_regeneracion;
    for t_107_117 in range(2088, 2100):
        expr_MR_107 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_107[-1];
        nuev_el_MR_107 = el_MReclamada_107[-1] - expr_MR_107 + tasa_SLR_RCP85_2050_2100;
        el_MReclamada_107.append(nuev_el_MR_107);
        tas_deposicion_MR_107_117 += expr_MR_107;
    print("La deposicion de la marisma reclamada en el rango 1.07-1.17 sera de: " + str(tas_deposicion_MR_107_117))

    tas_deposicion_MR_117_127 = 0;
    el_MReclamada_117 = [1.238];

    for t_117_127 in range(2033, 2082):
        tas_deposicion_MR_117_127 += deposicion_marisma_regeneracion;
    for t_117_127 in range(2082, 2100):
        expr_MR_117 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_117[-1];
        nuev_el_MR_117 = el_MReclamada_117[-1] - expr_MR_117 + tasa_SLR_RCP85_2050_2100;
        el_MReclamada_117.append(nuev_el_MR_117);
        tas_deposicion_MR_117_127 += expr_MR_117;
    print("La deposicion de la marisma reclamada en el rango 1.17-1.27 sera de: " + str(tas_deposicion_MR_117_127))

    tas_deposicion_MR_127_137 = 0;
    el_MReclamada_127 = [1.145];

    for t_127_137 in range(2033, 2076):
        tas_deposicion_MR_127_137 += deposicion_marisma_regeneracion;
    for t_127_137 in range(2076, 2100):
        expr_MR_127 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_127[-1];
        nuev_el_MR_127 = el_MReclamada_127[-1] - expr_MR_127 + tasa_SLR_RCP85_2050_2100;
        el_MReclamada_127.append(nuev_el_MR_127);
        tas_deposicion_MR_127_137 += expr_MR_127;
    print("La deposicion de la marisma reclamada en el rango 1.27-1.37 sera de: " + str(tas_deposicion_MR_127_137))

    tas_deposicion_MR_137_147 = 0;
    el_MReclamada_137 = [1.052];

    for t_137_147 in range(2033, 2070):
        tas_deposicion_MR_137_147 += deposicion_marisma_regeneracion;
    for t_137_147 in range(2070, 2100):
        expr_MR_137 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_137[-1];
        nuev_el_MR_137 = el_MReclamada_137[-1] - expr_MR_137 + tasa_SLR_RCP85_2050_2100;
        el_MReclamada_137.append(nuev_el_MR_137);
        tas_deposicion_MR_137_147 += expr_MR_137;
    print("La deposicion de la marisma reclamada en el rango 1.37-1.47 sera de: " + str(tas_deposicion_MR_137_147))

    tas_deposicion_MR_147_157 = 0;
    el_MReclamada_147 = [0.961];

    for t_147_157 in range(2033, 2063):
        tas_deposicion_MR_147_157 += deposicion_marisma_regeneracion;
    for t_147_157 in range(2063, 2100):
        expr_MR_147 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_147[-1];
        nuev_el_MR_147 = el_MReclamada_147[-1] - expr_MR_147 + tasa_SLR_RCP85_2050_2100;
        el_MReclamada_147.append(nuev_el_MR_147);
        tas_deposicion_MR_147_157 += expr_MR_147;
    print("La deposicion de la marisma reclamada en el rango 1.47-1.57 sera de: " + str(tas_deposicion_MR_147_157))

    tas_deposicion_MR_157_167 = 0;
    el_MReclamada_157 = [0.868];

    for t_157_167 in range(2033, 2057):
        tas_deposicion_MR_157_167 += deposicion_marisma_regeneracion;
    for t_157_167 in range(2057, 2100):
        expr_MR_157 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_157[-1];
        nuev_el_MR_157 = el_MReclamada_157[-1] - expr_MR_157 + tasa_SLR_RCP85_2050_2100;
        el_MReclamada_157.append(nuev_el_MR_157);
        tas_deposicion_MR_157_167 += expr_MR_157;
    print("La deposicion de la marisma reclamada en el rango 1.57-1.67 sera de: " + str(tas_deposicion_MR_157_167))

    tas_deposicion_MR_167_177 = 0;
    el_MReclamada_167 = [0.775];

    for t_167_177 in range(2033, 2051):
        tas_deposicion_MR_167_177 += deposicion_marisma_regeneracion;
    for t_167_177 in range(2051, 2100):
        expr_MR_167 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_167[-1];
        nuev_el_MR_167 = el_MReclamada_167[-1] - expr_MR_167 + tasa_SLR_RCP85_2050_2100;
        el_MReclamada_167.append(nuev_el_MR_167);
        tas_deposicion_MR_167_177 += expr_MR_167;
    print("La deposicion de la marisma reclamada en el rango 1.67-1.77 sera de: " + str(tas_deposicion_MR_167_177))

    tas_deposicion_MReclamada_177_187 = 0;
    el_MReclamada_177 = [
        0.707];  # Las elevaciones se han obtenido calculando 2,47m + (0.0078 * (2046-2017))- elevacion cuando alcance el equilibrio

    for t_177_187 in range(2033, 2045):
        tas_deposicion_MReclamada_177_187 += deposicion_marisma_regeneracion;
    for t_177_187 in range(2045, 2050):
        expr_MR_177 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_177[-1];
        nuev_el_MR_177 = el_MReclamada_177[-1] - expr_MR_177 + tasa_SLR_RCP85_2000_2050;
        el_MReclamada_177.append(nuev_el_MR_177);
        tas_deposicion_MReclamada_177_187 += expr_MR_177;
    for t_177_187 in range(2050, 2100):
        expr_MR_177 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_177[-1];
        nuev_el_MR_177 = el_MReclamada_177[-1] - expr_MR_177 + tasa_SLR_RCP85_2050_2100;
        el_MReclamada_177.append(nuev_el_MR_177);
        tas_deposicion_MReclamada_177_187 += expr_MR_177;
    print("La deposicion de la marisma reclamada en el rango 1.77-1.87 sera de: " + str(
        tas_deposicion_MReclamada_177_187))

    tas_deposicion_MReclamada_187_197 = 0;
    el_MReclamada_187 = [
        0.659];  # Las elevaciones se han obtenido calculando 2,47m + (0.0078 * (2046-2017))- elevacion cuando alcance el equilibrio

    for t_187_197 in range(2033, 2038):
        tas_deposicion_MReclamada_187_197 += deposicion_marisma_regeneracion;
    for t_187_197 in range(2038, 2050):
        expr_MR_187 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_187[-1];
        nuev_el_MR_187 = el_MReclamada_187[-1] - expr_MR_187 + tasa_SLR_RCP85_2000_2050;
        el_MReclamada_187.append(nuev_el_MR_187);
        tas_deposicion_MReclamada_187_197 += expr_MR_187;
    for t_187_197 in range(2050, 2100):
        expr_MR_187 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_187[-1];
        nuev_el_MR_187 = el_MReclamada_187[-1] - expr_MR_187 + tasa_SLR_RCP85_2050_2100;
        el_MReclamada_187.append(nuev_el_MR_187);
        tas_deposicion_MReclamada_187_197 += expr_MR_187;
    print("La deposicion de la marisma reclamada en el rango 1.87-1.97 sera de: " + str(
        tas_deposicion_MReclamada_187_197))

    tas_deposicion_MReclamada_197_207 = 0;
    el_MReclamada_197 = [
        0.596];  # Las elevaciones se han obtenido calculando 2,47m + (0.0078 * (2046-2017))- elevacion cuando alcance el equilibrio

    for t_197_207 in range(2033, 2050):
        expr_MR_197 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_197[-1];
        nuev_el_MR_197 = el_MReclamada_197[-1] - expr_MR_197 + tasa_SLR_RCP85_2000_2050;
        el_MReclamada_197.append(nuev_el_MR_197);
        tas_deposicion_MReclamada_197_207 += expr_MR_197;
    for t_197_207 in range(2050, 2100):
        expr_MR_197 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_197[-1];
        nuev_el_MR_197 = el_MReclamada_197[-1] - expr_MR_197 + tasa_SLR_RCP85_2050_2100;
        el_MReclamada_197.append(nuev_el_MR_197);
        tas_deposicion_MReclamada_197_207 += expr_MR_197;
    print("La deposicion de la marisma reclamada en el rango 1.97-2.07 sera de: " + str(
        tas_deposicion_MReclamada_197_207));

    tas_deposicion_MReclamada_207_217 = 0;
    el_MReclamada_207 = [
        0.496];  # Las elevaciones se han obtenido calculando 2,47m + (0.0078 * (2046-2017))- elevacion cuando alcance el equilibrio

    for t_207_217 in range(2033, 2050):
        expr_MR_207 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_207[-1];
        nuev_el_MR_207 = el_MReclamada_207[-1] - expr_MR_207 + tasa_SLR_RCP85_2000_2050;
        el_MReclamada_207.append(nuev_el_MR_207);
        tas_deposicion_MReclamada_207_217 += expr_MR_207;
    for t_207_217 in range(2050, 2100):
        expr_MR_207 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_207[-1];
        nuev_el_MR_207 = el_MReclamada_207[-1] - expr_MR_207 + tasa_SLR_RCP85_2050_2100;
        el_MReclamada_207.append(nuev_el_MR_207);
        tas_deposicion_MReclamada_207_217 += expr_MR_207;
    print("La deposicion de la marisma reclamada en el rango 2.07-2.17 sera de: " + str(
        tas_deposicion_MReclamada_207_217))

    tas_deposicion_MReclamada_217_227 = 0;
    el_MReclamada_217 = [
        0.396];  # Las elevaciones se han obtenido calculando 2,47m + (0.0078 * (2046-2017))- elevacion cuando alcance el equilibrio

    for t_217_227 in range(2033, 2050):
        expr_MR_217 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_217[-1];
        nuev_el_MR_217 = el_MReclamada_217[-1] - expr_MR_217 + tasa_SLR_RCP85_2000_2050;
        el_MReclamada_217.append(nuev_el_MR_217);
        tas_deposicion_MReclamada_217_227 += expr_MR_217;
    for t_217_227 in range(2050, 2100):
        expr_MR_217 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_217[-1];
        nuev_el_MR_217 = el_MReclamada_217[-1] - expr_MR_217 + tasa_SLR_RCP85_2050_2100;
        el_MReclamada_217.append(nuev_el_MR_217);
        tas_deposicion_MReclamada_217_227 += expr_MR_217;
    print("La deposicion de la marisma reclamada en el rango 2.17-2.27 sera de: " + str(
        tas_deposicion_MReclamada_217_227))

    tas_deposicion_MReclamada_227_237 = 0;
    el_MReclamada_227 = [
        0.296];  # Las elevaciones se han obtenido calculando 2,47m + (0.0078 * (2046-2017))- elevacion cuando alcance el equilibrio

    for t_227_237 in range(2033, 2050):
        expr_MR_227 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_227[-1];
        nuev_el_MR_227 = el_MReclamada_227[-1] - expr_MR_227 + tasa_SLR_RCP85_2000_2050;
        el_MReclamada_227.append(nuev_el_MR_227);
        tas_deposicion_MReclamada_227_237 += expr_MR_227;
    for t_227_237 in range(2050, 2100):
        expr_MR_227 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_227[-1];
        nuev_el_MR_227 = el_MReclamada_227[-1] - expr_MR_227 + tasa_SLR_RCP85_2050_2100;
        el_MReclamada_227.append(nuev_el_MR_227);
        tas_deposicion_MReclamada_227_237 += expr_MR_227;
    print("La deposicion de la marisma reclamada en el rango 2.27-2.37 sera de: " + str(
        tas_deposicion_MReclamada_227_237))

    tas_deposicion_MReclamada_237_247 = 0;
    el_MReclamada_237 = [
        0.196];  # Las elevaciones se han obtenido calculando 2,47m + (0.0078 * (2046-2017))- elevacion cuando alcance el equilibrio

    for t_237_247 in range(2033, 2050):
        expr_MR_237 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_237[-1];
        nuev_el_MR_237 = el_MReclamada_237[-1] - expr_MR_237 + tasa_SLR_RCP85_2000_2050;
        el_MReclamada_237.append(nuev_el_MR_237);
        tas_deposicion_MReclamada_237_247 += expr_MR_237;
    for t_237_247 in range(2050, 2100):
        expr_MR_237 = (0.00009 * float(concentracion) + 0.000015 * float(produccion_biomasa)) * el_MReclamada_237[-1];
        nuev_el_MR_237 = el_MReclamada_237[-1] - expr_MR_237 + tasa_SLR_RCP85_2050_2100;
        el_MReclamada_237.append(nuev_el_MR_237);
        tas_deposicion_MReclamada_237_247 += expr_MR_237;
    print("La deposicion de la marisma reclamada en el rango 2.37-2.47 sera de: " + str(
        tas_deposicion_MReclamada_237_247))

    # Reclasificamos el raster de la marisma reclamada que se volvera a inundar con el SLR con la sedimentacion que tendra
    # cada rango de elevaciones:
    depo_maris_reclamada_RCP85_2100 = Reclassify(raster_marisma_reclamada_errota, "VALUE",RemapRange([[-1000000, 970, "NODATA"],
                                     [970, 1070, round(tas_deposicion_MR_097_107 * 1000)],[1070, 1170, round(tas_deposicion_MR_107_117 * 1000)],
                                     [1170, 1270, round(tas_deposicion_MR_117_127 * 1000)],[1270, 1370, round(tas_deposicion_MR_127_137 * 1000)],
                                     [1370, 1470, round(tas_deposicion_MR_137_147 * 1000)],[1470, 1570, round(tas_deposicion_MR_147_157 * 1000)],
                                     [1570, 1670, round(tas_deposicion_MR_157_167 * 1000)],[1670, 1770, round(tas_deposicion_MR_167_177 * 1000)],
                                     [1770, 1870,round(tas_deposicion_MReclamada_177_187 * 1000)],[1870, 1970,round(tas_deposicion_MReclamada_187_197 * 1000)],
                                     [1970, 2070,round(tas_deposicion_MReclamada_197_207 * 1000)],[2070, 2170,round(tas_deposicion_MReclamada_207_217 * 1000)],
                                     [2170, 2270,round(tas_deposicion_MReclamada_217_227 * 1000)],[2270, 2370,round(tas_deposicion_MReclamada_227_237 * 1000)],
                                     [2370, 2470,round(tas_deposicion_MReclamada_237_247 * 1000)],[2470, 2570, round(depo_247*1000)], [2570, 2670, round(depo_257*1000)], [2670, 2770, round(depo_267*1000)], [2770, 2870, round(depo_277*1000)],
                                 [2870, 2970, round(depo_287*1000)], [2970, 3070, round(depo_297*1000)], [3070, 3170, round(depo_307*1000)], [3170, 3270, round(depo_317*1000)],
                                 [3270, 3370, round(depo_327*1000)], [3370, 3470, round(depo_337*1000)], [3470,3493,0],[3493, 100000000, "NODATA"]]))
    depo_maris_reclamada_RCP85_2100.save(
        r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Deposicion_marisma_Reclamada_RCP85_2100");
    direc_depo_marisma_reclamada_RCP85_2100 = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Deposicion_marisma_Reclamada_RCP85_2100";

    # Reclasificamos el raster de las marismas en regeneracion para tener la deposicion por rangos que tendra dicha zona:
    depo_maris_regeneracion_RCP85_2100 = Reclassify(raster_marisma_regeneracion, "VALUE",RemapRange([[-10000, 870, "NODATA"],
                                            [870,970, round(deposicion_087_097*1000)],[970,1070, round(deposicion_097_107*1000)],
                                            [1070,1170, round(deposicion_107_117*1000)],[1170,1270, round(deposicion_117_127*1000)],
                                            [1270,1370, round(deposicion_127_137*1000)],[1370, 1470, round(deposicion_137_147*1000)],
                                            [1470,1570, round(deposicion_147_157*1000)],[1570,1670, round(deposicion_157_167*1000)],
                                            [1670, 1770, round(deposicion_167_177 * 1000)],
                                            [1770, 1870, round(deposicion_177_187 * 1000)],[1870, 1970, round(deposicion_187_197 * 1000)],
                                            [1970, 2070, round(deposicion_197_207 * 1000)], [2070, 2170, round(deposicion_207_217 * 1000)],
                                            [2170, 2270, round(tasa_deposicion_217 * 1000)],[2270, 2370, round(tasa_deposicion_227 * 1000)],
                                            [2370, 2470, round(tasa_deposicion_237 * 1000)],  [2470, 2570, round(depo_247*1000)], [2570, 2670, round(depo_257*1000)], [2670, 2770, round(depo_267*1000)], [2770, 2870, round(depo_277*1000)],
                                            [2870, 2970, round(depo_287*1000)], [2970, 3070, round(depo_297*1000)], [3070, 3170, round(depo_307*1000)], [3170, 3270, round(depo_317*1000)],
                                            [3270, 3370, round(depo_327*1000)], [3370, 3470, round(depo_337*1000)], [3470,3493,0],[3493, 100000000, "NODATA"]]))
    depo_maris_regeneracion_RCP85_2100.save(
        r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Deposicion_marisma_regen_RCP85_2100")
    direc_depo_maris_regeneracion_RCP85_2100 = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Deposicion_marisma_regen_RCP85_2100";

    #Reclasificamos el raster con los datos de la tasa de deposicion, por rangos, para representar la tasa de deposicion (aumento de
    # la elevacion en mm para el año 2050 en la zona de estudio para el escenario RCP4.5 y el año 2050:
    deposicion_RCP85_2100 = Reclassify(raster_Marisma, "VALUE", RemapRange([[-10000, 870,"NODATA"],[870, 970, round(tasa_deposicion_087*1000)],
                                 [970, 1070, round(tasa_deposicion_097*1000)], [1070, 1170, round(tasa_deposicion_107*1000)], [1170, 1270, round(tasa_deposicion_117*1000)],
                                 [1270, 1370, round(tasa_deposicion_127*1000)], [1370, 1470, round(tasa_deposicion_137*1000)], [1470, 1570, round(tasa_deposicion_147*1000)],
                                 [1570, 1670, round(tasa_deposicion_157*1000)], [1670, 1770, round(tasa_deposicion_167*1000)], [1770, 1870, round(tasa_deposicion_177*1000)],
                                 [1870, 1970, round(tasa_deposicion_187*1000)], [1970, 2070, round(tasa_deposicion_197*1000)], [2070, 2170, round(tasa_deposicion_207*1000)],
                                 [2170, 2270, round(tasa_deposicion_217*1000)], [2270, 2370, round(tasa_deposicion_227*1000)], [2370, 2470, round(tasa_deposicion_237*1000)],
                                 [2470, 2570, round(depo_247*1000)], [2570, 2670, round(depo_257*1000)], [2670, 2770, round(depo_267*1000)], [2770, 2870, round(depo_277*1000)],
                                 [2870, 2970, round(depo_287*1000)], [2970, 3070, round(depo_297*1000)], [3070, 3170, round(depo_307*1000)], [3170, 3270, round(depo_317*1000)],
                                 [3270, 3370, round(depo_327*1000)], [3370, 3470, round(depo_337*1000)], [3470,3493,0],[3493, 100000000, "NODATA"]]))
    deposicion_RCP85_2100.save(r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Deposicion_RCP85_2100")
    direcc_depo_RCP85_2100 = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Deposicion_RCP85_2100"

    # Reclasificamos el raster de marismas de zonas inundables por el SLR (zonas de cultivo) para tener en cuenta la interaccion
    # deposicion-SLR en las zonas que se inundarán con el SLR:
    depo_RCP85_2100_zonas_inundables = Reclassify(raster_zonas_cultivo, "VALUE", RemapRange([[870, 2570, round(depo_247 * 1000)],
                                        [2570, 2670, round(depo_257 * 1000)],[2670, 2770, round(depo_267 * 1000)],[2770, 2870, round(depo_277 * 1000)],
                                        [2870, 2970, round(depo_287 * 1000)],[2970, 3070, round(depo_297 * 1000)],[3070, 3170, round(depo_307 * 1000)],
                                        [3170, 3270, round(depo_317 * 1000)],[3270, 3370, round(depo_327 * 1000)],[3370, 3470, round(depo_337*1000)],
                                        [3470,3493,0],[3493, 1000000, "NODATA"]]));
    depo_RCP85_2100_zonas_inundables.save(
        r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Deposicion_RCP85_2100_zonas_inundables")
    direcc_depo_RCP85_2100_zonas_inundables = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Deposicion_RCP85_2100_zonas_inundables"

    #Ahora ya tenemos el raster con la deposicion que habra en la zona de estudio segun el escenario RCP4.5 y para el año 2100,
    #asumiendo que desde el limite inferior hasta el superior donde se encuentran las marismas de Urdaibai de acuerdo a distintos
    #estudios, son las potenciales zonas de las marismas (aunque en realidad no haya por distintos factores y suponiendo que serían
    #marismas consolidadas con unas tasas de deposicion acorde a su elevacion.

    #Pues bien, sumamos los dos rasteres (elevacion en mm y deposicion en mm) para obtener la nueva altura que tendra la marisma.
    elevacion_RCP85_2100 = RasterCalculator([raster_Marisma, direcc_depo_RCP85_2100], ["marisma", "depo"],
                                            "(marisma+depo)")
    elevacion_RCP85_2100.save(
       r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Elevacion_RCP85_2100")
    direc_elevacion_RCP85_2100 = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Elevacion_RCP85_2100"

    elevacion_RCP85_2100_zona_inundable = RasterCalculator([raster_zonas_cultivo, direcc_depo_RCP85_2100_zonas_inundables],
        ["zonas_inun", "depo_inun"], "(zonas_inun+depo_inun)")
    elevacion_RCP85_2100_zona_inundable.save(
        r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Elevacion_RCP85_2100_zonas_inundables");
    direc_elevacion_RCP85_2100_zonas_inundables = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Elevacion_RCP85_2100_zonas_inundables";

    elevacion_marisma_regener_RCP85_2100 = RasterCalculator(
        [raster_marisma_regeneracion, direc_depo_maris_regeneracion_RCP85_2100],
        ["mar_reg", "deposi_regen"], "(mar_reg + deposi_regen)")
    elevacion_marisma_regener_RCP85_2100.save(
        r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Elevacion_marism_regener_RCP85_2100")
    direc_elevacion_marisma_regener_RCP85_2100 = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Elevacion_marism_regener_RCP85_2100";

    elevacion_MR_RCP85_2100 = RasterCalculator([raster_marisma_reclamada_errota, direc_depo_marisma_reclamada_RCP85_2100], ["MR", "depos_MR"],
                                               "(MR + depos_MR)");
    elevacion_MR_RCP85_2100.save(r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Elevacion_marism_Reclamada_RCP85_2100")
    direc_MR_RCP85_2100 = r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Elevacion_marism_Reclamada_RCP85_2100";

    #Una vez que tenemos la elevacion nueva de la zona de estudio debido a la deposicion fusionamos los rasteres de la nueva
    #elevacion de la marisma con el raster de elevaciones original para que tenga las nuevas elevaciones y tenga en cuenta los
    #valores del raster original en las zonas donde no hay marisma (y asi no ponga "NODATA").
    comb_elevacion_RCP85_2100 = arcpy.management.MosaicToNewRaster([direc_elevacion_RCP85_2100, direc_elevacion_RCP85_2100_zonas_inundables,direc_elevacion_marisma_regener_RCP85_2100,direc_MR_RCP85_2100], r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb",
                                    "Elevacion_Combi_Terreno_RCP85_2100", 25830, "32_BIT_FLOAT", 1, 1, "FIRST")

    #Ya tenemos el la elevacion que habra en la zona de estudio en 2050 segun el escenario 2050, ahora volvemos a reclasificar dicho
    #raster para obtener la potencial distribucion de la marisma en dicho escenario y año:
    pot_distribucion_RCP85_2100 = Reclassify(comb_elevacion_RCP85_2100, "VALUE", RemapRange([[-100000,1893,"NODATA"], [1893,3493,0],[3493, 1000000,"NODATA"]]))
    pot_distribucion_RCP85_2100.save(r"C:\Student\MasterGIS\EjerciciosPrueba\ServiciosEcosistemicosUrdaibai\EvolucionMarismas.gdb\Pot_Distribucion_RCP85_2100")