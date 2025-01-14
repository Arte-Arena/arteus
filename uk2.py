def create_union_jack_svg(file_path):
    # Define SVG header and footer
    svg_header = """<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1200 600\">
        <rect width=\"1200\" height=\"600\" fill=\"#012169\" />"""
    
    svg_footer = "</svg>"

    # Define flag elements
    elements = [
        # White diagonal cross
        """<polygon points=\"0,0 200,0 1200,400 1200,600 1000,600 0,200\" fill=\"white\" />""",
        """<polygon points=\"1200,0 1000,0 0,400 0,600 200,600 1200,200\" fill=\"white\" />""",

        # Red diagonal cross
        """<polygon points=\"0,0 120,0 1200,380 1200,450 1080,450 0,120\" fill=\"#C8102E\" />""",
        """<polygon points=\"1200,0 1080,0 0,380 0,450 120,450 1200,120\" fill=\"#C8102E\" />""",

        # White horizontal and vertical cross
        """<rect x=\"0\" y=\"250\" width=\"1200\" height=\"100\" fill=\"white\" />""",
        """<rect x=\"550\" y=\"0\" width=\"100\" height=\"600\" fill=\"white\" />""",

        # Red horizontal and vertical cross
        """<rect x=\"0\" y=\"275\" width=\"1200\" height=\"50\" fill=\"#C8102E\" />""",
        """<rect x=\"575\" y=\"0\" width=\"50\" height=\"600\" fill=\"#C8102E\" />"""
    ]

    # Combine elements into SVG content
    svg_content = svg_header + "\n".join(elements) + svg_footer

    # Write to file
    with open(file_path, "w") as svg_file:
        svg_file.write(svg_content)

# Specify the output file path
output_file = "union_jack.svg"
create_union_jack_svg(output_file)

print(f"SVG file '{output_file}' created successfully!")
