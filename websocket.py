import asyncio
import websockets
import sys
import csv

#df = pd.read_csv(sys.argv[1])
csvReader = csv.reader(open(sys.argv[1]),delimiter=',')
#format: "id,lat,lng,time"

async def send(websocket, path):  
#    for idx, row in df.iterrows():
#        data = str(row['차량번호'])+","+str(row['Y좌표'])+","+str(row['X좌표'])+","+str(row['시분초'])
	for row in csvReader:
		data = row[0]+","+row[1]+","+row[2]+","+row[3]
		await websocket.send(data)
		await asyncio.sleep(0.01) 
        
start_server = websockets.serve(send, '143.248.91.29', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
