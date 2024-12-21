from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/api/handler', methods=['POST'])
def handler():
    body = request.json
    if app.debug:
        print(body)

    # 回调验证
    if body and body.get('type') == 'url_verification':
        return jsonify({'challenge': body.get('challenge')})

    if body and body.get('header', {}).get('event_type') == 'url.preview.get':
        return jsonify({
            'inline': {
                'i18n_title': {
                    'zh_cn': 'Hello MarsCode',
                },
                'image_key': 'img_v3_02gp_bc939d82-ad8d-4dd0-856d-c26e2d161b9g',
            },
        })

    return jsonify({})

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'