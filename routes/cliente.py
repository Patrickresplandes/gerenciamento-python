from flask import Blueprint, render_template, request
from database.cliente import CLIENTES

cliente_route = Blueprint('cliente', __name__)

"""
Rota de Clientes

/clientes/ (get) - Listar clientes
/clientes/post (post) - inserir o cliente no servidor 
/clientes/<id> (get) - obter dados de um cliente
/clientes/new (get) - renderiza o formulario para criar um cliente
/clientes/<id>/edit (get) - renderizar um formulario para editar um cliente
/clientes/<id>/update (put) - atualizar os dados do cliente
/clientes/<id>/delete (delete) - deleta o registro do usuario
"""


@cliente_route.route('/')
def lista_clientes():
   return render_template('lista_clientes.html', clientes=CLIENTES)

@cliente_route.route('/', methods=['POST'])
def inserir_clientes():
   data= request.json
   novo_usuario = {
      "id":len(CLIENTES) + 1,
      "nome":data['nome'],
      "email":data['email'],
   }

   CLIENTES.append(novo_usuario)
   return render_template('item_clientes.html', cliente=novo_usuario)

@cliente_route.route('/new')
def form_cliente():
   return render_template('form_clientes.html')


@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
   cliente = list(filter(lambda c: c['id'] == cliente_id, CLIENTES))[0]
   return render_template('detalhe_clientes.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
      cliente = None
      for c in CLIENTES:
         if c['id'] == cliente_id:
            cliente = c
      return render_template('form_clientes.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def update_cliente(cliente_id):
   cliente_editado = None

   #obter dados do form
   data = request.json
   #obter usuario pelo id
   for c in CLIENTES: 
      if c['id'] == cliente_id:
         c['nome'] = data.nome
         c['email'] = data.email

         cliente_editado = c
   #editar usuario
   return render_template('item_clientes.html', cliente=cliente_editado)

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def delete_cliente(cliente_id):
   global CLIENTES
   CLIENTES =  [ c for c in CLIENTES if c['id'] != cliente_id ]

   return {'delete': 'ok'}