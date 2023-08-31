import random
from jinja2 import Template

# Jinja2 template for the unicorn drawing
template_string = r"""
\documentclass{standalone}
\usepackage{tikz}

\begin{document}
\begin{tikzpicture}
    % Head and neck
    \draw[{{ headneck_style }}] ({{ headneck_coordinates }}) ellipse ({{ headneck_xradius }} and {{ headneck_yradius }});
    
    % Eyes
    \draw[fill={{ eye_color }}] ({{ left_eye_x }}, {{ left_eye_y }}) circle ({{ eye_radius }});
    \draw[fill={{ eye_color }}] ({{ right_eye_x }}, {{ right_eye_y }}) circle ({{ eye_radius }});
    
    % Nostrils
    \draw[fill=black] (0.2,-0.3) circle (0.045);
    \draw[fill=black] (-0.2,-0.3) circle (0.045);
    
    % Ears
    \draw (-0.8,1.1) -- (-0.6,1.6) -- (-0.4,1.2);
    \draw (0.8,1.1) -- (0.6,1.6) -- (0.4,1.2);
    
    % Body
    \draw[{{ body_style }}] ({{ body_coordinates }}) ellipse ({{ body_xradius }} and {{ body_yradius }});
    
    % Legs
    \draw (1.5,-1.5) -- (1.5,-2.5);
    \draw (2.5,-1.5) -- (2.5,-2.5);
    \draw (3,-1.5) -- (3,-2.5);
    \draw (3.8,-1.5) -- (3.8,-2.5);
    
    % Tail
    \draw[{{ tail_style }}] ({{ tail_coordinates }}) .. controls (0.5,0.8) and (1.5,0.4) .. (1,0);
    
    % Horn
    \draw[{{ horn_style }}] (0,2) -- (-0.2,1.5) -- (0,3) -- (0.2,1.5) -- cycle;
    
    % Mane
    \draw[{{ mane_style }}] (-0.5, 1.4) .. controls (-0.6, 2.5) and (-1.5, 2.5) .. (-1, 1.4);
    \draw[{{ mane_style }}] (0, 1.5) .. controls (-0.1, 2.6) and (-1, 2.6) .. (-0.5, 1.5);
    \draw[{{ mane_style }}] (0.5, 1.4) .. controls (0.4, 2.5) and (-0.5, 2.5) .. (0, 1.4);
\end{tikzpicture}
\end{document}
"""

template = Template(template_string)

# Function to generate a random color
def random_color():
    cols = ['blue', 'red', 'green', 'yellow', 'orange', 'purple', 'brown', 'black', 'white']
    return random.choice(cols)
    # return "#{:06x}".format(random.randint(0, 0xFFFFFF))

# Generate 20 different unicorn drawings
for i in range(21):
    output = template.render(
        # headneck_x = random.randint(0, 10),
        # headneck_y = random.randint(0, 10),
        headneck_xradius = random.randint(0, 2),
        headneck_yradius = random.randint(0, 2),
        headneck_coordinates = "0,0", # "{},{}".format(random.randint(-10, 10), random.randint(-10, 10)),
        headneck_style = "fill={}".format(random_color()),
        left_eye_x = random.randint(-1, 1), # random.randint(-10, -5),
        left_eye_y = random.randint(-1, 1), # random.randint(5, 10),
        right_eye_x = random.randint(-1, 1),
        right_eye_y = random.randint(-1, 1),
        eye_radius = random.randint(0, 1),
        eye_color = random_color(),
       # body_x = random.randint(-10, 10),
       # body_y = random.randint(-10, 10),
        body_xradius = random.randint(0, 3),
        body_yradius = random.randint(0, 3),
        body_style = "fill={}".format(random_color()),
        body_coordinates = "{},{}".format(random.randint(-2, 2), random.randint(-2, 2)),
        tail_xradius = random.randint(0, 3),
        tail_yradius = random.randint(0, 3),
        tail_coordinates = '4.5, -1', # "{},{}".format(random.randint(-10, 10), random.randint(-10, 10)),
        tail_style = 'very thick', # "fill={}".format(random_color()),
        horn_style = 'very thick',
        mane_style =  'very thick'
        # horn_style = "fill={}".format(random_color()),
        # mane_style = "fill={}".format(random_color())
    )

    with open("unicorn{}.tex".format(i), "w") as f:
        f.write(output)

# Original values for the template variables
original_values = {
    'headneck_style': '',
    'headneck_coordinates': '0,0',
    'headneck_xradius': '1',
    'headneck_yradius': '1.4',
    'eye_color': 'black',
    'left_eye_x': '0.3',
    'left_eye_y': '0.5',
    'right_eye_x': '-0.3',
    'right_eye_y': '0.5',
    'eye_radius': '0.08',
    'body_style': '',
    'body_coordinates': '2,-0.5',
    'body_xradius': '1.5',
    'body_yradius': '1',
    'tail_style': 'very thick',
    'tail_coordinates': '4.5,-1',
    'horn_style': 'very thick',
    'mane_style': 'very thick'
}
output = template.render(**original_values)
with open("unicornOriginal.tex".format(i), "w") as f:
        f.write(output)

