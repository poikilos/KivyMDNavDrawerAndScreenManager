from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList

# See
# https://github.com/HeaTTheatR/KivyMD/wiki/Components-Navigation-Drawer


class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class NavDrawerAndScreenManagerApp(MDApp):

    def build(self):
        return Builder.load_file("main.kv")

    def openScreen1(self, itemdrawer):
        # print("TOGGLE: {}".format(event))  # ItemDrawer object
        # print("{}:".format(itemdrawer.text)) # "Screen ?" where ?=#
        # print("{}:".format(itemdrawer.id))
        # ^ itemdrawer.id is None unless it was set in the ItemDrawer
        #   constructor call (or in kv if using kv instead).
        # print("{}:".format(itemdrawer.name))
        self.openScreen("screen1")

    def openScreen2(self, itemdrawer):
        self.openScreen("screen2")

    def openScreen(self, screenName):
        self.root.ids.screen_manager.current = screenName
        self.root.ids.nav_drawer.set_state("close")

    def on_start(self):
        self.root.ids.content_drawer.ids.md_list.add_widget(
            ItemDrawer(icon="screen1", text="Screen 1",
                       on_release=self.openScreen1)
        )
        self.root.ids.content_drawer.ids.md_list.add_widget(
            ItemDrawer(icon="screen2", text="Screen 2",
                       on_release=self.openScreen2)
        )


if __name__ == "__main__":
    NavDrawerAndScreenManagerApp().run()
