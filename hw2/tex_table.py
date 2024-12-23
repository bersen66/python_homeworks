

def table_body(src):
    for l_column, r_column in src:
        yield f'\t{l_column} & {r_column}'


def with_hline(func):
    def wrapper(*args, **kwargs):
        yield "\t\\hline"
        for line in func(*args, **kwargs):
            yield line + " \\\\ \\hline "
    return wrapper


def with_centering(func):
    def wrapper(*args, **kwargs):
        yield "\t\\centering"
        for line in func(*args, **kwargs):
            yield line
    return wrapper


def with_caption(caption, func):
    def wrapper(*args, **kwargs):
        yield f"\t\\caption{{{caption}}}"
        for line in func(*args, **kwargs):
            yield line
    return wrapper


def with_tabular(pattern, func):
    def wrapper(*args, **kwargs):
        yield f"\t\\begin{{tabular}}{{{pattern}}}"
        for line in func(*args, **kwargs):
            yield f'\t{line}'
        yield f"\t\\end{{tabular}}"
    return wrapper



def make_table(func):
    def wrapper(*args, **kwargs):
        yield f"\\begin{{table}}[h!]"
        for line in func(*args, **kwargs):
            yield line
        yield f"\\end{{table}}"
    return wrapper


def make_document(func):
    def wrapper(*args, **kwargs):
        yield f"\\documentclass{{article}}"
        yield f"\\begin{{document}}"
        for line in func(*args, **kwargs):
            yield f"\t{line}"
        yield f"\\end{{document}}"
    return wrapper
