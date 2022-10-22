# CIScraper

This webscraper is utilized for the purposes of Campus Insights user recruitment. The application retrieves social media handles given a specific hash tag post or topic, filtering profiles to legitimate users of 10K+ followers with 500+ likes on the most recent post. Then it exports the usernames to csv to which we read the csv and run get_user_email on all usernames that are public to acquire emails. If the handles are not public, we store them in a separate csv. 

## How to Run
Run program through webscraper.py file. Need to install selenium first through pip3 install selenium
