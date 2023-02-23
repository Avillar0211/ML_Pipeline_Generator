import pandas

def read(Filename):
    aux = pandas.read_xml(Filename)
    Frame =  pandas.DataFrame(aux)
    return Frame
    