#!/usr/bin/python

from mytex import *
import argparse

def main(image_dir, image_name, output_file):
    TableBody = [
        (1, 2),
        ("Hello", "world"),
        ("Floppa", "the big cat")
    ]

    table = make_table(with_centering(with_caption("MyTable", with_tabular("|c|c|", with_hline(table_body)))))

    doc = complex_document(
        enable_images(image_dir),
        inclue_graphics(image_name).then(table, TableBody)
    )


    with open(output_file, 'w') as file:
        for line in doc:
            file.writelines(f"{line}\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a LaTeX document with an image and a table.')
    parser.add_argument('image_dir', type=str, help='Directory containing the image.')
    parser.add_argument('image_name', type=str, help='Name of the image file (including extension).')
    parser.add_argument('output_file', type=str, help='Name of the output LaTeX file.')

    # Parse the arguments
    args = parser.parse_args()

    # Call the main function with parsed arguments
    main(args.image_dir, args.image_name, args.output_file)
