import os
from flask import Flask, render_template, request
import qrcode

app = Flask(__name__)

@app.route("/qr.html", methods=['GET', 'POST'])
def qr():
    if request.method == 'POST':
        data = request.form.get('textlink')
        if data:
            try:
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(data)
                qr.make(fit=True)
                img = qr.make_image(fill_color="black", back_color="white")
                file_path = os.path.join(app.root_path, 'static', 'photos', 'qrcode.png')
                img.save(file_path)
                return render_template("qr.html")
            except Exception as e:
                # Handle any unexpected errors
                return "Error occurred: " + str(e)
    return render_template("qr.html")

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
