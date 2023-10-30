import argparse
import os
import markdown

# Function to convert Markdown to HTML
def convert_md_to_html(input_file):
    # Read the Markdown content from the input file
    with open(input_file, "r", encoding="utf-8") as file:
        markdown_content = file.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(
        markdown_content,
        extensions=["markdown.extensions.tables", "markdown.extensions.fenced_code"],
    )

    # Determine the output filename (replace .md with .html)
    output_file = input_file.replace(".md", ".html")

    # Write the HTML content to the output file
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(html_content)

    print("Conversion complete. HTML file saved as", output_file)

def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="Convert Markdown to HTML")

    # Add a positional argument for the input file
    parser.add_argument("input_file", help="Input Markdown file to convert")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Check if the input file exists
    if not os.path.exists(args.input_file):
        print("Error: Input file does not exist.")
        return

    # Check if the input file has a .md extension
    if not args.input_file.lower().endswith(".md"):
        print("Error: Input file is not a Markdown file (.md).")
        return

    # Call the conversion function
    convert_md_to_html(args.input_file)

if __name__ == "__main__":
    main()
