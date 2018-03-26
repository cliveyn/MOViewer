# MOViewer

## Usage
  ### Batch mode
    1. Run index.html on a web browser
    2. Load a source file
  
  ### Streaming mode
    1. Set an ip address of a server in websocket.py and index.html
    2. Run websocket.py with the specified source file (> python websocket.py sourcefile.csv)
    3. Open index.html on a web browser
    4. Click ws_start

- Each line of the soure file shoul be in a format as "id,latitude,longitude,time" 

## Requirement
  ### Server
    - Python 3.5+
    - Packages: asyncio, websockets

  ### Client
    - Web browser
