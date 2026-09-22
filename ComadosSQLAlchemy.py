from BlogHashtagTreinamentos import app, db
from BlogHashtagTreinamentos.models import Usuario, Post

with app.app_context():
    db.create_all()  #### Cria as tabelas no banco de dados.


    #### INSERT

    """
    
   
    with app.app_context():
        usuario = Usuario(username='Fernanda', senha='654321', email='nanduka_martins@hotmail.com', cursos="Primeiros Socorros")
        db.session.add(usuario)
        db.session.commit()
    """


    """
    
    with app.app_context():
        listar_usuario = Usuario.query.first()
        print(listar_usuario.username)
        print(listar_usuario.email)
        print(listar_usuario.senha)

    """

    """
    
    with app.app_context():
        listar_usuario = Usuario.query.all()
        print(listar_usuario[0])
    
    """

    """
    
    with app.app_context():
        lista_usario = Usuario.query.filter_by(cursos="Primeiros Socorros").first()
        print(lista_usario.email)
        print(lista_usario.senha)
        print(lista_usario.cursos)
        print(lista_usario.username)
    
    """

    #### INSERT

    """
    
    with app.app_context():
        post = Post(titulo='Enfermagem nas escolas', corpo="O papel da disciplina enfermagem na escolas do ensino básico",id_usuario=2)
        db.session.add(post)
        db.session.commit()
        
    """

    """
    
    meu_post = Post.query.filter_by(titulo='Enfermagem nas escolas').first()
    print(meu_post.id_usuario)
    print(meu_post.autor.username)
    
    """