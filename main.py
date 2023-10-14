from flask import Flask, jsonify
from config import key
import openai
from flask import render_template, request, send_file
import os
openai.api_key = key
from gtts import gTTS


app = Flask(__name__)



@app.route('/')
def imagezen():
  return render_template('imagezen.html', )


@app.route('/generateimages/<prompt>')
def generate(prompt):
  print("prompt:", prompt)
  response = openai.Image.create(prompt=prompt, n=3, size="256x256")
  print(response)
  return jsonify(response)






app.run(host='0.0.0.0', port=81)
