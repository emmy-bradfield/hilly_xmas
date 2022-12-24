# $Merry$ $Christmas,$ $Hilary!$

Dear Hilly, <br/>
&nbsp; &nbsp; After many moons of crying into VSCode at last, it is here! Your xmas gift has arrived. Below are the details on how to run the pre-package executable (dist: recommended) or to download the source files and rebuild from the python script (dev) if you wish to change the source code itself. <br/>
&nbsp; &nbsp; I hope this little bot, which admittedly has consumed more of our time than it should have, brings you plenty of joy and makes you smile! <br/>
Lots of love <br/>
Emily and Ammar

--- 

## Setup and Installation

### Quickstart (app)

#### Requirements
* A Windows machine on which to execute .exe files

#### Setup

1. navigate to ./app
2. download the file hillybot.exe
3. once download is complete, open hillybot.exe
4. enjoy!

### Full build from src (dev)

#### Requirements
* [Python 3.10.6](https://www.python.org/downloads/) with [PIP Package Manager](https://pypi.org/project/pip/)
* [Git Bash](https://git-scm.com/downloads)
* [PyInstaller (*optional: for packaging only*)](https://pyinstaller.org/en/stable/)

#### Setup
1. Clone the repo, install the packages, and move into dev/
```
git clone https://www.github.com/emmy-bradfield/hilly_xmas
python -m pip install -r requirements.txt
cd dev
```
4. From the terminal, you can run the app with
```
python app.py
```
5. To access OpenAI's Davinici you will need a API key. This is included in dist/hillybot.exe, but if you're rebuilding you can aquire one from [OpenAI's Website](https://openai.com/api/) for free
6. Once you have the API key, simply create '.env' file in the dev directory, with
```
HILLYBOT_API="<your-API-key>"
```
or, you can change your environment variables using the below on Windows
```
set OPENAI_API_KEY=<you-API-key>
```
7. From here, you are free to amend the script however you want. Once you're happy with it, you can package it to .exe Firstly, make sure you change the hidden imports path in hillybot.spec to match your import location. Then, use PyInstaller to handle the rest by executing:
```
pyinstaller --distpath ./dist --clean -y hillybot.spec
```

## About

### Built With
* [OpenAi's Davinci](https://www.github.com/openai)
* [SpaCy](https://github.com/explosion/spaCy)

### Contributors
* [DarkbyteAT](https://www.github.com/darkbyteAT)
* [emmy-bradfield](https://www.github.com/emmy-bradfield)

### Licensing
Licenced with MIT. See [Licencing Page](https://github.com/emmy-bradfield/hilly_xmas/blob/master/LICENSE)
