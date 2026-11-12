from app import app


def test_pagina_inicial():
    app.config["TESTING"] = True
    cliente = app.test_client()

    resposta = cliente.get("/")

    assert resposta.status_code == 200
    assert b"cidadao" in resposta.data.lower()
