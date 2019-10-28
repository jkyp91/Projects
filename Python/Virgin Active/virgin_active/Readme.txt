Virgin Active Class Booker

--Getting Started--
You'll need python 3.7 and to install the package requirements. This can be 
done by running the command `pip3 install -r requirements.txt`.

--Contents--
The two main files in the script are `class_booker.py` and `club_information.py`.
The former attempts to book classes that satisfy the following conditions:
- Not already booked
- Not full
- Reformer Pilates at 6:45 / 7:00 on a Weekday
- 9:00 Weekend

The conditions can be modified in the `is_valid_class` function found in the
`http_requests.py` file.

The latter file, downloads and caches the clubs classes and the instructor names.
These are viewable in the `data` folder.

--Login Information--
Currently, username and password information are stored in the `secrets.py` file.
This isn't best practice but because no one else will use this, it's ok.

--Running the script--
The club's information seems to change every now again and therefore the 
`club_information.py` should first be run. This is strictly not necessary to
book a class but ensures the displayed information is correct.

To book a class, simply then run the `class_booker.py` file.

These can both be done using the command `python3 <filename>` or if that
doesn't work `python3 -m <filename>`

--Scheduling the script--
To schedule the script, you'll need to set up a cron job. This can be done
from the terminal using crontab.

See this link for guidance.
https://www.jessicayung.com/automate-running-a-script-using-crontab/

You should probably have 2 cron jobs, one for the club info update and one
to book classes. 

The cron jobs will probably look like this:
`45 6 * * * [full_file_path]/club_information.py >/dev/null 2>&1`
`0 7 * * * [full_file_path]/class_booker.py >/dev/null 2>&1`

Before doing that, you'll need to make sure that you change a) the shebang at
the top of each script (see the file) and b) you make the file executable. You
can do this with the command `chmod +x <file>`. 
