"""VoyageFlow AI — demo local sem dados reais. Python 3.10+; sem dependências externas."""
import json
import os
import re
import sqlite3
import uuid
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).parent
DB = ROOT / "voyageflow_demo.db"
MAX_BODY = 12000

def classify(message):
    text = message.strip()
    if not 1 <= len(text) <= 3000:
        raise ValueError("Mensagem deve ter entre 1 e 3000 caracteres")
    low = text.casefold()
    groups = {
        "orcamento": ("orçamento", "orcamento", "preço", "preco", "cotação", "cotacao"),
        "documentacao": ("passaporte", "visto", "documento"),
        "alteracao": ("cancelar", "alterar", "remarcar", "reembolso"),
        "reserva": ("reservar", "reserva", "hotel", "passagem"),
    }
    scores = {name: sum(term in low for term in terms) for name, terms in groups.items()}
    category = max(scores, key=scores.get) if max(scores.values()) else "geral"
    priority = "alta" if any(term in low for term in ("urgente", "amanhã", "amanha", "hoje", "perdi o voo")) else "normal"
    return {"categoria": category, "prioridade": priority, "resumo": text[:240],
            "resposta_sugerida": "Olá! Recebemos sua solicitação. Um consultor confirmará as informações e os próximos passos.",
            "origem": "regras (sem LLM)", "revisao_humana": True}

def setup():
    with sqlite3.connect(DB) as con:
        con.execute("""CREATE TABLE IF NOT EXISTS solicitacoes
            (id TEXT PRIMARY KEY, criado_em TEXT NOT NULL, destino TEXT NOT NULL,
            periodo TEXT NOT NULL, viajantes INTEGER NOT NULL, mensagem TEXT NOT NULL,
            categoria TEXT NOT NULL, prioridade TEXT NOT NULL)""")

class Handler(BaseHTTPRequestHandler):
    def respond(self, code, obj):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if urlparse(self.path).path != "/":
            self.send_error(404)
            return
        data = (ROOT / "index.html").read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_POST(self):
        if self.path != "/api/solicitacoes":
            self.send_error(404)
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length < 2 or length > MAX_BODY:
                raise ValueError("Tamanho de solicitação inválido")
            payload = json.loads(self.rfile.read(length))
            destino = str(payload.get("destino", "")).strip()
            periodo = str(payload.get("periodo", "")).strip()
            viajantes = int(payload.get("viajantes", 0))
            mensagem = str(payload.get("mensagem", "")).strip()
            if not (1 <= len(destino) <= 100 and 1 <= len(periodo) <= 100 and 1 <= viajantes <= 30):
                raise ValueError("Preencha destino, período e número de viajantes")
            analysis = classify(mensagem)
            protocol = "VG-" + uuid.uuid4().hex[:10].upper()
            with sqlite3.connect(DB) as con:
                con.execute("INSERT INTO solicitacoes VALUES (?,?,?,?,?,?,?,?)",
                    (protocol, datetime.now(timezone.utc).isoformat(), destino, periodo,
                     viajantes, mensagem, analysis["categoria"], analysis["prioridade"]))
            self.respond(201, {"protocolo": protocol, "analise": analysis})
        except (ValueError, TypeError, json.JSONDecodeError) as exc:
            self.respond(422, {"erro": str(exc)})

if __name__ == "__main__":
    setup()
    print("Demo local: http://127.0.0.1:8765")
    ThreadingHTTPServer(("127.0.0.1", 8765), Handler).serve_forever()
