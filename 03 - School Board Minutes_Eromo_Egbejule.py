{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# School Board Minutes\n",
    "\n",
    "Scrape all of the school board minutes from http://www.mineral.k12.nv.us/pages/School_Board_Minutes\n",
    "\n",
    "Save a CSV called `minutes.csv` with the date and the URL to the file. The date should be formatted as YYYY-MM-DD.\n",
    "\n",
    "**Bonus:** Download the PDF files\n",
    "\n",
    "**Bonus 2:** Use [PDF OCR X](https://solutions.weblite.ca/pdfocrx/index.php) on one of the PDF files and see if it can be converted into text successfully.\n",
    "\n",
    "* **Hint:** If you're just looking for links, there are a lot of other links on that page! Can you look at the link to know whether it links or minutes or not? You'll want to use an \"if\" statement.\n",
    "* **Hint:** You could also filter out bad links later on using pandas instead of when scraping\n",
    "* **Hint:** If you get a weird error that you can't really figure out, you can always tell Python to just ignore it using `try` and `except`, like below. Python will try to do the stuff inside of 'try', but if it hits an error it will skip right out.\n",
    "* **Hint:** Remember the codes at http://strftime.org\n",
    "* **Hint:** If you have a date that you've parsed, you can use `.dt.strftime` to turn it into a specially-formatted string. You use the same codes (like %B etc) that you use for converting strings into dates.\n",
    "\n",
    "```python\n",
    "try:\n",
    "  blah blah your code\n",
    "  your code\n",
    "  your code\n",
    "except:\n",
    "  pass\n",
    "```\n",
    "\n",
    "* **Hint:** You can use `.apply` to download each pdf, or you can use one of a thousand other ways. It'd be good `.apply` practice though!"
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
    "import requests\n",
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
    "driver.get(\"http://www.mineral.k12.nv.us/pages/School_Board_Minutes\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "page = driver.find_element_by_id('livesite-page-content-left')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "minute_page2 = page.find_elements_by_tag_name('p')[4:-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "minutesss = []\n",
    "for item in minute_page2:\n",
    "    date = item.text.strip()\n",
    "#     print(date)\n",
    "    try:\n",
    "        url = item.find_element_by_tag_name('a').get_attribute('href')\n",
    "        minutesss.append({\n",
    "            'date': date,\n",
    "            'url': url\n",
    "        })\n",
    "    except:\n",
    "        pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
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
       "      <th>date</th>\n",
       "      <th>url</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>September 1, 2020</td>\n",
       "      <td>http://www.mineral.k12.nv.us/files/9.1.20_minu...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>August 11, 2020</td>\n",
       "      <td>http://www.mineral.k12.nv.us/files/8.11.20_min...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>July 28, 2020</td>\n",
       "      <td>http://www.mineral.k12.nv.us/files/7.28.20_min...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>July 14, 2020</td>\n",
       "      <td>http://www.mineral.k12.nv.us/files/7.14.20_min...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>June 16, 2020</td>\n",
       "      <td>http://www.mineral.k12.nv.us/files/6.16.20_min...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                date                                                url\n",
       "0  September 1, 2020  http://www.mineral.k12.nv.us/files/9.1.20_minu...\n",
       "1    August 11, 2020  http://www.mineral.k12.nv.us/files/8.11.20_min...\n",
       "2      July 28, 2020  http://www.mineral.k12.nv.us/files/7.28.20_min...\n",
       "3      July 14, 2020  http://www.mineral.k12.nv.us/files/7.14.20_min...\n",
       "4      June 16, 2020  http://www.mineral.k12.nv.us/files/6.16.20_min..."
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.DataFrame(minutesss)\n",
    "df.head()"
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
