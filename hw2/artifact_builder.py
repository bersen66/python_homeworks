from mytex import *


def create_artifact_table(path):

    generator = simple_document(make_table(with_centering(with_caption("MyTable", with_tabular("|c|c|", with_hline(table_body))))))

    TableBody = [
        (1, 2),
        ("Hello", "world"),
        ("Floppa", "the big cat")
    ]

    with open(path, 'w') as file:
        for line in generator(TableBody):
            file.writelines(f"{line}\n")


def create_artifact_with_image(path):
    doc = complex_document(enable_images("./images/"), inclue_graphics("image.png"))
    with open(path, 'w') as file:
        for line in doc:
            file.writelines(f"{line}\n")




if __name__ == "__main__":
    create_artifact_table("artifacts/doc_with_table.tex")
    create_artifact_with_image("artifacts/doc_with_image.tex")
