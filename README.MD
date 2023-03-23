<div align="center" id="cabecalho">
    <h1>API Rest com BD</h1>
    <h3>Franck Allyson da Silva Rocha </h3>
    <h4>4º Período | BSI | IFNMG Campus Salinas</h4>
</div>

<hr>

<ul style="list-style: none;">
    <li>
        <h3>1. Linguagem e Framework Escolhido</h3>
        <div style="padding-left: 30px;">
            Para este exercício, foi escolhido a linguagem Python e o Framework <a href="https://www.djangoproject.com/">Django</a>.<br> O Django disponibiliza a utilização de outro framework, o <i>Django Rest Framework</i>, e com isso a implementação fica <b>extremamente</b> fácil! Vamos continuar!
        </div>
    </li>
    <hr>
    <li>
        <h3>2. Banco de Dados Escolhido</h3>
        <div style="padding-left: 30px;">
            O banco de dados escolhido foi o que o próprio django disponibiliza na criação: <b>SQLite</b>. <br>
            Como não vamos manipular grandes quantidades de dados, ele se torna o ideal. Além de ser o mais indicado para pequenos testes.
        </div>
    </li>
    <hr>
    <li>
        <h3>3. DBaaS escolhido</h3>
        <div style="padding-left: 30px;">
            Não se fez necessário a escolha de um DBaaS específico. Apenas vamos utilizar um ambiente de desenvolvimento integrado (IDE) e serviço de hospedagem web baseado na linguagem de programação Python, o nome dele é <a href="https://www.bing.com/ck/a?!&&p=3ab8966ee8547ad5JmltdHM9MTY3OTQ0MzIwMCZpZ3VpZD0zYjAzYzMwNC01MzA3LTYxNTctMzEzYi1kMTYxNTI5MTYwM2YmaW5zaWQ9NTE5OA&ptn=3&hsh=3&fclid=3b03c304-5307-6157-313b-d1615291603f&psq=python+anywhere+%c3%a9+um+dbaas%3f&u=a1aHR0cHM6Ly93d3cucHl0aG9uYW55d2hlcmUuY29tLw&ntb=1">PythonAnywhere</a>. <br>
            Ele já faz todo o serviço de disponibilizar o banco de dados e a API que criamos, possibilitando que as requisições aconteçam.
        </div>
    </li>
    <hr>
    <li>
        <h3>4. Documentação do Projeto</h3>
        <ul style="list-style:none;">
            <li>
                <h4>4.1. Descrição e Objetivos</h4>
                <div style="padding-left: 30px;">
                    Este projeto é uma API de Biblioteca, disponibilizamos Autores, Gêneros, Idiomas e Livros. Os três primeiros estão associados aos Livros por meio de relacionamentos do banco de dados, logo, só poderemos criar um Livro se tivermos autores, gêneros e idiomas já inseridos na API. No mais, padrão, as requisições entregam dados em JSON. <br>
                    O principal Objetivo com a execução desse projeto é aprender conceitos de API, Backend e também do próprio Django. Eu particularmente pretendo trabalhar  focado na parte do back-end então pra mim é de grande valia. 
                </div>
            </li>
            <hr>
            <li>
                <h4>4.2. Tecnologias e Ferramentas Utilizadas</h4>
                <div style="padding-left: 30px;">
                    <ul>
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
                <h4>4.3. Como Replicar o projeto</h4>
                <div style="padding-left: 30px;">
                    Neste momento iremos ver um passo a passo de como replicar o projeto feito nessa atividade. Irei lhe ensinar minuciosamente cada passo até chegar ao Deploy e testagem. 
                </div>
                <ol style="list-style: none;">
                    <li>
                        <h5>4.3.1. Preparação do ambiente</h5>
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
                                    <h6>Criação do Projeto</h6>
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
                                    <h6>Instalação das dependências</h6>
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
                                <li>
                                    <h6>Inicio da produção</h6>
                                    <div style="padding-left: 30px;">
                                        Com as dependências instaladas, iremos começar a produção. <br><br>
                                        O primeiro comando que daremos ao terminal é:<br><br>
                                        <kbd style="background-color: grey; color: white;"> 
                                            django-admin startproject NOME_DO_PROJETO
                                        </kbd><br>
                                        Este comando irá criar uma pasta que contem arquivos de configuração do seu site, portanto, escolhemos o nome config para ele. Veja a estrutura gerada:
                                        <img src="https://img001.prntscr.com/file/img001/FDEpFSM6ReqMUF9o2sn1KQ.png"><br>
                                        <b>Obs: </b><i>script</i> é o nome do nosso ambiente virtual. 
                                    </div>
                                </li>
                            </ul>
                        </div>
                    </li>
                </ol>
            </li>
        </ul>
    </li>
    <hr>
</ul>
