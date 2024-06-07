from flask import Flask, request, jsonify

app = Flask(__name__)


kullanicilar = []

def kullanici_olustur(kullanici_id, kullanici_adi):
    kullanici = {"id": kullanici_id, "ad": kullanici_adi}
    kullanicilar.append(kullanici)
    return kullanici

# ID'ye göre kullanıcı getirme
def kullanici_getir(kullanici_id):
    for kullanici in kullanicilar:
        if kullanici["id"] == kullanici_id:
            return kullanici
    return None

# Tüm kullanıcıları getirme
def tum_kullanicilari_getir():
    return kullanicilar

@app.route('/kullanici', methods=['POST'])
def kullanici_olustur_endpoint():
    veri = request.get_json()
    kullanici_id = veri.get("id")
    kullanici_adi = veri.get("ad")
    kullanici = kullanici_olustur(kullanici_id, kullanici_adi)
    return jsonify(kullanici), 201

@app.route('/kullanici/<int:kullanici_id>', methods=['GET'])
def kullanici_getir_endpoint(kullanici_id):
    kullanici = kullanici_getir(kullanici_id)
    if kullanici:
        return jsonify(kullanici)
    else:
        return jsonify({"hata": "Kullanıcı bulunamadı"}), 404

@app.route('/kullanicilar', methods=['GET'])
def tum_kullanicilari_getir_endpoint():
    return jsonify(tum_kullanicilari_getir())

if __name__ == '__main__':
    app.run(debug=True)
