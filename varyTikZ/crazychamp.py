from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'), variable_start_string='<<', variable_end_string='>>', block_start_string="<%", block_end_string="%>", comment_start_string="<#", comment_end_string="#>")
template = env.get_template('crazychimpanzee.tex')

import random

def random_rgb_color():
    colors = ["red", "blue", "orange", "brown", "pink", "green", "yellow", "purple", "cyan", "magenta", "teal", "black"]
    colors.extend(["BlueGrey900", "Purple100", "BlueGrey500", "BlueGrey100", "Purple100", "Yellow50", "Grey100"])
    return random.choice(colors)
 

def random_scale(min_value=0.5, max_value=2.0):
    return random.uniform(min_value, max_value)



parameters = { 'head_background_color': 'green',
    'head_foreground_color': 'yellow',
    'body_background_color': 'green',
    'face_overlay_color': 'red',
    'face_overlay_foreground_color': 'orange',
    'lower_face_base_color': 'purple',
    'lower_face_overlay_color': 'purple',
    'ear_color': 'white', # eye color
    'eye_color': 'black', # nose color
    'mouth_outline_color': 'yellow' # mouth color
}

# original_parameters = {
#     'head_background_color': 'blue', # left ear color, outter 
#     'head_foreground_color': 'red', # left ear color, inner
#     'body_background_color': 'yellow', # left overlay color 
#     'face_overlay_color': 'blue', # right overlay color with right ear color, outter 
#     'face_overlay_foreground_color': 'pink', # right ear color, inner
#     'lower_face_base_color': 'white', # left face color
#     'lower_face_overlay_color': 'orange', # right face color
#     'ear_color': 'BlueGrey900', # eye color
#     'eye_color': 'Pink300', # nose color
#     'mouth_outline_color': 'Pink300'
# }

import random

def random_color_variation():
    colors = ["red", "blue", "orange", "brown", "pink", "green", "yellow", "purple", "cyan", "magenta", "teal", "black"]
    colors.extend(["BlueGrey700", "Pink100", "BlueGrey900", "Pink300"])
    return random.choice(colors) 

def random_variation(base_parameters, color_variation=50, angle_variation=90, scale_variation=0.5):
    parameters = base_parameters.copy()

    for key in parameters:
        if key.endswith('_color'):
            parameters[key] = random_color_variation()

    parameters['rotation_angle'] = (parameters['rotation_angle'] + random.randint(-angle_variation, angle_variation)) % 360
    parameters['scaling_factor'] += random.uniform(-scale_variation, scale_variation)
    return parameters

original_revised_parameters = {
    'left_ear_outer_color': 'BlueGrey700',
    'left_ear_inner_color': 'Pink100',
    'left_overlay_color': 'BlueGrey700',
    'right_overlay_color': 'BlueGrey900',
    'right_ear_outer_color': 'BlueGrey900',
    'right_ear_inner_color': 'Pink200',
    'left_face_color': 'Pink100',
    'right_face_color': 'Pink200',
    'eye_color': 'BlueGrey900',
    'nose_color': 'Pink300',
    'mouth_outline_color': 'Pink300',
    'rotation_angle': 45,  # Angle of rotation in degrees
    'scaling_factor': 1.5   # Scaling factor for the size
}

randomized_parameters = random_variation(original_revised_parameters)

output = template.render(randomized_parameters)

print (output)


