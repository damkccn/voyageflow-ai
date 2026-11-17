# Executar localmente

Requisitos: Python 3.10+.

```bash
python app.py
```

Abra http://127.0.0.1:8765. Execute `python -m unittest discover -v` para testes.

**Limites:** esta é uma demonstração com classificação por regras, sem autenticação e sem API de LLM. A base SQLite local não deve receber dados pessoais reais. O formulário demonstra a ideia do VoyageFlow; o painel do consultor e a integração do FlowAgent com LLM ainda são trabalhos futuros.

## Roadmap
1. Integração do módulo FlowAgent com LLM e saída JSON validada.
2. Painel protegido para consultores.
3. Testes de integração, tratamento de erros, proteção de dados e logs sem PII.
4. Deploy de backend em serviço apropriado (GitHub Pages hospeda apenas front-end estático).
