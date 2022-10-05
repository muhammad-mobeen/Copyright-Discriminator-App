import photoshop.api as ps
# import win32com.client
# from photoshop import Session
import os


# style 1

# psApp = win32com.client.Dispatch("Photoshop.Application")

# psApp.Open(os.getcwd() + r"\script_template.psd")

# psApp.doJavaScript(os.getcwd() + r"\script.jsx")

app = ps.Application()
app.load(os.getcwd() + r"\script_template.psd")
app.doJavaScript(os.getcwd() + r"\script.jsx")