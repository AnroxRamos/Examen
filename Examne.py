#Jose Angel Pinto Ramos 26
from abc import ABC, abstractmethod
import os
os.system("cls")

class Empleado_J26(ABC):
    def __init__(self, rfc, apellidos, nombres):
        #ENCAPSULAMIENTO
        self._rfc = rfc
        self._apellidos = apellidos
        self._nombres = nombres
    
    @abstractmethod
    def calcular_ingresos(self):
        pass
    
    @abstractmethod
    def calcular_descuento(self):
        pass
    
    @abstractmethod
    def calcular_sueldo_neto(self):
        pass
    
    def mostrar_informacion(self):
        return f"Empleado: {self._nombres} {self._apellidos}, RFC: {self._rfc}"
 
class EmpleadoVendedor_J26(Empleado_J26):
    def __init__(self, rfc, apellidos, nombres, monto_vendido, tasa_comision):
        super().__init__(rfc, apellidos, nombres)
        self.monto_vendido = monto_vendido
        self.tasa_comision = tasa_comision
 
    def calcular_ingresos(self):
        return self.monto_vendido * self.tasa_comision
 
    def calcular_bonificacion(self):
        if self.monto_vendido < 1000:
            return 0
        
        elif 1000 <= self.monto_vendido <= 5000:
            return self.calcular_ingresos() * 0.05
        
        else:
            return self.calcular_ingresos() * 0.10
 
    def calcular_descuento(self):
        ingresos = self.calcular_ingresos()
        
        if ingresos < 1000:
            return ingresos * 0.11
        
        elif ingresos <= 5000:
            return ingresos * 0.15
        
        else:
            return ingresos * 0.15
    
    def calcular_sueldo_neto(self):
        ingresos = self.calcular_ingresos()
        
        bonificacion = self.calcular_bonificacion()
        
        descuento = self.calcular_descuento()
        
        sueldo_neto = ingresos + bonificacion - descuento
#EXCEPCIONES 
        if sueldo_neto < 150:
            raise SalarioInvalidoException("El salario es menor al minimo.")
        return sueldo_neto
 
class EmpleadoPermanente_J26(Empleado_J26):
    def __init__(self, rfc, apellidos, nombres, sueldo_base, numero_seguro_social):
        super().__init__(rfc, apellidos, nombres)
        self.sueldo_base = sueldo_base
        self.numero_seguro_social = numero_seguro_social
 
    def calcular_ingresos(self):
        return self.sueldo_base
 
    def calcular_descuento(self):
        return self.sueldo_base * 0.11
 
    def calcular_sueldo_neto(self):
        ingresos = self.calcular_ingresos()
        
        descuento = self.calcular_descuento()
        
        sueldo_neto = ingresos - descuento
#EXCEPCIONES   
        if sueldo_neto < 150:
            raise SalarioInvalidoException("El salario es menor al mimimo.")
        return sueldo_neto
    
class SalarioInvalidoException(Exception):
    pass

# Pruebas y Polimorfismo
try:
    vendedor = EmpleadoVendedor_J26("12345", "Tilin", "Juan", 3000, 0.5)
    print(vendedor.mostrar_informacion())
    print(f"Ingresos: {vendedor.calcular_ingresos()}")
    print(f"Bonificación: {vendedor.calcular_bonificacion()}")
    print(f"Sueldo Neto: {vendedor.calcular_sueldo_neto()}")
    
    print("-"*40)
    print("Permanente")
    permanente = EmpleadoPermanente_J26("67890", "Sech", "Pepe", 6000, "12345678")
    print(permanente.mostrar_informacion())
    print(f"Ingresos: {permanente.calcular_ingresos()}")
    print(f"Sueldo Neto: {permanente.calcular_sueldo_neto()}")
    
except SalarioInvalidoException as tilin:
    print(tilin)