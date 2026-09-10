# Music Library System

A Python `Song` class that models individual songs while also tracking
library-wide statistics — total song count, unique genres and artists,
and per-genre/per-artist song tallies. Built as part of a lab exploring
class attributes and class methods in Python.

## Description

This project simulates the core of a music streaming service's song
catalog. Each `Song` object stores its own `name`, `artist`, and `genre`,
while class-level attributes and methods automatically maintain
aggregate insights across every song ever created — useful for features
like recommendations and analytics.

## Features

- Create individual `Song` objects with a name, artist, and genre
- Automatically track the total number of songs created
- Maintain a list of all unique genres and artists
- Count how many songs exist per genre and per artist

## Installation

Clone the repo and install dependencies with Pipenv:

\`\`\`bash
git clone <your-repo-url>
cd python-music-library-system-lab
pipenv install
pipenv shell
\`\`\`

## Usage

\`\`\`python
from song import Song

song1 = Song("99 Problems", "Jay Z", "Rap")
song2 = Song("Halo", "Beyonce", "Pop")

print(Song.count)          # 2
print(Song.genres)         # ['Rap', 'Pop']
print(Song.artists)        # ['Jay Z', 'Beyonce']
print(Song.genre_count)    # {'Rap': 1, 'Pop': 1}
print(Song.artist_count)   # {'Jay Z': 1, 'Beyonce': 1}
\`\`\`

## Running Tests

\`\`\`bash
cd lib
pytest testing/song_test.py -v
\`\`\`

![Passing tests](screenshot.png)

## Tech Stack

- Python 3
- pytest

## Contributing

1. Fork the repo
2. Create a feature branch (\`git checkout -b feature-name\`)
3. Commit your changes
4. Push and open a pull request

## Authors

- Your Name

## License

This project is licensed for educational purposes as part of a coding lab.