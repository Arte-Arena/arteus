def create_3d_book_mockup_svg(file_path, image_url):
    # Define SVG header and footer
    svg_header = """<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1000 1200\">
        <rect width=\"1000\" height=\"1200\" fill=\"#FFFFFF\" />"""

    svg_footer = "</svg>"

    # Define 3D book shape
    book_shape = """
        <polygon points=\"300,300 700,200 700,900 300,1000\" fill=\"#F5F5F5\" stroke=\"#000000\" stroke-width=\"3\" />
        <polygon points=\"300,300 250,250 250,950 300,1000\" fill=\"#E0E0E0\" stroke=\"#000000\" stroke-width=\"3\" />
        <polygon points=\"700,200 750,150 750,850 700,900\" fill=\"#D0D0D0\" stroke=\"#000000\" stroke-width=\"3\" />
        <line x1=\"300\" y1=\"300\" x2=\"300\" y2=\"1000\" stroke=\"#000000\" stroke-width=\"2\" />
        <line x1=\"700\" y1=\"200\" x2=\"700\" y2=\"900\" stroke=\"#000000\" stroke-width=\"2\" />"""

    image_element = f"""
        <image href=\"{image_url}\" x=\"300\" y=\"300\" width=\"400\" height=\"600\" preserveAspectRatio=\"xMidYMid slice\" />"""

    # Combine elements into SVG content
    svg_content = svg_header + book_shape + image_element + svg_footer

    # Write to file
    with open(file_path, "w") as svg_file:
        svg_file.write(svg_content)

# Specify the output file path and image URL
output_file = "3d_book_mockup.svg"
image_url = "https://example.com/book_cover.png"  # Replace with your image URL or local file path
create_3d_book_mockup_svg(output_file, image_url)

print(f"SVG file '{output_file}' created successfully!")