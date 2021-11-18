# Autor: Luís Humbeto Chaves Senno
# Data: 18/11/2021
# Linguagem: Python 3.9.5 64-bit
# Problema: Euler Project 246

import math

class Elipse():
    def __init__(self, a, b, c, foco1, foco2):
        self.a = a
        self.b = b
        self.c = c
        self.f1 = foco1
        self.f2 = foco2
        self.centro = [(foco1[0] + foco2[0]) / 2, (foco1[1] + foco2[1]) / 2] # achando o centro da elipse para fazer o deslocamento

    #def deslocar_origem():

    def esta_fora(self, p): 
        if (((p[0] / self.a) ** 2 + ((p[1] / self.b) ** 2)) > 1):
            return True
        else:
            return False

    def pontos_de_tangencia(self, p): # Para cordenadas (X,Y) X > 0 e Y > 0 já que o denominador é múltiplo de X e Y
        aux = p[0] ** 2 / self.a ** 2 + p[1] ** 2 / self.b ** 2
        x1 = (p[0] + self.a * p[1] / self.b * math.sqrt(aux - 1)) / aux
        x2 = (p[0] - self.a * p[1] / self.b * math.sqrt(aux - 1)) / aux
        y1 = (1 - p[0] / self.a * x1 / self.a) * self.b / (p[1] / self.b)
        y2 = (1 - p[0] / self.a * x2 / self.a) * self.b / (p[1] / self.b)
        pontos = [x1,y1,x2,y2]
        return pontos

#Como já foram obtidos os pontos de tangência, para evitar fazer calculos complicados com a tangente e os coeficientes angulares
#foi feito um triângulo com os pontos PRS e então usada a lei dos cossenos para se obter o angulo
def angulo_entre_retas(p, r, s): 
    lado_a = math.dist(p, r)
    lado_b = math.dist(p, s)
    lado_c = math.dist(r, s)
    angulo = math.degrees(math.acos((lado_a ** 2 + lado_b ** 2 - lado_c ** 2)/(2 * lado_a * lado_b))) #lei dos cossenos
    return angulo



e = Elipse(7500, 2500 * math.sqrt(5), 5000, [-5000,0], [5000,0]) # dados obtidos por cálculo no pdf anexado ou fornecidos no problema

# Eixo Y 
m = math.tan(0.5 * (math.pi + math.radians(45)))  # inclinação do ponto mais longe no eixo Y que ainda é valido (calculos e desenho no pdf)
ultimo_y = int(math.sqrt(e.b**2 + e.a**2*(m*m)))
pontos_y = (ultimo_y - int(e.b))
pontos_y *= 2 # Positivos e negativos

# Eixo X
m = math.tan(math.pi - 0.5 * math.radians(45))  # inclinação do ponto mais longe no eixo X que ainda é valido (calculos e desenho no pdf)
ultimo_x = int(math.sqrt(e.a ** 2 + e.b **2 / (m * m)))
pontos_x = (ultimo_x - int(e.a))
pontos_x *= 2 # Positivos e negativos

# Pontos no primeiro quadrante
# Devido a simetria gerada ao se deslocar a elipse para a origem podemos obter todos os pontos multiplicando o resultado obtido por 4
y_max =  ultimo_y + 1 #limites obtido analisando a geometria do problema e sabendo da posição mais distante nos eixos x e y validas
x_max = ultimo_x + 1
y_min = 0
pontos_quadrante = 0
for x in range (1, x_max): #limite obtido analisando a geometria do problema no GeoGebra
    for y in range(1, 19000):
        p=[x,y]
        if (e.esta_fora(p) == True):
            y_min = y - 1 #garante que não vai eliminar um ponto válido
            break
    for y in range(y_max, 0, -1): #usa o máximo cálculado já que o próximo maximo sempre sera menor que o anterior, questão de otimização
        p=[x,y]
        pontost = e.pontos_de_tangencia(p)
        r = [pontost[0], pontost[1]]
        s = [pontost[2], pontost[3]]
        if (angulo_entre_retas(p, r, s) > 45):
            y_max = y 
            break
        y_max = 0
    if (y_max > 0):
        pontos_quadrante += y_max - y_min
    else:
        break
pontos_quadrante *= 4

pontos_total = pontos_quadrante + pontos_x + pontos_y
print(pontos_total)
