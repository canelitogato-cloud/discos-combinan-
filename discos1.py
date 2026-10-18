import math
import random
import time
import sympy as sp

class NeuronaEnigmaEsferica:
    def __init__(self, orden_rotores=["D1", "D2", "D3"]):
        self.x = sp.Symbol('x')
        self.separacion = 0.88
        self.GRADIENTE_OBJETIVO = 3.141592653589793  # π (3.1416)
        self.TOLERANCIA = 0.10  # Margen de acoplamiento del trinquete Enigma
        
        self.orden_rotores = orden_rotores

        # LOS COMPONENTES DE TUS TRES DISCOS (ESTRICTAMENTE CONSERVADOS)
        self.formulas_algebra = [self.x**2 + 2*self.x, sp.sin(self.x), 3*self.x, self.x**3, sp.exp(self.x)]
        self.formulas_derivadas = ["derivada_simple", "derivada_cuadratica", "mantener"]
        self.formulas_integrales = ["integral_indefinida", "multiplicar_por_x", "integral_definida_0_1"]

        self.mapeo_discos = {
            "D1": {"nombre": "Álgebra/Física", "contenido": self.formulas_algebra},
            "D2": {"nombre": "Derivadas", "contenido": self.formulas_derivadas},
            "D3": {"nombre": "Integrales", "contenido": self.formulas_integrales}
        }

        print("==================================================================================")
        print("🔒 MOTOR CRIPTOGRÁFICO ENIGMA HIPERESFÉRICO ACTIVADO (FILTRO SILENCIOSO)")
        print(f" -> Orden de Rotores en los ejes Z: {self.orden_rotores}")
        print(f" -> Separación constante de placas: {self.separacion} unidades.")
        print(f" -> Operando en silencio... Solo se imprimirán los desbloqueos automáticos.")
        print("==================================================================================\n")

    def reflector_sinaptico(self, componente1, componente2, componente3):
        algebra = None
        derivada = None
        integral = None

        elementos = [componente1, componente2, componente3]
        for i, rotor in enumerate(self.orden_rotores):
            if rotor == "D1": algebra = elementos[i]
            if rotor == "D2": derivada = elementos[i]
            if rotor == "D3": integral = elementos[i]

        print(f"   |-- 🧩 Componentes alineados en la vertical de {self.separacion} u.:")
        print(f"   |   [Base]: {componente1}  •  [Centro]: {componente2}  •  [Tope]: {componente3}")

        if derivada == "derivada_simple":
            intermedio = sp.diff(algebra, self.x)
            paso_txt = f"d/dx [{algebra}] = {intermedio}"
        elif derivada == "derivada_cuadratica":
            intermedio = sp.diff(algebra, self.x, 2)
            paso_txt = f"d²/dx² [{algebra}] = {intermedio}"
        else:
            intermedio = algebra
            paso_txt = f"Mantiene [{algebra}]"

        if integral == "integral_indefinida":
            formula_final = sp.integrate(intermedio, self.x)
            op_txt = f"∫({intermedio}) dx"
        elif integral == "integral_definida_0_1":
            formula_final = sp.integrate(intermedio, (self.x, 0, 1))
            op_txt = f"∫₀¹({intermedio}) dx"
        else:
            formula_final = intermedio * self.x
            op_txt = f"({intermedio}) * x"

        print(f"   |-- 🧪 Cifrado Intermedio: {paso_txt}")
        print(f"   |-- 🔥 Procesamiento Reflector: {op_txt}")
        print(f"   └── 📝 FÓRMULA INÉDITA GENERADA: {formula_final}\n")
        print("-" * 80)

    def descifrar_espacio_esferico(self, pasos=300):
        a1, a2, a3 = 0.0, 0.0, 0.0

        for paso in range(1, pasos + 1):
            a1 += 0.12
            
            if abs(a1 % math.pi) < self.TOLERANCIA:
                a2 -= 0.08
                if abs(a2 % math.pi) < self.TOLERANCIA:
                    a3 += 0.05

            r1 = a1 % (2 * math.pi)
            r2 = a2 % (2 * math.pi)
            r3 = a3 % (2 * math.pi)

            gradiente_actual = (abs(r1 - r2) + abs(r3 - r2)) % math.pi
            gradiente_renderizado = gradiente_actual * 2.0

            if abs(gradiente_renderizado - self.GRADIENTE_OBJETIVO) < self.TOLERANCIA:
                print(f"✨ [Paso {paso:03d}] 🔓 ¡CÓDIGO ENIGMA DESBLOQUEADO! Gradiente: {gradiente_renderizado:.4f}")
                
                # 🛠️ CORRECCIÓN: Extraer de mapeo usando strings ("D1", "D3", "D2") de forma indexada individualmente
                c1 = random.choice(self.mapeo_discos[self.orden_rotores[0]]["contenido"])
                c2 = random.choice(self.mapeo_discos[self.orden_rotores[1]]["contenido"])
                c3 = random.choice(self.mapeo_discos[self.orden_rotores[2]]["contenido"])
                
                self.reflector_sinaptico(c1, c2, c3)
                time.sleep(0.5)

if __name__ == "__main__":
    clave_rotores = ["D1", "D3", "D2"]  
    maquina = NeuronaEnigmaEsferica(orden_rotores=clave_rotores)
    maquina.descifrar_espacio_esferico(pasos=300)