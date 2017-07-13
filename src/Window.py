#!/usr/bin/env python
# -*- coding: utf8 -*-

# To run: python3 Window.py
import Euristic as euristic
import NaiveBayes as naiveBayes
import random
import gi
gi.require_version('Gtk', '3.0');
from gi.repository import Gtk
gi.require_version('Gdk', '3.0');
from gi.repository import Gdk

from gi.repository import GObject

CLASS_1_TIP = ("Your hand is not too good. You should raise your bet a bit"  +
" (if you can), and take another card always\nchecking how safe it is to do so" +
" (Below 45% is not too good, and you should hold!).")

CLASS_2_TIP = ("You have a decent hand. You could raise your bet a bit (if you can)," +
" and take another card, since it should\nbe really safe to do so (but check how safe anyway! ).")

CLASS_3_TIP = ("You have an excellent hand! You should really raise your bet and hold," +
" since it's very likely you will win. If you\nthink your hand is not too good and it's safe to" +
" take another card, do it, but don't raise the bet too much.")

WIN_TIP = ("Wow! Lucky you! Go ahead, raise the bet to the top (if you can) and hold to win!")

ACE_TIP = ("You have at least an Ace in your hand, which means you have two choices! If you use your Ace as a 1, " +
"\ntake the first tip, and if you use it as an 11, take the second tip!\n\n" + "1. You probably won't go " +
"over 21 using it as 1, but if your hand is over 16, it would be better to hold\n and raise the bet a little bit." +
"\n\n2. Check how safe it is to get another card, but it's very likely that your hand is already a very good\none "+
"(over 16 is great!); you should raise your bet considerably before holding.")

def set_margin (widget, amount):
    widget.set_margin_left (amount);
    widget.set_margin_right (amount);
    widget.set_margin_top (amount);
    widget.set_margin_bottom (amount);

def set_margin_sides (widget, amount):
    widget.set_margin_left (amount);
    widget.set_margin_right (amount);

class Deck ():

    def __init__ (self):
        self.reset ();

    def reset (self):
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

    def get_cards (self, validate = False):
        values = list ();

        values.append (self.card_1.get_value ());
        values.append (self.card_2.get_value ());
        values.append (self.card_3.get_value ());
        values.append (self.card_4.get_value ());
        values.append (self.card_5.get_value ());

        _values = list ();

        current_value = 0;
        if (validate):
            current_value = self.get_value ();

        for i in values:
            if (i > 0):
                if (validate and i == 11):
                    _values.append (1);
                else:
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
        self.emit('value_changed', self.get_value ())

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

    def reset (self):
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
            self.get_style_context ().add_class ("error");
        else:
            self.get_style_context ().remove_class ("error");

class BlackjackerAccount (Gtk.Grid):

    def __init__ (self):
        Gtk.Grid.__init__ (self);
        set_margin (self, 12);
        self.get_style_context ().add_class ("frame");
        self.get_style_context ().add_class ("view");
        self.set_orientation (Gtk.Orientation.VERTICAL);
        self.set_row_spacing (6);

        self.pot_value = 10;
        self.cash_value = 90;

        pot = Gtk.Label ("Pot: $10");
        cash = Gtk.Label ("Cash: $90");
        handClass = Gtk.Label("Test");
        raise_button = Gtk.Button ("Raise Bet (- $10)");

        self.pot = pot;
        self.cash = cash;
        self.handClass = handClass;
        self.raise_button = raise_button;

        raise_button.connect ("clicked", self.increase_pot);

        self.results = Gtk.Label ("Hold");
        self.button = Gtk.Button ();
        self.button.add (self.results);
        self.button.set_hexpand (True);

        pot.set_halign (Gtk.Align.START);
        cash.set_halign (Gtk.Align.START);
        handClass.set_halign (Gtk.Align.START);

        pot.set_margin_top (6);
        set_margin_sides (pot, 6);
        set_margin_sides (cash, 6);
        set_margin_sides (handClass,6);
        set_margin_sides (raise_button, 6);
        set_margin_sides (self.button, 6);
        self.button.set_margin_bottom (6);

        pot.get_style_context ().add_class ("h4");
        cash.get_style_context ().add_class ("h4");
        handClass.get_style_context ().add_class("ha");
        raise_button.get_style_context ().add_class ("destructive-action");
        raise_button.get_style_context ().add_class ("h4");
        raise_button.get_style_context ().add_class ("h3");
        self.button.get_style_context ().add_class ("suggested-action");
        self.button.get_style_context ().add_class ("h1");

        self.add (pot);
        self.add (cash);
        self.add (handClass);
        self.add (raise_button);
        self.add (self.button);

    def increase_pot (self, button):
        self.cash_value = self.cash_value - 10;
        self.pot_value = self.pot_value + 10;

        if (self.cash_value <= 0):
            self.deactivate_raise ();

        self.pot.set_label ("Pot: $" + str (self.pot_value));

        self.cash.set_label ("Cash: $" + str (self.cash_value));

    def check_lost (self):
        if (self.cash_value == 0):
            self.button.set_sensitive (False);
            self.button.set_tooltip_text ("Quit to restart...");

    def deactivate_raise (self):
        self.raise_button.set_sensitive (False);

    def reset_round (self, won):
        if (won):
            self.cash_value = self.cash_value + self.pot_value * 2;

        self.pot_value = 0;
        self.pot.set_label ("Pot: $0");
        self.cash.set_label ("Cash: $" + str (self.cash_value));

        if (self.cash_value > 0):
            self.button.set_sensitive (True);
            self.raise_button.set_sensitive (True);
        else:
            self.button.set_sensitive (False);
            self.raise_button.set_sensitive (False);

    def start_round (self):
        self.raise_button.clicked ();

