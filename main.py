import input_outputimport process_textmovie_text_file = "the-full-bee-movie-script.txt"if __name__ == '__main__':    movie_text = input_output.get_text_from_file(movie_text_file)    action_value = 0    keywords = ""    word_occurrence = ""    while action_value != 4:        print("1: Count word\n2: Show keywords graph\n3: Save performed actions data to file\n4: Exit")        print("Write number between 1 and 4:")        action_value = int(input())        if action_value < 1:            print("Wrong number")        elif action_value == 1:            print("Enter word you want to count:")            word = input()            word_occurrence = process_text.count_word(word, movie_text)        elif action_value == 2:            keywords = process_text.create_graph(movie_text)        elif action_value == 3:            print("Write the name of the movie:")            movie_name = input()            text = "MOVIE OVERVIEW:\n" + word_occurrence + "\n" + keywords            process_text.save_data(movie_name, text)        elif action_value > 4:            print("Wrong number")    print("EXIT")