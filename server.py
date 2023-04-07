import asyncio
from threadsnake.turbo import *

app:Application = Application(8089)

@app.get('/')
def main(app:Application, req:HttpRequest, res:HttpResponse):
    res.end('Ready')

asyncio.run(app.run())