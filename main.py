import subprocess
subprocess.call(["python", "image_scraper.py"])
print("Do you want to continue? y/n : ", end="")
x = input()
if x == "y" or x == "Y":
    subprocess.call(["python", "photoshopy.py"])
else:
    print("Bye Bye!")