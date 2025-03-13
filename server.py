from flask import Flask, Response

app = Flask(__name__)

@app.route('/plivo-xml')
def plivo_xml():
    xml_response = """<?xml version="1.0" encoding="UTF-8"?>
    <Response>
        <Dial>
            <Sip>sip:elevenlabs.sip.twilio.com</Sip>
        </Dial>
    </Response>"""
    return Response(xml_response, mimetype='application/xml')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
