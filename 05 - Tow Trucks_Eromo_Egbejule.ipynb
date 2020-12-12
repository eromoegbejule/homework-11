{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Texas Tow Trucks (`.apply` and `requests`)\n",
    "\n",
    "We're going to scrape some [tow trucks in Texas](https://www.tdlr.texas.gov/tools_search/)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Import your imports"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/Users/eromoegbejule/.pyenv/versions/3.8.2/lib/python3.8/site-packages/pandas/compat/__init__.py:120: UserWarning: Could not import the lzma module. Your installed Python is incomplete. Attempting to use lzma compression will result in a RuntimeError.\n",
      "  warnings.warn(msg)\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from selenium import webdriver"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "driver = webdriver.Chrome()\n",
    "driver.get(\"https://www.tdlr.texas.gov/tools_search/\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Search for the TLDR Number `006565540C`, and scrape the information on that company\n",
    "\n",
    "Using [license information system](https://www.tdlr.texas.gov/tools_search/), find information about the tow truck number above, displaying the\n",
    "\n",
    "- The business name\n",
    "- Owner/operator\n",
    "- Phone number\n",
    "- License status (Active, Expired, Etc)\n",
    "- Physical address\n",
    "\n",
    "If you can't figure a 'nice' way to locate something, your two last options might be:\n",
    "\n",
    "- **Find a \"parent\" element, then dig inside**\n",
    "- **Find all of a type of element** (like we did with `td` before) and get the `[0]`, `[1]`, `[2]`, etc\n",
    "- **XPath** (inspect an element, Copy > Copy XPath)\n",
    "\n",
    "These kinds of techniques tend to break when you're on other result pages, but... maybe not! You won't know until you try.\n",
    "\n",
    "> - *TIP: When you use xpath, you CANNOT use double quotes or Python will get confused. Use single quotes.*\n",
    "> - *TIP: You can clean your data up if you want to, or leave it dirty to clean later*\n",
    "> - *TIP: The address part can be tough, but you have a few options. You can use a combination of `.split` and list slicing to clean it now, or clean it later in the dataframe with regular expressions. Or other options, too, probably*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# click tldr button\n",
    "tldr_button = driver.find_element_by_id('mcrbutton')\n",
    "tldr_button.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# click tldr textbox to input text\n",
    "textbox = driver.find_element_by_id('mcrdata')\n",
    "textbox.send_keys('006565540C')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "# submit\n",
    "submit_button = driver.find_element_by_id('submit3')\n",
    "submit_button.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Name:    H & A TOWING LLC'"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "master_table = driver.find_elements_by_tag_name('tr')\n",
    "company_table = master_table[5].find_element_by_tag_name('td')\n",
    "name = company_table.text.strip()\n",
    "name"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Owner/Officer:   HANEEN ABBAS MOHAMMEDAWI / MANAGER'"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "owner_code = master_table[6].find_element_by_tag_name('td')\n",
    "owner = owner_code.text.strip()\n",
    "owner"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Phone:   512-999-8883'"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "phone_code = master_table[7].find_element_by_tag_name('td')\n",
    "phone = phone_code.text.strip()\n",
    "phone"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Certificate Information: Status:  Active'"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "status_code = master_table[8]\n",
    "status = status_code.text.strip()\n",
    "status"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "import re"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'11710 JOSEPH CLAYTON DR AUSTIN, TX. 78753'"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "address_code = master_table[9].find_elements_by_tag_name('td')[1]\n",
    "address_text = address_code.text.strip()\n",
    "address_text2 = re.sub(\"\\n\",' ',address_text)\n",
    "address_regex = r\"Physical: (.*)\"\n",
    "address_list = re.findall(address_regex,address_text2)\n",
    "for item in address_list:\n",
    "    address = item\n",
    "address"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Carrier Type:  Tow Truck Company\\nNumber of Active Tow Trucks:   2\\n\\nAddress Information\\nMailing:\\n391 ROAD 51022\\nCLEVELAND, TX. 77327\\n\\nPhysical:\\n11710 JOSEPH CLAYTON DR\\nAUSTIN, TX. 78753'"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "address_text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Adapt this to work inside of a single cell\n",
    "\n",
    "Double-check that it works. You want it to print out all of the details."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "H & A TOWING LLC\n",
      "HANEEN ABBAS MOHAMMEDAWI / MANAGER\n",
      "512-999-8883\n",
      "Active\n",
      "11710 JOSEPH CLAYTON DR AUSTIN, TX. 78753\n"
     ]
    }
   ],
   "source": [
    "driver.get(\"https://www.tdlr.texas.gov/tools_search/\")\n",
    "\n",
    "# Go across page, search, submit\n",
    "tldr_button = driver.find_element_by_id('mcrbutton')\n",
    "tldr_button.click()\n",
    "textbox = driver.find_element_by_id('mcrdata')\n",
    "textbox.send_keys('006565540C')\n",
    "submit_button = driver.find_element_by_id('submit3')\n",
    "submit_button.click()\n",
    "\n",
    "# output info\n",
    "\n",
    "# company\n",
    "master_table = driver.find_elements_by_tag_name('tr')\n",
    "company_table = master_table[5].find_element_by_tag_name('td')\n",
    "name_text = company_table.text.strip()\n",
    "name_regex = r\"Name:    (.*)\"\n",
    "name_list = re.findall(name_regex,name_text)\n",
    "for item in name_list:\n",
    "    name = item\n",
    "print(name)\n",
    "\n",
    "# owner\n",
    "owner_code = master_table[6].find_element_by_tag_name('td')\n",
    "owner_text = owner_code.text.strip()\n",
    "owner_regex = r\"Owner/Officer:   (.*)\"\n",
    "owner_list = re.findall(owner_regex,owner_text)\n",
    "for item in owner_list:\n",
    "    owner = item\n",
    "print(owner)\n",
    "\n",
    "# phone number\n",
    "phone_code = master_table[7].find_element_by_tag_name('td')\n",
    "phone_text = phone_code.text.strip()\n",
    "phone_regex = r\"Phone:   (.*)\"\n",
    "phone_list = re.findall(phone_regex,phone_text)\n",
    "for item in phone_list:\n",
    "    phone = item\n",
    "print(phone)\n",
    "\n",
    "# status\n",
    "status_code = master_table[8]\n",
    "status_text = status_code.text.strip()\n",
    "status_regex = r\"Certificate Information: Status:  (.*)\"\n",
    "status_list = re.findall(status_regex,status_text)\n",
    "for item in status_list:\n",
    "    status = item\n",
    "print(status)\n",
    "\n",
    "# address\n",
    "address_code = master_table[9].find_elements_by_tag_name('td')[1]\n",
    "address_text = address_code.text.strip()\n",
    "address_text2 = re.sub(\"\\n\",' ',address_text)\n",
    "address_regex = r\"Physical: (.*)\"\n",
    "address_list = re.findall(address_regex,address_text2)\n",
    "for item in address_list:\n",
    "    address = item\n",
    "print(address)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Using .apply to find data about SEVERAL tow truck companies\n",
    "\n",
    "The file `trucks-subset.csv` has information about the trucks, we'll use it to find the pages to scrape.\n",
    "\n",
    "### Open up `trucks-subset.csv` and save it into a dataframe"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
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
       "      <th>TDLR Number</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>006565540C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0654479VSF</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>006564940C</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  TDLR Number\n",
       "0  006565540C\n",
       "1  0654479VSF\n",
       "2  006564940C"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv('trucks-subset.csv')\n",
    "df\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Go through each row of the dataset, displaying the URL you will need to scrape for the information on that row\n",
    "\n",
    "You don't have to actually use the search form for each of these - look at the URL you're on, it has the number in it!\n",
    "\n",
    "For example, one URL might look like `https://www.tdlr.texas.gov/tools_search/mccs_display.asp?mcrnumber=006565540C`.\n",
    "\n",
    "- *TIP: Use .apply and a function*\n",
    "- *TIP: You'll need to build this URL from pieces*\n",
    "- *TIP: You probably don't want to `print` unless you're going to fix it for the next question \n",
    "- *TIP: pandas won't showing you the entire url! Run `pd.set_option('display.max_colwidth', None)` to display aaaalll of the text in a cell*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrape_trucks(df):\n",
    "    slug = df['TDLR Number']\n",
    "    link = f'https://www.tdlr.texas.gov/tools_search/mccs_display.asp?mcrnumber={slug}'\n",
    "    print(link)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://www.tdlr.texas.gov/tools_search/mccs_display.asp?mcrnumber=006565540C\n",
      "https://www.tdlr.texas.gov/tools_search/mccs_display.asp?mcrnumber=0654479VSF\n",
      "https://www.tdlr.texas.gov/tools_search/mccs_display.asp?mcrnumber=006564940C\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "0    None\n",
       "1    None\n",
       "2    None\n",
       "dtype: object"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.apply(scrape_trucks, axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Save this URL into a new column of your dataframe, called `url`\n",
    "\n",
    "- *TIP: Use a function and `.apply`*\n",
    "- *TIP: Be sure to use `return`*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrape_trucks(df):\n",
    "    slug = df['TDLR Number']\n",
    "    link = f'https://www.tdlr.texas.gov/tools_search/mccs_display.asp?mcrnumber={slug}'\n",
    "    \n",
    "    data = {}\n",
    "    data['TDLR_number'] = df['TDLR Number']\n",
    "    data['url'] = link\n",
    "    \n",
    "    return pd.Series(data)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Go through each row of the dataset, printing out information about each tow truck company.\n",
    "\n",
    "Now will be **scraping** inside of your function.\n",
    "\n",
    "- The business name\n",
    "- Owner/operator\n",
    "- Phone number\n",
    "- License status (Active, Expired, Etc)\n",
    "- Physical address\n",
    "\n",
    "Just print it out for now.\n",
    "\n",
    "- *TIP: use .apply*\n",
    "- *TIP: You'll be using the code you wrote before, but converted into a function*\n",
    "- *TIP: Remember how the TDLR Number is in the URL? You don't need to do the form submission if you don't want!*\n",
    "- *TIP: Make sure you adjust any variables so you don't scrape the same page again and again*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrape_trucks(df):\n",
    "    slug = df['TDLR Number']\n",
    "    link = f'https://www.tdlr.texas.gov/tools_search/mccs_display.asp?mcrnumber={slug}'\n",
    "    print(link)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
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
       "      <th>TDLR_number</th>\n",
       "      <th>url</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>006565540C</td>\n",
       "      <td>https://www.tdlr.texas.gov/tools_search/mccs_d...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0654479VSF</td>\n",
       "      <td>https://www.tdlr.texas.gov/tools_search/mccs_d...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>006564940C</td>\n",
       "      <td>https://www.tdlr.texas.gov/tools_search/mccs_d...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  TDLR_number                                                url\n",
       "0  006565540C  https://www.tdlr.texas.gov/tools_search/mccs_d...\n",
       "1  0654479VSF  https://www.tdlr.texas.gov/tools_search/mccs_d...\n",
       "2  006564940C  https://www.tdlr.texas.gov/tools_search/mccs_d..."
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.apply(scrape_trucks, axis=1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Scrape the following information for each row of the dataset, and save it into new columns in your dataframe.\n",
    "\n",
    "- The business name\n",
    "- Owner/operator\n",
    "- Phone number\n",
    "- License status (Active, Expired, Etc)\n",
    "- Physical address\n",
    "\n",
    "It's basically what we did before, but using the function a little differently.\n",
    "\n",
    "- *TIP: Same as above, but you'll be returning a `pd.Series` and the `.apply` line is going to be a lot longer*\n",
    "- *TIP: Save it to a new dataframe!*\n",
    "- *TIP: Make sure you change your `df` variable names correctly if you're cutting and pasting - there are a few so it can get tricky*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Save your dataframe as a CSV named `tow-trucks-extended.csv`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Re-open your dataframe to confirm you didn't save any extra weird columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Process the entire `tow-trucks.csv` file\n",
    "\n",
    "We just did it on a short subset so far. Now try it on all of the tow trucks. **Save as the same filename as before**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.8.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
