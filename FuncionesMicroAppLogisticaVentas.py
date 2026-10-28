import datetime
import random
import time
import sys
import os
def GenCodDesc_MicroAppLogVent():
    Num_Al = ["1", "2", "3", "4", "5"]
    Voc_Min_Al = ["a", "e", "i", "o", "u"]
    Voc_May_Al = ["A", "E", "I", "O", "U"]
    Sim_Al = ["%", "!", "¡", "?", "¿"]
    Num_Al_Esc = random.choice(Num_Al)
    Voc_Min_Al_Esc = random.choice(Voc_Min_Al)
    Voc_May_Al_Esc = random.choice(Voc_May_Al)
    Sim_Al_Esc = random.choice(Sim_Al)
    CodDescGen_MicroAppLogVent = Num_Al_Esc + Voc_Min_Al_Esc + Voc_May_Al_Esc + Sim_Al_Esc
    return CodDescGen_MicroAppLogVent
def CargAcc_MicroAppLogVent():
    TiempCarg_MicroAppLogVent = time.sleep(1.5)
    return TiempCarg_MicroAppLogVent
def Ver_StockFull_MicroAppLogVent(StockFull_MicroAppLogVent):
    print(f"{'ID':<4} {'CODIGO':<12} {'TIPO':<8} {'NOMBRE':<25} {'CANT':<6} {'PRECIO':<8}")
    for Lub in StockFull_MicroAppLogVent:
        print(f"{Lub.ID_Prod:<4} {Lub.Cod_UnManAl:<12} {Lub.Tipo_Lub:<8} {Lub.Nomb_lub:<25} {Lub.Cant_Caj_Lub:<6} {Lub.Prec_Caj_Lub:<8}")
def BusID_StockFull_MicroAppLogVent(IDBus_Stock, List_Stock):
    for Lub in List_Stock:
        if IDBus_Stock == Lub.ID_Prod:
            return Lub
    return None
def CalcDesc_MicroAppLogVent(CodDesc_MALV, TupUs_MALV, MontPagAcu_MALV):
    if CodDesc_MALV == TupUs_MALV[2]:
        Desc_MALV = MontPagAcu_MALV * 0.10
        NuevPagConDesc = MontPagAcu_MALV - Desc_MALV
        print("----------------------------------------------------")
        print(f"| EL PAGO QUE HARA CON EL DESCUENTO APLICADO ES DE : {NuevPagConDesc} NUEVOS SOLES ")
        print("----------------------------------------------------")
        return NuevPagConDesc
    else:
        print("-----------------------------------------")
        print(f"| NO PUDO ACCEDER AL DESCUENTO - PAGARA : {MontPagAcu_MALV} NUEVOS SOLES ")
        print("-----------------------------------------")
        return MontPagAcu_MALV
def ModCantCaj_StockFull_MicroAppLogVent(IDBus_Stock, List_Stock, NuevCant_CajLub):
    Lub = BusID_StockFull_MicroAppLogVent(IDBus_Stock, List_Stock)
    if Lub is not None:
        return Lub.ActualizarCantCajLub_MicroAppLogVent(NuevCant_CajLub)
    else:
        print("---------------------------------------")
        print(f"| ERROR : LUBRICANTE {IDBus_Stock} NO ENCONTRADO |")
        print("---------------------------------------")
        return False
def ModPrecCaj_StockFull_MicroAppLogVent(IDBus_Stock, List_Stock, NuevPrec_CajLub):
    Lub = BusID_StockFull_MicroAppLogVent(IDBus_Stock, List_Stock)
    if Lub is not None:
        return Lub.ActualizarPrecCajLub_MicroAppLogVent(NuevPrec_CajLub)
    else:
        print("---------------------------------------")
        print(f"| ERROR : LUBRICANTE {IDBus_Stock} NO ENCONTRADO |")
        print("---------------------------------------")
        return False
def CompCajLub_StockFull_MicroAppLogVent(IDBus_Stock, List_Stock, CantComp_CajLub):
    Lub = BusID_StockFull_MicroAppLogVent(IDBus_Stock, List_Stock)
    if Lub is not None:
        return Lub.ComprarLub_MicroAppLogVent(CantComp_CajLub)
    else:
        print("---------------------------------------")
        print(f"| ERROR : LUBRICANTE {IDBus_Stock} NO ENCONTRADO |")
        print("---------------------------------------")
        return False
def GenRepModCantLub_MicroAppLogVent(IDBus_Stock_Enc, Nom_Stock_Enc, CantCaj_Act):
    os.makedirs("Data", exist_ok=True)
    Fecha_Act = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("Data/Stock_Act_Cant.txt", "a" , encoding="utf-8") as Arch:
        Arch.write(f"| FECHA DE ACTUALIZACION : {Fecha_Act}\n")
        Arch.write(f"| ID : {IDBus_Stock_Enc} | NOMBRE : {Nom_Stock_Enc} | CANT : {CantCaj_Act}\n")
def GenRepModPrecLub_MicroAppLogVent(IDBus_Stock_Enc, Nom_Stock_Enc, PrecCaj_Act):
    os.makedirs("Data", exist_ok=True)
    Fecha_Act = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("Data/Stock_Act_Prec.txt", "a" , encoding="utf-8") as Arch:
        Arch.write(f"| FECHA DE ACTUALIZACION : {Fecha_Act}\n")
        Arch.write(f"| ID : {IDBus_Stock_Enc} | NOMBRE : {Nom_Stock_Enc} | PREC : {PrecCaj_Act}\n")
def GenRepParcCompLub_MicroAppLogVent(IDBus_Stock_Enc, Nom_Stock_Enc, CantCaj_Comp, PrecCaj_Comp, SubTotal_Comp, MonAcum_Comp):
    os.makedirs("Data", exist_ok=True)
    Fecha_Comp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("Data/Comp_Stock.txt", "a", encoding="utf-8") as Arch:
        Arch.write(f"| FECHA DE COMPRA : {Fecha_Comp}\n")
        Arch.write(f"| ID : {IDBus_Stock_Enc} | NOMBRE : {Nom_Stock_Enc} | CANT : {CantCaj_Comp} | PREC : {PrecCaj_Comp} | TOTAL X LUB : {SubTotal_Comp} TOTAL ACUM : {MonAcum_Comp}\n")
def GenRepFinCompLub_MicroAppLogVent(CodDesc_Comp, MonAcum_Comp, MonTot_Comp):
    os.makedirs("Data", exist_ok=True)
    Fecha_Cierre_Comp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("Data/Comp_Stock.txt", "a", encoding="utf-8") as Arch:
        if  MonAcum_Comp == MonTot_Comp:
            Arch.write(f"| FECHA DE CIERRE : {Fecha_Cierre_Comp}\n")
            Arch.write(f"| CODIGO DESC : {CodDesc_Comp} | NO ACCEDIO AL DESCUENTO - PAGARA : {MonTot_Comp} NUEVOS SOLES\n")
        else:
            Arch.write(f"| FECHA DE CIERRE : {Fecha_Cierre_Comp}\n")
            Arch.write(f"| CODIGO DESC : {CodDesc_Comp} | DESCUENTO APLICADO - PAGARA : {MonTot_Comp} NUEVOS SOLES\n")
def Salir_MicroAppLogVent():
    return sys.exit()