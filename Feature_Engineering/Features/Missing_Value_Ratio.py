from Feature_Engineering.Features.Single_Data_Feature import single_data_feature

class Missing_Value_Ratio(single_data_feature):

    def __init__(self):
        super().__init__()

    def engineering(self, dFrame):
        ratio = dFrame.isnull().sum()/len(dFrame)*100
        print('Missing Value Ratio: ')
        print(ratio)
        return dFrame
    