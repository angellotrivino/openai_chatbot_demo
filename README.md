# openAI chatbot demo

- **By:** Angello Triviño Umaña

- **Contact:** angello.trivinio@gmail.com

ChatBot with using OpenAI API, also, using Telegram's BotFather

## Licence

 This project has The MIT License (MIT) Copyright (c) 2024, Angello Triviño Umaña

## Directories Distribution
```
├── LICENCE
├── README.md
├── data
│   ├── 0_external
│   ├── 0_raw
│   ├── 1_intermediate
│   └── 2_processed
├── docs
├── environment.yaml
├── notebooks
│   └── 0.0-openai_chatbot_demo-introduction.ipynb
├── reports
├── requirements.txt
├── scripts
├── setup.py
└── openai_chatbot_demo_packages
    ├── __init__.py
    ├── utils
    │   ├── __init__.py
    │   └── get_path.py
    └── visualization
        ├── __init__.py
        └── visualization.py

```

## How to activate the enviroment
you could review the libraries and dependencies to use in *eviroment.yalm* file

- Create a new enviroment with conda:

```
conda env create -f environment.yml
activate openai-py39
```

- If you are using pip
  
create a new enviroment to this proyect (env is the enviroment's name, so could have another name) 

``` 
python3 -m venv env
```

then activate

``` 
source env/bin/activate
```
finally install the libraries:

``` 
pip install -r requirements.txt 
```

## What is the project?

### Demo chatbot with OpenAI API using Telegram's BotFather. 

Example: https://t.me/openai_demo_chatbot 

* System Context on Spanish: "Eres un asistente que da información de Anuncios Publicitarios.". You can change the Context System on the file ~/openai_chatbot_demo_package/utils/updates_telegram_openai.py on function-> def get_openai_response(prompt)

1. Create bot from https://telegram.me/BotFather
2. Launch script: python ~/scripts/openai_chatbot_demo.py
3. Send message on bot create from Telegram's FatherBot
4. Add entorn variables in file config on Ubuntu is on the file bashrc. Open File with command -> nano ~/.bashrc -> add:
        export OPENAI_API_KEY="adkhfdnj48dmm#"
        export TELEGRAM_API_KEY="adjdjd__d4$"
Save file