# 🎮 Top Games Data Science

A Python data analysis project focused on collecting and analyzing information about the Top 250 video games from RAWG.io.

---

# 📌 Project Overview

The goal of this project is to demonstrate the complete workflow of:
- web scraping
- data collection
- data cleaning
- exploratory data analysis
- data grouping and filtering
- data visualization

The project uses Selenium to scrape detailed information about the top-rated games from RAWG.io and analyzes the collected dataset using Pandas and Matplotlib.

---

# 🛠 Technologies Used

- Python
- Selenium
- Pandas
- Matplotlib
- Jupyter Notebook
- PyCharm

---

# 📂 Project Structure

```bash
top_games_data_science/
│
├── data_projekt_web_scraping.py
├── projekt.ipynb
├── graf_zad_2.ipynb
├── rawg_top_250_detailed.csv
└── README.md
```

---

# 📊 Dataset Information

The dataset was collected directly from RAWG.io using Selenium web scraping.

The dataset contains:
- 250 video games
- 9 columns of data

## Dataset Columns

| Column | Description |
|---|---|
| Title | Game title |
| Release Date | Official release date |
| Playtime | Average playtime |
| Metascore | Game rating |
| Developer | Game developer |
| Publisher | Game publisher |
| Age Rating | Age restriction |
| Genre | Game genre |
| Platforms | Supported gaming platforms |

---

# 🌐 Web Scraping

The scraping process was implemented using Selenium.

The scraper:
1. Opens RAWG.io
2. Navigates to the Top 250 games section
3. Scrolls through the page to load all games
4. Opens each game page individually
5. Extracts detailed information
6. Saves the data into a CSV file

## Extracted Data

The scraper collects:
- game title
- release date
- average playtime
- metascore
- developer
- publisher
- age rating
- genre
- supported platforms

The final dataset is stored in:

```bash
rawg_top_250_detailed.csv
```

---

# 📈 Data Analysis

The project includes multiple examples of data analysis using Pandas.

## Examples of Analysis

- displaying dataset structure
- calculating average Metascore
- selecting rows and columns
- searching games by title
- searching games by developer
- grouping games by publisher
- grouping games by genre
- filtering games with ratings above 90
- dictionary-based game lookup
- function-based game search
- loop-based developer search

## Average Game Rating

The average Metascore of all games in the dataset:

```bash
88.54
```

---

# 📉 Data Visualization

Several visualizations were created using Matplotlib.

## Included Graphs

### Histogram
Distribution of Metascore ratings across all games.

### Spider / Radar Chart
Top 8 genres based on average Metascore.

### Heatmap
Average Metascore by publisher and age rating.

---

# ▶️ How to Run the Project

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/marko1989bjj/top_games_data_science.git
```

---

## 2️⃣ Install Dependencies

```bash
pip install selenium pandas matplotlib
```

---

## 3️⃣ Run the Web Scraper

```bash
python data_projekt_web_scraping.py
```

---

## 4️⃣ Open Jupyter Notebook

```bash
jupyter notebook
```

Open:

```bash
projekt.ipynb
```

---

# 🎯 Project Goals

This project was created to practice:
- Python programming
- Web scraping with Selenium
- Working with datasets
- Data analysis using Pandas
- Data visualization with Matplotlib
- Working with CSV files
- Git and GitHub workflow

---

# 📚 Example Features

✔ Search games by title  
✔ Search games by developer  
✔ Calculate average ratings  
✔ Group games by genre or publisher  
✔ Generate visual reports  
✔ Analyze game statistics  

---

# 👨‍💻 Author

Marko Aleksic

GitHub:
https://github.com/marko1989bjj

---

# 📄 License

This project is intended for educational and portfolio purposes.
