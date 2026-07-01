# Movie Recommender System

A Streamlit-powered movie recommendation app built with the TMDB 5000 movie dataset. Pick a movie you like, and the app suggests five similar movies with posters fetched from The Movie Database API.

## Features

- Search or select a movie from an interactive dropdown.
- Get five content-based movie recommendations.
- View movie posters directly inside the Streamlit interface.
- Build the similarity matrix from the CSV data at runtime so the repository stays lightweight.
- Simple local setup with Python and Streamlit.

## Screenshots

![Movie recommender home screen](ss/Screenshot%20(3140).png)

![Movie recommendations preview](ss/Screenshot%20(3141).png)

![Movie selection dropdown](ss/Screenshot%20(3142).png)

![Recommendation results](ss/Screenshot%20(3143).png)

## Tech Stack

- Python
- Streamlit
- Pandas
- Scikit-learn
- Requests
- TMDB API

## Project Structure

```text
Movie Recommender System/
├── app.py
├── requirements.txt
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── ss/
│   ├── Screenshot (3140).png
│   ├── Screenshot (3141).png
│   ├── Screenshot (3142).png
│   └── Screenshot (3143).png
└── README.md
```

## Run Locally

Clone the repository and move into the project folder:

```powershell
git clone https://github.com/mian-arham-haroon/Movie-Recommender-System.git
cd "Movie Recommender System"
```

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Start the app:

```powershell
streamlit run app.py
```

Open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

If PowerShell blocks script execution, run this command once in the same terminal session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

## Dataset

This project uses the TMDB 5000 Movies and Credits datasets. The recommendation logic is built from the CSV data directly at runtime, so no large serialized model file is required.

## Notes

- Poster images are fetched from TMDB at runtime, so an internet connection is required when using the app.
- The repository keeps the project lightweight by avoiding oversized binary assets.
