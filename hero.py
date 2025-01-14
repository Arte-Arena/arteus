def create_superhero_mockup_svg(file_path):
    # Define SVG header and footer
    svg_header = """<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 800 1200\">
        <rect width=\"800\" height=\"1200\" fill=\"#ADD8E6\" />"""

    svg_footer = "</svg>"

    # Define superhero body
    body_shape = """
        <ellipse cx=\"400\" cy=\"700\" rx=\"150\" ry=\"300\" fill=\"#FFD700\" stroke=\"#000000\" stroke-width=\"3\" />
        <rect x=\"300\" y=\"450\" width=\"200\" height=\"300\" fill=\"#FF4500\" stroke=\"#000000\" stroke-width=\"3\" />
        <circle cx=\"400\" cy=\"350\" r=\"100\" fill=\"#FAD02E\" stroke=\"#000000\" stroke-width=\"3\" />"""

    # Define mask and cape
    mask_and_cape = """
        <path d=\"M350,300 Q400,270 450,300 Q420,350 380,350 Z\" fill=\"#000000\" />
        <polygon points=\"300,450 400,600 500,450 400,200\" fill=\"#8B0000\" fill-opacity=\"0.7\" />"""

    # Combine elements into SVG content
    svg_content = svg_header + body_shape + mask_and_cape + svg_footer

    # Write to file
    with open(file_path, "w") as svg_file:
        svg_file.write(svg_content)

# Specify the output file path
output_file = "superhero_mockup.svg"
create_superhero_mockup_svg(output_file)

print(f"SVG file '{output_file}' created successfully!")
