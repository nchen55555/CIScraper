# CIScraper

webscraper.ipynb contains a function that gets the user’s username given a specific hash tag post
Filter_profiles.ipynb filters profiles so we get legitimate users 
	Criteria: 
10K+ followers 
500+ likes on most recent post
 
1. get list of usernames by searching for a hashtag
2. export usernames to csv
3. read csv and run get_user_email on all usernames
4. export data (username, email) to csv (additional data you might want to export: num of followers, age)
 
** NOTE: we should probably only run get_user_email on accounts that have 20k+ followers and a certain ratio of followers to engagement (e.g. likes/comments) on their most recent post. Since there are bot accounts on IG that have fake emails, these fake emails might freeze our account if we send an email to them!!! **

## How to Run
Run program through webscraper.ipynb file, inputting specific hashtag requests accordingly.
