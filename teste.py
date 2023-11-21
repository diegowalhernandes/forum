from app import app, database
from models import Usuario, Post

#with app.app_context():
    #database.create_all()

#with app.app_context():
#    usuario = Usuario(username="Teste", email="teste@teste.com", senha='123456')
#    usuario2 = Usuario(username="Teste2", email="teste2@teste.com", senha='123456')

#    database.session.add(usuario)
#    database.session.add(usuario2)

#    database.session.commit() """

#with app.app_context():
#   meus_usuarios = Usuario.query.first()
#    print(meus_usuarios.id)
#    print(meus_usuarios.email)
#    print(meus_usuarios.senha)

#with app.app_context():
#    meu_post = Post(id_usuario=1, titulo="Testando criação de Post", corpo="Aqui vai o conteudo do post")
#    database.session.add(meu_post)
#    database.session.commit()

#with app.app_context():
#    post = Post.query.first()
#    print(post.titulo)
#    print(post.corpo)
#    print(post.autor.email)

with app.app_context():
    database.drop_all()
    database.create_all()