from flask import Flask
from mysqlconn import MysqlConn

app = Flask(__name__)


@app.route("/anos")
def retorna_lista_anos_prova():
    mysql = MysqlConn()
    lista = mysql.retorna_lista_anos_prova()
    return lista

@app.route("/vendas_por_ano/<id>")
def retorna_vendas_por_ano (id):
    mysql = MysqlConn()
    lista = mysql.retorna_vendas_por_ano(id)
    return lista

@app.route("/cliente_da_venda/<id>")
def retorna_id_cliente_que_realizou_compra (id):
    mysql = MysqlConn()
    lista = mysql.retorna_id_cliente_que_realizou_compra(id)
    return lista
    
@app.route("/nome_do_cliente/<id>")
def retorna_nome_do_cliente_fiel (id):
    mysql = MysqlConn()
    lista = mysql.retorna_nome_do_cliente_fiel(id)
    return lista



app.run(port=8080,debug=True)
    
    