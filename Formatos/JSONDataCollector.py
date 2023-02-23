import pandas

def read(Filename):
    aux = pandas.read_json(Filename)
    Frame =  pandas.DataFrame(aux)
    return Frame
    