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
            Para este exercício, foi escolhido a linguagem Python e o Framework Django.<br> O Django disponibiliza a utilização de outro framework, o <i>Django Rest Framework</i>, e com isso a implementação fica <b>extremamente</b> fácil! Vamos continuar!
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
            </li>
        </ul>
    </li>
    <hr>
</ul>
