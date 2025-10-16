import sys
from identifier import Identifier
def main():
        if len(sys.argv) == 1:
            print("Uso: python main.py <string>")    
        else:
            id_obj = Identifier()
            if id_obj.validate_identifier(sys.argv[1]):
                print("Valido")
            else:
                print("Invalido")

                
if __name__ == "__main__":
        main()
