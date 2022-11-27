import photoshop.api as ps
# import win32com.client
# from photoshopy import Session
import os, shutil
import time


class Administrator:
    def __init__(self):
        print("Intialising..........!")
        self.psm = Photoshop_Manager()
        print("Photoshop has been Intialised.......>>>>")
        self.ps_imgs_dir = "Photoshoped_images"
        self.ps_imgs_dir_temp = "Photoshoped_images_temp"
        self.country_dir = os.getcwd() + "\\Images\\"
        self.country_list = os.listdir(self.country_dir)

    def start(self):
        if os.path.exists(self.ps_imgs_dir):
            shutil.rmtree(self.ps_imgs_dir)
            print("Successfully Deleted Previous Photoshoped Data..........>>>>>")

        for i, country in enumerate(self.country_list, 1):
            print("\n___________________________________________________________")
            print("[{}/{}] Country: {}".format(i, len(self.country_list), country))
            cities = os.listdir(self.country_dir + country)

            for x, city in enumerate(cities, 1):
                print("\n_____________________________")
                print("[{}/{}] City: {}".format(x, len(cities), city))
                places = os.listdir(self.country_dir + country + "\\" + city)

                for y, place in enumerate(places, 1):
                    print("\n_____________")
                    print("[{}/{}] Place: {}".format(y, len(places), place))
                    images_dir = self.country_dir + country + "\\" + city + "\\" + place
                    self.ps_driver(images_dir)
                    self.rename_images(place)  # Since images name are based on place names
                    self.scopify_images(country, city, place)
        # Delete temp data
        if os.path.exists(self.ps_imgs_dir_temp):
            shutil.rmtree(self.ps_imgs_dir_temp)
            print("Successfully Deleted Temporary Photoshoped Data..........>>>>>")
    
    def ps_driver(self, images_dir):
        self.psm.remove_prev_clutter()
        self.psm.import_images(images_dir)
        self.psm.arrange_layer_stack()
        self.psm.save_changes()
        self.psm.run_script()

    def rename_images(self, place):
        ps_images_list = os.listdir(self.ps_imgs_dir_temp)
        for i, img in enumerate(ps_images_list, 1):
            extension = os.path.splitext(img)[1]
            old_name = os.getcwd() + "\\" + self.ps_imgs_dir_temp + "\\" + img
            new_name = os.getcwd() + "\\" + self.ps_imgs_dir_temp + "\\" + place + str(i) + extension
            os.rename(old_name, new_name)


    # Re-arranges photoshoped images in their orginal folder structure
    def scopify_images(self, country, city, place):
        print("\n____________________________________________________________________")
        print("Scopifying the Photoshoped Images for: {}/{}/{}".format(country, city, place))
        ps_temp_dir = os.getcwd() + "\\" + self.ps_imgs_dir_temp
        main_dir = os.getcwd() + "\\" + self.ps_imgs_dir
        country_dir = main_dir + "\\" + country
        city_dir = country_dir + "\\" + city
        place_dir = city_dir + "\\" + place
        len_ps_temp_dir = len(os.listdir(ps_temp_dir))

        if not os.path.exists(main_dir):
            os.mkdir(main_dir)
        if not os.path.exists(country_dir):
            os.mkdir(country_dir)
        if not os.path.exists(city_dir):
            os.mkdir(city_dir)
        if not os.path.exists(place_dir):
            os.mkdir(place_dir)

        for i, img in enumerate(os.listdir(ps_temp_dir), 1):
            file = ps_temp_dir + "\\" + img
            move_to = place_dir + "\\"
            shutil.move(file, move_to)
            print("[{}/{}] Moved file: {} --> {}".format(i, len_ps_temp_dir, file, move_to))
        
        print("\nSuccessfully Scopified all images for: {}/{}/{}".format(country, city, place))
        print("_________________________________________________________________________")


class Photoshop_Manager:
    def __init__(self):
        self.extensions_to_avoid = [".webp", ".cms"]
        self.app = ps.Application()
        self.doc = self.app.load(os.getcwd() + r"\script_template.psd")
        self.boss_layer = self.doc.layers.getByName("Group 1")
        # self.images_list = os.listdir(os.getcwd()+ r"\Images")
        self.desc = ps.ActionDescriptor()
        self.jsx_file = os.getcwd() + r"\script.jsx"
    
    def remove_prev_clutter(self):
        print("\nDeleting previous data___________________________")
        if self.doc.layers.length > 1:
            for layer in self.doc.layers:
                if layer.name != self.boss_layer.name:
                    layer_name = layer.name
                    layer.remove()
                    print("{} Deleted!".format(layer_name))
        print("Done_____________________________________________")
    
    def import_images(self, images_dir):
        print("\nImporting Images_________________________________")
        images_list = os.listdir(images_dir)

        for img in images_list:
            try:  # Supported Formats try
                extension = os.path.splitext(img)[1]
                if not extension in self.extensions_to_avoid:
                    self.desc.putPath(self.app.charIDToTypeID("null"), images_dir + "\\" + img)
                    event_id = self.app.charIDToTypeID("Plc ")  # `Plc` need one space in here.
                    self.app.executeAction(event_id, self.desc)
                    print("{} Imported!".format(img))
                else:
                    self.app.beep()
                    print("XXXX Image: {} was avoided because of unsupported format!".format(img))
            except Exception as e:
                self.app.beep()
                print("ERROR Importing {}: {}".format(img, e))
            
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
    start_time = time.time()

    # ----------Start------------- #
    # agent = Photoshop_Manager()
    # agent.remove_prev_clutter()
    # agent.import_images()
    # agent.arrange_layer_stack()
    # agent.save_changes()
    # agent.run_script()
    # agent.exit()
    admin = Administrator()
    admin.start()
    # ------------End------------- #

    end_time = time.time() - start_time
    print("--- %s seconds ---" % (end_time))
    print("Program took: {} minutes".format(end_time/60))