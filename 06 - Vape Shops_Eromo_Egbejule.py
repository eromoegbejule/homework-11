{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Scraping Maryland Business Licenses with Selenium\n",
    "\n",
    "Maryland has a [great portal](https://jportal.mdcourts.gov/license/pbPublicSearch.jsp) for searching business licenses, but the only problem is you have to check a box in order to get in.\n",
    "\n",
    "1. Try to visit [the public search page](https://jportal.mdcourts.gov/license/pbPublicSearch.jsp)\n",
    "2. Get redirected to a \"I agree to this\" page. Click that you've read the disclaimer, click Enter the Site.\n",
    "3. Click \"Search License Records\" down at the bottom of the page\n",
    "4. You're now on the search page! From the \"Jurisdiction\" dropdown, select \"Statewide\"\n",
    "5. In the \"Trade Name\" field, type \"Vap%\" to try to find vape shops\n",
    "6. Click \"Next\" in the bottom right-hand corner to go to the next page\n",
    "7. Click \"Click for detail\" to see the details for a specific business license.\n",
    "\n",
    "That's a lot of stuff! **Let's get to work.**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Import what you need"
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
    "driver.get(\"https://jportal.mdcourts.gov/license/pbPublicSearch.jsp\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Preparation\n",
    "\n",
    "### When you search for a business license, what URL should Selenium try to visit first?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Evade disclaimer\n",
    "box = driver.find_element_by_id('checkbox')\n",
    "box.click()\n",
    "submit_button = driver.find_elements_by_class_name('copy')[1].find_elements_by_tag_name('input')[1]\n",
    "submit_button.click()"
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
    "**It isn't going to work, though! It's going to redirect to that intro page.** You can use *Incognito mode* to go back through the \"Check the box, etc\" series of pages, or you can close and re-open Chrome.\n",
    "\n",
    "- Check the checkbox, then submit the form to accept their terms of service\n",
    "\n",
    "Selenium can submit forms by either\n",
    "\n",
    "- Selecting the form and using `.submit()`, or\n",
    "- Selecting the button and using `.click()`\n",
    "\n",
    "You only need to be able to get **one, not both.**\n",
    "\n",
    "- *TIP: if something doesn't have anything special about it, xpath might be your best bet*"
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
    "Now click the **Search License Records** link up top in the navigation to get to the search page.\n",
    "\n",
    "- *TIP: Honestly you could also just visit the URL directly now since you filled out that terms of service thing*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "get_license_search = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[6]/td[2]/a[2]')\n",
    "get_license_search.click()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Perform your search\n",
    "\n",
    "Pick \"Statewide\" for the jurisdiction dropdown, and `VAP%` into the Trade Name field. The `%` is a wildcard.\n",
    "\n",
    "*TIP: I wish I could put this on CourseWorks, but it looks too ugly: [Selenium snippets](http://jonathansoma.com/lede/foundations-2018/classes/selenium/selenium-snippets/) will help you with the dropdown*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "#select dropdown and statewide\n",
    "jurisdiction = driver.find_element_by_id('slcJurisdiction')\n",
    "jurisdiction_click = jurisdiction.click()\n",
    "statewide = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[4]/td[2]/form/table/tbody/tr[2]/td/select/option[2]')\n",
    "statewide.click()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "And now, of course, **submit the form**.\n",
    "\n",
    "- *TIP: Since scrolling to buttons can be a pain, sometimes it's easier to select the form and use `.submit()` instead of `.click()`ing the button*"
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
    "## (Try to) scrape the results\n",
    "\n",
    "Let's start by just **printing this stuff**. We'll save it as a dataframe later on.\n",
    "\n",
    "For now, just scrape **each store's name**, then cry a little. Fact: this is an impossible and miserable page. "
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
    "To avoid struggling with the search results page, we're going to use the **detail page** instead. Try to figure out how to select it and click it inside of your `for` loop.\n",
    "\n",
    "- *TIP: Instead of just looking for an `a` or an `img`, you might want to look for one of its parents first, then click. This might affect the way you print out the shop's name, too*\n",
    "- *TIP: Not all of them have links! You can wrap in try/except to skip it, or you can check to see if the shop's status is Pending.*"
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
   "metadata": {
    "collapsed": true
   },
   "source": [
    "Okay, now let's get to action. For each result, **click the link to the detail page** and print out the following information:\n",
    "\n",
    "- Mailing address\n",
    "- Location address\n",
    "- License information (you can keep it as one field)\n",
    "- Total amount paid\n",
    "- Issued by\n",
    "- If you're feeling crazy, get the licenses, too.\n",
    "\n",
    "If it doesn't have a detail page, just print out the name and that's all we need.\n",
    "\n",
    "- *TIP: `try`/`except` is probably going to be your friend. What's it do?\n",
    "- *TIP: When you're done getting the information, you probably want to click back to the search results*\n",
    "- *TIP: You might enjoy `find_element_by_partial_link_text` to do that*\n",
    "- *TIP: Licenses can be acquired by doing some really odd list slicing - think about where it starts and where it ends, relative to the beginning and end of everything.*\n",
    "\n",
    "> **IMPORTANT NOTE:** This is doomed!!!! It's useful to do, but your current process is doomed. Once you get a `stale element reference` error move on to the next cell."
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
    "### Stale message reference\n",
    "\n",
    "Once you navigate away from a page, and you go back to it, you (sometimes, usually) can't use the variables from the first time you were on the page. So, we got a list of results when we first visited, clicked to the details page, clicked back, and now our original list is \"stale.\"\n",
    "\n",
    "This is sad.\n",
    "\n",
    "Let's try this again: loop through the results and create a dataframe with `name` and `url` columns. And yes, some of them won't have URLs. No clicking links, just saving URLs."
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
    "### Getting all of the results\n",
    "\n",
    "After you've looped through the results on one page, we're going to want to go to the next page! Add a line to make it click the 'Next' button down at the bottom\n",
    "\n",
    "- *TIP: `find_element_by_partial_link_text` will be your friend*\n",
    "- *TIP: You might need to do the scrolling thing to get it onto the screen (and by that I mean, you WILL need to, so you should)*\n",
    "\n",
    "Confirm that it moves to the next page (it doesn't need to scrape anything yet)"
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
    "### Wrapping with `while`\n",
    "\n",
    "> Go back to the first page of results before you try to run this\n",
    "\n",
    "You have a bunch of scraping code. It clicks the next button, then it stops. But you'd like it to go back up to the top! You can make that happen with a special `while` loop.\n",
    "\n",
    "```python\n",
    "while True:\n",
    "    # Scrape your stuff\n",
    "    # Click next button\n",
    "```\n",
    "\n",
    "This will go on FOREVER AND EVER until there is an error (when it can't find the Next button on the last page of results, you'll get a `NoSuchElement` error when it tries to find the next button).\n",
    "\n",
    "- *Tip: Print out \"Scraping a new page\" every time you visit a new page, just to check that it's working*"
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
    "### Making it perfect\n",
    "\n",
    "> Go back to the first page of results before you try to run this\n",
    "\n",
    "Wrap all of your code in a `try`/`except` so that it doesn't finish with an error and you'll be good to go.\n",
    "\n",
    "**Confirm your list has all of the vape shops in it.** If not, check where you are creating your empty list (`[]`) - if you do it in the wrong spot, it will overwrite your list every time you visit a page."
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
    "### Save this data as a csv\n",
    "\n",
    "The filename should be `vape-shops-basic.csv`. You should have 24 rows."
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
    "# Okay, let's scrape!\n",
    "\n",
    "All right, get the actual data!\n",
    "\n",
    "### Look at the URL of your first row\n",
    "\n",
    "- *TIP: Remember `pd.set_option('display.max_colwidth', None)` will let you see alllll of your strings*"
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
    "### Okay, it doesn't have a URL!\n",
    "\n",
    "Let's drop all of the ones without URLs. You should be down to **17 rows**"
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
    "Now look at the first one."
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
    "### Use Selenium to visit that page"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# .iloc[0] means \"give me the first row\", kind of like .head(1), but\n",
    "# it allows me to use .url to pull out the actual url. I only did this\n",
    "# so that I could use a variable - you just needed to cut and paste\n",
    "url = df.iloc[0].url\n",
    "url"
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
    "### Now, just like you did before, grab the additional data\n",
    "\n",
    "You should probably save it into a dictionary! Don't try to put it into the dataframe yet, though. You want:\n",
    "\n",
    "- Mailing address\n",
    "- Location address\n",
    "- License information (you can keep it as one field)\n",
    "- Total amount paid\n",
    "- Issued by\n",
    "- If you're feeling crazy, get the licenses, too.\n",
    "\n",
    ".\n",
    "\n",
    "- *TIP: Licenses can be acquired by doing some really odd list slicing - think about where it starts and where it ends, relative to the beginning and end of everything.*\n",
    "- *TIP: If you've gotten addicted to xpath, total amount paid and issued by might not work with it when doing other shops. You'll want to test it! It's because xpath relies on things like \"it's the fourth row\" but maybe there are more or fewer licenses sometimes, right? But you know it's always a certain number from the last row, so maybe use negative numbers with `.find_elements_by_...`? This is probably a confusing explanation.*"
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
    "### Move all of this into one cell\n",
    "\n",
    "It should visit the URL, then grab the data and put it into a dictionary."
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
    "### Change it into a function\n",
    "\n",
    "You'll want to have this function accept a `row`, and send back a `pd.Series`. You can just use `pd.Series(your_dictionary)` (but it better have a better name than `your_dictionary`!).\n",
    "\n",
    "- *TIP: Make sure you `return` something!*\n",
    "- *TIP: Make sure you change everything to reflect the row's url, not the URL you typed in*"
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
    "### Use your dataframe and `.apply` to pull all of the data from the vape shops\n",
    "\n",
    "Once you know it's working, use the whole \n",
    "\n",
    "- *TIP: Try using it with `.head(3)` first*\n",
    "- *TIP: You'll want to use `.apply` with your new function*\n",
    "- *TIP: Issued By and Total Paid are goign to give you problems if you tried to use xpath! Try checking the classes and think about find_elementSSSSS and working backwards instead of forwards.*\n",
    "- *TIP: You might need a `try`/`except`*\n",
    "- *TIP: Make sure you're using `axis=1`*\n",
    "- *TIP: Use `.join` the big thing with all of the `dfs` - make sure you name them right!*"
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
    "## Save as `vape-total.csv`\n",
    "\n",
    "Make sure you don't save the index! Open it up in a text editor or Excel to make sure it's correct."
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
