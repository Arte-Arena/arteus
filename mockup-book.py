def create_book_mockup_svg(file_path, image_url):
    # Define SVG header and footer
    svg_header = """<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 800 1000\">
        <rect width=\"800\" height=\"1000\" fill=\"#FFFFFF\" />"""
    
    svg_footer = "</svg>"

    # Define book shape and image
    book_shape = """
        <rect x=\"100\" y=\"100\" width=\"600\" height=\"800\" fill=\"#F5F5F5\" stroke=\"#000000\" stroke-width=\"5\" />
        <line x1=\"400\" y1=\"100\" x2=\"400\" y2=\"900\" stroke=\"#000000\" stroke-width=\"2\" />"""
    
    image_element = f"""
        <image href=\"{image_url}\" x=\"150\" y=\"150\" width=\"500\" height=\"700\" preserveAspectRatio=\"xMidYMid slice\" />"""

    # Combine elements into SVG content
    svg_content = svg_header + book_shape + image_element + svg_footer

    # Write to file
    with open(file_path, "w") as svg_file:
        svg_file.write(svg_content)

# Specify the output file path and image URL
output_file = "book_mockup.svg"
image_url = "https://example.com/book_cover.png"  # Replace with your image URL or local file path
create_book_mockup_svg(output_file, image_url)

print(f"SVG file '{output_file}' created successfully!")


