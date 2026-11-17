# VoyageFlow AI — Triagem de viagens

**Status:** protótipo demonstrativo em evolução. O FlowAgent é o módulo de IA planejado para a próxima etapa.

## Executar o código deste repositório
Requer Python 3.10+ e não precisa de dependências externas:

```bash
python app.py
```

Acesse http://127.0.0.1:8765. O formulário gera um protocolo, registra a solicitação em SQLite local e devolve categoria, prioridade e sugestão de resposta **baseadas em regras, não em LLM**.

Testes: `python -m unittest discover -v`.

## Evolução planejada: FlowAgent AI
- Integrar um LLM para resumos e sugestões estruturadas com validação de saída
- Incluir revisão humana e painel autenticado do consultor
- Adicionar testes de integração e controles de segurança/privacidade

Este repositório contém uma **demonstração simplificada**. O protótipo anterior de formulário multipasso e painel é uma base de desenvolvimento separada; não está integrado a esta demonstração. Não use dados pessoais reais nem disponibilize este servidor diretamente na internet.

[Portfólio](https://damkccn.github.io/damaris-portfolio/cases/voyageflow.html) · [Instruções](DEVELOPMENT.md)
