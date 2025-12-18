

## 📚 Descrição do Projeto
O **Educa_Quiz-POO** é um sistema de quiz educacional desenvolvido com base nos princípios da **Programação Orientada a Objetos (POO)** em **Python**.  
O sistema permite a criação de quizzes compostos por perguntas, além do registro de usuários e do histórico de tentativas realizadas.

---

## 🧩 1. PRINCIPAIS CLASSES DO SISTEMA

### 🔹 Pergunta (classe base)
Classe base que representa uma pergunta do quiz.  
Define os atributos e comportamentos comuns a todos os tipos de perguntas.

**Responsabilidades:**
- Armazenar o enunciado da pergunta  
- Armazenar a resposta correta  
- Verificar se a resposta do usuário está correta  

---

### 🔹 Quiz
Classe responsável por representar um quiz completo.

**Relacionamento:**
- Agrega várias instâncias da classe `Pergunta`

**Responsabilidades:**
- Gerenciar a lista de perguntas  
- Controlar o fluxo do quiz  
- Calcular a pontuação final  

---

### 🔹 Usuario
Classe que representa o usuário do sistema.

**Responsabilidades:**
- Armazenar informações do usuário  
- Iniciar quizzes  
- Consultar o histórico de tentativas  

---

### 🔹 Tentativa
Classe responsável por registrar uma tentativa de um usuário em um quiz.

**Relacionamentos:**
- Associada a um `Usuario`  
- Associada a um `Quiz`

**Responsabilidades:**
- Registrar data e hora da tentativa  
- Armazenar respostas fornecidas  
- Registrar a pontuação obtida  

---

## 🔗 Relação entre as Classes
- Um `Quiz` contém várias `Pergunta`  
- Um `Usuario` pode realizar várias `Tentativa`  
- Cada `Tentativa` está associada a um único `Usuario` e a um único `Quiz`

  ------------

  ## 👥 2. DETALHAMENTO DE RESPONSABILIDADES TÉCNICAS

### 👩‍💻 SAMIRA VIEIRA — CTO (Chief Technology Officer)
**Foco:** Arquitetura do sistema, configuração global e regras de negócio.  
**Responsabilidade principal:** Garantir que o sistema respeite as configurações globais e orquestrar o fluxo do jogo (lógica de controle).

#### 🔧 Tarefa 1 — Configuração do Sistema
Criar e gerenciar o arquivo `settings.json`, responsável por armazenar configurações globais do sistema, incluindo:
- Duração padrão do quiz
- Número máximo de tentativas permitidas por usuário
- Pesos associados a cada nível de dificuldade das perguntas

#### 🎮 Tarefa 2 — Game Controller
Implementar a classe `GameController` em `src/controllers/game_controller.py`, responsável por:
- Carregar e validar as configurações do arquivo `settings.json`
- Verificar se o usuário ainda possui tentativas disponíveis
- Calcular a pontuação final do quiz com base nos pesos definidos

#### 🔗 Tarefa 3 — Integração
Definir interfaces ou métodos abstratos que devem ser seguidos pelas implementações das camadas de modelo e persistência, garantindo padronização e integração entre os módulos desenvolvidos pela equipe.

---

### 🗄️ FELIPE EMMANUEL — IT Technician
**Foco:** Infraestrutura de dados e persistência utilizando SQL puro (SQLite).  
**Responsabilidade principal:** Garantir que os dados sejam armazenados e recuperados corretamente, sem uso de ORM.

#### 🧱 Tarefa 1 — Database Setup
Criar o banco de dados SQLite em `data/quiz.db` e definir as tabelas:
- `Perguntas`
- `Usuarios`
- `Tentativas`

#### 📦 Tarefa 2 — Data Access Object (DAO)
Implementar o padrão DAO em `src/dao/repository.py`, contendo funções SQL puras para:
- `save_question(pergunta_obj)` — Inserção de perguntas
- `get_all_questions()` — Consulta de perguntas
- `save_attempt(user_id, score)` — Registro de tentativas e pontuação

**Requisito crítico:**  
Todas as queries devem ser parametrizadas utilizando `?`, evitando SQL Injection.

---

### 🧠 MARCUS VINICIUS — Software Engineer
**Foco:** Modelagem de domínio e Programação Orientada a Objetos (POO).  
**Responsabilidade principal:** Implementar as classes centrais do sistema, garantindo encapsulamento e validações internas.

#### ❓ Tarefa 1 — Classe Pergunta
Implementar `src/models/pergunta.py` com:
- Uso de `@property` para validar:
  - Quantidade de alternativas (mínimo 3 e máximo 5)
  - Índice da resposta correta dentro do intervalo válido
- Implementação de `__eq__` para evitar perguntas duplicadas (enunciado + tema)
- Implementação de `__str__` para representação textual legível

#### 📝 Tarefa 2 — Classe Quiz
Implementar `src/models/quiz.py` com:
- Sobrescrita de `__len__` para retornar a quantidade de perguntas
- Sobrescrita de `__iter__` para permitir iteração sobre as perguntas
- Método para calcular a pontuação máxima do quiz (soma dos pesos das perguntas)

#### 👤 Tarefa 3 — Classe Usuario
Modelar a classe `Usuario`, responsável por:
- Armazenar dados do usuário
- Agregar a lista de tentativas realizadas
- Facilitar o acesso ao histórico de desempenho

---

### 🖥️ THIERRY BARROS — Software Engineer
**Foco:** Interface gráfica e interação com o usuário utilizando Streamlit.  
**Responsabilidade principal:** Transformar dados e classes em telas visuais, sem conter lógica de negócio complexa.

#### 🚪 Tarefa 1 — Entry Point
Configurar o arquivo `app.py` para controlar a navegação entre:
- Área Administrativa
- Área do Aluno  
(utilizando sidebar ou abas do Streamlit)

#### 🛠️ Tarefa 2 — Tela Administrativa
Criar a interface `views/admin_page.py` para cadastro de perguntas, utilizando os métodos DAO para persistência no banco de dados.

#### 🎯 Tarefa 3 — Tela do Quiz
Criar a interface `views/quiz_page.py` que:
- Exiba as perguntas sequencialmente
- Utilize `st.session_state` para controlar o índice da pergunta atual
- Ao final, exiba o gabarito e a nota obtida pelo usuário

---

### 🧪 RAMON FIRMINO — QA (Quality Assurance)
**Foco:** Testes unitários e validação de requisitos.  
**Responsabilidade principal:** Garantir que as regras do sistema sejam cumpridas e identificar falhas.

#### ✅ Tarefa 1 — Testes de Modelos
Criar `tests/test_models.py` utilizando `pytest` para:
- Verificar erro ao criar pergunta com menos de 3 alternativas
- Verificar erro ao definir índice de resposta fora do intervalo válido

#### 📏 Tarefa 2 — Testes de Regras
Criar `tests/test_rules.py` para:
- Simular um usuário excedendo o número máximo de tentativas definido no `settings.json`

#### 🐞 Tarefa 3 — Relatório de Bugs
Documentar falhas encontradas, especialmente na integração entre:
- Camada de persistência (Banco de Dados)
- Camada de interface (Streamlit)

---







