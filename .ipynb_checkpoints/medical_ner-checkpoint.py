# # -*- coding: utf-8 -*-
# """Medical_NER.ipynb

# Automatically generated by Colaboratory.

# Original file is located at
#     https://colab.research.google.com/drive/1ga0nijQu9MALKGRM9IK17q00IZ8iRRV4
# """

# # Commented out IPython magic to ensure Python compatibility.
# from google.colab import drive
# drive.mount('/content/drive')
# # %cd drive
# # %cd "My Drive"
# # %cd "Colab Notebooks"
# # /content/drive/My Drive/Colab Notebooks
# # %cd "Dr.Kojima_JOB"

# !pip install bioc

# import os
# files = os.listdir("data")

# val_name = []
# for a_file in files:
#   print(a_file)
#   with open("data/"+a_file, 'r') as fp:
#     dynmc_name = a_file.replace(".xml","")
#     locals()[dynmc_name] = bioc.load(fp)
#     val_name.append(dynmc_name)

# """# BioCCollectionオブジェクト調査"""

# import bioc

# # bioc.bioc.BioCCollection型
# with open("data/aimed_bioc.xml", 'r') as fp:
#   anem_bioc = bioc.load(fp)

# # # bioc.biocxml.decoder.BioCXMLDocumentReader型
# # reader = bioc.BioCXMLDocumentReader("data/anem_bioc.xml")

# # # bioc.bioc.BioCDocument型
# # for document in reader:
# #   print(document)
# #   print(type(document))

# for key, value in anem_bioc.__dict__.items():
#   print(key, ':', value,type(value))

# anem_bioc.__str__()

# document = anem_bioc.__dict__["documents"]

# for key, value in document[0].__dict__.items():
#   print(key, ':', value,type(value))

# type(document.__dict__["passages"][0])

# a_BioCPassage_list = document.__dict__["passages"]

# for key, value in a_BioCPassage_list[0].__dict__.items():
#   print(key, ':', value,type(value))

# a_BioCAnnotation_list = a_BioCPassage_list[0].__dict__["annotations"]
# a_BioCRelations_list = a_BioCPassage_list[0].__dict__["relations"]

# for key, value in a_BioCAnnotation_list[0].__dict__.items():
#   print(key, ':', value,type(value))

# for key, value in a_BioCRelations_list[0].__dict__.items():
#   print(key, ':', value,type(value))

import itertools
import csv
import os
import bioc

def get_AllData(filename):
  # bioc.biocxml.decoder.BioCXMLDocumentReader型
  all_data = []
  reader = bioc.BioCXMLDocumentReader("data/"+filename+".xml")

  # bioc.bioc.BioCDocument型
  for document in reader:
    for key, value in document.__dict__.items():
      document_id = document.__dict__["id"]

      for passage in document.__dict__["passages"]:
        text = passage.__dict__["text"]

        ann_ids_texts = []
        for annotation in passage.__dict__["annotations"]:
          ann_id = annotation.__dict__["id"]
          ann_text = annotation.__dict__["text"]
          ann_ids_texts.append([ann_id,ann_text])
        
        for pair in itertools.combinations(ann_ids_texts, 2):
          a,b = list(pair)
          match = False

          if a[0] == b[0]:
            match = True
            print("True")

          row = [document_id,text,a[0],b[0],a[1],b[1],match]

          all_data.append(row)

  return all_data



xml_files = os.listdir("data")
print(xml_files)

files = []
for a_xml_file in xml_files:
  print(a_xml_file)
  with open("data\\"+a_xml_file, 'r') as fp:
    dynmc_name = a_xml_file.replace(".xml","")
    locals()[dynmc_name] = bioc.load(fp)
    files.append(dynmc_name)


for filename in files:
  print(filename)
  all_data = get_AllData(filename)

  with open("data_NEW\\"+filename+'.csv', 'w', newline='') as f:
    writer = csv.writer(f,delimiter=',')
    writer.writerows(all_data)
    print("save!")
