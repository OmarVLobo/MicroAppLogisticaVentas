from FuncionesMicroAppLogisticaVentas import *
from ClasesMetodosMicroAppLogisticaVentas import *
UsMicroApp_LogVent = ()
ContIntAcc_MicroAppLogVent = 0
NumMaxIntAcc_MicroAppLogVent = 2
LimitIntAlc_MicroAppLogVent = False
MontPagAcu_MicroAppLogVent = 0.0
MontMinPagAcu_MicroAppLogVent = 3000.0
OpMenu_MicroAppLogVent = {1:"REALIZAR OPERACIONES CON LUBRICANTES", 2:"SALIR DE LA MICROAPP LOGISTICA DE VENTAS"}
if not UsMicroApp_LogVent:
    print("---------------------------------------------------------------------")
    RespUs_MicroAppLogVent = str(input(f"| ¿DESEA CREAR UN USUARIO EN NUESTRA MICRO APP LOGISTICA DE VENTAS? : "))
    if RespUs_MicroAppLogVent == "si" or RespUs_MicroAppLogVent == "SI":
        try:
            print("--------------------------------")
            NomIngUs_MicroAppLogVent = str(input(f"| INGRESE SU NOMBRE DE USUARIO : "))
            if not NomIngUs_MicroAppLogVent.isalpha():
                raise ValueError(f" EL NOMBRE DE USUARIO DEBE TENER SOLO LETRAS |")
            print("------------------------------------")
            ContIngUs_MicroAppLogVent = int(input(f"| INGRESE SU CONTRASEÑA DE USUARIO : "))
            ListUsMicroApp_LogVent = list(UsMicroApp_LogVent)
            ListUsMicroApp_LogVent.append(NomIngUs_MicroAppLogVent)
            ListUsMicroApp_LogVent.append(ContIngUs_MicroAppLogVent)
            ListUsMicroApp_LogVent.append(GenCodDesc_MicroAppLogVent())
            UsMicroApp_LogVent = tuple(ListUsMicroApp_LogVent)
            print("----------------------------")
            print(f"| EL USURIO REGISTRADO FUE : {UsMicroApp_LogVent[0]} Y SU CODIGO DE DESCUENTO ES : {UsMicroApp_LogVent[2]}")
            print("-------------------------------------------------------")
            RespUsAcc_MicroAppVentLog = str(input(f"| ¿DESEA INGRESAR A LA MICRO APP LOGISTICA DE VENTAS? : "))
            if RespUsAcc_MicroAppVentLog == "si" or RespUsAcc_MicroAppVentLog == "SI":
                print("--------------------------------")
                NomIngUsAcc_MicroAppLogVent = str(input(f"| INGRESE SU NOMBRE DE USUARIO : "))
                print("------------------------------------")
                ContIngUsAcc_MicroAppLogVent = int(input(f"| INGRESE SU CONTRASEÑA DE USUARIO : "))
                CargAcc_MicroAppLogVent()
                while NomIngUsAcc_MicroAppLogVent != UsMicroApp_LogVent[0] or ContIngUsAcc_MicroAppLogVent != UsMicroApp_LogVent[1]:
                    ContIntAcc_MicroAppLogVent += 1
                    print("----------------------------------------------------------")
                    print(f"| ACCESO DENEGADO - USUARIO Y / O CONTRASEÑA INCORRECTOS |")
                    print("------------------")
                    print(f"| INTENTO NUMERO : {ContIntAcc_MicroAppLogVent}")
                    print("--------------------------------")
                    NomIngUsAcc_MicroAppLogVent = str(input("| INGRESE SU NOMBRE DE USUARIO : "))
                    print("------------------------------------")
                    ContIngUsAcc_MicroAppLogVent = int(input("| INGRESE SU CONTRASEÑA DE USUARIO : "))
                    CargAcc_MicroAppLogVent()
                    if ContIntAcc_MicroAppLogVent >= NumMaxIntAcc_MicroAppLogVent and (NomIngUsAcc_MicroAppLogVent != UsMicroApp_LogVent[0] or ContIngUsAcc_MicroAppLogVent != UsMicroApp_LogVent[1]):
                        print("-----------------------------------------------------------------------------------")
                        print(f"| LIMITE DE INTENTOS CUBIERTO - CERRANDO MICROAPP LOGISTICA DE VENTAS POR SEGURIDAD...")
                        print("-----------------------------------------------------------------------------------")
                        LimitIntAlc_MicroAppLogVent = True
                        break
                if not LimitIntAlc_MicroAppLogVent and NomIngUsAcc_MicroAppLogVent == UsMicroApp_LogVent[0] and ContIngUsAcc_MicroAppLogVent == UsMicroApp_LogVent[1]:
                    CargAcc_MicroAppLogVent()
                    print("-------------------------------------------------")
                    print(f"| BIENVENIDO A LA MICRO APP LOGISTICA DE VENTAS |")
                    print("-------------------------------------------------")
                    for CodOp, NomOp in OpMenu_MicroAppLogVent.items():
                        print(f"| {CodOp} | {NomOp}")
                    print("-------------------------------------------------")
                    OpEsc_MicroAppLogVent = int(input(f"| INGRESE LA OPCION QUE ESCOGIO : "))
                    match (OpEsc_MicroAppLogVent):
                        case 1:
                            print("-----------------------------------------------------------------")
                            Ver_StockFull_MicroAppLogVent(StockFull_MicroAppLogVent)
                            print("-----------------------------------------------------------------")
                            Opc_OtOp_MicroAppLogVent = str(input(f"| OPCIONES A ESCOGER - | ACTUALIZAR LUBRICANTE | COMPRAR LUBRICANTE | : "))
                            if Opc_OtOp_MicroAppLogVent == "al" or Opc_OtOp_MicroAppLogVent == "AL":
                                try:
                                    print("--------------------------------")
                                    CodLubBus_StockMicroAppLogVent = int(input(f"| INGRESE CODIGO DE LUBRICANTE : "))
                                    LubEncStock_MicroAppLogVent = (BusID_StockFull_MicroAppLogVent(CodLubBus_StockMicroAppLogVent, StockFull_MicroAppLogVent))
                                    if LubEncStock_MicroAppLogVent is None:
                                        print("---------------------------------------")
                                        print(f"| ERROR : LUBRICANTE {CodLubBus_StockMicroAppLogVent} NO ENCONTRADO |")
                                    if LubEncStock_MicroAppLogVent is not None:
                                        print("-----------------------")
                                        print(f"| LUBRICANTE ENCONTRADO {LubEncStock_MicroAppLogVent} ")
                                        print("---------------------------------------------------")
                                        OpEscActLub_MicroAppLogVent = str(input(f"| OPCIONES DE ACTUALIZACION - | CANTIDAD | PRECIO : "))
                                        if OpEscActLub_MicroAppLogVent == "cant" or OpEscActLub_MicroAppLogVent == "CANT":
                                            print("-----------------------------------------------------------")
                                            NuevCantLub_MicroAppLogVent = int(input(f"| INGRESE LA NUEVA CANTIDAD DE CAJAS PARA ESTE LUBRICANTE : "))
                                            ModCantCaj_StockFull_MicroAppLogVent(CodLubBus_StockMicroAppLogVent, StockFull_MicroAppLogVent, NuevCantLub_MicroAppLogVent)
                                            print(BusID_StockFull_MicroAppLogVent(CodLubBus_StockMicroAppLogVent, StockFull_MicroAppLogVent))
                                            print("---------------------------------------------------------------")
                                            LubEncStock_MicroAppLogVent.Cant_Caj_Lub = NuevCantLub_MicroAppLogVent
                                            GenRepModCantLub_MicroAppLogVent(LubEncStock_MicroAppLogVent.ID_Prod, LubEncStock_MicroAppLogVent.Nomb_lub, LubEncStock_MicroAppLogVent.Cant_Caj_Lub)
                                            RespUs_MicroAppLogVent = str(input(f"| ¿DESEA ACTUALIZAR LA CANTIDAD DE CAJAS DE OTRO LUBRICANTE ? : "))
                                            while RespUs_MicroAppLogVent == "si" or RespUs_MicroAppLogVent == "SI":
                                                print("---------------------------------")
                                                CodLubBus_StockMicroAppLogVent = int(input(f"| INGRESE CODIGO DEL LUBRICANTE : "))
                                                LubEncStock_MicroAppLogVent = (BusID_StockFull_MicroAppLogVent(CodLubBus_StockMicroAppLogVent, StockFull_MicroAppLogVent))
                                                if LubEncStock_MicroAppLogVent is None:
                                                    print("---------------------------------------")
                                                    print(f"| ERROR : LUBRICANTE {CodLubBus_StockMicroAppLogVent} NO ENCONTRADO |")
                                                    break
                                                if LubEncStock_MicroAppLogVent is not None:
                                                    print("-----------------------")
                                                    print(f"| LUBRICANTE ENCONTRADO {LubEncStock_MicroAppLogVent} ")
                                                    print("-----------------------------------------------------------")
                                                    NuevCantLub_MicroAppLogVent = int(input(f"| INGRESE LA NUEVA CANTIDAD DE CAJAS PARA ESTE LUBRICANTE : "))
                                                    ModCantCaj_StockFull_MicroAppLogVent(CodLubBus_StockMicroAppLogVent, StockFull_MicroAppLogVent, NuevCantLub_MicroAppLogVent)
                                                    print(BusID_StockFull_MicroAppLogVent(CodLubBus_StockMicroAppLogVent, StockFull_MicroAppLogVent))
                                                    print("--------------------------------------------------------------")
                                                    LubEncStock_MicroAppLogVent.Cant_Caj_Lub = NuevCantLub_MicroAppLogVent
                                                    GenRepModCantLub_MicroAppLogVent(LubEncStock_MicroAppLogVent.ID_Prod, LubEncStock_MicroAppLogVent.Nomb_lub, LubEncStock_MicroAppLogVent.Cant_Caj_Lub)
                                                    RespUs_MicroAppLogVent = str(input("| ¿DESEA ACTUALIZAR LA CANTIDAD DE CAJAS DE OTRO LUBRICANTE? : "))
                                            if RespUs_MicroAppLogVent == "no" or RespUs_MicroAppLogVent == "NO":
                                                print("--------------------------------------------------------------------------------------------------------")
                                                print(f"| UN ARCHIVO CON LAS CANTIDADES ACTUALIZADAS DE LAS CAJAS DE LUBRICANTES FUE CREADO EN LA CARPETA DATA |")
                                                print("--------------------------------------------------------------------------------------------------------")
                                                print(Salir_MicroAppLogVent())
                                        elif OpEscActLub_MicroAppLogVent == "prec" or OpEscActLub_MicroAppLogVent == "PREC":
                                            print("-------------------------------------------------------------")
                                            NuevPrecLub_MicroAppLogVent = float(input(f"| INGRESE EL NUEVO PRECIO DE LAS CAJAS PARA ESTE LUBRICANTE : "))
                                            ModPrecCaj_StockFull_MicroAppLogVent(CodLubBus_StockMicroAppLogVent, StockFull_MicroAppLogVent, NuevPrecLub_MicroAppLogVent)
                                            print(BusID_StockFull_MicroAppLogVent(CodLubBus_StockMicroAppLogVent, StockFull_MicroAppLogVent))
                                            print("----------------------------------------------------------------")
                                            LubEncStock_MicroAppLogVent.Prec_Caj_Lub = NuevPrecLub_MicroAppLogVent
                                            GenRepModPrecLub_MicroAppLogVent(LubEncStock_MicroAppLogVent.ID_Prod, LubEncStock_MicroAppLogVent.Nomb_lub, LubEncStock_MicroAppLogVent.Prec_Caj_Lub)
                                            RespUs_MicroAppLogVent = str(input(f"| ¿DESEA ACTUALIZAR EL PRECIO DE LAS CAJAS DE OTRO LUBRICANTE? : "))
                                            while RespUs_MicroAppLogVent == "si" or RespUs_MicroAppLogVent == "SI":
                                                print("---------------------------------")
                                                CodLubBus_StockMicroAppLogVent = int(input(f"| INGRESE CODIGO DEL LUBRICANTE : "))
                                                LubEncStock_MicroAppLogVent = (BusID_StockFull_MicroAppLogVent(CodLubBus_StockMicroAppLogVent, StockFull_MicroAppLogVent))
                                                if LubEncStock_MicroAppLogVent is None:
                                                    print("---------------------------------------")
                                                    print(f"| ERROR : LUBRICANTE {CodLubBus_StockMicroAppLogVent} NO ENCONTRADO |")
                                                    break
                                                if LubEncStock_MicroAppLogVent is not None:
                                                    print("-----------------------")
                                                    print(f"| LUBRICANTE ENCONTRADO {LubEncStock_MicroAppLogVent} ")
                                                    print("-------------------------------------------------------------")
                                                    NuevPrecLub_MicroAppLogVent = float(input(f"| INGRESE EL NUEVO PRECIO DE LAS CAJAS PARA ESTE LUBRICANTE : "))
                                                    ModPrecCaj_StockFull_MicroAppLogVent(CodLubBus_StockMicroAppLogVent, StockFull_MicroAppLogVent, NuevPrecLub_MicroAppLogVent)
                                                    print(BusID_StockFull_MicroAppLogVent(CodLubBus_StockMicroAppLogVent, StockFull_MicroAppLogVent))
                                                    print("----------------------------------------------------------------")
                                                    LubEncStock_MicroAppLogVent.Prec_Caj_Lub = NuevPrecLub_MicroAppLogVent
                                                    GenRepModPrecLub_MicroAppLogVent(LubEncStock_MicroAppLogVent.ID_Prod, LubEncStock_MicroAppLogVent.Nomb_lub, LubEncStock_MicroAppLogVent.Prec_Caj_Lub)
                                                    RespUs_MicroAppLogVent = str(input(f"| ¿DESEA ACTUALIZAR EL PRECIO DE LAS CAJAS DE OTRO LUBRICANTE? : "))
                                            if RespUs_MicroAppLogVent == "no" or RespUs_MicroAppLogVent == "NO":
                                                print("-----------------------------------------------------------------------------------------------------")
                                                print("| UN ARCHIVO CON LOS PRECIOS ACTUALIZADOS DE LAS CAJAS DE LUBRICANTES FUE CREADO EN LA CARPETA DATA |")
                                                print("-----------------------------------------------------------------------------------------------------")
                                                print(Salir_MicroAppLogVent())
                                        else:
                                            print("---------------------------------------------")
                                            print(f"| ESTA OPCION DE ACTUALIZACION NO ES VALIDA |")
                                            print("---------------------------------------------")
                                except ValueError:
                                    print("---------------------------------------------------")
                                    print(f"| ERROR - SOLO SE PUEDEN INGRESAR NUMEROS ENTEROS |")
                                    print("---------------------------------------------------")
                            elif Opc_OtOp_MicroAppLogVent == "cl" or Opc_OtOp_MicroAppLogVent == "CL":
                                try:
                                    print("--------------------------------")
                                    CodLubBus_StockMicroAppLogVent = int(input(f"| INGRESE CODIGO DE LUBRICANTE : "))
                                    LubEncStock_MicroAppLogVent = BusID_StockFull_MicroAppLogVent(CodLubBus_StockMicroAppLogVent, StockFull_MicroAppLogVent)
                                    if LubEncStock_MicroAppLogVent is None:
                                        print("---------------------------------------")
                                        print(f"| ERROR : LUBRICANTE {CodLubBus_StockMicroAppLogVent} NO ENCONTRADO |")
                                    if LubEncStock_MicroAppLogVent is not None:
                                        print("-----------------------")
                                        print(f"| LUBRICANTE ENCONTRADO {LubEncStock_MicroAppLogVent} ")
                                        print("---------------------------------------------")
                                        CantCajComp_MicroAppLogVent = int(input("| INGRESE LA CANTIDAD DE CAJAS QUE COMPRARA : "))
                                        MontPagUnitCajLub_MicroAppLogVent = CantCajComp_MicroAppLogVent * LubEncStock_MicroAppLogVent.Prec_Caj_Lub
                                        MontPagAcu_MicroAppLogVent += MontPagUnitCajLub_MicroAppLogVent
                                        CompCajLub_StockFull_MicroAppLogVent(CodLubBus_StockMicroAppLogVent, StockFull_MicroAppLogVent, CantCajComp_MicroAppLogVent)
                                        print(f"| EL MONTO ACUMULADO A PAGAR ES DE : {MontPagAcu_MicroAppLogVent} ")
                                        print("------------------------------------")
                                        GenRepParcCompLub_MicroAppLogVent(LubEncStock_MicroAppLogVent.ID_Prod, LubEncStock_MicroAppLogVent.Nomb_lub, CantCajComp_MicroAppLogVent, LubEncStock_MicroAppLogVent.Prec_Caj_Lub, MontPagUnitCajLub_MicroAppLogVent, MontPagAcu_MicroAppLogVent)
                                        RespUs_MicroAppLogVent = str(input("| ¿DESEA COMPRAR CAJAS DE OTRO LUBRICANTE? : "))
                                        while RespUs_MicroAppLogVent == "si" or RespUs_MicroAppLogVent == "SI":
                                            print("--------------------------------")
                                            CodLubBus_StockMicroAppLogVent = int(input(f"| INGRESE CODIGO DE LUBRICANTE : "))
                                            LubEncStock_MicroAppLogVent = BusID_StockFull_MicroAppLogVent(CodLubBus_StockMicroAppLogVent, StockFull_MicroAppLogVent)
                                            if LubEncStock_MicroAppLogVent is None:
                                                print("---------------------------------------")
                                                print(f"| ERROR : LUBRICANTE {CodLubBus_StockMicroAppLogVent} NO ENCONTRADO |")
                                                break
                                            if LubEncStock_MicroAppLogVent is not None:
                                                print("-----------------------")
                                                print(f"| LUBRICANTE ENCONTRADO {LubEncStock_MicroAppLogVent} ")
                                                print("---------------------------------------------")
                                                CantCajComp_MicroAppLogVent = int(input("| INGRESE LA CANTIDAD DE CAJAS QUE COMPRARA : "))
                                                MontPagUnitCajLub_MicroAppLogVent = CantCajComp_MicroAppLogVent * LubEncStock_MicroAppLogVent.Prec_Caj_Lub
                                                MontPagAcu_MicroAppLogVent += MontPagUnitCajLub_MicroAppLogVent
                                                CompCajLub_StockFull_MicroAppLogVent(CodLubBus_StockMicroAppLogVent, StockFull_MicroAppLogVent, CantCajComp_MicroAppLogVent)
                                                print(f"| EL MONTO ACUMULADO A PAGAR ES DE : {MontPagAcu_MicroAppLogVent} ")
                                                print("------------------------------------")
                                                GenRepParcCompLub_MicroAppLogVent(LubEncStock_MicroAppLogVent.ID_Prod, LubEncStock_MicroAppLogVent.Nomb_lub, CantCajComp_MicroAppLogVent, LubEncStock_MicroAppLogVent.Prec_Caj_Lub, MontPagUnitCajLub_MicroAppLogVent, MontPagAcu_MicroAppLogVent)
                                                RespUs_MicroAppLogVent = str(input("| ¿DESEA COMPRAR CAJAS DE OTRO LUBRICANTE? : "))
                                        if RespUs_MicroAppLogVent == "no" or RespUs_MicroAppLogVent == "NO":
                                            if MontPagAcu_MicroAppLogVent >= MontMinPagAcu_MicroAppLogVent:
                                                print("----------------------------------")
                                                CodDescIng_MicroAppLogVent = str(input("| INGRESE SU CODIGO DE DESCUENTO : "))
                                                MontTotComp_MicroAppLogVent = CalcDesc_MicroAppLogVent(CodDescIng_MicroAppLogVent, UsMicroApp_LogVent, MontPagAcu_MicroAppLogVent)
                                                GenRepFinCompLub_MicroAppLogVent(CodDescIng_MicroAppLogVent, MontPagAcu_MicroAppLogVent, MontTotComp_MicroAppLogVent)
                                            print("| UN ARCHIVO CON TODAS LAS COMPRAS DE LUBRICANTES REALIZADAS FUE CREADO EN LA CARPETA DATA |")
                                            print("--------------------------------------------------------------------------------------------")
                                            print(Salir_MicroAppLogVent())
                                except ValueError:
                                    print("---------------------------------------------------")
                                    print(f"| ERROR - SOLO SE PUEDEN INGRESAR NUMEROS ENTEROS |")
                                    print("---------------------------------------------------")
                            else:
                                print("------------------------------------")
                                print(f"| LA OPCION INGRESADA NO ES VALIDA |")
                                print("------------------------------------")
                        case 2:
                            print("---------------------------------------")
                            print(f"| SALIENDO DE LA MICROAPP, HASTA PRONTO {UsMicroApp_LogVent[0]} ...")
                            print("---------------------------------------")
                            CargAcc_MicroAppLogVent()
                            print(Salir_MicroAppLogVent())
                        case _:
                            print("---------------------------------------------------------------------")
                            print(f"| LA OPCION INGRESADA NO EXISTE EN LA MICRO APP LOGISTICA DE VENTAS |")
                            print("---------------------------------------------------------------------")
                            print(Salir_MicroAppLogVent())
            elif RespUsAcc_MicroAppVentLog == "no" or RespUsAcc_MicroAppVentLog == "NO":
                print("-------------")
                print(f"| HASTA LUEGO {UsMicroApp_LogVent[0]} ...")
                print("-------------")
                print(Salir_MicroAppLogVent())
        except ValueError:
            print("--------------------")
            print("| ERROR ENCONTRADO : ALGUN DATO INGRESADO ES INCORRECTO ")
            print("--------------------")
            print(Salir_MicroAppLogVent())
    elif RespUs_MicroAppLogVent == "no" or RespUs_MicroAppLogVent == "NO":
        print("-------------")
        print(f"| HASTA LUEGO ...")
        print("-------------")
        print(Salir_MicroAppLogVent())
else:
    print("--------------------------------------------------------------------")
    print(f"| LA MICROAPP LOGISTICA DE VENTAS CUENTA CON UN USUARIO REGISTRADO |")
    print("--------------------------------------------------------------------")
    print(Salir_MicroAppLogVent())