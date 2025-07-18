# Melody Hub 

**Melody Hub** is an Informatics Practices project designed to analyze Spotify data, uncover trends in music, and explore user preferences, artist performance, and cultural patterns across countries and timelines. This Python-based software enables both admin and user operations like managing data records, visualizing insights, and generating reports.

---

## 📌 Project Details

- **Subject:** Informatics Practices (065)
- **Project Name:** Melody Hub
- **Theme:** Analysis of Spotify
- **Student:** Rudraksh Tank (Class XII - A)
- **Session:** 2023–2024
- **School:** St. Xavier’s School, Nevta

---

## 🎯 Objective

- Analyze trends in global music consumption using Spotify data.
- Provide dual interfaces (Admin & User) for managing and exploring datasets.
- Allow CRUD operations on user, song, artist, podcast, playlist, and country data.
- Visualize key statistics through charts and graphs.
- Offer powerful search, sort, and report-generation capabilities.

---

## 🗃️ Data Source

Datasets were taken from:
- [Spotify Tracks Dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset)
- [Spotify User Behavior Dataset](https://www.kaggle.com/datasets/meeraajayakumar/spotify-user-behavior-dataset)
- [Top Spotify Songs 2023](https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023)
- [Mockaroo.com](https://mockaroo.com/) for synthetic data generation

---

## 🧾 CSV Files

Each CSV file represents a core entity in the system:
- `User.csv`: User ID, Name, Email, Password, Registration Date, Gender, Subscription, Review, Rating
- `Podcast.csv`: Name, Creator, Genre, Language, Episodes, Rating
- `Country.csv`: Country Name, Continent, Users, Popular Genre, Avg. Listening Time
- `Playlist.csv`: Playlist ID, Name, Creator, Song IDs, Views, Duration
- `Song.csv`: Song ID, Name, Artists, Year, Spotify Playlists, Streams
- `Artist.csv`: Artist ID, Name, Nationality, Ranking, Followers, Monthly Listeners

---

## 🧑‍💻 Features

### 🔐 Admin Console
- Import, export CSV files
- Add, delete, and modify records
- Full CRUD operations on all datasets
- Modify individual fields for precision updates

### 🙋‍♀️ User Console
- Read, search, and sort records
- Generate detailed reports based on criteria
- Visualize data through:
  - Line Charts (e.g., Podcast Genre vs Episodes)
  - Bar Graphs (e.g., Continent vs No. of Users)
  - Histograms (e.g., Podcast Ratings, Song Release Year)

---

## 📊 Technologies Used

- **Language:** Python
- **Libraries:** `pandas`, `matplotlib`, `time`
- **Data Storage:** CSV files
- **IDE:** Can be run on any Python environment (IDLE, VS Code, etc.)

---

## 🔍 Functionality

- **Search**: Find users by subscription, songs by year, podcasts by language, etc.
- **Sort**: Order artists by ranking, countries by user count, etc.
- **Reports**: Generate CSV-based reports on filtered data (e.g., users with rating > 4).
- **Visualizations**: Generate insightful charts to understand music trends.

