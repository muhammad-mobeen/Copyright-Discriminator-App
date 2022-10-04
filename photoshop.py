import win32com.client
import os

psApp = win32com.client.Dispatch("Photoshop.Application")

psApp.Open(r"D:\Github\Copyright-Discriminator-App\Images\1200px-Badshahi_Mosque_front_picture.jpg")

