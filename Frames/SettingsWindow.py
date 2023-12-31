"""Settings Window"""

import customtkinter
from Frames.CustomElements.scrollableentry import ScrollableEntry
from Frames.ColorSettingsWindow import ColorSettingsWindow


def has_non_zero_element(list_to_check: list) -> bool:
    """
    Checks if a list has a non-zero element.
    :param list_to_check: List to check in.
    :return: True if it contains one and False if not.
    """

    for e in list_to_check:
        if e != 0:
            return True

    return False


def recurse_until_found_or_not(object_to_find, current_object, object_to_find_name: str, debug: bool = False) -> object:
    """
    Recurse over an object list and checks until finding the object requested.
    """

    # Since the Object we want to find is that one, we can be happy and do what we wanted.
    if debug:
        print("\nComparing both objects:", current_object, object_to_find, "with name: ", object_to_find_name)

    if type(current_object) == dict:
        # Dictionary Object:
        try:
            return recurse_until_found_or_not(object_to_find, current_object["sphere"], "Sphere")
        except KeyError:
            pass

        try:
            return recurse_until_found_or_not(object_to_find, current_object["halfspace"], "Halfspace")
        except KeyError:
            pass

        try:

            if current_object["Group"] == object_to_find:
                return object_to_find

            for obj in current_object["Group"].objects:

                if debug:
                    print(f"Group JSON: New Object {obj}")

                new_obj = recurse_until_found_or_not(object_to_find, obj, obj.__class__.__name__.title())

                if new_obj == object_to_find:
                    return object_to_find

            return None

        except KeyError:
            print("Weak Error Log: Dictionary Object is Unknown")
            return None

    if current_object is object_to_find:
        return object_to_find

    elif object_to_find_name == "Group":

        for obj in current_object:
            if debug:
                print(f"Group Objects: New Object {obj}")

            new_obj = recurse_until_found_or_not(object_to_find, obj, obj.__class__.__name__.title())

            if new_obj == object_to_find:
                return object_to_find

        return None

    elif object_to_find is None:
        return None

    elif object_to_find_name == "Sphere":
        if object_to_find == current_object:
            return current_object
        else:
            return None

    elif object_to_find_name == "Halfspace":

        if object_to_find == current_object:
            return current_object
        else:
            return None

    elif object_to_find_name == "Group":

        for obj in current_object["Group"]:
            if debug:
                print(f"Group JSON: New Object {obj}")

            new_obj = recurse_until_found_or_not(object_to_find, obj, obj.__class__.__name__.title())

            if new_obj == object_to_find:
                return object_to_find

        return None

    else:
        print(f"\nWeak Error Log: Unknown Object: Returning None. Object is {current_object} with object to find"
              f" {object_to_find} and type of current object {type(current_object)}")

        return None


