# Humpback
- Humpback is a new type agent based on a new language Orca. It can handle multi-step tasks in a more stable manner. It supports debugging the results of each step in a multi-step run, just as you debug python code in vscode.

## todo
- natural language to Orca;
- python code in prompt;

## INSTATLL
```
git clone https://github.com/LB-Young/HumpBack.git
cd HumpBack
pip install -r requirements.txt
```

## RUN
- You need to contact the author to get all the processing logic in the Orca folder first.
```
start backend server: uvicorn backend.app:app
start frontend server: streamlit run frontend/main.py
```