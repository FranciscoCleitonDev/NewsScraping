import textwrap

def format_text(texto, width=49):
    return "\n".join(textwrap.wrap(texto, width))

def filter_results(txt):
    return txt.split(';')[0].strip()
