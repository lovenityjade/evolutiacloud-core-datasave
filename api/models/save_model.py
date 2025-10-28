# save_model.py - Save file model
class Save:
    def __init__(self, savefilename, savecore, console, savesize, savepath, lastsync):
        self.savefilename = savefilename  # File name
        self.savecore = savecore          # RetroArch core used
        self.console = console            # Original console
        self.savesize = savesize          # File size in bytes
        self.savepath = savepath          # Path on server
        self.lastsync = lastsync          # Last sync date/time