class BlackjackWindow (Gtk.Window):

    def print_value (self, hand, value):
        self.account.deactivate_raise ();
        self.show_results ();

    def __init__ (self):
        Gtk.Window.__init__ (self, title= "Blackjacker");
        self.game_over = False;
        self.win = False;

        self.set_size_request (300, 180);
        self.deck = Deck ();

        grid = Gtk.Grid ();
        grid.set_orientation (Gtk.Orientation.VERTICAL);

        self.pc = Hand (self.deck);
        self.pc.set_sensitive (False);
        self.pc.set (self.deck.get ());

        account = BlackjackerAccount ();

        self.account = account;
        self.results = account.results;
        self.button = account.button;
        self.handClass = account.handClass;

        self.button.connect ("clicked", self.main_button_clicked);

        grid.add (self.pc);
        grid.add (account);
        self.hand = Hand (self.deck);
        self.hand.connect ("value_changed", self.print_value);

        self.hand.set (self.deck.get ());
        self.hand.set (self.deck.get ());

        grid.add (self.hand);

        self.add (grid);
        self.show_results ();
        self.account.raise_button.set_sensitive (True);

    def main_button_clicked (self, button):
        self.account.deactivate_raise ();
        if (self.game_over):
            self.reset ();
            self.account.start_round ();
        else:
            self.run_game ();

    def reset (self):
        self.game_over = False;
        self.hand.reset ();
        self.hand.set_sensitive (True);
        self.pc.reset ();
        self.deck.reset ();
        self.results.set_label ("Hold");
        self.hand.set (self.deck.get ());
        self.pc.set (self.deck.get ());
        self.hand.set (self.deck.get ());
        self.account.reset_round (self.win);
        self.win = False;

    def run_game (self):
        pc = self.pc;
        hand = self.hand;

        hand_value = hand.get_value ();
        pc_value = pc.get_value ();

        win = True;

        if (hand_value > 21):
            win = False;

        while (pc_value < 17 and euristic.calculateProbability (pc.get_cards (True), hand.get_cards (True)) > 40.0):
            pc.set (self.deck.get ());
            pc_value = pc.get_value ();

        if (win and pc_value <= 21):
            win = hand_value > pc_value

        if (win):
            self.results.set_label ("You Won!");
        else:
            self.results.set_label ("You Lost :(");
            self.account.check_lost ();
            self.account.deactivate_raise ();

        self.win = win;
        self.game_over = True;
        hand.set_sensitive (False);

    def show_results (self):
        hand_value = self.hand.get_value ();

        if (hand_value > 21):
            self.results.set_label ("You Lost :(");
            self.game_over = True;
            self.button.set_tooltip_text ("Click to restart...");
            self.account.check_lost ();
            return;

        string = "You: " + str (hand_value);
        string = string + " - House : " + str (self.pc.get_value ());

        house_cards = self.pc.get_cards (True);
        user_cards = self.hand.get_cards (True);

        string = string + " - Safe next card: " + str (euristic.calculateProbability (user_cards, house_cards)) + "%";

        #player's hand clssification

        bayesResult = naiveBayes.naiveBayes(user_cards)

        #If there is an Ace in the hand, change the tip to a special one
        if 1 not in user_cards:

            if(bayesResult == 1):
                self.handClass.set_label (CLASS_1_TIP);
            elif(bayesResult == 2):
                self.handClass.set_label (CLASS_2_TIP);
            else:
                self.handClass.set_label (CLASS_3_TIP);
        else:
            self.handClass.set_label (ACE_TIP)

        if hand_value == 21:
            self.handClass.set_label(WIN_TIP);

        self.button.set_tooltip_text (string);

def main():
    win = BlackjackWindow ();
    win.connect ("delete-event", Gtk.main_quit);
    win.show_all ();
    Gtk.main ();

if __name__ == '__main__':
    main()
