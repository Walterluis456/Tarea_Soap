from zeep import Client

client = Client('http://localhost:8000')
result = client.service.Saludar(nombre="Walterluis")
result1= client.service.SumaDosNumeros(x=2,y=2)
result2 = client.service.CadenaPalindromo(cadena="ojo")
print(result)
print(result1)
print(result2)