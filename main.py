"""
    ENSF 592 P23

    Group 25 - Project

    A terminal-based application for computing and printing statistics

    Usage : python main.py
            
    Notes : Expecting xlsx file in the Data folder to be present
            Pandas, Numpy, Matplotlib,Seaborn libraries need to be installed
            The following python files need to be present: user_input, show_general_stats, boring_stats

    Created by Braden and Christian 
"""


#Import libraries and functions
from user_input import *
from show_general_stats import GeneralStats
from boring_stats import *
import pandas as pd
import warnings


###########################################################
#
#            Main Loop
#
##########################################################


warnings.filterwarnings("ignore")


def main():
    datasets = []
    list_of_indexes = ["song_name", "key", "mode", "time_signature"]
    
    welcome_user()

    try:
        for i_index in range(1,4):
            tmp_data = []
            
            for j_index in range(1,3):
                # read xlsx files
                fragment_data = pd.read_excel(f"./Data/dataset{i_index}-{j_index}.xlsx")
                tmp_data.append(fragment_data)
            
            # merge data
            dataset = pd.merge(tmp_data[0], tmp_data[1], left_index=True, right_index=True)
            
            # clean DataFrame using masking
            dataset.drop_duplicates()
            dataset["song_name"] = dataset["song_name"].str.replace(r'[^\x00-\x7F]+', '')
            dataset = dataset[dataset.song_name.str.match("[a-zA-Z0-9]+") & dataset.song_name.notna()]
            dataset = dataset[~dataset.song_name.str.match("[0-9]+\s[0-9]+")]
            dataset = dataset[~dataset.song_name.str.match("[0-9]+:[0-9]+")]
            datasets.append(dataset)
    except FileNotFoundError as e:
        print(f"{type(e)}\nExiting with error.")
        exit()
    
    # concatenate DataFrames
    df = [datasets[i_index].set_index(list_of_indexes) for i_index in range(len(datasets))]
    group_25_song_database = pd.concat([df[0], df[1], df[2]]).sort_index()
    genre_list = list(group_25_song_database.genre.unique())

    #ask for user song genre
    genre = get_genre_from_user(genre_list)

    #Create a sub array based on user entered genre 
    sub_genre_df = group_25_song_database.loc[group_25_song_database["genre"] == genre]
    song_list = sub_genre_df.index.get_level_values(0)

    #ask for user song name
    song_name = get_song_name_from_user(song_list, genre)
    
    # TotalBeats = Tempo(BPM) * (Durations * 0.001)
    group_25_song_database["total_beats"] = ((group_25_song_database["tempo"] * group_25_song_database["duration_ms"]*0.001)/60).astype(int)
    
    # Boringness = loudness + tempo + (energy*100) + (danceability*100)
    group_25_song_database["boringness"] = (group_25_song_database["loudness"] + group_25_song_database["tempo"] + (group_25_song_database["energy"]*100) + (group_25_song_database["danceability"]*100))
    
    # GenerealStats object to display dataset statistics
    overall_stats = GeneralStats(group_25_song_database, song_name, genre, genre_list)
    
    explain_values("bar graph", genre)
    for label in overall_stats.described_values:
        overall_stats.show_bar_graph(overall_stats.described_values[label], label)
    
    explain_values("histogram", genre)
    overall_stats.show_histogram()

    explain_values("distributions", genre)
    overall_stats.show_distributions()

    explain_values("pie chart", genre)
    overall_stats.show_pie_chart()
    
    explain_values("scatter", genre)
    boring_stats(group_25_song_database, song_name, genre)

    # Columns are a cut from the tempo column with a range of 40
    # Index is the genre
    # Values come from the mean of duration_ms
    explain_values("pivot", genre)
    print("\nPivot Table\n" + "="*90)
    tempo = pd.cut(group_25_song_database["tempo"], [40,80,120,160,200,240])
    print(group_25_song_database.pivot_table("duration_ms",index="genre",columns=tempo))
    
    print("\nDescribe Table\n" + "="*120 + "\n")
    print(group_25_song_database.describe())

    suggested_song = suggest_song(group_25_song_database, song_name, genre)
    explain_values("suggested song", genre, song_name, suggested_song)

    print("\nExporting new DataFrame to Excel ☕\n")
    file_name = "./finaloutput.xlsx"
    group_25_song_database.to_excel(file_name)

    goodbye_user()


if __name__ == "__main__":
    main()