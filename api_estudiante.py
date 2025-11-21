from flask import Flask,jsonify,request
import json

app=Flask(__name__)

@app.route("/recibir", methods=['POST'])
def recibirInfo():
    print("Info Nueva!!")
    datos=request.get_json()
    ficheroNuevo="mensaje_Enviado.json"
    try:
        with open(ficheroNuevo,"w",encoding="UTF-8") as fichero:
            json.dump(datos,fichero,indent=4)
        return jsonify({"Mensaje": "Envio recibido con exito"}), 200
    except Exception as e:
        print(f"Error {e}")
        return jsonify({"Mensaje":"Error"})

if __name__=='__main__':
    app.run("0.0.0.0",debug=True,port=5000)
        

