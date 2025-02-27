import json

# Cargar el JSON
data = [
 {
   "FECHA REGISTRO": "2022-08-02T10:20:48.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 62,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Técnico",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA HECHO EN PEREIRA / SEC COMPETITIVIDAD",
   "DESCRIPCIÓN": "ENTREGA REGISTRO INVIMA"
 },
 {
   "FECHA REGISTRO": "2022-08-02T11:28:13.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 40,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Técnico",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA HECHO EN PEREIRA / SEC COMPETITIVIDAD",
   "DESCRIPCIÓN": "ENTREGA REGISTRO INVIMA"
 },
 {
   "FECHA REGISTRO": "2022-08-02T11:30:41.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 37,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Profesional Universitario",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA HECHO EN PEREIRA / SEC COMPETITIVIDAD",
   "DESCRIPCIÓN": "ENTREGA REGISTRO INVIMA"
 },
 {
   "FECHA REGISTRO": "2022-08-02T11:45:24.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 62,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Profesional Universitario",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA HECHO EN PEREIRA / SEC COMPETITIVIDAD",
   "DESCRIPCIÓN": "ENTREGA DE REGISTRO INVIMA"
 },
 {
   "FECHA REGISTRO": "2022-08-02T13:37:06.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 38,
   "GÉNERO": "Masculino",
   "NIVEL DE EDUCACIÓN": "Profesional Universitario",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA HECHO EN PEREIRA / SEC COMPETITIVIDAD",
   "DESCRIPCIÓN": "ENTREGA REGISTRO INVIMA"
 },
 {
   "FECHA REGISTRO": "2022-08-02T13:38:38.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 44,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Profesional Universitario",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA HECHO EN PEREIRA / SEC COMPETITIVIDAD",
   "DESCRIPCIÓN": "ENTREGA REGISTRO INVIMA"
 },
 {
   "FECHA REGISTRO": "2022-08-02T13:39:58.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 49,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Post-grado",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA HECHO EN PEREIRA / SEC COMPETITIVIDAD",
   "DESCRIPCIÓN": "ENTREGA REGISTRO INVIMA"
 },
 {
   "FECHA REGISTRO": "2022-08-02T13:41:29.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 41,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Profesional Universitario",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA HECHO EN PEREIRA / SEC COMPETITIVIDAD",
   "DESCRIPCIÓN": "ENTREGA REGISTRO INVIMA"
 },
 {
   "FECHA REGISTRO": "2022-08-02T14:39:13.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 29,
   "GÉNERO": "Masculino",
   "NIVEL DE EDUCACIÓN": "Profesional Universitario",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA HECHO EN PEREIRA / SEC COMPETITIVIDAD",
   "DESCRIPCIÓN": "ENTREGA REGISTRO INVIMA"
 },
 {
   "FECHA REGISTRO": "2022-08-02T14:42:00.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 66,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Técnico",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA HECHO EN PEREIRA / SEC COMPETITIVIDAD",
   "DESCRIPCIÓN": "ENTREGA REGISTRO INVIMA"
 },
 {
   "FECHA REGISTRO": "2022-08-02T14:44:02.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 64,
   "GÉNERO": "Masculino",
   "NIVEL DE EDUCACIÓN": "Técnico",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA HECHO EN PEREIRA / SEC COMPETITIVIDAD",
   "DESCRIPCIÓN": "ENTREGA REGISTRO INVIMA"
 },
 {
   "FECHA REGISTRO": "2022-08-02T14:48:58.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 40,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Técnico",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA HECHO EN PEREIRA / SEC COMPETITIVIDAD",
   "DESCRIPCIÓN": "ENTREGA REGISTRO INVIMA"
 },
 {
   "FECHA REGISTRO": "2022-08-02T14:51:14.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 43,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Profesional Universitario",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA HECHO EN PEREIRA / SEC COMPETITIVIDAD",
   "DESCRIPCIÓN": "ENTREGA REGISTRO INVIMA"
 },
 {
   "FECHA REGISTRO": "2022-08-02T16:19:17.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 50,
   "GÉNERO": "Masculino",
   "NIVEL DE EDUCACIÓN": "Profesional Universitario",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA HECHO EN PEREIRA / SEC COMPETITIVIDAD",
   "DESCRIPCIÓN": "ENTREGA REGISTRO INVIMA"
 },
 {
   "FECHA REGISTRO": "2022-08-02T16:23:09.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 34,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Profesional Universitario",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA HECHO EN PEREIRA / SEC COMPETITIVIDAD",
   "DESCRIPCIÓN": "ENTREGA REGISTRO INVIMA"
 },
 {
   "FECHA REGISTRO": "2022-08-02T16:24:16.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 53,
   "GÉNERO": "Masculino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA HECHO EN PEREIRA / SEC COMPETITIVIDAD",
   "DESCRIPCIÓN": "ENTREGA REGISTRO INVIMA"
 },
 {
   "FECHA REGISTRO": "2022-08-02T16:25:34.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 25,
   "GÉNERO": "Masculino",
   "NIVEL DE EDUCACIÓN": "Técnico",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA HECHO EN PEREIRA / SEC COMPETITIVIDAD",
   "DESCRIPCIÓN": "ENTREGA REGISTRO INVIMA"
 },
 {
   "FECHA REGISTRO": "2022-08-02T16:29:26.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 53,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Post-grado",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA HECHO EN PEREIRA / SEC COMPETITIVIDAD",
   "DESCRIPCIÓN": "ENTREGA REGISTRO INVIMA"
 },
 {
   "FECHA REGISTRO": "02/16/2022 05:21:31 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 65,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Técnico",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "REUNION JUNTA DE ACCION COMUNAL",
   "DESCRIPCIÓN": "REUNION EDILES Y COMUNEROS"
 },
 {
   "FECHA REGISTRO": "02/16/2022 05:22:44 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 66,
   "GÉNERO": "Masculino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "REUNION JUNTA DE ACCION COMUNAL",
   "DESCRIPCIÓN": "REUNION EDILES Y COMUNEROS"
 },
 {
   "FECHA REGISTRO": "02/16/2022 05:24:08 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 76,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Primaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "REUNION JUNTA DE ACCION COMUNAL",
   "DESCRIPCIÓN": "REUNION EDILES Y COMUNEROS"
 },
 {
   "FECHA REGISTRO": "02/16/2022 05:25:16 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 37,
   "GÉNERO": "Masculino",
   "NIVEL DE EDUCACIÓN": "Profesional Universitario",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "REUNION JUNTA DE ACCION COMUNAL",
   "DESCRIPCIÓN": "REUNION EDILES Y COMUNEROS"
 },
 {
   "FECHA REGISTRO": "02/17/2022 10:00:58 AM",
   "DEPENDENCIA GESTORA": "CEDE PERLA DEL OTÚN",
   "EDAD": 40,
   "GÉNERO": "Masculino",
   "NIVEL DE EDUCACIÓN": "Profesional Universitario",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ARTE Y CALLE",
   "DESCRIPCIÓN": "APOYO EMPRENDIMIENTOS"
 },
 {
   "FECHA REGISTRO": "02/17/2022 10:55:31 AM",
   "DEPENDENCIA GESTORA": "CEDE CONSOTA",
   "EDAD": 16,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PRESTAMO DE ESPACIO CEDE CONSOTA",
   "DESCRIPCIÓN": "ENSAYO GRUPO DE DANZA HUELA JUVENIL"
 },
 {
   "FECHA REGISTRO": "02/17/2022 10:58:08 AM",
   "DEPENDENCIA GESTORA": "CEDE CONSOTA",
   "EDAD": 15,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PRESTAMO DE ESPACIO CEDE CONSOTA",
   "DESCRIPCIÓN": "ENSAYO GRUO DE DANZAS HUELLA JUEVENIL"
 },
 {
   "FECHA REGISTRO": "02/17/2022 10:59:33 AM",
   "DEPENDENCIA GESTORA": "CEDE CONSOTA",
   "EDAD": 12,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PRESTAMO DE ESPACIO CEDE CONSOTA",
   "DESCRIPCIÓN": "ENSAYO GRUPO DE DANZAS HUELLA JUVENIL"
 },
 {
   "FECHA REGISTRO": "02/17/2022 11:02:37 AM",
   "DEPENDENCIA GESTORA": "CEDE CONSOTA",
   "EDAD": 18,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PRESTAMO DE ESPACIO CEDE CONSOTA",
   "DESCRIPCIÓN": "ENSAYO GRUPO DE DANZAS HUELLAS JUVENILES"
 },
 {
   "FECHA REGISTRO": "02/17/2022 11:03:50 AM",
   "DEPENDENCIA GESTORA": "CEDE CONSOTA",
   "EDAD": 14,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PRESTAMO DE ESPACIO CEDE CONSOTA",
   "DESCRIPCIÓN": "ENSAYO GRUPO DE DANZAS HUELLAS JUVENILES"
 },
 {
   "FECHA REGISTRO": "02/17/2022 11:05:08 AM",
   "DEPENDENCIA GESTORA": "CEDE CONSOTA",
   "EDAD": 15,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PRESTAMO DE ESPACIO CEDE CONSOTA",
   "DESCRIPCIÓN": "ENSAYO GRUPO DE DANZAS HUELLAS JUVENILES"
 },
 {
   "FECHA REGISTRO": "02/17/2022 11:06:46 AM",
   "DEPENDENCIA GESTORA": "CEDE CONSOTA",
   "EDAD": 14,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PRESTAMO DE ESPACIO CEDE CONSOTA",
   "DESCRIPCIÓN": "ENSAYO GRUPO DE DANZAS HUELLAS JUVENILES"
 },
 {
   "FECHA REGISTRO": "02/17/2022 11:08:14 AM",
   "DEPENDENCIA GESTORA": "CEDE CONSOTA",
   "EDAD": 16,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PRESTAMO DE ESPACIO CEDE CONSOTA",
   "DESCRIPCIÓN": "ENSAYO GRUPO DE DANZAS HUELLAS JUVENILES"
 },
 {
   "FECHA REGISTRO": "02/17/2022 11:09:44 AM",
   "DEPENDENCIA GESTORA": "CEDE CONSOTA",
   "EDAD": 18,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PRESTAMO DE ESPACIO CEDE CONSOTA",
   "DESCRIPCIÓN": "ENSAYO GRUPO DE DANZAS HUELLAS JUVENILES"
 },
 {
   "FECHA REGISTRO": "02/17/2022 11:10:50 AM",
   "DEPENDENCIA GESTORA": "CEDE CONSOTA",
   "EDAD": 13,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PRESTAMO DE ESPACIO CEDE CONSOTA",
   "DESCRIPCIÓN": "ENSAYO GRUPO DE DANZAS HUELLAS JUVENILES"
 },
 {
   "FECHA REGISTRO": "02/17/2022 11:12:57 AM",
   "DEPENDENCIA GESTORA": "CEDE CONSOTA",
   "EDAD": 17,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PRESTAMO DE ESPACIO CEDE CONSOTA",
   "DESCRIPCIÓN": "ENSAYO GRUPO DE DANZAS HUELLAS JUVENILES"
 },
 {
   "FECHA REGISTRO": "02/17/2022 11:18:07 AM",
   "DEPENDENCIA GESTORA": "CEDE CONSOTA",
   "EDAD": 19,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PRESTAMO DE ESPACIO CEDE CONSOTA",
   "DESCRIPCIÓN": "ENSAYO GRUPO DE DANZAS HUELLAS JUVENILES"
 },
 {
   "FECHA REGISTRO": "02/17/2022 11:19:37 AM",
   "DEPENDENCIA GESTORA": "CEDE CONSOTA",
   "EDAD": 17,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PRESTAMO DE ESPACIO CEDE CONSOTA",
   "DESCRIPCIÓN": "ENSAYO GRUPO DE DANZAS HUELLAS JUVENILES"
 },
 {
   "FECHA REGISTRO": "02/17/2022 11:21:14 AM",
   "DEPENDENCIA GESTORA": "CEDE CONSOTA",
   "EDAD": 25,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PRESTAMO DE ESPACIO CEDE CONSOTA",
   "DESCRIPCIÓN": "ENSAYO GRUPO DE DANZAS HUELLAS JUVENILES"
 },
 {
   "FECHA REGISTRO": "02/17/2022 11:22:23 AM",
   "DEPENDENCIA GESTORA": "CEDE CONSOTA",
   "EDAD": 16,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PRESTAMO DE ESPACIO CEDE CONSOTA",
   "DESCRIPCIÓN": "ENSAYO GRUPO DE DANZAS HUELLAS JUVENILES"
 },
 {
   "FECHA REGISTRO": "02/17/2022 11:24:15 AM",
   "DEPENDENCIA GESTORA": "CEDE CONSOTA",
   "EDAD": 17,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PRESTAMO DE ESPACIO CEDE CONSOTA",
   "DESCRIPCIÓN": "ENSAYO GRUPO DE DANZAS HUELLAS JUVENILES"
 },
 {
   "FECHA REGISTRO": "02/17/2022 11:27:27 AM",
   "DEPENDENCIA GESTORA": "CEDE CONSOTA",
   "EDAD": 14,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PRESTAMO DE ESPACIO CEDE CONSOTA",
   "DESCRIPCIÓN": "ENSAYO GRUPO DE DANZAS HUELLAS JUVENILES"
 },
 {
   "FECHA REGISTRO": "02/17/2022 11:28:32 AM",
   "DEPENDENCIA GESTORA": "CEDE CONSOTA",
   "EDAD": 29,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PRESTAMO DE ESPACIO CEDE CONSOTA",
   "DESCRIPCIÓN": "ENSAYO GRUPO DE DANZAS HUELLAS JUVENILES"
 },
 {
   "FECHA REGISTRO": "02/23/2022 10:06:18 AM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 41,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 10:08:45 AM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 38,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 10:10:08 AM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 50,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 10:56:20 AM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 59,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 11:21:40 AM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 26,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 11:44:09 AM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 29,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 11:45:26 AM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 50,
   "GÉNERO": "Masculino",
   "NIVEL DE EDUCACIÓN": "Profesional Universitario",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 11:47:04 AM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 46,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 11:51:58 AM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 33,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Profesional Universitario",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 12:00:11 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 35,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Técnico",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 01:52:21 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 28,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Técnico",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 01:57:52 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 27,
   "GÉNERO": "Masculino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 02:01:03 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 21,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 02:04:27 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 20,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Primaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 03:39:51 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 36,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 04:31:17 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 23,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Técnico",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 04:35:28 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 30,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 04:36:54 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 28,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Profesional Universitario",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 04:42:14 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 46,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Técnico",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 04:43:35 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 34,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 04:45:21 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 33,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 04:46:47 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 41,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Técnico",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 04:48:04 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 20,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 04:49:22 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 21,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 04:52:21 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 29,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Profesional Universitario",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 04:57:00 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 22,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 04:58:35 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 26,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 04:59:45 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 50,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Primaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOAGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 05:01:18 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 57,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Primaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 05:02:50 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 32,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 05:03:46 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 72,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 05:04:55 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 20,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Profesional Universitario",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 05:06:32 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 49,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Técnico",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 05:11:31 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 23,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 05:12:53 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 29,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 05:14:18 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 74,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Primaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 05:15:23 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 21,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 05:16:34 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 34,
   "GÉNERO": "Masculino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/23/2022 05:17:39 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 26,
   "GÉNERO": "Masculino",
   "NIVEL DE EDUCACIÓN": "Primaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ICBF",
   "DESCRIPCIÓN": "HOGARES COMUNITARIOS"
 },
 {
   "FECHA REGISTRO": "02/25/2022 11:32:56 AM",
   "DEPENDENCIA GESTORA": "CEDE PERLA DEL OTÚN",
   "EDAD": 24,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Profesional Universitario",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "CAPACITAXIONES CULINARIA",
   "DESCRIPCIÓN": "PREPARACION ALIMENTOS"
 },
 {
   "FECHA REGISTRO": "02/25/2022 12:04:29 PM",
   "DEPENDENCIA GESTORA": "CEDE PERLA DEL OTÚN",
   "EDAD": 48,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Técnico",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "ARTESANA",
   "DESCRIPCIÓN": "ARTESANIAS EN PUEDARAS, MADERA"
 },
 {
   "FECHA REGISTRO": "02/25/2022 12:14:01 PM",
   "DEPENDENCIA GESTORA": "CEDE PERLA DEL OTÚN",
   "EDAD": 32,
   "GÉNERO": "Masculino",
   "NIVEL DE EDUCACIÓN": "Post-grado",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "JUSTICIA RESTAURATIVA",
   "DESCRIPCIÓN": "CAPACITANCION A JOVENES EN COMDICION DE VULNERABILIDAD"
 },
 {
   "FECHA REGISTRO": "02/28/2022 05:30:52 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 15,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Primaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA CERO A SIEMPRE",
   "DESCRIPCIÓN": "ICBF"
 },
 {
   "FECHA REGISTRO": "02/28/2022 05:47:44 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 22,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Primaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA CERO A SIEMPRE",
   "DESCRIPCIÓN": "ICBF"
 },
 {
   "FECHA REGISTRO": "02/28/2022 05:49:46 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 26,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Técnico",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA CERO A SIEMPRE",
   "DESCRIPCIÓN": "ICBF"
 },
 {
   "FECHA REGISTRO": "02/28/2022 05:50:54 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 48,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Primaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA CERO A SIEMPRE",
   "DESCRIPCIÓN": "ICBF"
 },
 {
   "FECHA REGISTRO": "02/28/2022 05:52:00 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 20,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA CERO A SIEMPRE",
   "DESCRIPCIÓN": "ICBF"
 },
 {
   "FECHA REGISTRO": "02/28/2022 05:53:11 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 21,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Primaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA CERO A SIEMPRE",
   "DESCRIPCIÓN": "ICBF"
 },
 {
   "FECHA REGISTRO": "02/28/2022 05:54:47 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 22,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA CERO A SIEMPRE",
   "DESCRIPCIÓN": "ICBF"
 },
 {
   "FECHA REGISTRO": "02/28/2022 05:55:58 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 21,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA CERO A SIEMPRE",
   "DESCRIPCIÓN": "ICBF"
 },
 {
   "FECHA REGISTRO": "02/28/2022 05:57:31 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 26,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Técnico",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA CERO A SIEMPRE",
   "DESCRIPCIÓN": "ICBF"
 },
 {
   "FECHA REGISTRO": "02/28/2022 05:58:55 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 27,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA CERO A SIEMPRE",
   "DESCRIPCIÓN": "ICBF"
 },
 {
   "FECHA REGISTRO": "02/28/2022 06:00:09 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 21,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Primaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA CERO A SIEMPRE",
   "DESCRIPCIÓN": "ICBF"
 },
 {
   "FECHA REGISTRO": "02/28/2022 06:01:12 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 28,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Profesional Universitario",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA CERO A SIEMPRE",
   "DESCRIPCIÓN": "ICBF"
 },
 {
   "FECHA REGISTRO": "02/28/2022 06:02:48 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 23,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Tecnólogo",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA CERO A SIEMPRE",
   "DESCRIPCIÓN": "ICBF"
 },
 {
   "FECHA REGISTRO": "02/28/2022 06:04:06 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 17,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA CERO A SIEMPRE",
   "DESCRIPCIÓN": "ICBF"
 },
 {
   "FECHA REGISTRO": "02/28/2022 06:06:52 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 28,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA CERO A SIEMPRE",
   "DESCRIPCIÓN": "ICBF"
 },
 {
   "FECHA REGISTRO": "02/28/2022 06:08:02 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 29,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Primaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA CERO A SIEMPRE",
   "DESCRIPCIÓN": "ICBF"
 },
 {
   "FECHA REGISTRO": "02/28/2022 06:09:20 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 24,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA CERO A SIEMPRE",
   "DESCRIPCIÓN": "ICBF"
 },
 {
   "FECHA REGISTRO": "02/28/2022 06:10:20 PM",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 26,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "PROGRAMA CERO A SIEMPRE",
   "DESCRIPCIÓN": "ICBF"
 },
 {
   "FECHA REGISTRO": "2022-01-03T14:17:28.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 54,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Post-grado",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "SOCIALIZACION FONDO EMPRENDER",
   "DESCRIPCIÓN": "SENA"
 },
 {
   "FECHA REGISTRO": "2022-01-03T14:22:52.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 32,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Profesional Universitario",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "SOCIALIZACION FONDO EMPRENDER",
   "DESCRIPCIÓN": "SENA"
 },
 {
   "FECHA REGISTRO": "2022-01-03T15:12:39.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 40,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Técnico",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "SOCIALIZACION FONDO EMPRENDER",
   "DESCRIPCIÓN": "SENA"
 },
 {
   "FECHA REGISTRO": "2022-01-03T15:17:00.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 55,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Técnico",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "SOCIALIZACION FONDO EMPRENDER",
   "DESCRIPCIÓN": "SENA"
 },
 {
   "FECHA REGISTRO": "2022-01-03T15:19:12.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 50,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "SOCIALIZACION FONDO EMPRENDER",
   "DESCRIPCIÓN": "SENA"
 },
 {
   "FECHA REGISTRO": "2022-01-03T15:21:00.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 43,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Técnico",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "SOCIALIZACION FONDO EMPRENDER",
   "DESCRIPCIÓN": "SENA"
 },
 {
   "FECHA REGISTRO": "2022-01-03T15:24:00.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 33,
   "GÉNERO": "Masculino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "SOCIALIZACION FONDO EMPRENDER",
   "DESCRIPCIÓN": "SENA"
 },
 {
   "FECHA REGISTRO": "2022-01-03T15:30:31.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 38,
   "GÉNERO": "Masculino",
   "NIVEL DE EDUCACIÓN": "Técnico",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "SOCIALIZACION FONDO EMPRENDER",
   "DESCRIPCIÓN": "SENA"
 },
 {
   "FECHA REGISTRO": "2022-01-03T15:33:58.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 40,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "SOCIALIZACION FONDO EMPRENDER",
   "DESCRIPCIÓN": "SENA"
 },
 {
   "FECHA REGISTRO": "2022-01-03T15:42:49.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 43,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Técnico",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "SOCIALIZACION FONDO EMPRENDER",
   "DESCRIPCIÓN": "SENA"
 },
 {
   "FECHA REGISTRO": "2022-01-03T15:49:22.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 30,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Técnico",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "SOCIALIZACION FONDO EMPRENDER",
   "DESCRIPCIÓN": "SENA"
 },
 {
   "FECHA REGISTRO": "2022-01-03T15:53:05.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 21,
   "GÉNERO": "Masculino",
   "NIVEL DE EDUCACIÓN": "Tecnólogo",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "SOCIALIZACION FONDO EMPRENDER",
   "DESCRIPCIÓN": "SENA"
 },
 {
   "FECHA REGISTRO": "2022-01-03T15:55:08.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 43,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Post-grado",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "SOCIALIZACION FONDO EMPRENDER",
   "DESCRIPCIÓN": "SENA"
 },
 {
   "FECHA REGISTRO": "2022-01-03T16:40:23.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 22,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Técnico",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "SOCIALIZACION FONDO EMPRENDER",
   "DESCRIPCIÓN": "SENA"
 },
 {
   "FECHA REGISTRO": "2022-01-03T16:42:51.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 35,
   "GÉNERO": "Masculino",
   "NIVEL DE EDUCACIÓN": "Técnico",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "SOCIALIZACION FONDO EMPRENDER",
   "DESCRIPCIÓN": "SENA"
 },
 {
   "FECHA REGISTRO": "2022-01-03T16:58:59.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 53,
   "GÉNERO": "Masculino",
   "NIVEL DE EDUCACIÓN": "Tecnólogo",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "SOCIALIZACION FONDO EMPRENDER",
   "DESCRIPCIÓN": "SENA"
 },
 {
   "FECHA REGISTRO": "2022-01-03T17:04:44.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 43,
   "GÉNERO": "Masculino",
   "NIVEL DE EDUCACIÓN": "Profesional Universitario",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "SOCIALIZACION FONDO EMPRENDER",
   "DESCRIPCIÓN": "SENA"
 },
 {
   "FECHA REGISTRO": "2022-01-03T17:06:19.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 31,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Profesional Universitario",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "SOCIALIZACION FONDO EMPRENDER",
   "DESCRIPCIÓN": "SENA"
 },
 {
   "FECHA REGISTRO": "2022-01-03T17:07:40.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 60,
   "GÉNERO": "Masculino",
   "NIVEL DE EDUCACIÓN": "Técnico",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "SOCIALIZACION FONDO EMPRENDER",
   "DESCRIPCIÓN": "SENA"
 },
 {
   "FECHA REGISTRO": "2022-01-03T17:23:51.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 26,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "HOGARES COMUNITARIOS",
   "DESCRIPCIÓN": "ICBF"
 },
 {
   "FECHA REGISTRO": "2022-01-03T17:25:15.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 25,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "HOGARES COMUNITARIOS",
   "DESCRIPCIÓN": "ICBF"
 },
 {
   "FECHA REGISTRO": "2022-01-03T17:26:49.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 20,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "HOGARES COMUNITARIOS",
   "DESCRIPCIÓN": "ICBF"
 },
 {
   "FECHA REGISTRO": "2022-01-03T17:28:38.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 31,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Técnico",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "HOGARES COMUNITARIOS",
   "DESCRIPCIÓN": "ICBF"
 },
 {
   "FECHA REGISTRO": "2022-01-03T17:29:49.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 45,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "HOGARES COMUNITARIOS",
   "DESCRIPCIÓN": "ICBF"
 },
 {
   "FECHA REGISTRO": "2022-01-03T17:31:59.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 34,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "HOGARES COMUNITARIOS",
   "DESCRIPCIÓN": "ICBF"
 },
 {
   "FECHA REGISTRO": "2022-01-03T17:33:29.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 29,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Tecnólogo",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "HOGARES COMUNITARIOS",
   "DESCRIPCIÓN": "ICBF"
 },
 {
   "FECHA REGISTRO": "2022-01-03T17:34:37.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 25,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "HOGARES COMUNITARIOS",
   "DESCRIPCIÓN": "ICBF"
 },
 {
   "FECHA REGISTRO": "2022-01-03T17:35:58.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 22,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "HOGARES COMUNITARIOS",
   "DESCRIPCIÓN": "ICBF"
 },
 {
   "FECHA REGISTRO": "2022-01-03T17:37:12.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 32,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "HOGARES COMUNITARIOS",
   "DESCRIPCIÓN": "ICBF"
 },
 {
   "FECHA REGISTRO": "2022-01-03T17:38:29.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 24,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "HOGARES COMUNITARIOS",
   "DESCRIPCIÓN": "ICBF"
 },
 {
   "FECHA REGISTRO": "2022-01-03T17:39:47.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 28,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "HOGARES COMUNITARIOS",
   "DESCRIPCIÓN": "ICBF"
 },
 {
   "FECHA REGISTRO": "2022-01-03T17:41:08.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 27,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Profesional Universitario",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "HOGARES COMUNITARIOS",
   "DESCRIPCIÓN": "ICBF"
 },
 {
   "FECHA REGISTRO": "2022-01-03T17:42:22.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 30,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Técnico",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "HOGARES COMUNITARIOS",
   "DESCRIPCIÓN": "ICBF"
 },
 {
   "FECHA REGISTRO": "2022-01-03T17:43:30.000",
   "DEPENDENCIA GESTORA": "CEDE SAN NICOLÁS",
   "EDAD": 46,
   "GÉNERO": "Femenino",
   "NIVEL DE EDUCACIÓN": "Secundaria",
   "TIPO DE USUARIO": "Tejido Social (Se vincula con una actividad social)",
   "NOMBRE DE LA ACTIVIDAD": "HOGARES COMUNITARIOS",
   "DESCRIPCIÓN": "ICBF"
 }
]

# Modificar el campo "FECHA REGISTRO" para que solo contenga el año
for entry in data:
    fecha = entry["FECHA REGISTRO"]
    if "T" in fecha:  # Si la fecha tiene formato ISO (con hora)
        entry["FECHA REGISTRO"] = fecha.split("-")[0]  # Extraer solo el año
    else:  # Si la fecha tiene formato "MM/DD/YYYY HH:MM:SS AM/PM"
        entry["FECHA REGISTRO"] = fecha.split("/")[2].split(" ")[0]  # Extraer solo el año

    # Renombrar el campo "GÉNERO" a "GENERO" sin tilde
    if "GÉNERO" in entry:
        entry["GENERO"] = entry.pop("GÉNERO")

# Guardar el JSON modificado
with open("emprendimiento_juvenil_modificado.json", "w") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("JSON modificado guardado con éxito.")
