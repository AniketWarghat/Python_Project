# 📈 TCS Stock Price Analysis

A data visualization project analyzing TCS (Tata Consultancy Services) historical stock price data using Python and Matplotlib.

---

## 🗂️ Dataset
- **Source:** Live data fetched via `yfinance` library
- **Stock:** TCS.NS (NSE India)
- **Date Range:** January 2024 – March 2026
- **Total Records:** 536 trading days

---

## 🛠️ Tools & Libraries
| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| Pandas | Data loading, cleaning, sorting |
| Matplotlib | Data visualization & chart export |
| yfinance | Live stock data fetching |
| OS | Automated folder creation |
| Jupyter Notebook | Development environment |

---

## 📊 Concepts Covered
- Fetching live stock data using `yfinance`
- Automated folder creation using `os` module
- Data cleaning — null check, column renaming, date sorting
- Plotting OHLC (Open, High, Low, Close) price lines
- Calculating & plotting Moving Averages (MA20 & MA50)
- Peak price annotation with arrow using `plt.annotate()`
- Average price reference line using `axhline()`
- Dual subplot — Price chart + Volume bar chart
- Shared X-axis between subplots using `sharex=True`
- Chart export as high-resolution PNG (`dpi=150`)

---

## 📁 Project Structure
```
Project11_Stock_Price_Analysis/
├── 11_stock_analysis.ipynb   ← Main Jupyter Notebook
├── Data/
│   └── Stock_data.csv        ← Raw stock data (auto-saved)
├── Output/
│   └── Stock_Chart.png       ← Final exported chart
└── README.md                 ← Project documentation
```

---

## 📌 Key Outcome
Visualized TCS stock price trends over 200 trading days with MA20 & MA50 indicators, volume analysis, and peak price annotation — exported as a portfolio-ready chart.

---

## 👤 Author
**Aniket Warghat** — Python Projects
[GitHub Profile](https://github.com/AniketWarghat)