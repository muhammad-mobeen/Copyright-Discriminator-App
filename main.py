import subprocess
subprocess.call(["python", "image_scraper.py"])
print("Do you want to photoshop the images? y/n : ", end="")
x = input()
if x == "y" or x == "Y":
    subprocess.call(["python", "photoshopy.py"])
else:
    print("Bye Bye!")

print("Do you want to discriminate? y/n : ", end="")
y = input()
if y == "y" or y == "Y":
    subprocess.call(["python", "discriminator.py"])
else:
    print("Bye Bye!")