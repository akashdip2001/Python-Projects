import datetime
import time

end_time = datetime.datetime(2021, 12, 31) # change the year with a future year, Example: 2030, 2031, 2032, etc. according to your need
site_block = ["www.facebook.com", "facebook.com", "www.youtube.com", "youtube.com"]
host_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"
redirect = "127.0.0.1"

while True:
    if datetime.datetime.now() < end_time: # During working hours
        print("Working hours...")
        with open(host_path, 'r+') as host_file:
            content = host_file.read()
            for website in site_block:
                if website in content:  # If website is already blocked, pass
                    pass
                else:
                    host_file.write(redirect + " " + website + "\n")
                    
    else: # After working hours
        print("Fun hours...")
        with open(host_path, 'r+') as host_file:
            content = host_file.readlines()
            host_file.seek(0)
            for lines in content:
                if not any(website in lines for website in site_block):
                    host_file.write(lines)

            host_file.truncate()
    time.sleep(5) # Check every 5 seconds (using import time)

    # To run this script, you need to run it as an administrator
    # To do this, open the command prompt as an administrator and run the script from there
    # type "python website-block.py" to run the script

    # To unblock the websites, you can comment out the lines in the host file
    # or you can change the end_time before from the current year to the past year.
    