import matplotlib.pyplot as plt

def boring_stats(group_25_song_database, song_name, genre):
    """
        Show a scatter plot for 'Total Beats' vs 'Boringness' for the entered genre.

        Parameters
        =======================
        song_database (pd.DataFrame) : pandas DataFrame of song features
        song_name (str) : user chosen song
        song_genre (str) : user chosen genre

        No return value.
    """
    #Create a sub array based on user entered genre
    sub_genre_df = group_25_song_database.loc[group_25_song_database["genre"] == genre]
   
    #Sort data based on total beats
    sub_genre_df.sort_values("total_beats")

    #Single entry from data just the entered song
    song_values = sub_genre_df.loc[song_name][:]

    #Create scatter plot of boringness vs total beats
    plt.scatter(sub_genre_df.boringness, sub_genre_df.total_beats , s=5, c="#1db954", marker="o", label ="All Data")
    plt.scatter(song_values.boringness, song_values.total_beats, s=10, c="#cf0a2c", marker="s", label = song_name)
    plt.title("Total Beats vs Boringness", fontweight="bold", fontsize=20)
    plt.xlabel("Boringness")
    plt.ylabel("Total Beats")
    plt.legend(loc="upper left")
    plt.legend()
    plt.show()


def find_closest_target_value(boringness_stats, user_value):
    """
        In a given list of float, find the closest to the target value (that is not the same value).

        Parameters
        =======================
        boringness_stats (list[float]) : list of boringsness statistics
        user_value (float) : user boringsness value

        Returns (float) : closest value to target/user value
    """
    closest = None
    min_diff = float('inf')

    for num in boringness_stats:
        if num != user_value:
            diff = abs(num - user_value)
            if diff < min_diff:
                min_diff = diff
                closest = num

    return closest


def suggest_song(group_25_song_database, song_name, genre):
    """
        Suggests a song based on the closeness of boringness value compared to other songs in the same genre.

        Parameters
        =======================
        song_database (pd.DataFrame) : pandas DataFrame of song features
        song_name (str) : user chosen song
        song_genre (str) : user chosen genre

        Returns (str) : song suggestion
    """
    sub_genre_df = group_25_song_database.loc[group_25_song_database["genre"] == genre]
    tmp_df = sub_genre_df.loc[:, ["boringness"]]
    boringness_list = tmp_df["boringness"].values.tolist()
    
    user_df = group_25_song_database.loc[song_name]
    user_df = user_df[user_df.genre == genre]

    closest_boringness_value = find_closest_target_value(boringness_list, user_df.boringness.values[0])
    suggested_df = sub_genre_df[sub_genre_df.boringness == closest_boringness_value]

    song_name = suggested_df.index.get_level_values(0).to_list()
    
    if song_name:
        return song_name[0]
    else:
        return "No song suggestion found."