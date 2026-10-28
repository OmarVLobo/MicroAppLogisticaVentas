class Alm_Lub:
    def __init__(self, ID_Prod, Cod_UnManAl, Tipo_Lub, Nomb_lub, Cant_Caj_Lub, Prec_Caj_Lub):
        self.ID_Prod = ID_Prod
        self.Cod_UnManAl = Cod_UnManAl
        self.Tipo_Lub = Tipo_Lub
        self.Nomb_lub = Nomb_lub
        self.Cant_Caj_Lub = Cant_Caj_Lub
        self.Prec_Caj_Lub = Prec_Caj_Lub
    def __str__(self):
        return f"ID : {self.ID_Prod} CODIGO : {self.Cod_UnManAl} TIPO : {self.Tipo_Lub} NOMBRE : {self.Nomb_lub} CANT : {self.Cant_Caj_Lub} PRECIO : {self.Prec_Caj_Lub} "
    def ActualizarCantCajLub_MicroAppLogVent(self, NuevCant_CajLub):
        if not isinstance(NuevCant_CajLub, int):
            print("-----------------------------------------------------------")
            print(f"| ERROR - LA CANTIDAD INGRESADA DEBE SER UN NUMERO ENTERO |")
            print("-----------------------------------------------------------")
            return False
        if NuevCant_CajLub <= 0:
            print("-------------------------------------------------------")
            print(f"| ERROR - LA CANTIDAD INGRESADA DEBE SER MAYOR A CERO |")
            print("--------------------------------------------------------")
            return False
        self.Cant_Caj_Lub = NuevCant_CajLub
        print("-----------------------------------------------------------------")
        print(f"| LA CANTIDAD DE CAJAS PARA ESTE LUBRICANTE HA SIDO ACTUALIZADA |")
        print("-----------------------------------------------------------------")
        return True
    def ActualizarPrecCajLub_MicroAppLogVent(self, NuevPrec_CajLub):
        if not isinstance(NuevPrec_CajLub, float):
            print("------------------------------------------------------------")
            print(f"| ERROR - EL PRECIO INGRESADO DEBE TENER NUMEROS DECIMALES |")
            print("------------------------------------------------------------")
            return False
        if NuevPrec_CajLub <= 0:
            print("-----------------------------------------------------")
            print(f"| ERROR - EL PRECIO INGRESADO DEBE SER MAYOR A CERO |")
            print("-----------------------------------------------------")
            return False
        self.Prec_Caj_Lub = NuevPrec_CajLub
        print("-------------------------------------------------------------")
        print("| EL PRECIO POR CAJA DE ESTE LUBRICANTE HA SIDO ACTUALIZADO |")
        print("-------------------------------------------------------------")
        return True
    def ComprarLub_MicroAppLogVent(self, CantComp_CajLub):
        if not isinstance(CantComp_CajLub, int):
            print("--------------------------------------------------")
            print(f"| LA CANTIDAD DE CAJAS A COMPRAR DEBE SER ENTERA |")
            print("--------------------------------------------------")
            return False
        if CantComp_CajLub <= 0:
            print("--------------------------------------------------------")
            print(f"| LA CANTIDAD DE CAJAS A COMPRAR DEBE SER MAYOR A CERO |")
            print("--------------------------------------------------------")
            return False
        if not hasattr(self, "HistCompLub"):
            self.HistCompLub = []
        MonTotComp = CantComp_CajLub * self.Prec_Caj_Lub
        self.Cant_Caj_Lub += CantComp_CajLub
        self.HistCompLub.append(MonTotComp)
        TotGenComp = sum(self.HistCompLub)
        print("-----------------------------------")
        print(f"| EL MONTO PARCIAL A PARGAR ES DE : {TotGenComp} NUEVOS SOLES |")
        print("-----------------------------------")
        return True
Lub_1 = Alm_Lub(1, "M40-SH001", "Mono-G", "Shell Rimula R2 SAE 40", 12, 285.00)
Lub_2 = Alm_Lub(2, "M50-MB002", "Mono-G", "Mobil Delvac 30 SAE 50", 8, 310.50)
Lub_3 = Alm_Lub(3, "M40-CS003", "Mono-G", "Castrol CRB ULTRA GT40", 15, 270.00)
Lub_4 = Alm_Lub(4, "M40-VT004", "Mono-G", "Vistony Monograd 40 HD", 20, 195.00)
Lub_5 = Alm_Lub(5, "M50-CH005", "Mono-G", "Chevron Delo 400 SAE 5", 6, 325.00)
Lub_6 = Alm_Lub(6,"MG15-SH006", "Mult-G", "Shell Rimula R4 15W-40", 10, 420.00)
Lub_7 = Alm_Lub(7,"MG15-MB007", "Mult-G", "Mobil Delvac MX 15W-40", 12, 445.00)
Lub_8 = Alm_Lub(8,"MG20-CS008", "Mult-G", "Castrol UltraGTX 20W-50", 18, 350.00)
Lub_9 = Alm_Lub(9,"MG20-VT009", "Mult-G", "Vistony Premium 20W-G50", 25, 245.00)
Lub_10 = Alm_Lub(10,"MG15-RP010", "Mult-G", "Repsol Diesel 15w-40T", 9, 395.00)
StockFull_MicroAppLogVent = [Lub_1, Lub_2, Lub_3, Lub_4, Lub_5, Lub_6, Lub_7, Lub_8, Lub_9, Lub_10]