# Comandos Executados no Projeto Tirindicator

Este arquivo lista os comandos principais executados via terminal durante a configuração e desenvolvimento do projeto.

## 1. Estrutura de Pastas
```powershell
mkdir app, frontend, data, tests -ErrorAction SilentlyContinue
```

## 2. Configuração do Ambiente Virtual (venv)
```powershell
# Criação do venv usando o caminho absoluto do Python 3.14
& "C:\Program Files\Python314\python.exe" -m venv venv

# Ativação (Manual pelo usuário)
.\venv\Scripts\Activate.ps1
```

## 3. Instalação de Dependências
```powershell
# Upgrade do PIP
.\venv\Scripts\python.exe -m pip install --upgrade pip

# Instalação das dependências do projeto
.\venv\Scripts\pip.exe install -r requirements.txt

# Instalação de dependência adicional para validação de email no Pydantic
.\venv\Scripts\pip.exe install email-validator
```

## 4. Inicialização de Pacotes e Testes
```powershell
# Criação de arquivos __init__.py para transformar pastas em pacotes Python
New-Item -Path app\__init__.py, frontend\__init__.py, tests\__init__.py -ItemType File -Force

# Execução de testes unitários do motor de recomendação
$env:PYTHONPATH="."; .\venv\Scripts\pytest tests/test_recommendation.py
```

## 5. Gerenciamento de Processos e Portas
```powershell
# Verificação de processos na porta 8000
Get-NetTCPConnection -LocalPort 8000 -ErrorAction SilentlyContinue | Select-Object OwningProcess

# Encerramento de processo travado (exemplo)
Stop-Process -Id <PID> -Force
```

## 6. Execução da Aplicação
```powershell
# Comando unificado (Backend na porta 8080 e Frontend Streamlit)
.\venv\Scripts\python.exe run_app.py
```

## 7. Verificação de Arquivos
```powershell
# Verificar persistência do banco de dados
dir data\tirindicator.db
```
