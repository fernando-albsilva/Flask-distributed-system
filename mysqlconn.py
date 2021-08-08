import mysql.connector
import json
from flask_jsonpify import jsonify

class MysqlConn:
    
        
    
    # Prova
    
    def retorna_lista_anos_prova(self):
        
        conn = mysql.connector.connect (host="sd2021-1.cyq7mrt5yfwe.us-east-1.rds.amazonaws.com", port="3306", user="admin", passwd="admin1234", database="chinook");
       
        cursor = conn.cursor()
            
        cursor.execute("select distinct year(InvoiceDate) from invoices")
           
        results = cursor.fetchall()
            
        objeto =[]
        
        lista=[dict(zip(cursor.column_names,x)) for x in results]
       
        print(type(lista))
          
        return jsonify(lista)
        
        
                
    def retorna_vendas_por_ano(self,id):
            
        conn = mysql.connector.connect (host="sd2021-1.cyq7mrt5yfwe.us-east-1.rds.amazonaws.com", port="3306", user="admin", passwd="admin1234", database="chinook");
       
        cursor = conn.cursor()
            
        cursor.execute(f"select invoiceid from invoices where year(invoicedate) = {id}")
           
        results = cursor.fetchall()
            
        objeto =[]
        
        lista=[dict(zip(cursor.column_names,x)) for x in results]
       
        print(type(lista))
          
        return jsonify(lista)
       
       
                    
    def retorna_id_cliente_que_realizou_compra(self,id):
            
        conn = mysql.connector.connect (host="sd2021-1.cyq7mrt5yfwe.us-east-1.rds.amazonaws.com", port="3306", user="admin", passwd="admin1234", database="chinook");
       
        cursor = conn.cursor()
            
        cursor.execute(f"select customerId from invoices where invoiceid =  {id}")
           
        results = cursor.fetchall()
            
        objeto =[]
        
        lista=[dict(zip(cursor.column_names,x)) for x in results]
       
        print(type(lista))
          
        return jsonify(lista)
        
        

    def retorna_nome_do_cliente_fiel(self,id):
        
        conn = mysql.connector.connect (host="sd2021-1.cyq7mrt5yfwe.us-east-1.rds.amazonaws.com", port="3306", user="admin", passwd="admin1234", database="chinook");
       
        cursor = conn.cursor()
            
        cursor.execute(f"SELECT FirstName,Lastname FROM chinook.customers where CustomerId = {id}")
           
        results = cursor.fetchall()
            
        objeto =[]
        
        lista=[dict(zip(cursor.column_names,x)) for x in results]
       
        print(type(lista))
          
        return jsonify(lista)