#!/usr/bin/python

from gi.repository import Gtk

class Window():

    def __init__(self):

        self.win = Gtk.Window()
        self.win.set_position(Gtk.WindowPosition.CENTER)
        self.win.connect("destroy", Gtk.main_quit)

    def set_size(self, sizex, sizey):

        self.win.set_default_size(sizex,sizey)

    def set_title(self, title):

        self.win.set_title(title)

    def add_to_win(self, obj):

        self.win.add(obj)

    def close_win(self, window):

        Gtk.main_quit()

    def add_accel_group(self, group):

        self.win.add_accel_group(group)

    def hide(self, widget):

        self.win.hide()

    def show_all(self):

        self.win.show_all()
