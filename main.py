import csv
from pathlib import Path
import re

def remove_emojis(data):
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', data)

# iterate over dirs
pathlist = Path("input").glob('**/*.csv')
for path in pathlist:
    # because path is object not string
    path_in_str = str(path)

    with open(path_in_str, 'r') as rf:
        reader = csv.reader(rf, delimiter=',')

        with open(f"output/{path_in_str[5:]}", 'w') as temp_file:
            writer = csv.writer(temp_file)
            for row in reader:
                for index, column in enumerate(row):
                    row[index] = remove_emojis(column)
                writer.writerow(row)
