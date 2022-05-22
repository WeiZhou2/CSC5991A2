from flask import Flask
import requests
import random
app = Flask(__name__)

jokes = [
    {
        "joke": "Q: \"Whats the object-oriented way to become wealthy?\" A: Inheritance",
        "author": "Alok Moghe"
    },
    {
        "joke": "It’s not a bug, it's a feature",
        "author": "Angie Johnson"
    },
    {
        "joke": "Q: \"Why did the programmer quit his job?\" A: Because he didn't get arrays.",
        "author": "Alok Moghe"
    },
    {
        "joke": "Q: \"Why was the DBA divorced?\" A: Because the DBA has one to many relationships.",
        "author": "Vivek San"
    },
    {
        "joke": "Q: \"Name the kind of tree you can hold in your hand?\" A: A palm tree!.",
        "author": "Online"
    },
    {
        "joke": "Q: \"What do kids play when their mom is using the phone\" A: Bored games.",
        "author": "Online"
    },
    {
        "joke": "Q: \"What’s the smartest insect?\" A: A spelling bee!.",
        "author": "Online"
    },
    {
        "joke": "Q: \"Why did the teddy bear say no to dessert?\" A: Because she was stuffed!.",
        "author": "Online"
    },
    {
        "joke": "Q: \" What fruit do twins love?\" A: Pears!.",
        "author": "Online"
    },
    {
        "joke": "Q: \"What time is it when people are throwing pieces of bread at your head?\" A: Time to duck.",
        "author": "Online"
    }
]

@app.route('/joke/', methods=['GET'])
def local_jokes():
    randomNumber = random.randint(0, len(jokes)-1);
    return jokes[randomNumber]

@app.route('/online-joke/', methods=['GET'])
def online_jokes():
    response = requests.get('https://v2.jokeapi.dev/joke/Any')
    return response.json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



