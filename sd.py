import requests
import base64
import os, glob

IMG_FOLDER = input()
image_extensions = ["jpg", "jpeg", "png"]

headers = {
    'Accept': '*/*',
    'Content-Type': 'application/json',
    'Origin': 'http://localhost:7860',
    'Referer': 'http://localhost:7860',
}

def gen(img, **kwargs):
    json_data = {
      "fn_index": kwargs["index"],
      "data": [
        0,
        kwargs["prompt"],
        kwargs["nprompt"],
        "None",
        "None",
        img,
        None,
        None,
        None,
        "Draw mask",
        kwargs["steps"],
        "Euler a",
        4,
        "original",
        False,
        False,
        1,
        1,
        kwargs["cfg"],
        kwargs["denoise"],
        kwargs["seed"],
        -1,
        0,
        0,
        0,
        False,
        kwargs["height"],
        kwargs["width"],
        "Just resize",
        False,
        32,
        "Inpaint masked",
        "",
        "",
        "None",
        "Not set",
        "Not set",
        "Not set",
        "Not set",
        "No focus",
        "None",
        "",
        True,
        True,
        "",
        "",
        True,
        50,
        True,
        1,
        0,
        False,
        4,
        1,
        "",
        128,
        8,
        [
          "left",
          "right",
          "up",
          "down"
        ],
        1,
        0.05,
        128,
        4,
        "fill",
        [
          "left",
          "right",
          "up",
          "down"
        ],
        False,
        False,
        None,
        "",
        "",
        64,
        "None",
        "Seed",
        "",
        "Nothing",
        "",
        True,
        False,
        False,
        None
      ]
    }
    response = requests.post('http://localhost:7860/api/predict/', headers=headers, json=json_data)
    
prompt="best quality, masterpiece, laboratories environment, cyberpunk, dark scary"
nprompt = "noise, top right corner, something in bottom right corner, center bottom hud, (hud), text, minimap, first person hand, lowres, error, people, humans, bodies, digits, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, artist name"


i=0
for extension in image_extensions:
    for file_path in glob.glob(os.path.join(IMG_FOLDER, f"*.{extension}")):
        i+=1
        if(i%3!=0)
            continue
        
        with open(file_path, "rb") as image_file:
            img_bytes = image_file.read()
            encoded_string = f"data:image/{extension};base64,{base64.b64encode(img_bytes).decode()}"
            gen(encoded_string, index=35, steps=40, cfg=12, denoise=0.8, height=576, width=1024, seed=-1, prompt=prompt, nprompt=nprompt)
