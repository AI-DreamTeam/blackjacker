#!/usr/bin/env python
# -*- coding: utf8 -*-

# To run: python3 Window.py

import random
import gi
gi.require_version('Gtk', '3.0');
from gi.repository import Gtk
gi.require_version('Gdk', '3.0');
from gi.repository import Gdk

from gi.repository import GObject

def set_margin (widget, amount):
    widget.set_margin_left (amount);
    widget.set_margin_right (amount);
    widget.set_margin_top (amount);
    widget.set_margin_bottom (amount);

class Deck ():

    def __init__ (self):
        self.cards = list ();

        suits = "♥","♠","♦","♣";
        values = "A","2","3","4","5","6","7","8","9","10","J","Q","K";

        for v in values:
            for s in suits:
                self.cards.append ((v, s));

        random.shuffle(self.cards);
        random.shuffle(self.cards);
        random.shuffle(self.cards);
        random.shuffle(self.cards);
        random.shuffle(self.cards);

    def get (self):
        return self.cards.pop ();

class Hand (Gtk.Grid, GObject.GObject):
    __gsignals__ = {
    'value_changed' : (GObject.SIGNAL_RUN_LAST, GObject.TYPE_NONE,
                        (GObject.TYPE_INT,))
    }

    def __init__ (self, deck):
        Gtk.Grid.__init__ (self);
        self.deck = deck;

        self.card_1 = Card ();
        self.card_2 = Card ();
        self.card_3 = Card ();
        self.card_4 = Card ();
        self.card_5 = Card ();

        self.card_1.connect ("clicked", self.request_card);
        self.card_2.connect ("clicked", self.request_card);
        self.card_3.connect ("clicked", self.request_card);
        self.card_4.connect ("clicked", self.request_card);
        self.card_5.connect ("clicked", self.request_card);

        self.add (self.card_1);
        self.add (self.card_2);
        self.add (self.card_3);
        self.add (self.card_4);
        self.add (self.card_5);

    def get_cards (self):
        values = list ();

        values.append (self.card_1.get_value ());
        values.append (self.card_2.get_value ());
        values.append (self.card_3.get_value ());
        values.append (self.card_4.get_value ());
        values.append (self.card_5.get_value ());
        
        _values = list ();
        for i in values:
            if (i > 0):
                _values.append (i);
            
        return _values;

    def get_value (self):
        values = self.get_cards ();
        aces = 0;
        out = 0;
        for val in values:
            if (val == 11):
                aces += 1;
            out += val;

        while (out > 21 and aces > 0):
            aces -= 1;
            out -= 10;

        if (out > 21):
            self.set_sensitive (False);

        return out;

    def request_card (self, card):
        if self.is_set (card):
            card.set_values (self.deck.get ());
        self.emit('value_changed', self.get_value ())

    def is_set (self, card):
        return card.number1.get_label () == "";

    def set (self, card):
        if self.is_set (self.card_1):
            self.card_1.set_values (card);
        elif self.is_set (self.card_2):
            self.card_2.set_values (card);
        elif self.is_set (self.card_3):
            self.card_3.set_values (card);
        elif self.is_set (self.card_4):
            self.card_4.set_values (card);
        elif self.is_set (self.card_5):
            self.card_5.set_values (card);

    def set_1 (self, card):
        self.card_1.set_values (card);

    def set_2 (self, card):
        self.card_2.set_values (card);

    def set_3 (self, card):
        self.card_3.set_values (card);

    def set_4 (self, card):
        self.card_4.set_values (card);

    def set_5 (self, card):
        self.card_5.set_values (card);

    def reset ():
        self.card_1.set_values (("", ""));
        self.card_2.set_values (("", ""));
        self.card_3.set_values (("", ""));
        self.card_4.set_values (("", ""));
        self.card_5.set_values (("", ""));

