#!/usr/bin/env python3 

import colorgram as cg

colors = cg.extract('hirst_tate_L02864_9.jpg', 100)  # 100 should give me each color, even though there are not 100 colors 

rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_color = (r, g, b) 
    rgb_colors.append(rgb_color)
    
print(rgb_colors)