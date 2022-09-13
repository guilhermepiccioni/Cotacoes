## Current Quotes.

In this project, the execution and visualization of the generated values is very simple.

First you will need to create the virtualenv. Run the command:

    make venv

In terminal run the command to activate:

    . venv/bin/activate (for Linux)

    . venv/Scripts/activate (for Windows)

Once this is done, run the command that will install the project's dependencies:

    make build

To generate a new spreadsheet with updated quotes, simply run the command:

    make trade

To view the data of all spreadsheets generated in the History_price directory, simply run the command:
    
    make history_trades

----------------------------------------------------------------------------------------------------

## Cotações Atuais.

Nesse projeto, e muito simples a execução e visualização  dos valores gerados.

Primeiro sera necessario a criação do virtualenv. Execute o comando:

    make venv

Em terminal execute o comando para ativação:

    . venv/bin/activate    (para Linux)

    . venv/Scripts/activate    (para Windows)

Feito isto, execute o comando que ira instalar as dependencias do projeto:

    make build

Para gerar uma nova planilha com cotaçoes atualizadas, basta executar o comando:

    make trade

Para visualizar os dados de todas as planilhas geradas no diretorio History_price, 
basta executar o comando:

    make history_trades