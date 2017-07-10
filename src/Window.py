#!/usr/bin/env python
# -*- coding: utf8 -*-

# To run: python3 Window.py

import gi
gi.require_version('Gtk', '3.0');
from gi.repository import Gtk

def set_margin (widget, amount):
    widget.set_margin_left (amount);
    widget.set_margin_right (amount);
    widget.set_margin_top (amount);
    widget.set_margin_bottom (amount);

class Card (Gtk.Grid):

    def __init__ (self):
        Gtk.Grid.__init__ (self);
        self.set_size_request (90, 110);

        self.number1 = Gtk.Label ("");
        self.number2 = Gtk.Label ("");
        self.symbol1 = Gtk.Label ("");
        self.symbol2 = Gtk.Label ("");

        set_margin (self, 12);
        set_margin (self.number1, 12);
        set_margin (self.number2, 12);
        set_margin (self.symbol1, 12);
        set_margin (self.symbol2, 12);

        self.attach (self.number1, 0, 0, 1, 1);
        self.attach (self.symbol2, 1, 0, 1, 1);
        self.attach (self.symbol1, 0, 1, 1, 1);
        self.attach (self.number2, 1, 1, 1, 1);
        self.get_style_context ().add_class ("card");
        self.get_style_context ().add_class ("h2");

    def set_values (self, number, symbol, color):
        self.number1.set_label (number);
        self.number2.set_label (number);
        self.symbol1.set_label (symbol);
        self.symbol2.set_label (symbol);

        if (color == "red"):
            self.get_style_context ().add_class ("error");
        else:
            self.get_style_context ().remove_class ("error");

class BlackjackWindow (Gtk.Window):

    def __init__ (self):
        Gtk.Window.__init__ (self, title= "Blackjacker");
        self.set_size_request (300, 180);
        grid = Gtk.Grid ();

        card = Card ();
        card.set_values ("5", "♥", "red");
        grid.add (card);

        card = Card ();
        card.set_values ("9", "♣", "black");
        grid.add (card);

        grid.add (Card ());
        grid.add (Card ());
        grid.add (Card ());

        self.add (grid)

def main():
    win = BlackjackWindow ();
    win.connect ("delete-event", Gtk.main_quit);
    win.show_all ();
    Gtk.main ();

if __name__ == '__main__':
    main()
