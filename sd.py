import requests
import base64
import os, glob

IMG_FOLDER = "1"

headers = {
    'Accept': '*/*',
    'Content-Type': 'application/json',
    'Origin': 'http://localhost:7860',
    'Referer': 'http://localhost:7860',
}

def gen(img, **kwargs):
    json_data = {
        'fn_index': kwargs["index"],
        'data': [
            'task(73141x8zk91y9ya5)',
            0,
            kwargs["prompt"],
            kwargs["nprompt"],
            [],
            img,
            None,
            None,
            None,
            None,
            None,
            None,
            kwargs["steps"],
            'Euler a',
            4,
            0,
            'original',
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
            'Just resize',
            'Whole picture',
            32,
            'Inpaint masked',
            '',
            '',
            'None',
            '<ul>\n<li><code>CFG Scale</code> should be 2 or lower.</li>\n</ul>\n',
            True,
            True,
            '',
            '',
            True,
            50,
            True,
            1,
            0,
            False,
            4,
            1,
            '<p style="margin-bottom:0.75em">Recommended settings: Sampling Steps: 80-100, Sampler: Euler a, Denoising strength: 0.8</p>',
            128,
            8,
            [
                'left',
                'right',
                'up',
                'down',
            ],
            1,
            0.05,
            128,
            4,
            'fill',
            [
                'left',
                'right',
                'up',
                'down',
            ],
            False,
            False,
            False,
            False,
            '',
            '<p style="margin-bottom:0.75em">Will upscale the image by the selected scale factor; use width and height sliders to set tile size</p>',
            64,
            'None',
            2,
            'Seed',
            '',
            'Nothing',
            '',
            True,
            False,
            False,
            [],
            '',
            '',
            '',
        ]
    }
    response = requests.post('http://localhost:7860/run/predict/', headers=headers, json=json_data, verify=False)

prompt="best quality, masterpiece, laboratories environment, cyberpunk, dark scary"
nprompt = "noise, top right corner, something in bottom right corner, center bottom hud, (hud), text, minimap, first person hand, lowres, error, people, humans, bodies, digits, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, artist name"

i=0
file_paths = glob.glob(os.path.join(IMG_FOLDER, "*.png"))
sorted_file_paths = sorted(file_paths)
for file_path in sorted_file_paths:
    i+=1
    if(i%3!=0):
        continue

    with open(file_path, "rb") as image_file:
        img_bytes = image_file.read()
        encoded_string = f"data:image/png;base64,{base64.b64encode(img_bytes).decode()}"
        gen(encoded_string, index=129, steps=40, cfg=12, denoise=0.8, height=720, width=1280, seed=-1, prompt=prompt, nprompt=nprompt)
