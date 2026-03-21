from flask import Flask
from flask import request,jsonify
from app.service.messageService import MessageService

app=Flask(__name__)
app.config.from_pyfile('config.py')

@app.route('/v1/ds/message/',methods=['POST'])
def handle_message():
    if not request.json or 'message' not in request.json:
        return jsonify({"error": "message is required"}), 400
    message=request.json.get('message')
    messageService=MessageService()
    result=messageService.process_message(message)
    return jsonify(result.model_dump())


@app.route('/',methods=['GET'])
def handle_get():  
 message="Oye punjabi aagye oye "
 return message



if __name__ == " __main__":
    print("Starting server.......")
    app.run(host="localhost", port=8080,debug=True)