import csv

def csv_to_markdown(input_file, output_file):
    with open(input_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        with open(output_file, mode='w', encoding='utf-8') as markdown_file:
            for row in reader:
                card = row['Card']
                strain_or_medium = row['strain/medium']
                description = row['Description']
                visual_concept = row['visual concept']
                symbolism = row['Symbolism']
                notes = row['Notes']

                # Determine if it is a strain or a medium based on the card type
                if "King" in card or "Queen" in card or "Knight" in card or "Page" in card:
                    strain_or_medium_header = "### Medium:\n"
                else:
                    strain_or_medium_header = "### Strain:\n"

                # Write the formatted content to the markdown file
                markdown_file.write(f"## {card}\n\n")
                markdown_file.write(strain_or_medium_header)
                markdown_file.write(f"{strain_or_medium}\n\n")
                markdown_file.write("### Visual Concept\n")
                markdown_file.write(f"{visual_concept}\n\n")
                markdown_file.write("### Symbolism\n")
                markdown_file.write(f"{symbolism}\n\n")
                if notes.strip():  # Only write notes if there are any
                    markdown_file.write("#### Notes\n")
                    markdown_file.write(f"{notes}\n\n")

if __name__ == "__main__":
    csv_to_markdown('input/decision_content.csv', 'output/concepts.md')