class SettingsWindow:
    """
    Settings Window Class to call it.
    """

    def __init__(self, object_to_display, master_app, main_reference) -> None:
        """
        Class representing a settings window.

        :param object_to_display: Object to display in Window.
        :param master_app: Main Window Reference
        """

        # Values
        self.object_to_display = object_to_display
        self.app = master_app
        self.main = main_reference

        # Window Constants
        self.width = 400
        self.height = 870

        self.toplevel = None

        # Frame
        self.main_frame = None

        # Label and Textbox for Position
        self.position_label = None
        self.position_textbox_x = None
        self.position_textbox_y = None
        self.position_textbox_z = None

        # Translation
        self.translate_label = None
        self.translate_textbox_0 = None
        self.translate_textbox_1 = None
        self.translate_textbox_2 = None
        self.translation = None

        # Rotation
        self.rotation_label = None
        self.rotation_textbox_0 = None
        self.rotation_textbox_1 = None
        self.rotation = None

        # Scale
        self.scale_label = None
        self.scale_textbox_0 = None
        self.scale_textbox_1 = None
        self.scale_textbox_2 = None
        self.scale = None

        # Index
        self.index_label = None
        self.index = None
        self.index_textbox = None

        # Parent
        self.parent_label = None
        self.parent = None
        self.parent_select_box = None

        # Radius
        self.radius_label = None
        self.radius = None
        self.radius_textbox = None

        # Normal Vector
        self.normal_label = None
        self.normal = None
        self.normal_textbox_x = None
        self.normal_textbox_y = None
        self.normal_textbox_z = None

        # Color settings
        self.color_label = None
        self.color_button = None

        self.colors = None
        self.colors_window = None

        # Save
        self.save_button_without_close = None
        self.save_button_with_close = None
        self.close_without_saving_button = None

        # Later Initialized Values
        self.object_coordinates = None
        self.name = None

    def open_window(self) -> None:
        """
        Opens the window for settings. (Must have created instance of class or else this will fail)
        """

        # Main Window
        self.toplevel = customtkinter.CTkToplevel(self.app)

        # Getting name
        self.name = self.object_to_display.__class__.__name__.title()

        self.toplevel.title(f"Settings Window -- {self.name}")
        self.toplevel.geometry(f"{self.width}x{self.height}")
        self.toplevel.grid_propagate(False)
        self.toplevel.resizable(False, False)

        # Most Important Frame
        self.main_frame = customtkinter.CTkFrame(self.toplevel)
        self.main_frame.configure(border_width=2, height=self.height - 10, width=self.width - 10)
        self.main_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nw")
        self.main_frame.grid_propagate(False)

        # Global Attributes are added first:

        # Translate
        self.translate_label = customtkinter.CTkLabel(self.main_frame, text="Translation: ", justify="center",
                                                      width=20, font=("Franklin Gothic Medium", 22))
        self.translate_label.grid(row=0, column=0, padx=15, pady=(10, 0))

        self.translation = self.object_to_display.translation

        self.translate_textbox_0 = ScrollableEntry(master=self.main_frame,
                                                   placeholder_text=self.translation[0], column=1,
                                                   text_in_front="X: ")
        self.translate_textbox_1 = ScrollableEntry(master=self.main_frame,
                                                   placeholder_text=self.translation[1], column=1, row=1,
                                                   text_in_front="Y: ")
        self.translate_textbox_2 = ScrollableEntry(master=self.main_frame,
                                                   placeholder_text=self.translation[2], column=1, row=2,
                                                   text_in_front="Z: ", pady=(10, 0))

        # Rotation
        self.rotation_label = customtkinter.CTkLabel(self.main_frame, text="Rotation: ", justify="center",
                                                     width=20, font=("Franklin Gothic Medium", 22))
        self.rotation_label.grid(row=3, column=0, padx=15, pady=(10, 0))

        self.rotation = self.object_to_display.rotation

        self.rotation_textbox_0 = ScrollableEntry(master=self.main_frame,
                                                  placeholder_text=self.rotation[0], column=1, row=3,
                                                  text_in_front="Angle: ")
        self.rotation_textbox_1 = ScrollableEntry(master=self.main_frame,
                                                  placeholder_text=self.rotation[1], column=1, row=4,
                                                  text_in_front="Dir.: ")

        # Scale
        self.scale_label = customtkinter.CTkLabel(self.main_frame, text="Scale: ", justify="center",
                                                  width=20, font=("Franklin Gothic Medium", 22))
        self.scale_label.grid(row=6, column=0, padx=15, pady=(10, 0))

        self.scale = self.object_to_display.scaling

        self.scale_textbox_0 = ScrollableEntry(master=self.main_frame,
                                               placeholder_text=self.scale[0], column=1, row=6,
                                               text_in_front="X: ")
        self.scale_textbox_1 = ScrollableEntry(master=self.main_frame,
                                               placeholder_text=self.scale[1], column=1, row=7,
                                               text_in_front="Y: ")
        self.scale_textbox_2 = ScrollableEntry(master=self.main_frame,
                                               placeholder_text=self.scale[2], column=1, row=8,
                                               text_in_front="Z: ", pady=(10, 0))

        current_row = 15

        # Coordinates of Object (If it is not a Group)
        if self.name == "Group":
            print("Debug Log: Given Object is a Group and does not contain any coordinates.")
        else:

            # Label and Textbox for Position
            self.position_label = customtkinter.CTkLabel(self.main_frame, text="Position: ", justify="center",
                                                         width=20, font=("Franklin Gothic Medium", 22))
            self.position_label.grid(row=9, column=0, padx=15, pady=(10, 0))

            self.object_coordinates = self.object_to_display.position

            self.position_textbox_x = ScrollableEntry(master=self.main_frame,
                                                      placeholder_text=self.object_coordinates[0], column=1,
                                                      text_in_front="X: ", row=9)
            self.position_textbox_y = ScrollableEntry(master=self.main_frame,
                                                      placeholder_text=self.object_coordinates[1], column=1, row=10,
                                                      text_in_front="Y: ")
            self.position_textbox_z = ScrollableEntry(master=self.main_frame,
                                                      placeholder_text=self.object_coordinates[2], column=1, row=11,
                                                      text_in_front="Z: ")

            # Index

            self.index_label = customtkinter.CTkLabel(self.main_frame, text="Index: ", justify="center",
                                                      width=20, font=("Franklin Gothic Medium", 22))

            self.index_label.grid(row=12, column=0, padx=15, pady=(10, 0))

            self.index = self.object_to_display.index

            self.index_textbox = ScrollableEntry(master=self.main_frame,
                                                 placeholder_text=self.index, column=1, row=12,
                                                 text_in_front="Index: ", _type="int", disable_negative_zero=True,
                                                 pady=(10, 0))

            # Parent

            self.parent = self.object_to_display.parent

            values_for_parent = [str(self.parent)]

            if "None" not in values_for_parent:
                values_for_parent.append("None")

            self.parent_label = customtkinter.CTkLabel(self.main_frame, text="Parent: ", justify="center",
                                                       width=20, font=("Franklin Gothic Medium", 22))

            self.parent_label.grid(row=13, column=0, padx=15, pady=(10, 0))

            self.parent_select_box = customtkinter.CTkComboBox(self.main_frame,
                                                               values=values_for_parent, width=200, height=24)
            self.parent_select_box.set(str(self.parent))
            self.parent_select_box.grid(row=13, column=1, padx=(5, 0), pady=(10, 0),
                                        columnspan=4)

            # Color Button

            self.color_label = customtkinter.CTkLabel(self.main_frame, text="Color Settings: ", justify="center",
                                                      width=40, font=("Franklin Gothic Medium", 22))

            self.color_label.grid(row=14, column=0, padx=15, pady=(10, 0))

            self.color_button = customtkinter.CTkButton(master=self.main_frame, text="Open Colors",
                                                        command=self.open_colors_window)
            self.color_button.grid(row=14, column=1, padx=(50, 0), pady=(10, 0), columnspan=4)

            # If the Object has unique attributes:

            if self.name == "Sphere":

                # Radius
                self.radius_label = customtkinter.CTkLabel(self.main_frame, text="Radius: ", justify="center",
                                                           width=20, font=("Franklin Gothic Medium", 22))

                self.radius_label.grid(row=15, column=0, padx=15, pady=(10, 0))

                self.radius = self.object_to_display.radius

                self.radius_textbox = ScrollableEntry(master=self.main_frame, placeholder_text=self.radius, column=1,
                                                      row=15, text_in_front="r: ", greater_than_zero=True,
                                                      pady=(10, 0), sticky="w")
                current_row += 2

            elif self.name == "Halfspace":
                # Normal Vector
                self.normal_label = customtkinter.CTkLabel(self.main_frame, text="Normal: ", justify="center",
                                                           width=20, font=("Franklin Gothic Medium", 22))

                self.normal_label.grid(row=15, column=0, padx=15, pady=(10, 0))

                self.normal = self.object_to_display.normal

                self.normal_textbox_x = ScrollableEntry(master=self.main_frame, placeholder_text=self.normal[0],
                                                        column=1,
                                                        row=15, text_in_front="X: ",
                                                        pady=(10, 0))

                self.normal_textbox_y = ScrollableEntry(master=self.main_frame, placeholder_text=self.normal[1],
                                                        column=1,
                                                        row=16, text_in_front="Y: ",
                                                        pady=(10, 0))

                self.normal_textbox_z = ScrollableEntry(master=self.main_frame, placeholder_text=self.normal[2],
                                                        column=1,
                                                        row=17, text_in_front="Z: ",
                                                        pady=(10, 0))
                current_row += 3

        # Save Buttons
        self.save_button_without_close = customtkinter.CTkButton(master=self.main_frame, text="Save Changes ",
                                                                 command=self.update_object_with_new_data, width=200)
        self.save_button_without_close.grid(row=current_row, column=1, padx=5, pady=(40, 0), sticky="n", columnspan=5)

        self.save_button_with_close = customtkinter.CTkButton(master=self.main_frame, text="Save Changes & Exit",
                                                              command=self.save_and_close, width=200)
        self.save_button_with_close.grid(row=current_row + 1, column=1, padx=5, pady=(20, 0), sticky="n", columnspan=5)

        self.close_without_saving_button = customtkinter.CTkButton(master=self.main_frame,
                                                                   text="Exit & Discard Unsaved Changes",
                                                                   command=self.close_self, width=200)
        self.close_without_saving_button.grid(row=current_row + 2, column=1, padx=5, pady=(20, 0),
                                              sticky="n", columnspan=5)

        # Actually Running:
        self.toplevel.grab_set()
        self.toplevel.mainloop()

    def update_object_with_new_data(self) -> None:
        """
        Updates an object with the current data. Requires a window to be open.
        """
        debug = False

        for obj in self.main.app.hierarchy:

            if debug:
                print(f"\nCurrent Object: {obj} with the name {obj.__class__.__name__.title()}"
                      f" (Finding: {self.object_to_display}).")

            object_found = recurse_until_found_or_not(self.object_to_display, obj, obj.__class__.__name__.title(),
                                                      debug)
            if object_found is not None:
                # If the Object is not empty (meaning we didn't find it)
                print("\nDebug Log: Found the object, writing the object new.")

                # Default Element Information Writing
                # Translation
                self.translation[0] = self.translate_textbox_0.get_value()
                self.translation[1] = self.translate_textbox_1.get_value()
                self.translation[2] = self.translate_textbox_2.get_value()

                if has_non_zero_element(self.translation):
                    object_found.translation = self.translation

                # Rotation
                self.rotation[0] = self.rotation_textbox_0.get_value()
                self.rotation[1] = self.rotation_textbox_1.get_value()

                if has_non_zero_element(self.rotation):
                    object_found.rotation = self.rotation

                # Scale
                self.scale[0] = self.scale_textbox_0.get_value()
                self.scale[1] = self.scale_textbox_1.get_value()
                self.scale[2] = self.scale_textbox_2.get_value()

                if has_non_zero_element(self.scale):
                    object_found.scaling = self.scale

                # Do the writing
                if self.name == "Sphere":
                    self.object_coordinates[0] = self.position_textbox_x.get_value()
                    self.object_coordinates[1] = self.position_textbox_y.get_value()
                    self.object_coordinates[2] = self.position_textbox_z.get_value()
                    self.index = self.index_textbox.get_value()
                    self.radius = self.radius_textbox.get_value()
                    self.parent = self.parent_select_box.get()

                    object_found.position = self.object_coordinates

                    object_found.index = self.index

                    object_found.radius = self.radius

                    object_found.parent = self.parent

                elif self.name == "Halfspace":
                    self.object_coordinates[0] = self.position_textbox_x.get_value()
                    self.object_coordinates[1] = self.position_textbox_y.get_value()
                    self.object_coordinates[2] = self.position_textbox_z.get_value()
                    self.index = self.index_textbox.get_value()
                    self.parent = self.parent_select_box.get()

                    self.normal[0] = self.normal_textbox_x.get_value()
                    self.normal[1] = self.normal_textbox_y.get_value()
                    self.normal[2] = self.normal_textbox_z.get_value()

                    object_found.position = self.object_coordinates
                    object_found.index = self.index
                    object_found.normal = self.normal
                    object_found.parent = self.parent

                return

        # If no object was found.
        # Let's hope that doesn't happen.

    def open_colors_window(self) -> None:
        """
        Opens the window to access the color settings. Takes over the current window.
        """
        print("Debug Log: Opening Colors Window.")

        self.colors_window = ColorSettingsWindow(self.object_to_display, self.toplevel, self,
                                                 recurse_until_found_or_not)
        self.colors_window.open_window()

        print("Debug Log: Closing Colors Window.")

        self.colors_window = None

    def close_self(self) -> None:
        """
        Closes the current Window.
        """

        print("Debug Log: Closing Settings Window.")

        # Label and Textbox for Position
        self.position_label.destroy()
        self.position_textbox_x.destroy()
        self.position_textbox_y.destroy()
        self.position_textbox_z.destroy()

        # Index
        self.index_label.destroy()
        self.index_textbox.destroy()

        # Parent
        self.parent_label.destroy()
        self.parent_select_box.destroy()

        # Radius
        if self.radius_label is not None:
            self.radius_label.destroy()
            self.radius_textbox.destroy()

        # Normal Vector
        if self.normal_label is not None:
            self.normal_label.destroy()
            self.normal_textbox_x.destroy()
            self.normal_textbox_y.destroy()
            self.normal_textbox_z.destroy()

        # Color settings
        self.color_label.destroy()
        self.color_button.destroy()

        if self.colors_window is not None:
            self.colors_window.destroy()

        # Save
        self.save_button_without_close.destroy()
        self.save_button_with_close.destroy()

        if self.close_without_saving_button is not None:
            self.close_without_saving_button.destroy()

        # Frame
        self.main_frame.destroy()

        # Window
        self.toplevel.destroy()

    def save_and_close(self) -> None:
        """
        Saves and closes the window.
        """

        self.update_object_with_new_data()
        self.close_self()
