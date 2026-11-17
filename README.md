# VoyageFlow AI

Sistema de triagem para agência de viagens, com evolução planejada para IA generativa.

## Problema
O consultor recebe contatos por WhatsApp sem as informações necessárias para preparar um orçamento.

## Protótipo inicial
- Formulário de triagem com perguntas condicionais
- Registro de solicitações e geração de protocolo
- Painel do consultor e direcionamento ao WhatsApp

**Status:** protótipo local; não validado para produção.

## Evolução: FlowAgent AI
Módulo em desenvolvimento para classificar intenção e prioridade, resumir solicitações e sugerir respostas para revisão humana. Há um protótipo separado com regras e integração opcional com LLM; a integração completa ao VoyageFlow ainda está pendente.

## Tecnologias
Python, FastAPI, SQLite, HTML, CSS, JavaScript.

## Próximos passos
Integração entre módulos, testes de ponta a ponta, autenticação, segurança e LGPD.

Nunca publique chaves de API, arquivos .env reais ou dados de clientes.
