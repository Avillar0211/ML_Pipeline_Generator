import pandas

def read(Filename):
    with open(Filename, 'r', encoding="utf-8") as f:
        dfs = pandas.read_html(f.read())
    Frame =  pandas.DataFrame(dfs[0])
    return Frame
    