from jinja2 import Environment, FileSystemLoader
import random

# def random_color():
#     return f"rgb:({random.random()},{random.random()},{random.random()})"

# def random_color():
#    r = random.randint(0, 100)
#    g = random.randint(0, 100)
#    b = random.randint(0, 100)
#    return f"rgb,100!red!{r}!green!{g}!blue!{b}"

# def random_color():
#    return "DeepOrange900"
def random_color():
    color_options = ['Blue500', 'Yellow50', 'Lime900', 'DeepOrange900']
    return random.choice(color_options)


# Set up the Jinja2 environment with custom delimiters and load the template
env = Environment(
    loader=FileSystemLoader('.'),
    variable_start_string='((',
    variable_end_string='))',
    block_start_string='(%',
    block_end_string='%)',
    comment_start_string='(#',
    comment_end_string='#)',
)
template = env.get_template('squid_template.tex')

# Define the eye colors (either original or blue)
original_eye_colors = {
    'outer_eye_color': 'Grey50',
    'inner_eye_color': 'BlueGrey900',
}

blue_eye_colors = {
    'outer_eye_color': 'blue',
    'inner_eye_color': 'blue!60!white',
}

# Choose the eye colors: either 'original_eye_colors' or 'blue_eye_colors'
eye_colors = blue_eye_colors # original_eye_colors  # Change this to 'blue_eye_colors' for blue eyes

# Define the spots
o_spots = [
    {'x': -32, 'y': 108, 'radius': 16},
    {'x': -40, 'y': 160, 'radius': 12},
    {'x': -20, 'y': 196, 'radius': 8},
    {'x': 40, 'y': 160, 'radius': 16},
    {'x': 64, 'y': 120, 'radius': 8},
    {'x': 40, 'y': 100, 'radius': 12},
]



# ... (other parts of the code)

# Define the random_mode flag (True for random colors, False for the default color)
random_mode = True

# Define the spots
o_spots = [
    {'x': -32, 'y': 108, 'radius': 16, 'color': random_color() if random_mode else 'DeepOrange300'},
    {'x': -40, 'y': 160, 'radius': 12, 'color': random_color() if random_mode else 'DeepOrange300'},
    {'x': -20, 'y': 196, 'radius': 8, 'color': random_color() if random_mode else 'DeepOrange300'},
    {'x': 40, 'y': 160, 'radius': 16, 'color': random_color() if random_mode else 'DeepOrange300'},
    {'x': 64, 'y': 120, 'radius': 8, 'color': random_color() if random_mode else 'DeepOrange300'},
    {'x': 40, 'y': 100, 'radius': 12, 'color': random_color() if random_mode else 'DeepOrange300'},
]

extra_spots = o_spots.copy()
extra_spots.append({'x': 20, 'y': 140, 'radius': 10, 'color': random_color() if random_mode else 'DeepOrange300'})
extra_spots.append({'x': 40, 'y': 120, 'radius': 16, 'color': random_color() if random_mode else 'DeepOrange300'})

# Render the template with the chosen eye colors and spots

crazy_tentacles = True # True
original_tentacles = False # True

prominent_mouth = True
agressive_shading = True



# Render the template with the chosen eye colors and spots
with open('squid_output.tex', 'w') as output_file:
    output_file.write(template.render(eye_colors, spots=extra_spots, crazy_tentacles=crazy_tentacles, prominent_mouth=prominent_mouth, agressive_shading=agressive_shading, original_tentacles=original_tentacles))
    print("Eye colors: ", eye_colors)
    print("Spots: ", extra_spots)
    print("Crazy tentacles: ", crazy_tentacles)
    print("Original tentacles: ", original_tentacles)
    print("Prominent mouth: ", prominent_mouth)
    print("Agressive shading: ", agressive_shading)
    
