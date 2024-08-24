ss_groupbox_bet_active = """
#groupbox_bet {
	font: 700 24pt "Forte";
	color:  rgba(212,185,58,255);
	background-color: rgba(33,44,38,255);
	border-radius: 20px;	
    margin-top: 0.9em;
    border: 1px solid rgb(212,185,58)
}

#groupbox_bet::title {
    subcontrol-origin: margin;
    subcontrol-position: top center; /* Başlığı ortalamak için */
    background-color: transparent;
}


#groupbox_bet QLabel {
	background-color: transparent;
	font: 700 12pt "Forte";
	color: rgba(212,185,58,255)
}

#groupbox_bet #frame_stake * {
	font: 700 16pt "Forte";
}

#groupbox_bet #label_stake_amount {
	font: 700 22pt "Forte";
}


#groupbox_bet QPushButton {
	background-color: rgba(212, 185, 58,20);
	border-radius: 10px;
	font: 700 16pt "Forte";
	color: rgb(212, 185, 58);
}

#groupbox_bet QPushButton::hover {
	background-color:rgba(212, 185, 58,50);
}



#groupbox_bet QSlider {
    background-color: transparent;
}

#groupbox_bet QSlider::groove:horizontal {
    height: 20px;
    background-color: rgba(0,0,0,40);
    border-radius: 10px;
}

#groupbox_bet QSlider::handle:horizontal {
	image: url(:/chips/coin.png);
    width: 20px;
    height: 20px;
    /* margin: -5px 0; Handle, groove'da ortalanacak */
    border-radius: 10px;
}


#groupbox_bet #label_bet_info {

	font: 10pt "Forte";
	color: rgba(212,185,58,150);
}

#frame_stake_amount QLabel {

	font: 10pt "Forte";
	color: rgba(212,185,58,150);
}


"""

ss_groupbox_move_active = """
#groupbox_move {
	font: 700 24pt "Forte";
	color: rgba(212,185,58,255);
	background-color: rgb(33,44,38);
    margin-top: 0.9em;
    border: 1px solid rgb(212,185,58);
}

#groupbox_move::title{
    subcontrol-origin: margin;
    subcontrol-position: top center; /* Başlığı ortalamak için */
    background-color: transparent;
}


#button_stand {
border-bottom-right-radius: 20px;
border-top-right-radius: 20px;
background-color: rgba(212, 185, 58,10);
}

#button_stand::hover {
background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0.1 rgba(0, 0, 0, 0), stop:1 rgba(212,185,58,80));
}

#button_hit {
border-bottom-left-radius: 20px;
border-top-left-radius: 20px;
background-color: rgba(212, 185, 58,10);
}

#button_hit::hover {
background-color: qlineargradient(spread:pad, x1:1, y1:0.5, x2:0, y2:0.5, stop:0.1 rgba(0, 0, 0, 0), stop:1 rgba(212,185,58,80));
}

#button_double {
border-radius: 20px;
background-color: rgba(166,42,53,20);
}

#button_double::hover {
background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0.1 rgba(0, 0, 0, 0), stop:1 rgba(166,42,53,140));
}


"""

ss_label_player_total_bust = """
color: rgba(236,14,56,255);
background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 0), stop: 0.7 rgba(236,14,56,25), stop:0.85 rgba(236,14,56,55), stop:1 rgba(236,14,56,105));
border:1 solid rgba(185,23,49,255);
"""

ss_label_player_total_text_bust = """
color: rgba(185,23,49,255)
"""

ss_label_player_total_blackjack = """
background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 0), stop: 0.7 rgba(14,14,14,25), stop:0.85 rgba(14,14,14,55), stop:1 rgba(14,14,14,105));
border:1 solid rgba(212,185,58,255);
"""
ss_label_dealer_blackjack = """
QLabel {
color: rgba(212,185,58,255)
}
"""

ss_frame_board_announce_active = """
#frame_board_announce {
background-color: rgba(212,185,58,255);
} """
