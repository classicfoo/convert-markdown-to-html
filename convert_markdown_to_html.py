import markdown

# Input and output file paths
input_file = "input.md"
output_file = "output.html"

# Read the Markdown content from the input file
with open(input_file, "r", encoding="utf-8") as file:
    markdown_content = file.read()

# Convert Markdown to HTML
html_content = markdown.markdown(
    markdown_content,
    extensions=["markdown.extensions.tables", "markdown.extensions.fenced_code"],
)

# Write the HTML content to the output file
with open(output_file, "w", encoding="utf-8") as file:
    file.write(html_content)

print("Conversion complete. HTML file saved as", output_file)
