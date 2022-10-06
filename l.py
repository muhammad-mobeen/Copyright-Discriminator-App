"""Import a image as a artLayer."""

from photoshop import Session
import os

images_list = os.listdir(os.getcwd()+ r"\Images")

images_path = os.getcwd() + "\\Images\\"

with Session(action="new_document") as ps:
    for img in images_list:
        desc = ps.ActionDescriptor
        print(images_path + img)
        desc.putPath(ps.app.charIDToTypeID("null"), images_path + img)
        event_id = ps.app.charIDToTypeID("Plc ")  # `Plc` need one space in here.
        ps.app.executeAction(ps.app.charIDToTypeID("Plc "), desc)

    # desc = ps.ActionDescriptor
    # desc.putPath(ps.app.charIDToTypeID("null"), os.getcwd() + r"\Images\ist.jpg")
    # event_id = ps.app.charIDToTypeID("Plc ")  # `Plc` need one space in here.
    # ps.app.executeAction(ps.app.charIDToTypeID("Plc "), desc)

# print(os.listdir(os.getcwd()+ r"\Images"))