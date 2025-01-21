ss_groupbox_bet_active = """
#groupbox_bet {
	font: 700 20pt "Forte";
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

#groupbox_bet #label_stake_amount {
	font: 700 16pt "Forte";
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
	image: url(:/icons/coin.png);
    width: 20px;
    height: 20px;
    /* margin: -5px 0; Handle, groove'da ortalanacak */
    border-radius: 10px;
}


#groupbox_bet #frame_stake {
background-color: transparent;
}

#groupbox_bet #label_bet_info {

	font: 10pt "Forte";
	color: rgba(212,185,58,150);
}
"""

ss_groupbox_move_active = """

#groupbox_move {
	font: 700 20pt "Forte";
	color:  rgba(212,185,58,255);
	background-color: rgb(33,44,38);
	border-radius: 20px;	
    margin-top: 0.9em;
	border: 1px solid rgb(212,185,58)
}

#groupbox_move::title{
    subcontrol-origin: margin;
    subcontrol-position: top center; /* Başlığı ortalamak için */
    background-color: transparent;
}


#frame_button_hit {
	background-color:  transparent;
	border-top-left-radius:  20px;	
	border-bottom-left-radius:  20px;	
}

#frame_button_hit::hover, #frame_button_stand::hover, #frame_button_double::hover  {
	background-color:  rgba(212,185,58,25);
}

#frame_button_stand {
	background-color:  transparent;
	border-radius: 0px;
}

#frame_button_double {
	background-color:  transparent;
	border-top-right-radius:  20px;	
	border-bottom-right-radius:  20px;	
}

QPushButton {
border:none;
background-color: transparent;
}
"""

ss_button_next_round_active = """
QPushButton::hover {
border: 2px solid rgba(212,185,58,255);
background-color: rgba(212,185,58,25);
}

QPushButton{
font: 16pt "Arial";
border: 2px solid  rgb(120,124,116);
border-radius: 15px;
color: rgba(212,185,58,255);
background-color:  rgb(45, 20, 9);

}
"""

ss_button_next_round_deactive = """
QPushButton{
font: 16pt "Arial";
border: 2px solid  rgba(120,124,116,0.1);
border-radius: 15px;
color: rgba(212,185,58,0.1);
background-color:  rgba(45, 20, 9,0);
}
"""