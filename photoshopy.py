import photoshop.api as ps
# import win32com.client
# from photoshopy import Session
import os

class Photoshop_Manager:
    def __init__(self):
        self.app = ps.Application()
        self.doc = self.app.load(os.getcwd() + r"\script_template.psd")
        self.boss_layer = self.doc.layers.getByName("Group 1")
        self.images_list = os.listdir(os.getcwd()+ r"\Images")
        self.desc = ps.ActionDescriptor()
        self.jsx_file = os.getcwd() + r"\script.jsx"
    
    def remove_prev_clutter(self):
        print("\nDeleting previous data___________________________")
        if self.doc.layers.length > 1:
            for layer in self.doc.layers:
                if layer.name != self.boss_layer.name:
                    print("{} Deleted!".format(layer.name))
                    layer.remove()
        print("Done_____________________________________________")
    
    def import_images(self):
        print("\nImporting Images_________________________________")
        for img in self.images_list:
            self.desc.putPath(self.app.charIDToTypeID("null"), os.getcwd() + "\\Images\\" + img)
            event_id = self.app.charIDToTypeID("Plc ")  # `Plc` need one space in here.
            self.app.executeAction(event_id, self.desc)
            print("{} Imported!".format(img))
        print("All Images Imported Successfully_________________")

    def arrange_layer_stack(self):
        print("\nArranging Layer Stack____________________________")
        for layer in self.doc.layers:
            if layer.name != self.boss_layer.name:
                layer.move(self.boss_layer, ps.ElementPlacement.PlaceAfter)
                layer.visible = False
                print("{} Moved and non-visible!".format(layer.name))
        print("Layer Stack Arranged_____________________________")

    def save_changes(self):
        self.doc.save()
        print("\nChanges Saved Successfully!")

    def run_script(self):
        print("\nRunning script.jsx..............")
        with open(self.jsx_file, "r") as f:
            ps_script = f.read()
        self.app.doJavaScript(ps_script)
        print("\nScript ran successfully. All Images edited!")

    def exit(self):
        self.doc.close()


if __name__ == "__main__":
    agent = Photoshop_Manager()
    agent.remove_prev_clutter()
    agent.import_images()
    agent.arrange_layer_stack()
    agent.save_changes()
    agent.run_script()
    agent.exit()