# Reservation Bot
I built this bot with Python & Selenium to automate a booking process for my school's gym during the peak of COVID. The bot is specifically built to be able to work on other people's PCs as an all-in-one executable. I did this using pyinstaller and bundling the chomedriver executable with it.

The gym was only allowing people to lift by reservation, and there were only 12 slots available each hour. As you can imagine, 12 spots fill nearly instantly in a school of ~30,000.

The spots updated at midnight, so I coded this bot to try and get a spot quickly and reliably, as well as when I couldn't stay up until midnight to book a gym reservation. Further developments upon the bot would've been to use requests directly, and mimic the headers/request sent by an actual reservation click, but the gym went back to allowing general attendance before that happened.


----

This was my first time using Selenium, and I didn't expect to have this much code. In the future, I would of course parameterize the code/clean it up better than this, but the bot serves no purpose anymore.
