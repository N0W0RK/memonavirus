# File to find Infectors that have not been infected
# results stored in infection_roots.txt
# 3.4.20

import pandas
import glob

all_files = glob.glob('../../data/memes_infections*.log')


def sort_files(files):
    key = lambda name: name[28:] if name[28:30].isdigit() else "4" + name[28:]
    return sorted(files, key=key)[1:]


all_files = sort_files(all_files)

infected = ["u/woodendoors7"]

get_file = lambda fname: pandas.read_csv(
    fname,
    sep='\t',
    header=None,
    names=['post_dt',
           'infectee_name',
           'infectee_post_id',
           'infector_name',
           'infector_post_id',
           'comment_or_submission']
)

dedupe_file = open("deduped.log", "w")

for file in all_files:

    print(file)
    df = get_file(file)
    df.sort_values('post_dt', inplace=True)

    for index, row in df.iterrows():

        if not row.infectee_name in infected:

            dedupe_file.write(row.post_dt + ";" + row.infectee_name + ";" + row.infectee_post_id + ";" + row.infector_name + ";" + row.infector_post_id + ";" + row.comment_or_submission + "\n")


dedupe_file.close()
