"""Python Wrapper"""
# Libraries
import customtkinter
import json

# Custom Imports
from Frames.LeftFrame import LeftFrame
from Frames.TopRightFrame import TopRightFrame
from Frames.BottomRightFrame import BottomRightFrame
from Frames.MiddleRightFrame import MiddleRightFrame


class MainWindow:
    """
    Main Window Class
    """

    def __init__(self) -> None:
        """
        Main Window Class.

        Does not require any parameters.
        """

        # Empty Dictionary for the File later.

        self.json_file = {}
        self.file_location = ""

        self.medium = {}
        self.sources = {}
        self.objects = {}
        self.screen = {}

        self.hierarchy = []

        # App Settings:

        self.app = customtkinter.CTk()

        self.width = 1200
        self.height = 800

        # Window Creation:

        self.app.title("Raytracing Viewer")
        self.app.geometry(f"{self.width}x{self.height}+0+0")
        self.app.grid_columnconfigure((1), weight=1)
        self.app.grid_rowconfigure((1, 0), weight=1)
        self.app.grid_propagate(False)
        self.app.resizable(False, False)

        # Frames

        self.left_frame = LeftFrame(self)
        self.top_right_frame = TopRightFrame(self)
        self.bottom_right_frame = BottomRightFrame(self)
        self.middle_right_frame = MiddleRightFrame(self)

    def main_loop(self) -> None:
        """
        Main Loop of Main Window (Use this to start it)
        """

        print("Debug Log: Starting Main Window.")
        self.app.mainloop()

    def load_file(self) -> None:
        """
        Loads the file into memory from the stored path.

        Requires having the self.file_location to be set.
        """

        print("Debug Log: Loading file given.")

        with open(self.file_location, "r") as f:
            self.json_file = json.load(f)

    def prepare_file(self) -> None:
        """
        Prepares input file for further usage. Requires the file to be loaded.
        """

        # First, we try to load the medium.
        try:
            self.medium = self.json_file["medium"]
            print("\nDebug Log: Found Medium Settings")
        except KeyError:
            print("\nWeak Error Log: Medium does not exist in file.")

        # Now the sources
        try:
            self.sources = self.json_file["sources"]
            print("Debug Log: Found Sources Settings")
        except KeyError:
            print("Weak Error Log: Sources does not exist in file.")

        # Now the objects
        try:
            self.objects = self.json_file["objects"]
            print("Debug Log: Found Objects Settings")
        except KeyError:
            print("Important Error Log: Objects does not exist in file.")
        try:
            self.screen = self.json_file["screen"]
            print("Debug Log: Found Screen Settings")
        except KeyError:
            print("Weak Error Log: Screen does not exist in file.")

        # Now we hope we have extracted everything.

        print("\n")


# Main Function
if __name__ == '__main__':

    # Create the Window Object and run it.
    app = MainWindow()
    app.main_loop()
