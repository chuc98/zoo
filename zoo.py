class animal:
        
    def get_tipo(self):
        nanimales= input("¿Cuantos animales quieres crear?")    
        print(nanimales)
        lista = ['x']
        
        for element in lista:
            set_nombre
        print (element)
    
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo   = tipo
       
    def set_nombre(self,nombre): 
        self.nombre = nombre
          
    def get_nombre(self):
       print(self.nombre)
       
    def set_tipo(self,tipo):
       self.tipo = tipo     
       
          
def main():
	animali = animal("pangoringo","pajaro")
	animali.set_nombre("nopango")
	animali.get_nombre()


if __name__ == "__main__":
	main()