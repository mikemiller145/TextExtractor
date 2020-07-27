import spacy
from collections import Counter
from .models import Data

nlp = spacy.load("en_core_web_sm")


# custom file that analyzes the file uploaded

# parse through text file and extracts people names
# counting how many times they were mentioned in text
def parse_through_file(file):
    content = file.read()
    content = content.decode()
    content = content.replace('\n', ' ').replace('\r', '')
    content = nlp(content)
    names = []
    # looks for all names in text
    for i in range(len(content.ents)):
        if content.ents[i].label_ == 'PERSON' and str(content.ents[i]).istitle():
            names.append(str(content.ents[i]))
    # find most frequently used names in text
    word_freq = Counter(names)
    common_words = word_freq.most_common(10)
    return common_words


# adds name list and frequency to Data table
def create_data(pk, common_words):
    wordlist = [lis[0] for lis in common_words]
    count = [lis[1] for lis in common_words]

    for i in range(len(wordlist)):
        new_data = Data(word=wordlist[i], count=count[i], upload_id=pk)
        new_data.save()
