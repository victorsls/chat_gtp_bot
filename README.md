# Chat Bot com OpenAI
Este é um projeto de um chat bot implementado em Python, utilizando a biblioteca OpenAI para gerar respostas contextualizadas. O chat bot possui respostas automáticas para perguntas e palavras-chave específicas e, quando necessário, recorre ao modelo de linguagem da OpenAI para fornecer respostas mais elaboradas.

**Funcionalidades\:**
- Respostas automáticas para perguntas e palavras-chave comuns.
- Utilização da API do OpenAI para respostas mais elaboradas e contextualizadas.
- Interface de linha de comando para interação fácil com o chat bot.

## Executando o Projeto

1. Certifique-se de ter o Docker instalado em sua máquina.
2. No terminal, navegue até o diretório raiz do projeto.
3. Renomeie o arquivo `.env.example` para `.env`.
4. Abra o arquivo `.env` e adicione sua chave de API da OpenAI na variável `OPENAI_API_KEY`.
5. Execute o seguinte comando para construir a imagem Docker e iniciar a aplicação:

   ```shell
   docker compose run app
   ```

6. A aplicação será iniciada e você verá as mensagens de boas-vindas no terminal.
7. Digite as mensagens de entrada e a aplicação responderá de acordo.
8. Para encerrar a aplicação, pressione `Ctrl + C` no terminal ou digite sair.

## Executando os Testes

1. Certifique-se de ter o Docker instalado em sua máquina.
2. No terminal, navegue até o diretório raiz do projeto.
3. Execute o seguinte comando para executar os testes:

   ```shell
   docker compose run tests
   ```

4. Os testes serão executados e você verá a saída dos resultados no terminal.

Lembre-se de ter o Docker e o Docker Compose corretamente instalados em sua máquina para poder executar os comandos.

**Nota:** Antes de executar o projeto, é necessário adicionar sua chave de API da OpenAI no arquivo `.env` na variável `OPENAI_API_KEY`. Certifique-se de fornecer uma chave válida para garantir o funcionamento correto da aplicação. Se a versão do seu docker compose for a mais antiga, utilize o comando *docker-compose* ao invés de *docker compose*. 

## Arquitetura e Design do Chat Bot
A arquitetura do chat bot consiste em duas principais classes: `ChatGPT` e `ChatBot`. A classe `ChatGPT` interage com o modelo OpenAI ChatGPT para gerar respostas com base no contexto da conversa. A classe `ChatBot` processa as mensagens dos usuários, utiliza correspondência de padrões para respostas automáticas e integra as respostas geradas pelo `ChatGPT` para fornecer respostas mais elaboradas e contextuais.

### Classe ChatGPT
- Interage com o modelo OpenAI ChatGPT através da API para gerar respostas.
- Utiliza o contexto da conversa para manter o contexto entre as interações.
- Implementa o método `get_response()` para enviar as mensagens do usuário para o modelo ChatGPT e obter a resposta gerada.

### Classe ChatBot
- Processa as mensagens dos usuários e verifica se há correspondência com padrões predefinidos para respostas automáticas.
- Utiliza a instância `ChatGPT` para gerar respostas mais elaboradas usando o modelo ChatGPT.
- Implementa o método `process_message()` para lidar com as mensagens do usuário e determinar a resposta apropriada.
- Controla a interação com o usuário por meio do método `run_chat_bot()`.

### Decisões de Design
- Abordagem baseada em classes: A utilização de classes fornece uma base de código estruturada e modular, facilitando a manutenção e a escalabilidade.
- Separação de responsabilidades: A separação de responsabilidades entre as classes `ChatGPT` e `ChatBot` garante clareza e modularidade.
- Integração com o ChatGPT: A integração com o modelo ChatGPT possibilita respostas mais sofisticadas e contextuais, melhorando a experiência do usuário.
- Correspondência de padrões: A utilização da correspondência de padrões com a classe `Chat` do NLTK permite respostas automáticas a perguntas específicas ou palavras-chave, aumentando a eficiência.
- Controle do contexto da conversa: O controle do contexto da conversa na classe `ChatGPT` garante respostas relevantes e coerentes, atualizando e mantendo o contexto a cada mensagem do usuário.

Essas decisões de design contribuem para a efetividade do chat bot, fornecendo respostas automáticas, respostas elaboradas e contextuais com o modelo ChatGPT e mantendo o contexto da conversa para interações coerentes. O design modular facilita a manutenção, a escalabilidade e a adição de novos recursos no futuro.