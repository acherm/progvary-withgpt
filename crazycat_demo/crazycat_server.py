from flask import Flask, render_template, request, send_file, jsonify
import random
from jinja2 import Environment, FileSystemLoader



app = Flask(__name__)

def random_rgb_color():
    # colors = ["red", "blue", "orange", "brown", "pink", "green", "yellow", "purple", "cyan", "magenta", "teal", "black"]
    colors = ["red", "blue", "orange", "brown", "pink", "green", "yellow", "purple", "cyan", "magenta", "teal", "black"]
    colors.extend(["BlueGrey900", "Purple100", "BlueGrey500", "BlueGrey100", "Purple100", "Yellow50", "Grey100"])
    return random.choice(colors)

def random_scale(min_value=0.5, max_value=2.0):
    return random.uniform(min_value, max_value)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cat.png")
def cat_svg():
    return send_file("templates/cat.png", mimetype="image/png", as_attachment=False)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json   

    env = Environment(loader=FileSystemLoader('.'), variable_start_string='<<', variable_end_string='>>', block_start_string="<%", block_end_string="%>", comment_start_string="<#", comment_end_string="#>")
    template = env.get_template('crazycat_template.tex')

    # main_body => tail 
    # head stripe => outter ear 
    # inner stripe => inner ear

    # Whisker spots scale => eye scale

    # whisker spots color => eyes color
    # eyes color => outter nose color
    # nose color => inner nose color
    # nose main color => head and paws color
    # face inner ellipses color => paws lower part color
    # face lower part color => lower part color
    # head surround color => central body color
    # head inner color => inner body color


    output = template.render(
    #     main_body_color="red",
    #     outter_ear_color="blue",
    #     inner_ear_color="orange",
    #     # outter_ear_scale=0.8,
    #     central_body_color="green",
    #     inner_body_color="yellow",
    #     head_paws_color="purple",
    #     outter_nose_color="brown",
    #     nose_color="pink",
    #     eyes_color="cyan",
    #     eyes_scale=1.5,
    #     lower_part_color="black",
    #     bottom_paws_color="magenta",
    #     whiskers_color="teal",
        tail_color=data['tail_color'],
        outter_ear_color=data['outter_ear_color'],
        inner_ear_color=data['inner_ear_color'],
        outter_ear_scale=data['outter_ear_scale'],
        central_body_color=data['central_body_color'],
        inner_body_color=data['inner_body_color'],
        head_paws_color=data['head_paws_color'],
        outter_nose_color=data['outter_nose_color'],
        nose_color=data['nose_color'],
        eyes_color=data['eyes_color'],
        eyes_scale=data['eyes_scale'],
        lower_part_color=data['lower_part_color'],
        bottom_paws_color=data['bottom_paws_color'],
        whiskers_color=data['whiskers_color'],
    #
    )

    # output = template.render(
    #     # tail_color="BlueGrey900",
    #     tail_color=data['tail_color'],
    #     outter_ear_color="BlueGrey900",
    #     inner_ear_color="Purple100",
    #     outter_ear_scale=data['outter_ear_scale'],
    #     # outter_ear_scale=1.0,
    #     central_body_color="BlueGrey900",
    #     inner_body_color="BlueGrey100",
    #     head_paws_color="BlueGrey900",
    #     outter_nose_color="BlueGrey500",
    #     nose_color="Purple100",
    #     eyes_color="Yellow50",
    #     eyes_scale=1.0,
    #     lower_part_color="BlueGrey900",
    #     bottom_paws_color="Grey100",
    #     whiskers_color="Grey100",
    # )
    # Assuming `output` is the image data (in bytes) or a base64 encoded string
    
    # write output in a file called "out.tex"
    with open("out.tex", "w") as f:
        f.write(output)

    # system call "pdflatex out.tex"
    import subprocess
    subprocess.call(["pdflatex", "out.tex"])

    # system call and translate PDF into PNG
    # subprocess.call(["convert", "-density", "300", "out.pdf", "-quality", "90", "out.png"])

    # system call and translate PDF into SVG
    # using pdf2svg crazycat_1.pdf cc1.svg
    subprocess.call(["pdf2svg", "out.pdf", "out.svg"])

    # in Flask, return a PNG file (image/png)
    # return send_file("out.svg", mimetype="image/svg", as_attachment=False)

    # return a SVG file 
    return send_file("out.svg", mimetype="image/svg+xml", as_attachment=False)
    
    # return jsonify({"image": output})

if __name__ == "__main__":
    app.run(debug=True)
