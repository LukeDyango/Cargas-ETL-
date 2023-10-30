#App que Extrae datos de un excel, limpia los datos y traspasa a otro para realizar carga de este archivo nuevo (ETL)
#Aclaro que esto lo hice para facilitar las tareas al area donde estaba asignado, donde esto se hacia manual y para mis compañeros era muy tedioso, esta me la dio mi jefe a realizar.


#Importamos las librerias requeridas
from tkinter import *
from tkinter import ttk
import tkinter as mytk
import os
from tkinter import messagebox
from tkinter import filedialog
import pandas as pd
from pandas import ExcelWriter
from datetime import datetime
import os



#VENTANA
ventana1= Tk()
ventana1.geometry("700x448")
ventana1.resizable(width = False, height = False)
ventana1.title("Gestion Operaciones")
ventana1['bg'] = '#a5aae0'

imagen = PhotoImage(file = "img/clo.png") #Esta imagen esta en la carpeta por si les da el error de "img/clo.png" don't exist
background = Label(image = imagen, text = "Imagen de fondo")                                                                                                                                                                                                                                 #Lukas estuvo aca :3
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
now = datetime.now()

a = now.month
b = now.day

Boton4  = PhotoImage(file = "img/Boton4.png")
Boton5  = PhotoImage(file = "img/Boton5.png")
Boton6 = PhotoImage(file = "img/Boton6.png")
Boton7 = PhotoImage(file = "img/Boton7.png")
Boton10 = PhotoImage(file = "img/Boton10.png")

def Ac1112():
 try:
  dc1112 = filedialog.askopenfilename()
 
  c12 = pd.read_csv(dc1112)

  filtro = c12[c12['ESTADO_CLO'] != 'PCO-100' ] #Filtro de los datos
  df3 = pd.DataFrame(filtro)

  Fc12 = df3['TELEFONO']
  Fc13 = df3['Cantidad_Cuotas']
  Fc14 = df3['TIPO_PLAN']
  filtro2 = Fc12.isnull().values.any()
  filtro3 = Fc13.isnull().values.any()
  filtro4 = Fc14.isnull().values.any()
  if filtro2 == True:
    messagebox.showerror(message=F"Datos de campaña 1112 Con errores De Datos Null en tabla TELEFONO "  , title="Aviso")
  elif filtro3 == True :
    messagebox.showerror(message=F"Datos de campaña 1112 Con errores De Datos Null en tabla Cantidad_Cuotas "  , title="Aviso")
  elif filtro4 == True :
    messagebox.showerror(message=F"Datos de campaña 1112 Con errores De Datos Null en TIPO_PLAN "  , title="Aviso")     
  else:  
   num=df3['NUM_SOLICITUD']
   ani=df3['TELEFONO']
   nom=df3['NOMBRE']
   cco=df3['Cantidad_Cuotas']
   ttp=df3['TIPO_PLAN']

 
  #DataFrame De la Carga

   dfr = pd.DataFrame({'Número de Suministro': num.values, #n? suministro
                      'Código de área': '',
                      'ANI': ani.values, #n.? celular
                      'Custom1': nom.values, #nombres
                      'Custom2': cco.values, #cantidad
                      'Custom3': ttp.values, #nombre seguro
                      'Custom4': '',
                      'Custom5': '',
                      'Custom6': '',
                      'Custom7': '',
                      'Custom8': '',
                      'Custom9': '',
                      'Custom10': '',}) 

  carpeta = now.strftime('%m-%d')
  dfr.to_csv(F'{carpeta}/Datos de carga 1112.csv',index = None, header=True)  
  filas = len(filtro)
  messagebox.showinfo(message=F"Datos de carga 1112 Creados {filas} Filas Cargadas  "  , title="Aviso")
 except:
   messagebox.showerror(message=F"Error al Seleccionar el Archivo, Asegurese De seleccionar el archivo Correspondiente", title="Error")
   
