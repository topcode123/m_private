import pickle
import json


def load_spin():
    dataspin = None
    with open("dataspin.p", "rb") as file:
        dataspin = pickle.load(file)


    # with open("./data_spin/DATA-FULL.txt") as raw_data_spin:
    # # with open("./data_spin/test_data.txt") as raw_data_spin:
    #     lines = [line.rstrip('\n') for line in raw_data_spin]

    # new_spin_data = dataspin

    # for line in lines:
    #     line = line.replace("{", "", 1)
    #     line = line.replace("}", "", 1)

    #     list_same_words = line.split("|")
    #     for word in list_same_words:
    #         if word not in new_spin_data:
    #             new_spin_data[word] = list(filter(lambda other_word: (other_word != word), list_same_words))

        
    # print(new_spin_data)
    # with open("new_dataspin.p", "wb") as new_pickle:
    #     pickle.dump(new_spin_data, new_pickle, protocol=pickle.HIGHEST_PROTOCOL)
    
    # todo write json to file text
    json_dataspin = json.dumps(dataspin, indent=4, ensure_ascii=False)
    
    with open("dataspin.json", "w") as outfile:
        outfile.write(json_dataspin)    


load_spin()