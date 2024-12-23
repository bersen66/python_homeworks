from tex_table import *

if __name__ == "__main__":
    generator = make_document(make_table(with_centering(with_caption("MyTable", with_tabular("|c|c|", with_hline(table_body))))))

    table_body = [
        (1, 2),
        ("Hello", "world"),
        ("Floppa", "the big cat")
    ]

    with open("table.tex", 'w') as file:
        for line in generator(table_body):
            file.writelines(f"{line}\n")