def Ac1116():
 try:
  dc1116 = filedialog.askopenfilename()
  c16 = pd.read_csv(dc1116)

  filtro = c16[c16['ESTADO_CLO'] != 'PCO-100' ] #Filtro de los datos
  df3 = pd.DataFrame(filtro)

  Fc16 = df3['TELEFONO']

  Fc18 = df3['NOMBRE_PLAN']

  filtro2 = Fc16.isnull().values.any()
  filtro3 = Fc18.isnull().values.any()

  if filtro2 == True:
    messagebox.showerror(message=F"Datos de campaña 1116 Con errores De Datos Null en tabla TELEFONO "  , title="Aviso")
  elif filtro3 == True :
    messagebox.showerror(message=F"Datos de campaña 1116 Con errores De Datos Null en NOMBRE_PLAN "  , title="Aviso")    
  else:
   num6=df3['NUM_SOLICITUD']
   ani6=df3['TELEFONO']
   nom6=df3['NOMBRE']
   ttp6=df3['NOMBRE_PLAN']

  
  #DataFrame De la Carga

   dfr = pd.DataFrame({'Número de Suministro': num6.values, #n? suministro
                     'Código de área': '',
                     'ANI': ani6.values, #n.? celular
                     'Custom1': nom6.values, #nombres
                     'Custom2': ttp6.values, #nombre plan
                     'Custom3': '',
                     'Custom4': '',
                     'Custom5': '',
                     'Custom6': '',
                     'Custom7': '',
                     'Custom8': '',
                     'Custom9': '',
                     'Custom10': '',})

  carpeta = now.strftime('%m-%d')
  dfr.to_csv(F'{carpeta}/Datos campaña 1116.csv',index = None, header=True)  
  filas = len(filtro)
  messagebox.showinfo(message=F"Datos de campaña 1116 Creados {filas} Filas Cargadas  "  , title="Aviso")
 except:
   messagebox.showerror(message=F"Error al Seleccionar el Archivo, Asegurese De seleccionar el archivo Correspondiente", title="Error")


def Ac1150():
    #Extraciion de datos
 try:   
  dc1150 = filedialog.askopenfilename()
  c50 = pd.read_csv(dc1150)

  filtro = c50[c50['ESTADO_CLO'] != 'PCO-100' ] #Filtro de los datos 
  #filtro2 = filtro.isnull().values.any() #IF "NULL"
  df3 = pd.DataFrame(filtro)
  Fc50 = df3['TELEFONO']
  #Fc51 = df3['FECHA_GESTION']
  #filtros para  datos null en tabla TELEFONO y FECHA_GESTION
  filtro2 = Fc50.isnull().values.any()
  #filtro3 = Fc51.isnull().values.any()
  if filtro2 == True:
    messagebox.showerror(message=F"Datos de campaña 1150 Con errores De Datos Null en tabla TELEFONO "  , title="Aviso")
  #elif filtro3 == True:
   # messagebox.showerror(message=F"Datos de campaña 1150 Con errores De Datos Null en tabla FECHA_GESTION"  , title="Aviso")
  else:
   
   num50=df3['NUM_SOLICITUD']
   ani50=df3['TELEFONO']
   nom50=df3['NOMBRE']
 

  #DataFrame De la Carga

  dfr = pd.DataFrame({'Número de Suministro': num50.values, #n? suministro
                     'Código de área': '',
                     'ANI': ani50.values, #n.? celular
                     'Custom1': '',
                     'Custom2': '',
                     'Custom3': nom50.values, #nombres
                     'Custom4': '',
                     'Custom5': '',
                     'Custom6': '',
                     'Custom7': '',
                     'Custom8': '',
                     'Custom9': ani50.values, #n.? celular
                     'Custom10': '',})

  carpeta = now.strftime('%m-%d')
  dfr.to_csv(F'{carpeta}/Datos campaña 1150.csv',index = None, header=True)  
  filas = len(filtro)
  messagebox.showinfo(message=F"Datos de campaña 1150 Creados {filas} Filas Cargadas  "  , title="Aviso")
 except:
    messagebox.showerror(message=F"Error al Seleccionar el Archivo, Asegurese De seleccionar el archivo Correspondiente", title="Error")

    
def cdi():  
  try:
    format = now.strftime('%m-%d')
    os.mkdir(format)
    messagebox.showinfo(message="Carpeta Creada Con Exito", title="Aviso")
  except :
    messagebox.showerror(message=F"Carpeta de {format} Ya Existente", title="Error")

def rvm():
  try:
   carpeta = now.strftime('%m-%d')
   c1112 = F'{carpeta}\Datos de carga 1112.csv'
   c1116 = F'{carpeta}\Datos campaña 1116.csv'
   c1150 = F'{carpeta}\Datos campaña 1150.csv'
   os.startfile(c1112)
   os.startfile(c1116)
   os.startfile(c1150)
  except:
    messagebox.showerror(message=F"Faltan Archivos Para La Revision", title="Error")


#botones

btnNuevo=Button(ventana1,image=Boton4,command= Ac1112)
btnNuevo.place(x=200, y=30) 
btnNuevo=Button(ventana1,image=Boton5,command= Ac1116)
btnNuevo.place(x=200, y=120) 
btnNuevo=Button(ventana1,image=Boton6,command= Ac1150)
btnNuevo.place(x=197, y=210) 
btnNuevo=Button(ventana1,image=Boton7,command= cdi)
btnNuevo.place(x=240, y=300) 
btnNuevo=Button(ventana1,image=Boton10,command= rvm)
btnNuevo.place(x=255, y=370) 



ventana1.mainloop()
