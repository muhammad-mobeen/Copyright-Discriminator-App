import photoshop.api as ps
# import win32com.client
# from photoshopy import Session
import os


# style 1

# psApp = win32com.client.Dispatch("Photoshop.Application")

# psApp.Open(os.getcwd() + r"\script_template.psd")

# psApp.doJavaScript(os.getcwd() + r"\script.jsx")

app = ps.Application()
app.load(os.getcwd() + r"\script_template.psd")
jsx_file = os.getcwd() + r"\script.jsx"
with open(jsx_file, "r") as f:
    scripte = f.read()

app.doJavaScript(scripte)