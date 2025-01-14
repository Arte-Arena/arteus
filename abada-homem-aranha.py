def create_carnival_abada_svg(file_path, image_url):
    # Define SVG header and footer
    svg_header = """<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 800 1000\">
        <rect width=\"800\" height=\"1000\" fill=\"#FFFFFF\" />"""
    
    svg_footer = "</svg>"

    # Define abadá shape and image
    abada_shape = """
        <path d=\"M200,200 Q150,100 300,50 L500,50 Q650,100 600,200 L700,400 L700,900 L100,900 L100,400 Z\" fill=\"#FF0000\" stroke=\"#000000\" stroke-width=\"5\" />"""
    
    image_element = f"""
        <image href=\"{image_url}\" x=\"150\" y=\"250\" width=\"500\" height=\"500\" preserveAspectRatio=\"xMidYMid slice\" />"""

    # Combine elements into SVG content
    svg_content = svg_header + abada_shape + image_element + svg_footer

    # Write to file
    with open(file_path, "w") as svg_file:
        svg_file.write(svg_content)

# Specify the output file path and image URL
output_file = "carnival_abada.svg"
image_url = "https://example.com/spiderman_image.png"  # Replace with your image URL or local file path
create_carnival_abada_svg(output_file, image_url)

print(f"SVG file '{output_file}' created successfully!")
