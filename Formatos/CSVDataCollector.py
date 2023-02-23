import pandas

def read(Filename):
    aux = pandas.read_csv(Filename)
    Frame =  pandas.DataFrame(aux)
    return Frame
    
    