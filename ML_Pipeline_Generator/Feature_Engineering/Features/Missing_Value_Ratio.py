from ML_Pipeline_Generator.Feature_Engineering.Features.Single_DataFeature import SingleDataFeature

class Missing_Value_Ratio(SingleDataFeature):

    def __init__(self):
        super().__init__()

    def engineering(self, dFrame):
        ratio = dFrame.isnull().sum()/len(dFrame)*100
        print('Missing Value Ratio: ')
        print(ratio)
        return dFrame
    