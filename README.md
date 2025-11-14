# 1. Identificação do programa
**Nome:** Identifier
**Descrição:** Uma função que dada uma string determina se a mesma é um identificador válido. uma string é válida como identificador caso comece por uma letra e tenha entre 1 a 6 caracteres.


# 2. Classes de equivalência e Análise de valor limite
O método utilizado para o teste foi o teste de caixa preta, neste teste o que importa são as entradas e saídas que o programa nos oferta, assim nossos critérios foram criados baseados no que esperamos do programa, segundo a descrição do sistema.

## 2.1 Classes de equivalência
### classes válidas:
1. código identificador que começa com uma letra e tem de 1 a 6 caracteres, sendo estes apenas letras e/ou dígitos. Classe V1

### classe inválidas:
código identificador que comece por um caractere fora do alfabeto. Classe I1
1. O código identificador é uma string vazia. Classe I2
2. O código identificador contém mais de 6 caracteres. Classe V3
3. O código identificador contém caracteres especiais. Classe V4
4. O código identificador contém caracteres de línguas estrangeiras. Classe V5


Regra de tamanho (1–6):

-   Valor mínimo: 1 caractere → válido desde que respeite a(s) outra(s) regra(s)
    
-   Valor abaixo do mínimo: 0 caracteres → inválido.
    
-   Valor máximo: 6 caracteres → válido desde que respeite a(s) outra(s) regra(s)
    
-   Valor acima do máximo: 7 caracteres ou mais → inválido.
    

Regra de Início (primeiro caractere deve ser uma letra):

-   Primeira posição é uma letra (a–z ou A–Z) → válida desde que respeite a(s) outra(s) regra(s).
    
-   Primeira posição é um dígito (0–9) → inválido.
    
-   Primeira posição é um símbolo ou espaço → inválido.
  

## 2.2 Casos de Teste
| Caso | Entrada | Descrição | Resultado Esperado |
| :--- | :--- | :--- | :--- |
| 1 | "a" | Mínimo válido (1 caractere, começa com letra) | Válido |
| 2 | "abcdef" | Máximo válido (6 letras) | Válido |
| 3 | "abcdefg" | Ultrapassa limite de tamanho | Inválido |
| 4 | "1abc" | Começa com número | Inválido |
| 5 |"a1b2" | Letras e números válidos | Válido |
| 6 | "a!b" | Contém símbolo inválido | Inválido |
| 7 | "" | Comprimento zero | Inválido |
| 8 | "Z9xK2" | Formato válido com mistura de casos | Válido |

# 4. Como testar em sua maquina local
O Identifier usa a biblioteca pytest para rodar os testes, foi usado um ambiente virtual nesse processo
 ### 4.1 iniciando o ambiente virtual
 Dentro da pasta teste-pytest/ (nível raiz do projeto):
** Windows:**

```
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac**

```
python3 -m venv venv
source venv/bin/activate
```

### 4.2 Instalando dependências do requirements.txt
instale os requisitos por meio do arquivo requirements.txt
```
pip install -r requirements.txt
```

Confirme que o pytest foi instalado:
```
pytest --version
```

### 4.3 Executando o teste
ainda dentro da pasta raiz do projeto execute o comando
```
pytest -v
```

os testes deverão rodar no terminal de sua maquina local, indicando se o programa atende os requisitos.

# 5. Execução de CI/CD
CI/CD significa Integração Contínua (CI) e Entrega Contínua/Implantação Contínua (CD).
Essa prática de integração permite testes automatizados de pontos centrais do sistema. Imaginando que o identifier é uma parte importante de um sistema maior poderiamos executar seu teste a cada novo merge feito para a branch principal do projeto, caso algum defeito exista no trecho automatizado podemos impedir que o erro chegue a produção do sistema
## 5.1 Imagens do funcionamento do CI/CD
### 5.1.1
primeiro é necessário criar um ambiente virtual no github para executrar os testes, o github automaticamente cria um trabalho que irá criar essa máquina de testes
![Criação de trabalhos](1.PNG)

### 5.1.2
O passo de checkout "baixa" o código do repositorio nessa maquina
![Checkout](2.PNG)

### 5.1.3
O passso de "Configurar python" configura na máquina qual a versão do python usar 
![Configurando python](3.PNG)

### 5.1.4
O passso de "Instalar dependencias" instala as dependencias do projeto
![baixando dependencias 2](4_1.PNG)
![baixando dependencias 2](4_2.PNG)

### 5.1.5
O passso de "Executar testes" executa os testes nos scripts teste_*.py que criamos, nesse caso test_identifier.py
![Executar testes](5.PNG)

### 5.1.6
Por último, o github executa, por conta propria, a limpeza da maquina de testes e finalização dos processos
![Executar testes](6.PNG)