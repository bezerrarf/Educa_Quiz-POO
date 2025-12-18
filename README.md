## 📚 Descrição do Projeto
O **Educa_Quiz-POO** é um sistema de quiz educacional desenvolvido com base nos princípios da **Programação Orientada a Objetos (POO)** em **Python**.  

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
**Responsabilidade principal:** Garantir que o sistema respeite as configurações globais e orquestrar o fluxo do jogo (lógica de controle).

#### 🔧 Tarefa 1 — Configuração do Sistema
Criar e gerenciar o arquivo `settings.json`, responsável por armazenar configurações globais do sistema, incluindo:
- Duração padrão do quiz
- Número máximo de tentativas permitidas por usuário
- Pesos associados a cada nível de dificuldade das perguntas

---

### 🗄️ FELIPE EMMANUEL — IT Technician
**Responsabilidade principal:** Garantir que os dados sejam armazenados e recuperados corretamente, sem uso de ORM.

#### 🧱 Tarefa 1 — Database Setup
Criar o banco de dados SQLite em `data/quiz.db` e definir as tabelas:
- `Perguntas`
- `Usuarios`
- `Tentativas`

---

### 🧠 MARCUS VINICIUS — Software Engineer
**Responsabilidade principal:** Implementar as classes centrais do sistema, garantindo encapsulamento e validações internas.

#### ❓ Tarefa 1 — Classe Pergunta
Implementar `src/models/pergunta.py` com:
- Uso de `@property` para validar:
  - Quantidade de alternativas (mínimo 3 e máximo 5)
  - Índice da resposta correta dentro do intervalo válido

---

### 🖥️ THIERRY BARROS — Software Engineer
**Responsabilidade principal:** Transformar dados e classes em telas visuais, sem conter lógica de negócio complexa.

#### 🚪 Tarefa 1 — Entry Point
Configurar o arquivo `app.py` para controlar a navegação entre:
- Área Administrativa
- Área do Aluno  
(utilizando sidebar ou abas do Streamlit)

---

### 🧪 RAMON FIRMINO — QA (Quality Assurance)
**Responsabilidade principal:** Garantir que as regras do sistema sejam cumpridas e identificar falhas.

#### ✅ Tarefa 1 — Testes de Modelos
Criar `tests/test_models.py` utilizando `pytest` para:
- Verificar erro ao criar pergunta com menos de 3 alternativas
- Verificar erro ao definir índice de resposta fora do intervalo válido

---







