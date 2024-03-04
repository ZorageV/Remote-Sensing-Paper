import splitfolders
input_folder="C:/Zorage/ML/Research/Remote sensing paper/Datasets/EuroSAT/"

splitfolders.ratio(input_folder,output="C:/Zorage/ML/Research/Remote sensing paper/Final Dataset",
                  seed=101,ratio=(.8,.1,.1),
                  group_prefix=None)