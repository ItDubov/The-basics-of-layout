from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def contacts_page(path):
    """
    Обрабатывает любой GET-запрос и возвращает страницу 'Контакты'.
    """
    return render_template("contacts.html"), 200, {"Content-Type": "text/html"}

if __name__ == "__main__":
    # Запуск сервера на локальном хосте
    app.run(host="0.0.0.0", port=5000)
