# MOViewer

- Usage
  <Batch mode>
    1. run index.html on a web browser
    2. load a source file
  
  <Streaming mode>
    1. set ip address of server in websocket.py and index.html
    2. run websocket.py with the specified source file (> python websocket.py sourcefile.csv)
    3. open index.html on a web browser
    4. click ws_start

* Each line of the soure file shoul be in a format as "id,latitude,longitude,time" 

- Requirement
  <Server>
    - Python 3.5+
    - Packages: asyncio, websockets

  <Client>
    - Web browser
