# To run: python3 Window.py

import gi
gi.require_version('Gtk', '3.0');
from gi.repository import Gtk


class BlackjackWindow (Gtk.Window):

    def __init__ (self):
        Gtk.Window.__init__ (self, title= "Blackjacker");
        self.set_size_request (300, 180);


def main():
    win = BlackjackWindow ();
    win.connect ("delete-event", Gtk.main_quit);
    win.show_all ();
    Gtk.main ();

if __name__ == '__main__':
    main()
