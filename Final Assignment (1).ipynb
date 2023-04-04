{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<center>\n",
    "    <img src=\"https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/Logos/organization_logo/organization_logo.png\" width=\"300\" alt=\"cognitiveclass.ai logo\"  />\n",
    "</center>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h1>Extracting and Visualizing Stock Data</h1>\n",
    "<h2>Description</h2>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Extracting essential data from a dataset and displaying it is a necessary part of data science; therefore individuals can make correct decisions based on the data. In this assignment, you will extract some stock data, you will then display this data in a graph.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2>Table of Contents</h2>\n",
    "<div class=\"alert alert-block alert-info\" style=\"margin-top: 20px\">\n",
    "    <ul>\n",
    "        <li>Define a Function that Makes a Graph</li>\n",
    "        <li>Question 1: Use yfinance to Extract Stock Data</li>\n",
    "        <li>Question 2: Use Webscraping to Extract Tesla Revenue Data</li>\n",
    "        <li>Question 3: Use yfinance to Extract Stock Data</li>\n",
    "        <li>Question 4: Use Webscraping to Extract GME Revenue Data</li>\n",
    "        <li>Question 5: Plot Tesla Stock Graph</li>\n",
    "        <li>Question 6: Plot GameStop Stock Graph</li>\n",
    "    </ul>\n",
    "<p>\n",
    "    Estimated Time Needed: <strong>30 min</strong></p>\n",
    "</div>\n",
    "\n",
    "<hr>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: yfinance==0.1.67 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (0.1.67)\n",
      "Requirement already satisfied: pandas>=0.24 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from yfinance==0.1.67) (1.3.5)\n",
      "Requirement already satisfied: requests>=2.20 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from yfinance==0.1.67) (2.28.1)\n",
      "Requirement already satisfied: lxml>=4.5.1 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from yfinance==0.1.67) (4.9.1)\n",
      "Requirement already satisfied: multitasking>=0.0.7 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from yfinance==0.1.67) (0.0.11)\n",
      "Requirement already satisfied: numpy>=1.15 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from yfinance==0.1.67) (1.21.6)\n",
      "Requirement already satisfied: python-dateutil>=2.7.3 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from pandas>=0.24->yfinance==0.1.67) (2.8.2)\n",
      "Requirement already satisfied: pytz>=2017.3 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from pandas>=0.24->yfinance==0.1.67) (2022.2.1)\n",
      "Requirement already satisfied: charset-normalizer<3,>=2 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from requests>=2.20->yfinance==0.1.67) (2.1.1)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from requests>=2.20->yfinance==0.1.67) (2022.9.24)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from requests>=2.20->yfinance==0.1.67) (1.26.11)\n",
      "Requirement already satisfied: idna<4,>=2.5 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from requests>=2.20->yfinance==0.1.67) (3.4)\n",
      "Requirement already satisfied: six>=1.5 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from python-dateutil>=2.7.3->pandas>=0.24->yfinance==0.1.67) (1.16.0)\n",
      "\n",
      "                  __    __    __    __\n",
      "                 /  \\  /  \\  /  \\  /  \\\n",
      "                /    \\/    \\/    \\/    \\\n",
      "███████████████/  /██/  /██/  /██/  /████████████████████████\n",
      "              /  / \\   / \\   / \\   / \\  \\____\n",
      "             /  /   \\_/   \\_/   \\_/   \\    o \\__,\n",
      "            / _/                       \\_____/  `\n",
      "            |/\n",
      "        ███╗   ███╗ █████╗ ███╗   ███╗██████╗  █████╗\n",
      "        ████╗ ████║██╔══██╗████╗ ████║██╔══██╗██╔══██╗\n",
      "        ██╔████╔██║███████║██╔████╔██║██████╔╝███████║\n",
      "        ██║╚██╔╝██║██╔══██║██║╚██╔╝██║██╔══██╗██╔══██║\n",
      "        ██║ ╚═╝ ██║██║  ██║██║ ╚═╝ ██║██████╔╝██║  ██║\n",
      "        ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝\n",
      "\n",
      "        mamba (0.15.3) supported by @QuantStack\n",
      "\n",
      "        GitHub:  https://github.com/mamba-org/mamba\n",
      "        Twitter: https://twitter.com/QuantStack\n",
      "\n",
      "█████████████████████████████████████████████████████████████\n",
      "\n",
      "\n",
      "Looking for: ['bs4==4.10.0']\n",
      "\n",
      "pkgs/main/linux-64       Using cache\n",
      "pkgs/main/noarch         Using cache\n",
      "pkgs/r/linux-64          Using cache\n",
      "pkgs/r/noarch            Using cache\n",
      "\n",
      "Pinned packages:\n",
      "  - python 3.7.*\n",
      "\n",
      "\n",
      "Transaction\n",
      "\n",
      "  Prefix: /home/jupyterlab/conda/envs/python\n",
      "\n",
      "  All requested packages already installed\n",
      "\n",
      "Requirement already satisfied: html5lib in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (1.1)\n",
      "Requirement already satisfied: webencodings in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from html5lib) (0.5.1)\n",
      "Requirement already satisfied: six>=1.9 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from html5lib) (1.16.0)\n",
      "Requirement already satisfied: nbformat in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (5.7.0)\n",
      "Requirement already satisfied: jupyter-core in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from nbformat) (4.11.1)\n",
      "Requirement already satisfied: traitlets>=5.1 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from nbformat) (5.4.0)\n",
      "Requirement already satisfied: fastjsonschema in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from nbformat) (2.16.2)\n",
      "Requirement already satisfied: jsonschema>=2.6 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from nbformat) (4.16.0)\n",
      "Requirement already satisfied: importlib-metadata>=3.6 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from nbformat) (4.11.4)\n",
      "Requirement already satisfied: typing-extensions>=3.6.4 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from importlib-metadata>=3.6->nbformat) (4.3.0)\n",
      "Requirement already satisfied: zipp>=0.5 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from importlib-metadata>=3.6->nbformat) (3.8.1)\n",
      "Requirement already satisfied: pkgutil-resolve-name>=1.3.10 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from jsonschema>=2.6->nbformat) (1.3.10)\n",
      "Requirement already satisfied: importlib-resources>=1.4.0 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from jsonschema>=2.6->nbformat) (5.9.0)\n",
      "Requirement already satisfied: attrs>=17.4.0 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from jsonschema>=2.6->nbformat) (22.1.0)\n",
      "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /home/jupyterlab/conda/envs/python/lib/python3.7/site-packages (from jsonschema>=2.6->nbformat) (0.18.1)\n"
     ]
    }
   ],
   "source": [
    "!pip install yfinance==0.1.67\n",
    "#!pip install pandas==1.3.3\n",
    "#!pip install requests==2.26.0\n",
    "!mamba install bs4==4.10.0 -y\n",
    "#!pip install plotly==5.3.1\n",
    "!pip install html5lib\n",
    "!pip install --upgrade nbformat"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import yfinance as yf\n",
    "import pandas as pd\n",
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import plotly.graph_objects as go\n",
    "from plotly.subplots import make_subplots"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Define Graphing Function\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In this section, we define the function `make_graph`. You don't have to know how the function works, you should only care about the inputs. It takes a dataframe with stock data (dataframe must contain Date and Close columns), a dataframe with revenue data (dataframe must contain Date and Revenue columns), and the name of the stock.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def make_graph(stock_data, revenue_data, stock):\n",
    "    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=(\"Historical Share Price\", \"Historical Revenue\"), vertical_spacing = .3)\n",
    "    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']\n",
    "    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']\n",
    "    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype(\"float\"), name=\"Share Price\"), row=1, col=1)\n",
    "    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype(\"float\"), name=\"Revenue\"), row=2, col=1)\n",
    "    fig.update_xaxes(title_text=\"Date\", row=1, col=1)\n",
    "    fig.update_xaxes(title_text=\"Date\", row=2, col=1)\n",
    "    fig.update_yaxes(title_text=\"Price ($US)\", row=1, col=1)\n",
    "    fig.update_yaxes(title_text=\"Revenue ($US Millions)\", row=2, col=1)\n",
    "    fig.update_layout(showlegend=False,\n",
    "    height=900,\n",
    "    title=stock,\n",
    "    xaxis_rangeslider_visible=True)\n",
    "    fig.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question 1: Use yfinance to Extract Stock Data\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using the `Ticker` function enter the ticker symbol of the stock we want to extract data on to create a ticker object. The stock is Tesla and its ticker symbol is `TSLA`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "tesla = yf.Ticker(\"TSLA\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using the ticker object and the function `history` extract stock information and save it in a dataframe named `tesla_data`. Set the `period` parameter to `max` so we get information for the maximum amount of time.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "tesla_data = tesla.history(period=\"max\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Reset the index** using the `reset_index(inplace=True)` function on the tesla_data DataFrame and display the first five rows of the `tesla_data` dataframe using the `head` function. Take a screenshot of the results and code from the beginning of Question 1 to the results below.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Volume</th>\n",
       "      <th>Dividends</th>\n",
       "      <th>Stock Splits</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2010-06-29</td>\n",
       "      <td>1.266667</td>\n",
       "      <td>1.666667</td>\n",
       "      <td>1.169333</td>\n",
       "      <td>1.592667</td>\n",
       "      <td>281494500</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2010-06-30</td>\n",
       "      <td>1.719333</td>\n",
       "      <td>2.028000</td>\n",
       "      <td>1.553333</td>\n",
       "      <td>1.588667</td>\n",
       "      <td>257806500</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2010-07-01</td>\n",
       "      <td>1.666667</td>\n",
       "      <td>1.728000</td>\n",
       "      <td>1.351333</td>\n",
       "      <td>1.464000</td>\n",
       "      <td>123282000</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2010-07-02</td>\n",
       "      <td>1.533333</td>\n",
       "      <td>1.540000</td>\n",
       "      <td>1.247333</td>\n",
       "      <td>1.280000</td>\n",
       "      <td>77097000</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2010-07-06</td>\n",
       "      <td>1.333333</td>\n",
       "      <td>1.333333</td>\n",
       "      <td>1.055333</td>\n",
       "      <td>1.074000</td>\n",
       "      <td>103003500</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Date      Open      High       Low     Close     Volume  Dividends  \\\n",
       "0 2010-06-29  1.266667  1.666667  1.169333  1.592667  281494500          0   \n",
       "1 2010-06-30  1.719333  2.028000  1.553333  1.588667  257806500          0   \n",
       "2 2010-07-01  1.666667  1.728000  1.351333  1.464000  123282000          0   \n",
       "3 2010-07-02  1.533333  1.540000  1.247333  1.280000   77097000          0   \n",
       "4 2010-07-06  1.333333  1.333333  1.055333  1.074000  103003500          0   \n",
       "\n",
       "   Stock Splits  \n",
       "0           0.0  \n",
       "1           0.0  \n",
       "2           0.0  \n",
       "3           0.0  \n",
       "4           0.0  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tesla_data.reset_index(inplace=True)\n",
    "tesla_data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question 2: Use Webscraping to Extract Tesla Revenue Data\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use the `requests` library to download the webpage [https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue](https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0220ENSkillsNetwork23455606-2022-01-01). Save the text of the response as a variable named `html_data`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = \"https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue\"\n",
    "html_data  = requests.get(url).text"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Parse the html data using `beautiful_soup`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "soup = BeautifulSoup(html_data,\"html5lib\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using `BeautifulSoup` or the `read_html` function extract the table with `Tesla Quarterly Revenue` and store it into a dataframe named `tesla_revenue`. The dataframe should have columns `Date` and `Revenue`.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<details><summary>Click here if you need help locating the table</summary>\n",
    "\n",
    "```\n",
    "    \n",
    "Below is the code to isolate the table, you will now need to loop through the rows and columns like in the previous lab\n",
    "    \n",
    "soup.find_all(\"tbody\")[1]\n",
    "    \n",
    "If you want to use the read_html function the table is located at index 1\n",
    "\n",
    "\n",
    "```\n",
    "\n",
    "</details>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "tesla_revenue = pd.DataFrame(columns=['Date', 'Revenue'])\n",
    "\n",
    "for table in soup.find_all('table'):\n",
    "\n",
    "    if ('Tesla Quarterly Revenue' in table.find('th').text):\n",
    "        rows = table.find_all('tr')\n",
    "        \n",
    "        for row in rows:\n",
    "            col = row.find_all('td')\n",
    "            \n",
    "            if col != []:\n",
    "                date = col[0].text\n",
    "                revenue = col[1].text.replace(',','').replace('$','')\n",
    "\n",
    "                tesla_revenue = tesla_revenue.append({\"Date\":date, \"Revenue\":revenue}, ignore_index=True)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Execute the following line to remove the comma and dollar sign from the `Revenue` column.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/home/jupyterlab/conda/envs/python/lib/python3.7/site-packages/ipykernel_launcher.py:1: FutureWarning: The default value of regex will change from True to False in a future version.\n",
      "  \"\"\"Entry point for launching an IPython kernel.\n"
     ]
    }
   ],
   "source": [
    "tesla_revenue[\"Revenue\"] = tesla_revenue['Revenue'].str.replace(',|\\$',\"\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Execute the following lines to remove an null or empty strings in the Revenue column.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "tesla_revenue.dropna(inplace=True)\n",
    "\n",
    "tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != \"\"]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Display the last 5 row of the `tesla_revenue` dataframe using the `tail` function. Take a screenshot of the results.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Revenue</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>48</th>\n",
       "      <td>2010-09-30</td>\n",
       "      <td>31</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>49</th>\n",
       "      <td>2010-06-30</td>\n",
       "      <td>28</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50</th>\n",
       "      <td>2010-03-31</td>\n",
       "      <td>21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>52</th>\n",
       "      <td>2009-09-30</td>\n",
       "      <td>46</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>53</th>\n",
       "      <td>2009-06-30</td>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          Date Revenue\n",
       "48  2010-09-30      31\n",
       "49  2010-06-30      28\n",
       "50  2010-03-31      21\n",
       "52  2009-09-30      46\n",
       "53  2009-06-30      27"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tesla_revenue.tail()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question 3: Use yfinance to Extract Stock Data\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using the `Ticker` function enter the ticker symbol of the stock we want to extract data on to create a ticker object. The stock is GameStop and its ticker symbol is `GME`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "GameStop = yf.Ticker(\"GME\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using the ticker object and the function `history` extract stock information and save it in a dataframe named `gme_data`. Set the `period` parameter to `max` so we get information for the maximum amount of time.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "gme_data = GameStop.history(period=\"max\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Reset the index** using the `reset_index(inplace=True)` function on the gme_data DataFrame and display the first five rows of the `gme_data` dataframe using the `head` function. Take a screenshot of the results and code from the beginning of Question 3 to the results below.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Volume</th>\n",
       "      <th>Dividends</th>\n",
       "      <th>Stock Splits</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2002-02-13</td>\n",
       "      <td>1.620129</td>\n",
       "      <td>1.693350</td>\n",
       "      <td>1.603296</td>\n",
       "      <td>1.691667</td>\n",
       "      <td>76216000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2002-02-14</td>\n",
       "      <td>1.712707</td>\n",
       "      <td>1.716073</td>\n",
       "      <td>1.670626</td>\n",
       "      <td>1.683250</td>\n",
       "      <td>11021600</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2002-02-15</td>\n",
       "      <td>1.683250</td>\n",
       "      <td>1.687458</td>\n",
       "      <td>1.658002</td>\n",
       "      <td>1.674834</td>\n",
       "      <td>8389600</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2002-02-19</td>\n",
       "      <td>1.666418</td>\n",
       "      <td>1.666418</td>\n",
       "      <td>1.578047</td>\n",
       "      <td>1.607504</td>\n",
       "      <td>7410400</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2002-02-20</td>\n",
       "      <td>1.615920</td>\n",
       "      <td>1.662210</td>\n",
       "      <td>1.603296</td>\n",
       "      <td>1.662210</td>\n",
       "      <td>6892800</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Date      Open      High       Low     Close    Volume  Dividends  \\\n",
       "0 2002-02-13  1.620129  1.693350  1.603296  1.691667  76216000        0.0   \n",
       "1 2002-02-14  1.712707  1.716073  1.670626  1.683250  11021600        0.0   \n",
       "2 2002-02-15  1.683250  1.687458  1.658002  1.674834   8389600        0.0   \n",
       "3 2002-02-19  1.666418  1.666418  1.578047  1.607504   7410400        0.0   \n",
       "4 2002-02-20  1.615920  1.662210  1.603296  1.662210   6892800        0.0   \n",
       "\n",
       "   Stock Splits  \n",
       "0           0.0  \n",
       "1           0.0  \n",
       "2           0.0  \n",
       "3           0.0  \n",
       "4           0.0  "
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gme_data.reset_index(inplace=True)\n",
    "gme_data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use the `requests` library to download the webpage <https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html>. Save the text of the response as a variable named `html_data`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = \"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html\"\n",
    "\n",
    "html_data  = requests.get(url).text"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Parse the html data using `beautiful_soup`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "soup = BeautifulSoup(html_data,\"html5lib\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using `BeautifulSoup` or the `read_html` function extract the table with `GameStop Quarterly Revenue` and store it into a dataframe named `gme_revenue`. The dataframe should have columns `Date` and `Revenue`. Make sure the comma and dollar sign is removed from the `Revenue` column using a method similar to what you did in Question 2.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<details><summary>Click here if you need help locating the table</summary>\n",
    "\n",
    "```\n",
    "    \n",
    "Below is the code to isolate the table, you will now need to loop through the rows and columns like in the previous lab\n",
    "    \n",
    "soup.find_all(\"tbody\")[1]\n",
    "    \n",
    "If you want to use the read_html function the table is located at index 1\n",
    "\n",
    "\n",
    "```\n",
    "\n",
    "</details>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "gme_revenue = pd.DataFrame(columns=['Date', 'Revenue'])\n",
    "\n",
    "for table in soup.find_all('table'):\n",
    "\n",
    "    if ('GameStop Quarterly Revenue' in table.find('th').text):\n",
    "        rows = table.find_all('tr')\n",
    "        \n",
    "        for row in rows:\n",
    "            col = row.find_all('td')\n",
    "            \n",
    "            if col != []:\n",
    "                date = col[0].text\n",
    "                revenue = col[1].text.replace(',','').replace('$','')\n",
    "\n",
    "                gme_revenue = gme_revenue.append({\"Date\":date, \"Revenue\":revenue}, ignore_index=True)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Display the last five rows of the `gme_revenue` dataframe using the `tail` function. Take a screenshot of the results.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Revenue</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>57</th>\n",
       "      <td>2006-01-31</td>\n",
       "      <td>1667</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58</th>\n",
       "      <td>2005-10-31</td>\n",
       "      <td>534</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>59</th>\n",
       "      <td>2005-07-31</td>\n",
       "      <td>416</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>60</th>\n",
       "      <td>2005-04-30</td>\n",
       "      <td>475</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>61</th>\n",
       "      <td>2005-01-31</td>\n",
       "      <td>709</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          Date Revenue\n",
       "57  2006-01-31    1667\n",
       "58  2005-10-31     534\n",
       "59  2005-07-31     416\n",
       "60  2005-04-30     475\n",
       "61  2005-01-31     709"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gme_revenue.tail()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question 5: Plot Tesla Stock Graph\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use the `make_graph` function to graph the Tesla Stock Data, also provide a title for the graph. The structure to call the `make_graph` function is `make_graph(tesla_data, tesla_revenue, 'Tesla')`. Note the graph will only show data upto June 2021.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "Mime type rendering requires nbformat>=4.2.0 but it is not installed",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m/tmp/ipykernel_1178/1765937996.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mmake_graph\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtesla_data\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtesla_revenue\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"Tesla\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m/tmp/ipykernel_1178/2068038883.py\u001b[0m in \u001b[0;36mmake_graph\u001b[0;34m(stock_data, revenue_data, stock)\u001b[0m\n\u001b[1;32m     13\u001b[0m     \u001b[0mtitle\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mstock\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     14\u001b[0m     xaxis_rangeslider_visible=True)\n\u001b[0;32m---> 15\u001b[0;31m     \u001b[0mfig\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mshow\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m~/conda/envs/python/lib/python3.7/site-packages/plotly/basedatatypes.py\u001b[0m in \u001b[0;36mshow\u001b[0;34m(self, *args, **kwargs)\u001b[0m\n\u001b[1;32m   3396\u001b[0m         \u001b[0;32mimport\u001b[0m \u001b[0mplotly\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mio\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mpio\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3397\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 3398\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mpio\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mshow\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   3399\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3400\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mto_json\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/conda/envs/python/lib/python3.7/site-packages/plotly/io/_renderers.py\u001b[0m in \u001b[0;36mshow\u001b[0;34m(fig, renderer, validate, **kwargs)\u001b[0m\n\u001b[1;32m    395\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mnbformat\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0mLooseVersion\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mnbformat\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__version__\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m<\u001b[0m \u001b[0mLooseVersion\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"4.2.0\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    396\u001b[0m             raise ValueError(\n\u001b[0;32m--> 397\u001b[0;31m                 \u001b[0;34m\"Mime type rendering requires nbformat>=4.2.0 but it is not installed\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    398\u001b[0m             )\n\u001b[1;32m    399\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mValueError\u001b[0m: Mime type rendering requires nbformat>=4.2.0 but it is not installed"
     ]
    }
   ],
   "source": [
    "make_graph(tesla_data, tesla_revenue, \"Tesla\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question 6: Plot GameStop Stock Graph\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use the `make_graph` function to graph the GameStop Stock Data, also provide a title for the graph. The structure to call the `make_graph` function is `make_graph(gme_data, gme_revenue, 'GameStop')`. Note the graph will only show data upto June 2021.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "Mime type rendering requires nbformat>=4.2.0 but it is not installed",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m/tmp/ipykernel_1178/2000178444.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mmake_graph\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mgme_data\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mgme_revenue\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'GameStop'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m/tmp/ipykernel_1178/2068038883.py\u001b[0m in \u001b[0;36mmake_graph\u001b[0;34m(stock_data, revenue_data, stock)\u001b[0m\n\u001b[1;32m     13\u001b[0m     \u001b[0mtitle\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mstock\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     14\u001b[0m     xaxis_rangeslider_visible=True)\n\u001b[0;32m---> 15\u001b[0;31m     \u001b[0mfig\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mshow\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m~/conda/envs/python/lib/python3.7/site-packages/plotly/basedatatypes.py\u001b[0m in \u001b[0;36mshow\u001b[0;34m(self, *args, **kwargs)\u001b[0m\n\u001b[1;32m   3396\u001b[0m         \u001b[0;32mimport\u001b[0m \u001b[0mplotly\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mio\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mpio\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3397\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 3398\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mpio\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mshow\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   3399\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3400\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mto_json\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/conda/envs/python/lib/python3.7/site-packages/plotly/io/_renderers.py\u001b[0m in \u001b[0;36mshow\u001b[0;34m(fig, renderer, validate, **kwargs)\u001b[0m\n\u001b[1;32m    395\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mnbformat\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0mLooseVersion\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mnbformat\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__version__\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m<\u001b[0m \u001b[0mLooseVersion\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"4.2.0\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    396\u001b[0m             raise ValueError(\n\u001b[0;32m--> 397\u001b[0;31m                 \u001b[0;34m\"Mime type rendering requires nbformat>=4.2.0 but it is not installed\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    398\u001b[0m             )\n\u001b[1;32m    399\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mValueError\u001b[0m: Mime type rendering requires nbformat>=4.2.0 but it is not installed"
     ]
    }
   ],
   "source": [
    "make_graph(gme_data, gme_revenue, 'GameStop')\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2>About the Authors:</h2> \n",
    "\n",
    "<a href=\"https://www.linkedin.com/in/joseph-s-50398b136/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0220ENSkillsNetwork23455606-2022-01-01\">Joseph Santarcangelo</a> has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.\n",
    "\n",
    "Azim Hirjani\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Change Log\n",
    "\n",
    "| Date (YYYY-MM-DD) | Version | Changed By    | Change Description          |\n",
    "| ----------------- | ------- | ------------- | --------------------------- |\n",
    "| 2022-02-28        | 1.2     | Lakshmi Holla | Changed the URL of GameStop |\n",
    "| 2020-11-10        | 1.1     | Malika Singla | Deleted the Optional part   |\n",
    "| 2020-08-27        | 1.0     | Malika Singla | Added lab to GitLab         |\n",
    "\n",
    "<hr>\n",
    "\n",
    "## <h3 align=\"center\"> © IBM Corporation 2020. All rights reserved. <h3/>\n",
    "\n",
    "<p>\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python",
   "language": "python",
   "name": "conda-env-python-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
