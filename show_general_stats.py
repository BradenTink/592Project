import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


class GeneralStats:
    """
        GeneralStats shows the general statistics for the entire dataset using graphs.

        ...

        Parameters
        =======================
        song_database (pd.DataFrame) : pandas DataFrame of song features
        song_name (str) : user chosen song
        song_genre (str) : user chosen genre
        genre_list (list[str]) : list of genres

        Attributes
        =======================
        song_database (pd.DataFrame) : pandas DataFrame of song features
        song_name (str) : user chosen song
        song_genre (str) : user chosen genre
        genre_list (list[str]) : list of genres

        column_names (list[str]) : song attribute from xlsx file
        described_values (dict{}) : contains mean, max, min values from the entire dataset dataset
        user_values (dict{}) : contains song attributes such energy, danceability ,liveness etc ...
    """

    def __init__(self, song_database, song_name, song_genre, genre_list):
        self.song_database = song_database
        self.song_name = song_name
        self.song_genre = song_genre
        self.genre_list = genre_list

        self.column_names = list(self.song_database.columns)
        self.column_names.remove("genre")
        self.described_values = self.get_described_values(["mean", "max", "min"])
        self.user_values = self.get_user_values()


    def get_described_values(self, described_indexes:list[str]):
        """
            Extracts values from the pandas describe() method.

            Parameters
            =======================
            described_indexes (list[str]) : aggregate labels such as min, max, mean

            Returns (dict{}) : aggregate values for each song attribute
        """
        described_values = {}
        described_database = self.song_database.describe()

        for label in described_indexes:
            described_values[label] = {}
            for column_name in self.column_names:
                characteristic = described_database[column_name]
                described_values[label][column_name] = characteristic[characteristic.index == label][0]

        return described_values


    def get_user_values(self):
        """
            Extracts all song attributes values user chosen song.

            No parameters.

            Returns (dict{}) : values for each song attribute
        """
        user_df = self.song_database.loc[self.song_name]
        user_df = user_df[user_df.genre == self.song_genre][:1]
        user_val = {}

        for column_name in self.column_names:
            user_val[column_name] = float(user_df.loc[:, column_name].values)

        return user_val


    def show_bar_graph(self, described_value, label):
        """
            Displays the bar graph for all song attribute values between 0 and 1.

            Parameters
            =======================
            described_value (dict{}) : contains all values for song attribute
            label (str) : label for aggregate value such as min, max, and mean

            Returns (dict{}) : values for each song attribute
        """
        unwanted_keys = ["tempo"]
        barWidth = 0.25
        bar_user = {characteristic:value for characteristic, value in self.user_values.items()}
        bar_data = {characteristic:value for characteristic, value in described_value.items()}
        big_values = [characteristic for characteristic, value in described_value.items() if (value > 1 or value < 0) and characteristic not in unwanted_keys]
        all_characteristics = list(bar_user.keys())

        fig, ax = plt.subplots(figsize =(10, 10))

        for characteristic in all_characteristics:
            if characteristic in unwanted_keys or characteristic in big_values:
                bar_user.pop(characteristic)
                bar_data.pop(characteristic)

        bar_user_values = list(bar_user.values())
        x_tick_labels = list(bar_user.keys())
        bar_data_values = list(bar_data.values())
        br1 = np.arange(len(bar_user))
        br2 = [x + barWidth for x in br1]

        # bar graphs
        ax.bar(br1, bar_data_values, color ="#cf0a2c", width = barWidth, edgecolor ="grey", label ="data")
        ax.bar(br2, bar_user_values, color = "#1db954", width = barWidth, edgecolor ="grey", label ="user")

        # graph aesthetics
        ax.set_xlabel("Audio Features", fontweight ="bold", fontsize = 15)
        ax.set_ylabel("Weighted Value", fontweight ="bold", fontsize = 15)
        ax.set_xticks([r + barWidth for r in range(len(x_tick_labels))])
        ax.set_xticklabels(x_tick_labels, rotation=65)
        ax.set_title(f"{self.song_name} Attributes Against Dataset - ({label})", fontweight ="bold", fontsize = 20)

        plt.legend()
        plt.show()


    def show_histogram(self):
        """
            Displays the histogram for all song attributes.

            No parameters and return value.
        """
        self.song_database.hist(figsize=(12, 10),
                            grid=False,
                            bins=20,
                            color='#1db954',
                            ec='#121212',
                            legend=True)
        
        plt.show()
        

    def show_distributions(self):
        """
            Displays the curve distributions for all song attributes.

            No parameters and return value.
        """
        x_axis = self.song_database.loc[:, :]
        x_axis = x_axis.drop(columns="genre")
        graph_count = 0
        plt.figure(figsize=(15, 12))

        for graph in x_axis.columns:
            plt.subplot(4, 4, graph_count+1)
            sns.distplot(x_axis[graph], color='#1db954', hist_kws=dict(edgecolor="#121212", linewidth=1))
            plt.xlabel(graph, fontsize=10)
            graph_count +=1

        plt.show()

    def show_pie_chart(self):
        """
            Displays pie chart for all song genre count.

            No parameters and return value.
        """

        #expecting only 8 genres
        colors = ["#1db594", "#ff59c7", "#a0a1cb", "#f31511", "#7e93ba", "#5d3fd3", "#d1ad00", "#e5e1e1"]
        
        genre_grouped = self.song_database.groupby(["genre"])["genre"].count()
        pie_labels, pie_values = genre_grouped.index, genre_grouped.values
        pie_labels = list(pie_labels)
        explode = [0 for _ in range(len(self.genre_list))]
        user_song_genre_index = pie_labels.index(self.song_genre)
        explode[user_song_genre_index] = 0.1
        
        genre_grouped = np.array(self.song_database.groupby(["genre"])["genre"].count())
        plt.pie(pie_values, labels=pie_labels, startangle=0, autopct='%1.2f%%', shadow=True, colors=colors, explode=explode)
        plt.title("Database Genre Pie Chart", fontsize=20, fontweight="bold", color="#121212")

        plt.show()