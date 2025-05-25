# 🇰🇪 Kenya Pesticide Watchdog

A project designed to help Kenyan farmers, researchers, and regulators identify potentially hazardous or banned pesticides in the market. The tool scrapes official pesticide data in Kenya and compares it against global banned pesticide databases.

---

## 🚀 Features

- 🔍 Scrape pesticide/insecticide data from Kenya's official Pest Control Products Board (PCPB)
- 🌍 Compare Kenyan products with internationally banned pesticide lists (EU, WHO, PAN)
- 🚨 Flag pesticides that may pose environmental or health hazards

---

## 🛠️ How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/KemboiM/Kenya-Pesticide.git
cd KenyaPesticideWatchdog
```

### 2. Installations

Make sure you have Python 3 installed, then run:

```bash
pip install -r requirements.txt
```

### 3. Scrape Pesticides from PCPB Website

```bash
python scraper/fetch_pesticides_kenya.py
```

This creates `kenya_pesticides.csv` with official Kenyan product info.

### 4. Compare with Banned List

Ensure you have a `banned_pesticides_world.csv` file in the root directory with a column called `active_ingredient`, then:

```bash
python scraper/banned_list_checker.py
```

This produces `flagged_products.csv` containing potentially banned or harmful chemicals.

---

## 📚 Educational Resources

- [PAN International List of Highly Hazardous Pesticides](https://pan-international.org/pan-international-list-of-highly-hazardous-pesticides/)
- [EU Pesticide Database](https://ec.europa.eu/food/plant/pesticides/eu-pesticides-database_en)
- [WHO Recommended Classification of Pesticides](https://www.who.int/publications/i/item/9789240005662)
- [Kenya Pest Control Products Board (PCPB)](https://www.pestcontrolproductsboard.go.ke/)

---

## 📁 File Structure

```
KenyaPesticideWatchdog/
├── Scripts/
│   ├── fetch_pesticides_kenya.py       # Scrapes Kenya pesticide list
│   ├── banned_list_checker.py          # Compares to global banned list
├── docs/
│   ├── resources.md                    # External links
│   ├── how_it_works.md                # Explanation of data flow
├── kenya_pesticides.csv                # Output from scraper (auto-generated)
├── flagged_products.csv                # Output from checker (auto-generated)
├── banned_pesticides_world.csv         # Your input banned list file
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 👥 Contributing

I welcome contributions from:
- Farmers and agricultural workers
- Data scientists
- Policy advocates
- Students and educators

Feel free to fork, open issues, or submit pull requests.

---

## 📄 License

[MIT License](LICENSE)
