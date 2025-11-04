# Cover Downloader - Usage Guide

**Tags:** `cover-downloader` `game-covers` `movie-covers` `user-guide` `tutorial` `documentation`

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Interface Overview](#interface-overview)
4. [Downloading Game Covers](#downloading-game-covers)
5. [Downloading Movie Covers](#downloading-movie-covers)
6. [Creating PDF](#creating-pdf)
7. [Text Editing](#text-editing)
8. [Frequently Asked Questions](#frequently-asked-questions)
9. [Error Solutions](#error-solutions)

## Introduction

Cover Downloader is a comprehensive tool that allows you to automatically download game and movie covers. This guide explains all features of the application in detail.

## Installation

### System Requirements
- Python 3.8 or higher
- Internet connection
- At least 1GB free disk space

### Installation Steps
1. Download and install Python from [python.org](https://python.org)
2. Download the project to your computer
3. Navigate to the project directory in the command line
4. Install required packages:
```bash
pip install -r requirements.txt
```
5. Start the application:
```bash
python main.py
```

## Interface Overview

The application consists of four main tabs:

### 1. Games Tab
- Game list selection
- Cover downloading
- Download status tracking

### 2. Movies Tab
- Movie list selection
- Cover downloading
- English name conversion
- Download status tracking

### 3. PDF Creator Tab
- Image selection
- Page layout settings
- PDF creation

### 4. Text Editor Tab
- Text file selection
- Text editing
- Sorting and cleaning
- Saving

## Downloading Game Covers

### Preparing Game List
1. Write game names in a text file
2. Arrange them so that each line contains one game name
3. Save the file with UTF-8 encoding

### Downloading Covers
1. Navigate to the "Games" tab
2. Click the "Select Game List" button
3. Select the file you prepared
4. Click the "Download Game Covers" button
5. The download process will begin

### After Download
- Successful downloads are marked with a green checkmark
- Failed downloads are marked with a red cross
- Failed downloads are saved to the "failed_games.txt" file

## Downloading Movie Covers

### Preparing Movie List
1. Write movie names in a text file
2. Arrange them so that each line contains one movie name
3. Save the file with UTF-8 encoding

### Downloading Covers
1. Navigate to the "Movies" tab
2. Click the "Select Movie List" button
3. Select the file you prepared
4. Click the "Download Movie Covers" button
5. The download process will begin

### English Name Conversion
1. Click the "Replace with English Names" button
2. The conversion process will begin
3. Results will be saved to the "FilmList_English.txt" file

## Creating PDF

### Selecting Images
1. Navigate to the "PDF Creator" tab
2. Click the "Select Images" button
3. Select the covers you want
4. Hold the Ctrl key to select multiple images

### Page Layout
1. Select page size
2. Adjust spacing between covers
3. Adjust page margins

### Creating PDF
1. Click the "Create PDF" button
2. The PDF file will be automatically created
3. You will receive a notification when the process is complete

## Text Editing

### Selecting File
1. Navigate to the "Text Editor" tab
2. Click the "Select Text File" button
3. Select the file you want to edit

### Editing Text
1. You can edit the text directly
2. Use the "Sort" button to sort alphabetically
3. Use the "Remove Duplicates" button to remove duplicate lines

### Saving
1. Click the "Save" button
2. Changes will be automatically saved

## Frequently Asked Questions

### 1. How to Get API Keys?
- Steam API: [Steam Developer](https://steamcommunity.com/dev/apikey)
- Twitch API: [Twitch Developer Console](https://dev.twitch.tv/console)
- OMDb API: [OMDb API](http://www.omdbapi.com/apikey.aspx)
- TMDB API: [TMDB API](https://www.themoviedb.org/settings/api)

### 2. How to Increase Download Speed?
- Check your internet connection
- Check API limits
- Avoid sending too many requests at the same time

### 3. Where Are Covers Downloaded?
- Game covers: "Oyunlar" (Games) folder
- Movie covers: "Filmler" (Movies) folder

## Error Solutions

### 1. API Connection Errors
- Check your API keys
- Check your internet connection
- Check API limits

### 2. File Read/Write Errors
- Check file permissions
- Ensure the file path is correct
- Use UTF-8 encoding

### 3. PDF Creation Errors
- Ensure selected images are valid
- Check that you have sufficient disk space
- Check image formats

### 4. Application Crash Issues
- Check your Python version
- Ensure required packages are installed
- Check the error message
