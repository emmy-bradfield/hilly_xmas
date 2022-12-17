# Merry Christmas, Hilary!

## Setup and Installation

### Quickstart

1. navigate to ./dist
2. download the file hillybot.exe
3. once download is complete, open hillybot.exe
4. enjoy!

### Installation and Full Setup (optional: for editing src files)

#### Requirements
* [Python 3.10.6](https://www.python.org/downloads/)
* [PIP Package Manager](https://pypi.org/project/pip/)
* [Git Bash](https://git-scm.com/downloads)

#### Setup
1. Open your desired project location
2. Clone this repo and move into the dev dir
```
git clone https://www.github.com/emmy-bradfield/hillybot
cd dev
```
3. Install requirements with PIP
```
python -m pip install -r requirements.txt
```
4. From the terminal, you can run the app with
```
python app.py
```

## Testing
don't

## Build as Exe
Following any changes you have made, there are two ways you can package the file into an executable for windows

**Build with PyInstaller**
```
pyinstaller --noconfirm --onefile --console --name "hillybot" --log-level "WARN" --debug "noarchive"  "path/to/file/app.py"
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
