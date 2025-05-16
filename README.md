# FIAP-Desenvolvimento-API-FastAPI

## Introdução ao FastAPI

O **FastAPI** é um framework moderno e rápido para a construção de APIs com Python 3.7+ baseado em padrões como Python type hints, Starlette e Pydantic. Ele foi projetado para ser fácil de usar, altamente performático e com foco em produtividade e robustez.

## Vantagens do FastAPI

- **Alta performance:** Utiliza o ASGI e é comparável em velocidade a frameworks como NodeJS e Go.
- **Tipagem forte:** Aproveita type hints do Python para validação automática de dados e geração de documentação interativa.
- **Documentação automática:** Gera documentação interativa (Swagger/OpenAPI) automaticamente.
- **Fácil de usar:** Sintaxe simples e intuitiva, facilitando o desenvolvimento rápido.
- **Validação de dados:** Integração com Pydantic para validação e serialização de dados.
- **Suporte a async:** Permite o uso de funções assíncronas para melhor performance em operações I/O.

## Desvantagens do FastAPI

- **Curva de aprendizado:** Pode ser mais complexo para iniciantes devido ao uso intensivo de tipagem e conceitos modernos do Python.
- **Ecossistema menor:** Ainda possui uma comunidade e quantidade de extensões menor que frameworks mais antigos como Flask ou Django.
- **Novidade:** Por ser relativamente novo, pode haver menos exemplos e materiais de suporte para casos muito específicos.

## Comparativo breve: FastAPI vs Flask vs Django

| Característica           | FastAPI                        | Flask                                         | Django                      |
|--------------------------|-------------------------------|-----------------------------------------------|-----------------------------|
| Performance              | Muito alta (ASGI, async)       | Boa (WSGI, sync)                              | Boa (WSGI, sync)            |
| Tipagem                  | Suporte nativo (type hints)    | Não possui                                    | Limitado                    |
| Documentação automática  | Sim (Swagger/OpenAPI)          | Não nativo                                    | Não nativo                  |
| Validação de dados       | Pydantic integrado             | Manual ou via extensões                       | Forms/ModelForms integrados |
| Facilidade de uso        | Sintaxe moderna, intuitiva     | Muito simples e direta                        | Estrutura robusta e completa|
| Comunidade               | Crescente                      | Muito consolidada                             | Muito consolidada           |
| Suporte a async          | Sim                            | Limitado                                      | Parcial (desde 3.1)         |
| ORM integrado            | Não                            | Não                                           | Sim                         |
| Admin automático         | Não                            | Não                                           | Sim                         |
| Servidor de desenvolvimento | Necessário ASGI externo (ex: Uvicorn, Hypercorn, Daphne) | Integrado (basta `python app.py`)           | Integrado (manage.py runserver) |
| Servidor para produção   | ASGI obrigatório (ex: Uvicorn, Hypercorn, Daphne) | WSGI obrigatório (ex: Gunicorn, uWSGI) (WSGI = Web Server Gateway Interface) | WSGI obrigatório (ex: Gunicorn, uWSGI) (WSGI = Web Server Gateway Interface) |

- **FastAPI** é recomendado para projetos que exigem alta performance, validação robusta de dados e documentação automática.
- **Flask** é indicado para projetos simples ou para quem busca um framework minimalista e com grande quantidade de recursos da comunidade.
- **Django** é ideal para aplicações completas, que necessitam de ORM, painel administrativo e uma estrutura robusta pronta para uso.

## O que é e para que serve o Uvicorn?

O **Uvicorn** é um servidor ASGI (Asynchronous Server Gateway Interface) leve e de alta performance, utilizado para executar aplicações Python modernas que suportam operações assíncronas, como o FastAPI. Ele é responsável por receber as requisições HTTP, encaminhá-las para a aplicação e retornar as respostas ao cliente.

> **Importante:** Para rodar aplicações FastAPI é obrigatório utilizar um servidor compatível com ASGI, como Uvicorn, Hypercorn ou Daphne. Não é possível executar FastAPI diretamente apenas com o Python padrão.

Já para aplicações Flask e Django em produção, é obrigatório o uso de um servidor WSGI (Web Server Gateway Interface), como Gunicorn ou uWSGI.

### Principais características do Uvicorn:
- **Performance elevada:** Projetado para lidar com grande volume de requisições de forma eficiente.
- **Suporte a async:** Permite o uso de recursos assíncronos do Python, melhorando a escalabilidade da aplicação.
- **Compatibilidade:** Pode ser utilizado com frameworks modernos como FastAPI, Starlette e Django (com ASGI).

### Quando usar o Uvicorn?
Sempre que você desenvolver uma API com FastAPI (ou outro framework ASGI), o Uvicorn é recomendado como servidor para rodar sua aplicação em ambiente de desenvolvimento ou produção.

**Exemplo de execução:**
```bash
uvicorn main:app --reload
```
No exemplo acima, `main` é o nome do arquivo Python (sem extensão) e `app` é o nome da instância FastAPI.

## Documentação automática no FastAPI

Uma das grandes vantagens do FastAPI é a geração automática de documentação interativa para a sua API, baseada nos padrões OpenAPI e JSON Schema. Assim que você define suas rotas e modelos de dados, o FastAPI cria duas interfaces de documentação acessíveis via navegador:

- **Swagger UI:** Disponível por padrão em `/docs`. É uma interface gráfica interativa onde você pode visualizar, testar e explorar todos os endpoints da sua API de forma prática e intuitiva.
- **ReDoc:** Disponível em `/redoc`. Oferece uma documentação mais detalhada e organizada, ideal para leitura e entendimento da estrutura da API.

Essas documentações são geradas automaticamente a partir do código, aproveitando os type hints do Python e as validações do Pydantic, facilitando o desenvolvimento, testes e integração com outros sistemas.