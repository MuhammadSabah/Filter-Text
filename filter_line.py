import re


def filter_sentences(lines):
    """
    Filter out lines that are empty, consist only of symbols, or are single characters (except meaningful letters).
    """
    filtered_lines = []
    for line in lines:
        stripped_line = line.strip()
        # Check if the line is meaningful (more than just punctuation or symbols)
        # Keep the line if it has alphanumeric characters or Arabic letters
        if stripped_line and (
                len(stripped_line) == 1 and re.match(r'[a-zA-Z\u0600-\u06FF]', stripped_line) or
                re.search(r'[a-zA-Z0-9\u0600-\u06FF]', stripped_line)
        ):
            filtered_lines.append(stripped_line)
    return filtered_lines


def write_lines_to_file(lines, output_file):
    """
    Write the filtered lines to a file.
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')


# Read the text corpus
with open('text-files/input/cleaned.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Filter out non-meaningful lines
filtered_lines = filter_sentences(lines)

# Write each filtered line to a new file
write_lines_to_file(filtered_lines, 'text-files/output/output.txt')