class Card (Gtk.Button):

    def __init__ (self):
        Gtk.Button.__init__ (self);
        self.grid = Gtk.Grid ();

        self.set_size_request (100, 130);
        self.set_can_focus (False);

        self.number1 = Gtk.Label ("");
        self.number2 = Gtk.Label ("");
        self.symbol1 = Gtk.Label ("");
        self.symbol2 = Gtk.Label ("");

        set_margin (self, 12);
        set_margin (self.number1, 12);
        set_margin (self.number2, 12);
        set_margin (self.symbol1, 12);
        set_margin (self.symbol2, 12);

        self.grid.attach (self.number1, 0, 0, 1, 1);
        self.grid.attach (self.symbol2, 1, 0, 1, 1);
        self.grid.attach (self.symbol1, 0, 1, 1, 1);
        self.grid.attach (self.number2, 1, 1, 1, 1);

        self.add (self.grid);
        self.get_style_context ().add_class ("card");
        self.get_style_context ().remove_class ("button");
        self.grid.get_style_context ().add_class ("h2");

        provider = Gtk.CssProvider ();

        css = ".card:active {\nbox-shadow: inset 0 0 0 1px alpha (#000, 0.05),\n 0 1px 0 0 alpha (@bg_highlight_color, 0.3);\n }";
        provider.load_from_data (bytes(css.encode ()));

        context = self.get_style_context ();
        context.add_provider (provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION);

    def get_value (self):
        label = self.number1.get_label ();
        if (label == ""):
            return 0;
        elif (label == "A"):
            return 11;
        elif (label == "J" or label == "Q" or label == "K"):
            return 10;
        else:
            return int (label);

    def set_values (self, card):
        self.number1.set_label (card[0]);
        self.number2.set_label (card[0]);
        self.symbol1.set_label (card[1]);
        self.symbol2.set_label (card[1]);

        if (card[1] == "♥" or card[1] == "♦"):
            self.grid.get_style_context ().add_class ("error");
        else:
            self.get_style_context ().remove_class ("error");

class BlackjackWindow (Gtk.Window):

    def print_value (self, hand, value):
        self.show_results ();
        print ("Test" + str (value));

    def __init__ (self):
        Gtk.Window.__init__ (self, title= "Blackjacker");
        self.set_size_request (300, 180);
        self.deck = Deck ();

        grid = Gtk.Grid ();
        grid.set_orientation (Gtk.Orientation.VERTICAL);

        self.pc = Hand (self.deck);
        self.pc.set_sensitive (False);
        self.pc.set (self.deck.get ());

        self.results = Gtk.Label ("Hold");
        self.button = Gtk.Button ();

        self.button.add (self.results);
        self.button.get_style_context ().add_class ("suggested-action");
        self.button.get_style_context ().add_class ("h1");
        set_margin (self.button, 12);

        grid.add (self.pc);
        grid.add (self.button);
        self.hand = Hand (self.deck);
        self.hand.connect ("value_changed", self.print_value);

        self.hand.set (self.deck.get ());
        self.hand.set (self.deck.get ());

        grid.add (self.hand);

        self.add (grid);
        self.show_results ();

    def show_results (self):
        string = "You: " + str (self.hand.get_value ());
        string = string + " - House : " + str (self.pc.get_value ());

        house_cards = self.pc.get_cards ();
        user_cards = self.hand.get_cards ();

        print (house_cards);
        print (user_cards);

        string = string + " - Safe next card: " + str (calculateProbability (user_cards, house_cards)) + "%";

        self.button.set_tooltip_text (string);

def calculateProbability(faceUpPlayerCards, faceUpHouseCards):
    points = 0
    total = 0
    for card in faceUpPlayerCards:
        points += card

    winCard = 21 - points 
    faceUpCards = len(faceUpPlayerCards) + len(faceUpHouseCards)
    nx = 0 

    for i in range(1, winCard+1):
        if(i >= 12):
            break

        for card in faceUpPlayerCards:
            if(card == i):
                nx += 1

        for card in faceUpHouseCards:
            if(card == i):
                nx += 1   

        #nx is the number of cards that has the same value that you need to get 21 points
        if(i == 10):
            p = (16-nx)
        else:
            p = (4-nx)

        p = p / (52 - faceUpCards)
        nx = 0
        total += p

    return total * 100

def main():
    win = BlackjackWindow ();
    win.connect ("delete-event", Gtk.main_quit);
    win.show_all ();
    Gtk.main ();

if __name__ == '__main__':
    main()
