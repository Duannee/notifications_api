# Notification API
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/Duannee/notifications_api/blob/main/LICENSE)

Bem-vindo à API de Notificações! Esta API foi projetada para gerenciar notificações de diferentes tipos, utilizando conexões WebSocket para notificações em tempo real e requisições HTTP para notificações relacionadas a eventos e cursos. Com arquitetura modular e uma abordagem bem testada, ela garante desempenho e organização.

## **Index**

1. [Visão Geral](#visão-geral)  
2. [Tipos de Notificações](#tipos-de-notificações)  
   - [Interações com Conteúdo (WebSocket)](#interações-com-conteúdo-websocket)  
   - [Cursos (HTTP com Signals)](#cursos-http-com-signals)  
   - [Eventos (HTTP com Signals)](#eventos-http-com-signals)  
3. [Tecnologias Utilizadas](#tecnologias-utilizadas)  
4. [Autenticação](#autenticação)  
5. [Rotas Disponíveis](#rotas-disponíveis)  
   - [Tags das Rotas](#tags-das-rotas)  
   - [Rotas de Cursos e Eventos](#rotas-de-cursos-e-eventos)  
   - [Rotas de WebSocket](#rotas-de-websocket)  
6. [Testes](#testes)  
7. [Documentação](#documentação)  
8. [Como Contribuir](#como-contribuir)  
9. [Contato](#contato)


## Visão Geral

A API gerencia notificações em tempo real para interações com conteúdo, além de notificações relacionadas a cursos e eventos. Utilizamos WebSocket para mensagens instantâneas e HTTP para notificações baseadas em mudanças estruturais, como atualizações de cursos ou eventos.

### Benefícios:
- Notificações em tempo real: Melhor experiência para o usuário com atualizações imediatas.
- Arquitetura desacoplada: Signals organizam as notificações relacionadas a cursos e eventos.
- Segurança: Autenticação com JSON Web Token (JWT).
- Performance: Banco de dados em Redis para maior eficiência no armazenamento de dados temporários.

  

## Tipos de Notificações

### Interações com Conteúdo (WebSocket)
As seguintes notificações são enviadas em tempo real via WebSocket:

1. **Novo comentário em um post**
  - Quando um usuário comenta em um post, os envolvidos recebem notificações instantaneamente.

2. **Novo like em um post**
  - Notifica o autor do post quando ele recebe um novo like.

3. **Resposta a um comentário**
  - Notifica o autor do comentário original.

4. **Novo like em um comentário**
  - Notifica o autor do comentário quando ele recebe um like.

### Cursos (HTTP com Signals)
As notificações relacionadas a cursos são tratadas via HTTP, com o auxílio de Signals para desacoplar a lógica de negócio da API. As notificações incluem:

5. **Novo curso disponível**
  - Quando um novo curso é criado, os usuários interessados são notificados.

6. **Atualização de curso**
  - Notifica os usuários inscritos quando há mudanças no curso, como novos módulos ou aulas.

### Eventos (HTTP com Signals) 
De forma semelhante às notificações de cursos, as notificações de eventos utilizam Signals. As notificações incluem:

7. **Novo evento criado**
  - Notifica os usuários interessados sobre a criação de um evento.

8. **Atualização de evento**
  - Notifica os inscritos quando um evento sofre alterações, como mudança de data ou local.



## Tecnologias Utilizadas
- Linguagem: Python.
- Frameworks: Django, Django Rest Framework (DRF).
- WebSocket: Django Channels.
- Autenticação: JWT via Simple JWT.
- Banco de Dados: Redis.
- Documentação: Swagger com DRF Spectacular.

# Autenticação
A API utiliza JWT (JSON Web Token) para autenticação.

### Como funciona:
1. Faça login via /api/token/ para obter:
- Access Token: Válido por 30 minutos.
- Refresh Token: Válido por 7 dias.
2. Use o Access Token no cabeçalho das requisições:
  ```makefile
  Authorization Bearer <your token>
  ```

# Rotas Disponíveis 
### Tags das Rotas 
As rotas estão organizadas por tags para facilitar a navegação:

- Token: Operações relacionadas à autenticação.
- WebSocket: Explicação de como conectar via WebSocket.
- Course: Gerenciamento e notificações de cursos (HTTP).
- Event: Gerenciamento e notificações de eventos (HTTP).

### Rotas de Cursos e Eventos 
Ambos os recursos (cursos e eventos) possuem três rotas principais:

1. PATCH: Atualizar parcialmente um curso/evento.
2. PUT: Atualizar completamente um curso/evento.
3. POST: Criar um novo curso/evento.

### Rotas de WebSocket
- GET /api/ws/notification
  Explica como utilizar as notificações em tempo real via WebSocket.
Para conectar-se ao WebSocket
1. User o endpoint:
   ```perl
   ws://localhost:8000/ws/notifications/
   ```
2. Envie o token JWT no cabeçalho da conexão

# Testes
- A API foi totalmente testada com testes unitários e testes de integração, utilizando:
 - Unittest: Para validar funcionalidades individuais.
 - TestCase: Para simular cenários completos.

# Documentação
A documentação completa da API foi criada com Swagger, utilizando o DRF Spectacular. Ela detalha todos os endpoints, exemplos de uso e resposta esperada.
Acesse a documentação através do link:
[Notification API Doc](http://127.0.0.1:8000/api/notification/docs/)

# Como contribuir
1. Faça o fork do repositório
2. Crie uma branch para suas alterações:
```bash
git checkout -b you-branch-name
```
3. Envie um pull request detalhando suas contribuições

# Contato
- Desenvolvedor: **Duanne Moraes**
- E-mail: duannemoraes.dev@gmail.com
- Linkedin: [Duanne Moraes Linkedin](https://www.linkedin.com/in/duanne-moraes-7a0376278/)









