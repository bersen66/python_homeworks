import mytex as mt


def create_artifact_table(path):

    generator = mt.simple_document(mt.make_table(mt.with_centering(mt.with_caption("MyTable", mt.with_tabular("|c|c|", mt.with_hline(mt.table_body))))))

    TableBody = [
        (1, 2),
        ("Hello", "world"),
        ("Floppa", "the big cat")
    ]

    with open(path, 'w') as file:
        for line in generator(TableBody):
            file.writelines(f"{line}\n")


def create_artifact_with_image(path):
    doc = mt.complex_document(mt.enable_images("./images/"), mt.inclue_graphics("image.png"))
    with open(path, 'w') as file:
        for line in doc:
            file.writelines(f"{line}\n")


if __name__ == "__main__":
    create_artifact_table("artifacts/doc_with_table.tex")
    create_artifact_with_image("artifacts/doc_with_image.tex")
