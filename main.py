from fastapi import FastAPI, HTTPException
import uvicorn 
import requests

app = FastAPI()

@app.get('/patente/id/{id}')
async def PatenteID(id:int):
	url = f"http://dextre.pythonanywhere.com/patente/{id}"
	response = requests.get(url)

	if response.status_code == 200:
		response_json = response.json()
		patente = response_json['patente']
		print(f'Placa Patente: {patente}')
	
	else:
		raise HTTPException(status_code=404, detail="¡Este ID no existe!")
	
	return f'Placa Patente: {patente}'

@app.get('/placa/patente/{placa}')
async def PlacaPatente(placa:str):
	url = f"https://dextre.pythonanywhere.com/patente/{placa}"
	response = requests.get(url)

	if response.status_code == 200:
		response_json = response.json()
		id = response_json['id']
		print (f'ID de la Placa Patente: {id}')
	else:
		raise HTTPException(status_code=404, detail="¡Esta Placa Patente no existe!")
	return f'ID de la Placa Patente: {id}'


if __name__=="__main__":
	uvicorn.run("main:app",port=3000,reload=True)

"""
Hay 2 formas de iniciar una app de FastApi.
	1- uvicorn main:app, la cual se le puede especificar --host, --port, --reload... etc.
	2- if __name__=="__main__":
			uvicorn.run("main:app",port=3000,reload=True)
		Se le especifica los parametros y asi se evita estar ejecutando el archivo por consola despues de los cambios.
"""