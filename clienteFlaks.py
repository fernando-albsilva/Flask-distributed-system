import requests
import json
import urllib.parse


anos = []
id_venda_por_ano = []
clientes_que_realizaram_compra = []
clientes_fieis=[]
lista_de_ids = []


api= "http://127.0.0.1:8080"

url= api+"/anos"

dados= requests.get(url).json()

#pega anos que existem vendas
for d in dados:
    anos.append(d['year(InvoiceDate)'])
  
    

#cria um dicionario com id de venda e o ano referente
for ano in anos:
    url= api+"/vendas_por_ano/" + str(ano)
    dados= requests.get(url).json()
    for d in dados:
        id_venda_por_ano.append({'ano':ano,'id_venda':d['invoiceid']})



#retorna id de clientes que realizaram compra a compra de acordo como id da venda, criando um dicionario com ano, id da venda e id do cliente. 
for elemento in id_venda_por_ano:
    url= api+"/cliente_da_venda/" + str(elemento['id_venda'])
    dados= requests.get(url).json()
    for d in dados:
        lista_de_ids.append(d['customerId'])
        clientes_que_realizaram_compra.append({'ano':elemento['ano'],'id_venda':elemento['id_venda'],'customerId':d['customerId']})


cont=0     
for cliente in lista_de_ids:
    for ano in anos:
        for elemento in clientes_que_realizaram_compra:
            if ( (cliente == elemento['customerId']) and (ano == elemento['ano']) ):
                cont=cont+1
                break
    if cont == len(anos):
        clientes_fieis.append(elemento['customerId'])   
    cont=0 
    
    
    
def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

clientes_fieis = remove_repetidos(clientes_fieis)




for clienteId in clientes_fieis:
    url= api+"/nome_do_cliente/" + str(clienteId)
    dados= requests.get(url).json()
    for d in dados:
        print("cliente fiel: "+d['FirstName']+" "+d['Lastname'])
      


