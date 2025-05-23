<h1 align="center">A simple web scraper</h1>

![Picture](images/bot.png)


## Usage

To use this lab, please follow the instructions below.

**1)** Clone the repository locally:

```
git clone git@github.com:nick22d/simple-web-scraper.git
```

**2)** Navigate into the repository:

```
cd simple-web-scraper/
```

**3)** Install the required libraries:

```
pip install -r requirements.txt
```

**4)** Launch the web server:

```
vagrant up
```

**5)** Scrape the coffee shop web site to obtain all products:

```
python scraper.py
```

**6)** Scrape the coffee shop web site to obtain all products worth more than $4:

```
python scrape-for-exp-coffees.py
```

**7)** Tear down the web server:

```
vagrant destroy -f
```