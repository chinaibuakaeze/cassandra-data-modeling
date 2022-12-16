import os, glob, csv, pandas as pd

def get_file_paths(data):
    #Walk through the events_data directory and get the absolute path of a list of files
    files_list = []
    files = os.walk(data)
    for root, dir, file in files:
        file = glob.glob(os.path.join(root,'*'))
        for f in file:
            files_list.append(os.path.abspath(f))
    return files_list

def write_file():
    #Create the csv file and write the header of the file
    header = ['artist', 'first_name', 'gender', 'item_number', 'last_name', 'length', 
    'level', 'location', 'sessionId', 'song_title', 'userId']
    with open("new_events_data.csv", 'w') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(header)


def read_file(files_list):
    #Read through the list of file paths and write into the new csv file
    for file in files_list:
        df = pd.read_csv(file)
        for index, row in df.iterrows():
            row_list = [row.artist, row.firstName, row.gender, row.itemInSession, row.lastName, row.length, 
            row.level, row.location, row.sessionId, row.song, row.userId]
            with open("new_events_data.csv", "a") as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(row_list)


def main():
    files_list = get_file_paths('event_data')
    write_file()
    read_file(files_list)

main()