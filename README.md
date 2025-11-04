# Cover Downloader

A comprehensive application for automatically downloading game and movie covers. Also includes features for editing downloaded covers in PDF format and managing text files.

**Tags:** `cover-downloader` `game-covers` `movie-covers` `steam-api` `twitch-api` `epic-games-api` `tmdb-api` `omdb-api` `pdf-generator` `python` `pyside6` `qt` `gui` `automation` `media-management`

## Features

### Game Covers
- Automatic game cover downloading using Steam, Twitch, and Epic Games APIs
- Automatic recognition and matching of Turkish game names
- Automatic detection of duplicate covers
- Reporting of games that couldn't be downloaded
- Supported platforms:
  - Steam
  - Twitch
  - Epic Games Store

### Movie Covers
- Automatic movie cover downloading using OMDb and TMDB APIs
- Automatic replacement of Turkish movie names with English equivalents
- Automatic detection of duplicate covers
- Reporting of movies that couldn't be downloaded
- Supported APIs:
  - OMDb API
  - TMDB API

### PDF Creator
- Edit downloaded covers in PDF format
- Automatic page layout and sizing
- Multiple page support
- Image optimization
- Customizable page sizes
- Adjustable spacing between covers

### Text Editor
- Edit text files
- Alphabetical sorting
- Remove duplicate lines
- UTF-8 encoding support
- Real-time editing and saving

## Installation

1. Install Python 3.8 or higher
2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Downloading Game Covers
1. Navigate to the "Games" tab
2. Click the "Select Game List" button
3. Select the txt file containing game names
4. Click the "Download Game Covers" button
5. Downloaded covers will be saved to the "Oyunlar" (Games) folder
6. Games that couldn't be downloaded will be written to "failed_games.txt"

### Downloading Movie Covers
1. Navigate to the "Movies" tab
2. Click the "Select Movie List" button
3. Select the txt file containing movie names
4. Click the "Download Movie Covers" button
5. Optionally use the "Replace with English Names" button
6. Downloaded covers will be saved to the "Filmler" (Movies) folder
7. Movies that couldn't be downloaded will be written to "failed_films.txt"

### Creating PDF
1. Navigate to the "PDF Creator" tab
2. Click the "Select Images" button
3. Select the covers
4. Adjust page size and layout
5. Click the "Create PDF" button
6. The PDF file will be automatically created

### Text Editing
1. Navigate to the "Text Editor" tab
2. Click the "Select Text File" button
3. Select the txt file you want to edit
4. Edit the text
5. Use the "Sort" or "Remove Duplicates" buttons
6. Click the "Save" button to save changes

## API Keys

The application uses the following APIs:
- Steam API
- Twitch API
- OMDb API
- TMDB API

You can update your API keys in the `src/utils/config.py` file.

## File Structure

```
archive-item-downloader/
├── src/
│   ├── api/              # API integrations
│   ├── ui/               # User interface components
│   ├── workers/          # Background processes
│   └── utils/            # Helper functions
├── main.py               # Main application file
├── film_cevir.py         # Movie translation helper file
├── requirements.txt      # Required packages
├── README.md            # This file
├── Oyunlar/             # Downloaded game covers
├── Filmler/             # Downloaded movie covers
└── resimler.pdf         # Generated PDF file
```

## Troubleshooting

### Common Errors and Solutions

1. API Connection Errors:
   - Ensure your API keys are correct
   - Check your internet connection
   - Check API limits

2. File Read/Write Errors:
   - Check file permissions
   - Ensure the file path is correct
   - Use UTF-8 encoding

3. PDF Creation Errors:
   - Ensure selected images are valid
   - Check that you have sufficient disk space

## Development

To contribute to the project:
1. Fork this repository
2. Create a new branch (`git checkout -b feature/newFeature`)
3. Commit your changes (`git commit -am 'New feature: X'`)
4. Push your branch (`git push origin feature/newFeature`)
5. Create a Pull Request

## License

This project is open source and available for use.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.