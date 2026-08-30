#Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
#.\setup_env.ps1
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt