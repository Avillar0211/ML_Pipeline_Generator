import pandas

def read(Filename):
    aux = pandas.read_excel(Filename)
    Frame =  pandas.DataFrame(aux)
    return Frame
    