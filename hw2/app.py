from mytex import *


TableBody = [
    (1, 2),
    ("Hello", "world"),
    ("Floppa", "the big cat")
]

table = make_table(with_centering(with_caption("MyTable", with_tabular("|c|c|", with_hline(table_body)))))

doc = complex_document(
    enable_images("./images/"),
    inclue_graphics("image.png").then(table, TableBody)
)


with open("artifacts/doc.tex", 'w') as file:
    for line in doc:
        file.writelines(f"{line}\n")
