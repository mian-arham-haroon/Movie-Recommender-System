# 🎬 Movie Recommender System

A sleek Streamlit-powered app that recommends movies based on similarity, using the TMDB 5000 movie dataset. Pick a movie you love and discover five fresh suggestions with posters fetched directly from TMDB.

## ✨ Highlights

- 🎯 Select any movie from an interactive dropdown
- 🎥 Get five smart movie recommendations instantly
- 🖼️ View movie posters directly in the app
- ⚡ Build recommendations from CSV data at runtime for a lightweight GitHub repo
- 🐍 Easy setup with Python and Streamlit

## 📽️ Demo Video

Watch the app in action and see the movie recommendations flow live:

<a href="video.mp4">
  <img src="ss/Screenshot%20(3140).png" alt="Demo video preview" width="100%" />
</a>

> If the preview does not open directly on GitHub, click the image or use the direct link to [video.mp4](video.mp4).

## 🧠 How It Works

- The app reads the TMDB movie dataset from the CSV files.
- It combines movie overview, genres, and keywords into a rich feature profile.
- A similarity model is built at runtime to find movies that feel similar to the one you choose.
- The app then displays five recommendations along with their posters.

## 📸 Screenshots

![Movie recommender home screen](ss/Screenshot%20(3140).png)

![Movie recommendations preview](ss/Screenshot%20(3141).png)

![Movie selection dropdown](ss/Screenshot%20(3142).png)

![Recommendation results](ss/Screenshot%20(3143).png)

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- Scikit-learn
- Requests
- TMDB API

## 📁 Project Structure

```text
Movie Recommender System/
├── app.py
├── requirements.txt
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── video.mp4
├── ss/
│   ├── Screenshot (3140).png
│   ├── Screenshot (3141).png
│   ├── Screenshot (3142).png
│   └── Screenshot (3143).png
└── README.md
```

## ▶️ Run Locally

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

## 📊 Dataset

This project uses the TMDB 5000 Movies and Credits datasets. The recommendation logic is built from the CSV data directly at runtime, so no large serialized model file is required.

## ℹ️ Notes

- Poster images are fetched from TMDB at runtime, so an internet connection is required when using the app.
- The repository stays lightweight by avoiding oversized binary assets.
