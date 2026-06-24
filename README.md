# Automação de Testes para Chatbot

## Objetivo

Automatizar o envio de perguntas para o chatbot via WhatsApp, eliminando a necessidade de copiar e colar manualmente cada mensagem durante os testes.

## Benefícios

* Redução do tempo gasto nos testes.
* Padronização da execução dos cenários.
* Facilidade para reproduzir testes.
* Permite que o analista foque apenas na validação das respostas.
* Configuração simples e rápida.
* Possibilita a execução de grandes volumes de testes com menor esforço operacional.

## Como funciona

1. Divida a tela do Windows.
2. Deixe o WhatsApp aberto em um lado.
3. Deixe o VS Code aberto no outro lado.
4. Configure a coordenada do campo de mensagem.
5. Execute o script.
6. O sistema enviará automaticamente todas as perguntas cadastradas.

## Configuração da Coordenada

Utilize o script abaixo para identificar a posição do mouse:

```python
import pyautogui
import time

time.sleep(2)
print(pyautogui.position())
```

Posicione o cursor sobre o campo de mensagem do WhatsApp e execute o script.

## Funcionalidades

* Envio automático de perguntas.
* Controle do intervalo entre mensagens.
* Lista de cenários totalmente editável.
* Interrupção manual via CTRL+C.
* Fácil adaptação para outros robôs e municípios.
* Configuração simples das coordenadas de clique.
* Possibilidade de testar diferentes fluxos e serviços do chatbot.

## Tecnologias Utilizadas

* Python
* PyAutoGUI
* Pyperclip

## Personalização dos Cenários de Teste

As perguntas utilizadas pela automação ficam armazenadas dentro da variável `perguntas_lista`.

Para adicionar novos cenários de teste, basta solicitar a uma Inteligência Artificial que gere as perguntas no seguinte formato:

```python
"Pergunta 1",
"Pergunta 2",
"Pergunta 3",
"Pergunta 4",
```

Ou seja, cada pergunta deve estar entre aspas e separada por vírgula, permitindo copiar e colar diretamente dentro da lista já existente no script.

Isso facilita a criação de novos testes sem necessidade de ajustes adicionais no código.

## Exemplo

```python
"Como faço para consultar meu IPTU?",
"Quais serviços estão disponíveis para cidadãos?",
"Como abrir um protocolo na prefeitura?",
"Como falar com um atendente humano?",
```

Basta copiar e colar os itens dentro da lista de perguntas.

## Observações

O intervalo entre mensagens pode ser ajustado conforme a necessidade do teste.

Atualmente o script utiliza 35 segundos entre cada envio para permitir a análise completa da resposta antes da próxima interação.

A ferramenta foi desenvolvida para agilizar a execução dos testes, eliminando tarefas repetitivas como copiar, colar e enviar perguntas manualmente, permitindo que o analista concentre seu tempo na validação das respostas e identificação de possíveis falhas do sistema.
