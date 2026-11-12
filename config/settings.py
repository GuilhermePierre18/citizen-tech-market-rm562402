"""Configuracoes do Citizen Tech Market."""
import os

DEBUG = True
REGIAO = "sa-east-1"
BUCKET = "ct-market-notas-fiscais"

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
