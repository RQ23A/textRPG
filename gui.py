#!/usr/bin/python
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from windows import Window
import time

class App():

    def __init__(self):

        # Main window creation
        self.app = Window()
        self.app.set_size(640,480)
        self.app.set_title("Game")

        # Creates the text box to type commands
        self.textentry = Gtk.Entry()
        self.textentry.set_placeholder_text("Insert command")
        self.textentry.connect("activate", self.do_stuff)

        # Creates the text windows to display output
        self.textview_story = Gtk.TextView()
        self.textbuffer_story = self.textview_story.get_buffer()
        self.textview_story.set_editable(False)
        self.textview_story.set_cursor_visible(False)
        self.textview_story.set_wrap_mode(Gtk.WrapMode.WORD)

        self.textview_cmdhist = Gtk.TextView()
        self.textbuffer_cmdhist = self.textview_cmdhist.get_buffer()
        self.textview_cmdhist.set_editable(False)
        self.textview_cmdhist.set_cursor_visible(False)

        self.textview_sidebar = Gtk.TextView()
        self.textbuffer_sidebar = self.textview_sidebar.get_buffer()
        self.textview_sidebar.set_editable(False)
        self.textview_sidebar.set_cursor_visible(False)

        # Create panes to divide the main window
        self.hpaned = Gtk.Paned.new(Gtk.Orientation.HORIZONTAL)
        self.hpaned.set_position(480)
        self.app.add_to_win(self.hpaned)

        self.vpaned1 = Gtk.Paned.new(Gtk.Orientation.VERTICAL)
        self.hpaned.add1(self.vpaned1)
        self.hpaned.add2(self.textview_sidebar)
        self.vpaned1.set_position(290)

        self.vpaned2 = Gtk.Paned.new(Gtk.Orientation.VERTICAL)
        self.vpaned1.add2(self.vpaned2)
        self.vpaned2.set_position(150)

        self.vpaned1.add1(self.textview_story)
        self.vpaned2.add1(self.textview_cmdhist)
        self.vpaned2.add2(self.textentry)

        # Set escape key to close app
        accGroup = Gtk.AccelGroup()
        key, modifier = Gtk.accelerator_parse('Escape')
        accGroup.connect(key, modifier, Gtk.AccelFlags.VISIBLE, Gtk.main_quit)
        self.app.add_accel_group(accGroup)

        self.app.show_all()

    def do_stuff(self, widget):

        text = widget.get_text() # Gets text from widget
        self.save_hist(text)
        if text == "help":
            self.print_text("Si ayuda es lo que buscas, aquí no la encontrarás.")
        elif text == "hola":
            self.print_text("Hola valiente jugador! Para la ayuda, escribe 'help' en la sección de comandos")
        widget.set_text('')

    def print_text(self, printable):

        time.sleep(2)
        self.textbuffer_story.set_text(printable)

    def save_hist(self, cmd):

        end_text = self.textbuffer_cmdhist.get_end_iter()
        self.textbuffer_cmdhist.insert(end_text, '> ' + cmd + '\n')

# Main loop

def main():
    app = App()
    Gtk.main()
if __name__=="__main__":
    main()
         
