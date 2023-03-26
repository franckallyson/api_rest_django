<div align="center" id="cabecalho">
    <h1>API Rest com BD</h1>
    <h3>Franck Allyson da Silva Rocha </h3>
    <h4>4º Período | BSI | IFNMG Campus Salinas</h4>
</div>

1. [Linguagem e Framework](#ling_frame)
2. [Banco de Dados Escolhido](#bd)
3. [DBaaS Escolhido](#dbaas)
4. [Documentação do projeto](#doc)
4.1. [Descrição e Objetivos](#desc_obj)
4.2. [Tecnologias utilizadas](#tec)
4.3. [Como replicar o Projeto](#replica)
4.4. [Como utilizar a API](#util)
4.5. [Deploy de uma API](#deploy)
4.6. [Endpoints Disponíveis](#endpoints)
5. [Creditos](#credits)
6. [Licença](#licenca)

<hr>

<ul style="list-style: none;">
    <li>
        <h3 id="ling_frame">1. Linguagem e Framework Escolhido</h3>
        <div style="padding-left: 30px;">
            Para este exercício, foi escolhido a linguagem Python e o Framework <a href="https://www.djangoproject.com/">Django</a>.<br> O Django disponibiliza a utilização de outro framework, o <i>Django Rest Framework</i>, e com isso a implementação fica <b>extremamente</b> fácil! Vamos continuar!
        </div>
    </li>
    <hr>
    <li>
        <h3 id="bd">2. Banco de Dados Escolhido</h3>
        <div style="padding-left: 30px;">
            O banco de dados escolhido foi o que o próprio django disponibiliza na criação: <b>SQLite</b>. <br>
            Como não vamos manipular grandes quantidades de dados, ele se torna o ideal. Além de ser o mais indicado para pequenos testes.
        </div>
    </li>
    <hr>
    <li>
        <h3 id="dbaas">3. DBaaS escolhido</h3>
        <div style="padding-left: 30px;">
            Não se fez necessário a escolha de um DBaaS específico. Apenas vamos utilizar um ambiente de desenvolvimento integrado (IDE) e serviço de hospedagem web baseado na linguagem de programação Python, o nome dele é <a href="https://www.bing.com/ck/a?!&&p=3ab8966ee8547ad5JmltdHM9MTY3OTQ0MzIwMCZpZ3VpZD0zYjAzYzMwNC01MzA3LTYxNTctMzEzYi1kMTYxNTI5MTYwM2YmaW5zaWQ9NTE5OA&ptn=3&hsh=3&fclid=3b03c304-5307-6157-313b-d1615291603f&psq=python+anywhere+%c3%a9+um+dbaas%3f&u=a1aHR0cHM6Ly93d3cucHl0aG9uYW55d2hlcmUuY29tLw&ntb=1">PythonAnywhere</a>. <br>
            Ele já faz todo o serviço de disponibilizar o banco de dados e a API que criamos, possibilitando que as requisições aconteçam.
        </div>
    </li>
    <hr>
    <li>
        <h3 id="doc">4. Documentação do Projeto</h3>
        <ul style="list-style:none;">
            <li>
                <h4 id="desc_obj">4.1. Descrição e Objetivos</h4>
                <div style="padding-left: 30px;">
                    Este projeto é uma API de Biblioteca, disponibilizamos Autores, Gêneros, Idiomas e Livros. Os três primeiros estão associados aos Livros por meio de relacionamentos do banco de dados, logo, só poderemos criar um Livro se tivermos autores, gêneros e idiomas já inseridos na API. No mais, padrão, as requisições entregam dados em JSON. <br>
                    O principal Objetivo com a execução desse projeto é aprender conceitos de API, Backend e também do próprio Django. Eu particularmente pretendo trabalhar  focado na parte do back-end então pra mim é de grande valia. 
                </div>
            </li>
            <hr>
            <li>
                <h4 id="tec">4.2. Tecnologias e Ferramentas Utilizadas</h4>
                <div style="padding-left: 30px;">
                    <ul>
                        <li>  
                            <h5><a href="https://www.postman.com/">PostMan</a> - ( Execução de testes das requisições )</h5>
                        </li>
                        <li>  
                            <h5>PyCharm - ( Ambiente de Desenvolvimento )</h5>
                        </li>
                        <li>  
                            <h5>PythonAnywhere - ( Serviço de Deploy )</h5>
                        </li>
                        <li>  
                            <h5>Django - ( Framework )</h5>
                        </li>
                        <li>  
                            <h5>Django Rest Framework - ( Framework para Desenvolvimento de API )</h5>
                        </li>
                        <li>  
                            <h5>Dependências e versões: </h5>
                            <div style="padding-left: 30px;">
                                <table>
                                <thead>
                                    <tr>
                                        <th>Dependência</th>
                                        <th>Versão</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>
                                            Python
                                        </td>
                                        <td>
                                            3.10.4
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>
                                            Django
                                        </td>
                                        <td>
                                            4.1.7
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>
                                            djangorestframework
                                        </td>
                                        <td>
                                            3.14.0
                                        </td>
                                    </tr>
                                </tbody>
                                </table>
                            </div>
                        </li>
                    </ul>
                </div>
            </li>
            <hr>
            <li>
                <h4 id="replica">4.3. Como Replicar o projeto</h4>
                <div style="padding-left: 30px;">
                    Neste momento iremos ver um passo a passo de como replicar o projeto feito nessa atividade. Irei lhe ensinar minuciosamente cada passo até chegar ao Deploy e testagem. 
                </div>
                <ol style="list-style: none;">
                    <li>
                        <h4>4.3.1. Preparação do ambiente</h4>
                        <div style="padding-left: 30px;">
                            <ul>
                                <li>
                                Tenha o Python instalado em sua máquina. Para isso, basta entrar neste link: <a href="https://www.python.org/downloads/">Download Python</a>.
                                </li>
                                <br>
                                <li>
                                Tenha um Editor de Código instalado em sua máquina. Recomendo tanto o <a href="https://www.jetbrains.com/pycharm/">PyCharm</a>, quanto o <a href="https://code.visualstudio.com/">VsCode</a>. Para esse tutorial, recomendamos o PyCharm, por ter sido o usado para o desenvolvimento dessa API. 
                                </li>
                                <br>
                                <li>
                                    <h5>Criação do Projeto</h5>
                                    <div style="padding-left: 30px;">
                                        Primeiramente você precisa entender o que é <b>ambiente virtual</b>. O ambiente virtual é nada mais do que uma forma de encapsular o que tudo o que o seu projeto terá: Dependências, Bibliotecas, etc. Ele permite que você isole todas as necessidades do projeto X e que ao criar um projeto Y, você não tenha as necessidades do X já instaladas, afinal, pode ser que você não precise de nenhuma. 
                                        <br><br>
                                        Para criar um projeto, basta ir no canto superior direito da sua IDE, clicar em <b>File</b>, e procurar por algo parecido com <b>New Project</b>, siga as instruções. 
                                        <br><br>
                                        Eu vou criar o meu projeto com o nome de <i>api_rest_django</i>. Para alterar o nome, mude o último nome na localização do seu projeto, veja: 
                                        <img src="https://img001.prntscr.com/file/img001/fVA65jZzSKCkxLDsh1wI2w.png">
                                        <img src="https://img001.prntscr.com/file/img001/hREm_EQERRKYT80QLS6T7A.png">
                                        <br><br>
                                        O PyCharm na aba de criação, já permite que você crie um ambiente virtual na criação do projeto, veja: 
                                        <img src="https://img001.prntscr.com/file/img001/wMi2CP6tQtS3iQv4j7AHVw.png">
                                        <br>
                                        Caso você selecione a segunda opção: <i>Previously Cofigured interpreter</i>, você não irá criar um ambiente virtual e terá que fazer isso manualmente via terminal. Iremos explicar a você como executar isso. 
                                        <br><br>
                                        Após criar seu projeto, caso não tenha o Ambiente virtual já definido, abra o terminal e digite os seguintes comandos:<br><br>
                                        <kbd style="background-color: grey; color: white;"> 
                                            python -m venv NOME_DO_AMBIENTE_VIRTUAL
                                        </kbd><br><br>
                                        Lembrando que NOME_DO_AMBIENTE_VIRTUAL é uma variável que você escolhe o nome. <br>
                                        Para ativar o Ambiente virtual, basta digitar: <br><br>
                                        <kbd style="background-color: grey; color: white;"> 
                                            NOME_DO_AMBIENTE_VIRTUAL/Scripts/activate
                                        </kbd><br><br>
                                        Pronto! Para verificar se foi ativo ou não, basta observar a linha de inserção do terminal, á esqueda dela você terá o nome do ambiente virtual entre parênteses. Exemplo:
                                        <br><br>
                                        <kbd style="background-color: grey; color: white;"> 
                                            (NOME_DO_AMBIENTE_VIRTUAL)  PS C:\Users\Franck\Faculdade\api_rest_django> 
                                        </kbd><br><br>
                                        <b>Pronto! Estamos prontos para começar, o nosso ambiente de desenvolvimento está preparado!</b>
                                    </div>
                                </li>
                                <li>
                                    <h5>Instalação das dependências</h5>
                                    <div style="padding-left: 30px;">
                                        Como já dissemos mais acima, as dependências do projeto não são muitas. Como o python já está instalado em sua máquina (Conforme solicitamos), você terá que instalar apenas as outras duas, use essas linhas de código no terminal: <br><br>
                                        <kbd style="background-color: grey; color: white;"> 
                                            pip install Django
                                        </kbd><br>
                                        O <a href="https://www.djangoproject.com/">Django</a> é um framework para desenvolvimento Web utilizando a linguagem python, iremos usar ele pois a estrutura e a forma como ele trabalha torna o nosso trabalho muito fácil. <br><br>
                                        <kbd style="background-color: grey; color: white;"> 
                                            pip install djangorestframework
                                        </kbd><br>
                                        O <a href="https://www.django-rest-framework.org/">Django Rest Framework</a> é outra ferramenta que utilizaremos, ela tem como principal função auxiliar na produção de APIs Rest. 
                                    </div>
                                </li>
                            </ul>
                        </div>
                    </li>
                    <li>
                        <h4>4.3.2. Inicio da Produção</h4>
                        <div style="padding-left: 30px;">
                        <ul>
                        <li>
                        <h5>Criando um projeto</h5>
                                    <div style="padding-left: 30px;">
                                        Com as dependências instaladas, iremos começar a produção. <br><br>
                                        O primeiro comando que daremos ao terminal é:<br><br>
                                        <kbd style="background-color: grey; color: white;"> 
                                            django-admin startproject NOME_DO_PROJETO .
                                        </kbd><br>
                                        Este comando irá criar uma pasta que contem arquivos de configuração do seu site, portanto, escolhemos o nome config para ele. Colocamos um PONTO no final, pois isso faz com que ele não crie uma pasta config dentro de outra pasta config. Veja a estrutura gerada:
                                        <img src="https://img001.prntscr.com/file/img001/sPsbuh_mRBKsG9Tr2fJzbw.png"><br>
                                        <b>Obs: </b><i>script</i> é o nome do nosso ambiente virtual. 
                                        <br><br>
                                        Cada um destes arquivos tem um significado, veja: 
                                        <ul>
                                        <li>
                                        <var>manage.py</var>: Um utilitário de linha de comando que permite que você interaja com isso Projeto Django de várias maneiras. Você pode ler todos os detalhes sobre em django-admin e manage.py.
                                        </li>
                                        <li>
                                        <var>config/__init__.py</var>: Um arquivo vazio que informa ao Python que isso diretório deve ser considerado um pacote Python. Se você é um iniciante em Python,<a href="https://docs.python.org/3/tutorial/modules.html#tut-packages"> leia mais sobre pacotes </a> nos documentos oficiais do Python.
                                        </li>
                                        <li>
                                        <var>config/settings.py</var>: Configurações/configuração para este Django projeto.<a href="https://docs.djangoproject.com/en/4.1/topics/settings/"> As configurações do Django </a> informarão tudo sobre como as configurações trabalho.
                                        </li>
                                        <li>
                                        <var>config/urls.py</var>: As declarações de URL para este projeto Django; um "sumário" do seu site com tecnologia Django. Você pode ler mais sobre URLs no <a href="https://docs.djangoproject.com/en/4.1/topics/http/urls/">dispatcher de URL</a>.
                                        </li>
                                        <li>
                                        <var>config/asgi.py</var>: Um ponto de entrada para servidores Web compatíveis com ASGI para sirva o seu projeto. <a href="https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/">Consulte Como implantar com ASGI</a> para obter mais detalhes.
                                        </li>
                                        <li>
                                        <var>config/wsgi.py</var>: Um ponto de entrada para servidores Web compatíveis com WSGI para sirva o seu projeto. <a href="https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/">Consulte Como implantar com o WSGI</a> para obter mais detalhes.
                                        </li>
                                        </ul>
                                        <br><br>
                                        Para o nosso tutorial, se preocupe apenas com o <var>Manage.py, setting.py e urls.py</var>.
                                    </div>
                        </li>
                        <li>
                            <h5>Criação de um App</h5>
                                <div style="padding-left: 30px;">
                                    Nesse momento o seu projeto ja está rodando localmente. Para verificar isso digite no terminal: 
                                    <br><br>
                                    <kbd style="background-color: grey; color: white;"> 
                                            py manage.py runserver
                                    </kbd><br><br>
                                    E você terá como resposta algo próximo a isso: <br>
                                    <img src="https://img001.prntscr.com/file/img001/e4iSgB7lTGONy6tVjumh0A.png"><br><br>
                                    Ao clicar no link, você irá para a página principal do Django: <br>
                                    <img src="https://img001.prntscr.com/file/img001/Tg0ojiPNRgyR5b9yJkYWjA.png"><br><br>
                                    Agora que você já viu que o seu Projeto está rodando, vamos iniciar a criação do App.<br><br>
                                    Começe digitando no terminal: <br>
                                    <kbd style="background-color: grey; color: white;">py manage.py startapp NOME_DO_APP </kbd><br><br>
                                    Escolhemos o nome biblioteca para o app. Este comando irá gerar os seguintes diretórios e arquivos: <br><br>
                                    <img src="https://img001.prntscr.com/file/img001/l7240RQrQjSR9XonD206pA.png"><br><br>
                                    Não iremos explicar uma por uma nesse momento, você irá entender no decorrer do desenvolvimento. <br><br>
                                    Vamos registrar o App criado no arquivo <var>settings.py</var>.
                                    <br><br>
                                    Adicione as duas últimas linhas da lista INSTALLED_APPS: 
                                    <img src="https://img001.prntscr.com/file/img001/c3u9tgxMR5SRjbwKiJr4Rw.png">
                                    <br>
                                    <var>biblioteca</var> è o nome do App que criamos. <br>
                                    <var>rest_framework</var> é a ferramenta que instalamos no início do desenvolvimento, ela será usada na produção da nossa API e o django pede para você registrar aí caso for usa-la. 
                                </li>
                                <li>
                                <h5>Construindo os Models</h5>
                                    <div style="padding-left: 30px;">
                                    Vamos começar criando os nossos Models. Segue uma explicação sobre eles: Um modelo no Django é um tipo especial de objeto -- ele é salvo em um banco de dados. Um banco de dados é uma coleção de dados. Ele é um local em que você vai salvar dados sobre usuários, suas postagens, etc. Usaremos um banco de dados chamado SQLite para armazenar as nossas informações.<br><br>
                                    Você pode observar que o banco de dados <var>db.sqlite3</var> foi criado quando criamos o app. Você pode altera-lo para algum que prefira, como MySQL ou Postgres. 
                                    <br><br>
                                    <a href="https://docs.djangoproject.com/pt-br/3.0/howto/legacy-databases/">Aprenda a alterar o banco de dados clicando aqui!</a> 
                                    <br><br>
                                    Agora vou facilitar pra você, os models são as tabelas do nosso banco de dados!
                                    <br><br>
                                    Vamos começar!
                                    <pre>
                                        <code>
from django.db import models
<br>
class Language(models.Model):
    """Model representing a Langugage (e.g, English, French, Japanese, etc..."""
    name = models.CharField(max_length=200, help_text="Enter the book's natural language (e.g. English, French, Japanese, etc.")
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name
        <br>
class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('died', null=True, blank=True)
    class Meta:
        ordering = ['last_name', 'first_name']
    def __str__(self):
        """String for representing the Model Object."""
        return f'{self.last_name}, {self.first_name}'
        <br>
class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')
    def __str__(self):
        """String for representing the Model Object"""
        return self.name
<br>
class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)
    # Foreign Key used because book can only have one author, but authors acn have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    # ManyToManyField used because genre can contain many books.
    # Genre class has already been defined, so we can specify the object above
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    <br>
    class Meta:
        ordering = ['title', 'author']
<br>
    def display_genre(self):
        """Creates a string for the Genre. This is required to display genre in Admin"""
        return ', '.join([genre.name for genre in self.genre.all()[:3]])
        <br>
    display_genre.short_description = 'Genre'
<br>
    def __str__(self):
        """String for representing the Model object"""
        return self.title
                                        </code>
                                    </pre>
                                    <br><br>
                                    Estes são os models, os termos usados ai são baseados em conceitos de banco de dados. Veja que os atributos recebem funções como:<br><code> charField, TextField, ForeignKey, DateField
                                    </code>.
                                    <br><br>São auto explicativos, ou seja, representam colunas da tabela com o tipo especificado, Text, Char, Date, etc.
                                    <br><br>
                                    Para aprender mais sobre banco de dados, <a href="https://www.devmedia.com.br/conceitos-fundamentais-de-banco-de-dados/1649">Clique Aqui</a>
                                    </div>  
                                </li>
                        </ul>
                        </div>
                    </li>
                    <li>
                        <h4>4.3.3. Criando os Serializers</h4>
                        <div style="padding-left: 30px;">
                        Serialização é o processo de transformar dados em um formato que pode ser armazenado ou transmitido e, então, reconstruído. Ele é usado em todas as partes do desenvolvimento de aplicações, ou quando estamos armazenando dados numa base de dados, na memória ou convertendo-os em arquivos.
                        <a href="https://labcodes.com.br/blog/pt-br/development/como-usar-serializers-de-django-rest-framework/#:~:text=Django%20vem%20com%20um%20m%C3%B3dulo%20de%20serializers%20que,as%20aplica%C3%A7%C3%B5es%20web%2C%20como%20JSON%2C%20YAML%20e%20XML.">Leia mais...</a>
                        <br><br>
                        Crie uma pasta dentro do seu diretório <code>NOME_DO_APP</code>, que no nosso exemplo é biblioteca, a pasta deve se chamar <code>serializer.py</code>
                        <br><br>
                        Faça o seguinte código:
                        <pre>
                        <code>
from rest_framework import serializers
from biblioteca.models import Book, Author, Genre, Language
<br>
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'summary', 'isbn', 'genre', 'language')
<br>
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
<br>
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
<br>
class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'
                        </code>
                        </pre>
                        <br><br>
                        Veja, começamos importando o módulo <code>serializers</code> disponibilizado pelo nosso <b>Django Rest Framework.</b> Depois disso importe as tabelas que você quer serializar, no nosso caso são todas. 
                        <br><br>
                        Para cada tabela você precisará criar um serializer. Extenda cada classe de <code>serializers.ModelSerializer</code>, defina o model utilizado e os campos que você quer serializar. De resto, o Django faz todo o trabalho!
                        <br><br>
                        Esses códigos irão permitir que transformemos os dados da tabela em um Json, para que retornemos isso ao usuário da nossa API. 
                        </div>
                    </li>
                    <li>
                    <h4>4.3.4. Criando as Views</h4>
                    <div style="padding-left: 30px;">
                    Uma função view, ou view para abreviar, é uma função Python que usa um solicitação da Web e retorna uma resposta da Web. Esta resposta pode ser o conteúdo HTML de uma página da Web, ou um redirecionamento, ou um erro 404, ou um documento XML, ou uma imagem . . . ou qualquer coisa, na verdade. A visão em si contém qualquer lógica arbitrária necessário para devolver essa resposta. Este código pode viver em qualquer lugar que você quiser, desde que como está no seu caminho Python. Não há outro requisito – nenhuma "magia", então para falar. Por uma questão de colocar o código em algum lugar, a convenção é colocar modos de exibição em um arquivo chamado , colocado em seu projeto ou diretório do <b>aplicativo.views.py</b>.
                    <a href="https://docs.djangoproject.com/en/4.1/topics/http/views/">Aprenda mais...</a>
                    <br><br>
                    As nossas views ficarão assim:
                    <pre>
                    <code>
from rest_framework import viewsets
from biblioteca.models import Book, Author, Genre, Language
from biblioteca.serializer import BookSerializer, AuthorSerializer, GenreSerializer, LanguageSerializer
<br>
class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
<br>
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
<br>
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
<br>
class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
                    </code>
                    </pre>
                    <ul>
                    <li>
                    <h5>ViewSets</h5>
                    No Django Rest Framework, <b>Viewsets</b> são classes que agrupam a lógica relacionada à exibição de objetos em uma API.
                    <br><br>
                    Eles fornecem uma maneira rápida e fácil de definir as visualizações CRUD (criar, ler, atualizar e excluir) comuns em uma API RESTful.
                    <br><br>
                    Os Viewsets geralmente funcionam em conjunto com os Routers do DRF, que mapeiam automaticamente as rotas HTTP para as funções CRUD do Viewset.
                    <br><br>
                    Existem vários tipos de Viewsets disponíveis no DRF, cada um oferecendo diferentes níveis de controle sobre o comportamento da API e a serialização dos dados.
                    <br><br>
                    Por exemplo, os ModelViewSet e ReadOnlyModelViewSet são Viewsets que se baseiam em modelos Django, enquanto o ViewSet padrão fornece a maior flexibilidade e controle para criar visualizações personalizadas.
                    <br><br>
                    Em resumo, os Viewsets do DRF são uma abstração útil que ajuda a simplificar a criação de APIs RESTful no Django, fornecendo um conjunto padronizado de funcionalidades para CRUD e mapeando as rotas HTTP automaticamente.</li><br>
                    <li>
                    <h5>query_sets</h5>
                    Já os <b>Querysets</b> são objetos do Django que representam uma consulta ao banco de dados. Eles permitem que você faça consultas complexas ao banco de dados e manipule os resultados. Quando você executa uma consulta no Django, ela retorna um queryset que contém todos os objetos correspondentes aos critérios da consulta.
<br><br>
Os querysets são bastante flexíveis e permitem que você faça operações como filtrar, ordenar e limitar os resultados da consulta. Eles também permitem que você aplique funções agregadas, como contar ou somar os valores de um campo.</li>
                    </ul>
                    <br><br>
                    Depois de entender isso, basta implementar, definimos o query_set e em seguida a classe de serialização, que recebe a classe Serializer que criamos no arquivo <code>Serializer.py</code>.
                    </div>
                    </li>
                    <li>
                    <h4>4.3.4. Indicando as Urls</h4>
                    <div style="padding-left: 30px;">
                    Após todas as views definidas, devemos informar quais serão as urls referentes á elas. Vamos fazer isso no arquivo <code>NOME_DO_PROJETO/urls.py</code>. No nosso caso, <code>config/urls.py</code>.
                    <br><br>
                    <pre>
                    <code>
from django.contrib import admin
from django.urls import path, include
from biblioteca.views import BooksViewSet, AuthorViewSet, GenreViewSet, LanguageViewSet
from rest_framework import routers
<br>
router = routers.DefaultRouter()
router.register(r'books', BooksViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'languages', LanguageViewSet)
<br>
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
                    </code>
                    </pre>
                    <br><br>
                    O mais importante nesse momento é entender o pacote <code>routers</code> que o rest_framework disponibiliza. 
                    <br><br>
                    Como estamos usando classes Viewset em vez de classes View, na verdade não precisamos criar a URL conf nós mesmos. As convenções para conectar recursos em exibições e urls podem ser manipuladas automaticamente, usando uma classe Router. Tudo o que precisamos fazer é registrar os conjuntos de exibição apropriados com um roteador e deixá-lo fazer o resto. <a href="https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/">Aprenda mais sobre routers.</a>
                    <br><br>
                    Já a rota de admin, é disponibilizada pelo próprio Django, para você ter acesso á página de administração do sistema. Para logar nela coloque <code>/admin</code> ao fim da url e digite login e senha do SuperUser. Parar criar o SuperUser digite no terminal: <br>
                    <kbd>py manage.py createsuperuser</kbd>
                    <br>Depois disso siga as instruções. 
                    <br><br>
                    Você verá uma tela próxima á isso: 
                    <img src="https://img001.prntscr.com/file/img001/7R72zmJGQqCi9Z29K2W-lA.png">
                    </div>
                    </li>
                </ol>
            </li>
            <br>
            <li>
            <h4 id="util">4.4. Como utilizar a API</h4>
            <div style="padding-left: 30px;">
                Para demonstrar o uso desta API irei utilizar o software PostMan, através dele você poderá observar como efetuar as solicitações GET, POST, DELETE e PUT (Atualizar). Vamos á Explicação:
                <br><br>
                Ah! Para utiliza-la não é necessário nenhum registro, apenas utilize as urls com alguma biblioteca específica de requisições HTTP da sua linguagem preferida, e já irá funcionar. Como você sabe, ela está retornando JSONs. 
                <br><br>
                <h5>4.4.1. GET</h5>
                <div style="padding-left: 30px;">
                Existem os <b>EndPoints</b>, eles nada mais são do que a url em que se encontra a nossa tabela, ao qual, definimos no pacote <code>urls.py</code>. Essa url permite que as solicitações sejam efetuadas. Existe implicitamente o EndPoint específico para cada dado inserido na tabela, que é referenciado através do ID do dado. Veja:
                <br>
                <img src="https://img001.prntscr.com/file/img001/O5a48lCeRBOdM4XkuqnpsQ.png">
                <br><br>
                <ul>
                <li>Colocamos o Endpoint, que é a url marcada circulada.</li>
                <li>Colocamos o verbo GET.</li>
                <li>Clique em SEND.</li>
                <li>A resposta foi 200, ou seja, tudo certo!</li>
                <li>O valor retornado é uma lista vazia, já que não temos livros cadastrados.</li>
                </ul>
                </div>
                <br><br>
                <h5>4.4.2. POST</h5>
                <div style="padding-left: 30px;">
                Agora vamos cadastrar Gêneros, Linguagens e autores, para por fim inserir o nosso livro. Para isso iremos utilizar o verbo POST, veja:
                <img src="https://img001.prntscr.com/file/img001/BluI-nsGQIOW5shzcmJPQw.png">
                <br><br>
                <ul>
                <li>Defini o endpoint de gêneros.</li>
                <li>Alterei para o verbo POST.</li>
                <li>Entrei na aba Body.</li>
                <li>Defini o dado (No caso do gênero só tem o parâmetro name).</li>
                <li>Após clicar em SEND, a reposta 201 é dada, deu tudo certo!</li>
                </ul>
                </div>
                <br><br>
                <h5>4.4.3. PUT</h5>
                <div style="padding-left: 30px;">
                Agora vamos atualizar o dado, para isso iremos acessar o endpoint específico de algum gênero. Faça o GET que já ensinamos e descubra o ID no gênero Ficção inserido. Tente fazer este exercício!
                <br><br>
                Após descobrir, insira o endpoint de gêneros seguido de <code>/id_do_genero/</code>. Mude para PUT, entre na aba de Body, mude para JSON e clique em SEND: Neste exemplo, iremos alterar o gênero ficção para aventura. 
                <img src="https://img001.prntscr.com/file/img001/ccVGyYtcQaSAIv0bxcTbGg.png">
                </div>
                <h5>4.4.4. DELETE</h5>
                <div style="padding-left:30px;">
                Agora vamos deletar esse mesmo dado atualizado, para isso, basta mudar o verbo para DELETE, no endpoint referente ao dado que você queira excluir, veja:
                <img src="https://img001.prntscr.com/file/img001/cyIf4PxfQIaDzQc_lklung.png"></img>
                </div>
                <h5>4.4.5. Teste através da própria interface</h5>
                <div style="padding-left: 30px;">
                O django já disponibiliza uma interface para você executar as mesmas ações citadas acima, e como você já entende disso, apenas irei mostrar onde fica: Acesse um endpoint da tabela e desça a tela até o fim, veja: 
                <img src="https://img001.prntscr.com/file/img001/SeuI9fBDSIOa3YwoFtlcZQ.png">
                <img src="https://img001.prntscr.com/file/img001/lWx0B7mIRZmUpQ-8jfSUoQ.png">
                </div>
            </div>
            </li>
            <li>
            <h4 id="deploy">4.5. Deploy de uma API</h4>
            <div style="padding-left: 30px;">
            Para efetuar o deploy na plataforma PythonAnywhere eu segui os tutoriais do site <a href="https://img001.prntscr.com/file/img001/lWx0B7mIRZmUpQ-8jfSUoQ.png">Acervo Lima</a>. Ele ensina de forma detalhada como executar o Deploy, siga o passo-a-passo e dará tudo certo!
            </div>
            </li>
            <li>
            <h4 id="endpoints">4.6. Endpoints Disponíveis</h4>
            <div style="padding-left:30px;">
            Para cada tabela criada nós temos dois Endpoints possíveis, genéricamente falando, já que para cada dado criado surge um Endpoint novo. Vamos lá, para cada model NOME_DO_MODEL criado nós teremos os endpoints: <code>https://URL_BASE/NOME_DO_MODEL/</code> e <code>https://URL_BASE/NOME_DO_MODEL/ID_DO_DADO/</code>.
            <br><br>
            Em nosso projeto temos quatro tabelas, logo teremos os seguintes endpoints: 
            <ul>
            <li>Books: <ul><li>"http://franckallyson.pythonanywhere.com/books/"</li><li>"http://franckallyson.pythonanywhere.com/books/id_do_livro/"</li></ul>
            </li>
            <li>Authors: <ul><li>"http://franckallyson.pythonanywhere.com/authors/"</li><li>"http://franckallyson.pythonanywhere.com/authors/id_do_autor/"</li></ul></li>
            <li>Genres: <ul><li>"http://franckallyson.pythonanywhere.com/genres/"</li><li>"http://franckallyson.pythonanywhere.com/genres/id_do_genero/"</li></ul></li>
            <li>Languages: <ul><li>"http://franckallyson.pythonanywhere.com/languages/"</li><li>"http://franckallyson.pythonanywhere.com/languages/id_do_idioma"</li></ul></li>
            </ul>
            <br><br>
            Agora vou exemplificar o uso de cada uma através da própria interface disponibilizada, mas você pode fazer pelo PostMan. 
            <ul>
            <li>Books: <ul><li>Usando no endpoint /Books/ GET E POST<img src="https://img001.prntscr.com/file/img001/SU7ayAP8Q6SaTXBtv-2CQA.png"><img src="https://img001.prntscr.com/file/img001/FUNLKkbBQ86bnibwCTUOIQ.png"></li><br><li>Usando no endpoint /Books/Id/ PUT<img src="https://img001.prntscr.com/file/img001/27_sSDwIT5asubTH97TA1w.png"><img src="https://img001.prntscr.com/file/img001/265CwI7aSuOqNrABWsZcUQ.png"></li></ul>
            </li>
            <li>Authors: <ul><li>Usando no Endpoint /authors/ GET E POST<img src="https://img001.prntscr.com/file/img001/pJ6f_w37Sxiv0VK0TFIQ9Q.png"><img src="https://img001.prntscr.com/file/img001/LghwlD0VS9iMGs1glXYFoQ.png"><img src="https://img001.prntscr.com/file/img001/SFAy8g4FT7e0XEIp1ikcXg.png"></li><li>Usando o endpoint /authors/id_do_autor/ PUT E DELETE<img src="https://img001.prntscr.com/file/img001/z0SFqEGIQV-VfgYDq85j9w.png"><img src="https://img001.prntscr.com/file/img001/QS_W7ERzSkuAAsckyN1hVQ.png"></li></ul></li>
            <li>Genres: <ul><li>Endpoint /genres/ GET E POST<img src="https://img001.prntscr.com/file/img001/OH5ItKIdQNO_6_fZf8YTDw.png"><img src="https://img001.prntscr.com/file/img001/miGOAl0kTUCOq4ZPFqlp4w.png"></li><li>/genres/id_do_genero/ PUT E DELETE<img src="https://img001.prntscr.com/file/img001/6XKDpV6ESd6_QoB3pLSa3A.png"><img src="https://img001.prntscr.com/file/img001/6P7BTp-wQeuH4Wdj3yXxJw.png"><img src="https://img001.prntscr.com/file/img001/5NjaK42WQMyhPYCB-RYcDA.png"></li></ul></li>
            <li>Languages: <ul><li>Endpoint /languages/ GET E POST:<img src="https://img001.prntscr.com/file/img001/f2zdNhEQQj69g3vlV9_lvw.png"><img src="https://img001.prntscr.com/file/img001/dq4biX9FTbmsFreGETKGjQ.png"></li><li>Endpoint /languages/id_da_linguagem/ PUT E DELETE<img src="https://img001.prntscr.com/file/img001/JLQP6YYRS2yJ-YorhrXiUA.png"><img src="https://img001.prntscr.com/file/img001/RkJTwtmFS2O41hbM2u7a3Q.png"><img src="https://img001.prntscr.com/file/img001/lDqCsx_STkSOGUjnyqOV9w.png"></li></ul></li>
            </ul>
            </div>
            </li>
        </ul>
    </li>
    <li>
    <h3 id="credits">5. Créditos</h3>
    <div style="padding-left: 30px;">
    <ul>
    <li><a href="https://www.django-rest-framework.org/">Django Rest Framework</a></li>
    <li><a href="https://www.djangoproject.com/">Django</a></li>
    <li><a href="https://www.youtube.com/watch?v=BKChTO8GADk&feature=youtu.be&ab_channel=Alura">Video ensinando criar uma API</a></li>
    <li><a href="https://acervolima.com/como-implantar-o-projeto-django-no-pythonanywhere/#:~:text=python3%20-m%20venv%20env%20%23%20criar%20ambiente%20virtual,instalou%20no%20bash%20Digite%20o%20comando%20no%20bash">Artigo ensinando fazer o deploy</a>/</li>
    </ul>
    </div>
    </li>
    <li>
    <h3 id="licenca">6. Licença</h3>
    <div style="padding-left: 30px;">GNU 3.0</div>
    </li>
    <hr>
</ul>
