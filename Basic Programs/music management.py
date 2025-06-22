def add_album(library, album_info):
    artist, title, year, songs = album_info
    library[title] = (artist, year, songs)
    return library

def create_playlist(library, song_selections):
    playlist = []
    for album_title, song in song_selections:
        if album_title in library:
            if song in library[album_title][2]:  # songs list is at index 2
                playlist.append(song)
    return playlist

def add_song_to_album(library, album_title, new_song):
    if album_title in library:
        artist, year, songs = library[album_title]
        if new_song not in songs:
            songs.append(new_song)
        library[album_title] = (artist, year, songs)
    return library

def remove_song_from_playlist(playlist, song):
    if song in playlist:
        playlist.remove(song)
    return playlist

def view_library(library):
    for album_title, info in library.items():
        artist, year, songs = info
        print(f"\nAlbum: {album_title}\nArtist: {artist}\nYear: {year}\nSongs: {songs}")

def view_playlist(playlist):
    print("\nCurrent Playlist:")
    for i, song in enumerate(playlist, 1):
        print(f"{i}. {song}")

# Main Menu
def main():
    library = {}
    playlist = []

    while True:
        print("\n----- Music Library Menu -----")
        print("1. Add a new album")
        print("2. Create a playlist")
        print("3. Add a song to an album")
        print("4. Remove a song from playlist")
        print("5. View music library")
        print("6. View playlist")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            artist = input("Enter artist name: ")
            title = input("Enter album title: ")
            year = int(input("Enter release year: "))
            songs = input("Enter song titles separated by commas: ").split(",")
            songs = [s.strip() for s in songs]
            album_info = (artist, title, year, songs)
            library = add_album(library, album_info)
            print("Album added successfully.")

        elif choice == '2':
            song_selections = []
            n = int(input("How many songs do you want to add to the playlist? "))
            for _ in range(n):
                album = input("Enter album title: ")
                song = input("Enter song name: ")
                song_selections.append((album, song))
            playlist = create_playlist(library, song_selections)
            print("Playlist created successfully.")

        elif choice == '3':
            album_title = input("Enter the album title: ")
            new_song = input("Enter the new song to add: ")
            library = add_song_to_album(library, album_title, new_song)
            print("Song added to album.")

        elif choice == '4':
            song = input("Enter the song to remove from playlist: ")
            playlist = remove_song_from_playlist(playlist, song)
            print("Song removed from playlist.")

        elif choice == '5':
            view_library(library)

        elif choice == '6':
            view_playlist(playlist)

        elif choice == '7':
            print("Exiting Music Library. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the program
main()
