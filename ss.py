
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
	image: url(:/chips/coin.png);
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
	color: rgba(212,185,58,255);
	background-color: rgb(33,44,38);
	border-radius: 20px;	
    margin-top: 0.9em;
    border: 1px solid rgb(212,185,58);
}

#groupbox_move::title{
    subcontrol-origin: margin;
    subcontrol-position: top center; /* Başlığı ortalamak için */
    background-color: transparent;
}


#groupbox_move #label_stake_amount {
	font: 700 16pt "Forte";
}


#groupbox_move QPushButton {
	background-color: rgba(212, 185, 58,20);
	border-radius: 20px;
	font: 700 16pt "Forte";
	color: rgb(212, 185, 58);
}

#groupbox_move QPushButton::hover {
	background-color:rgba(212, 185, 58,50);
}

#groupbox_move  #button_hit::hover {
border-bottom-left-radius: 0px;
}

#groupbox_move  #button_stand::hover {
border-bottom-right-radius: 0px;
}

#groupbox_move #frame_stake {
background-color: transparent;
}

#groupbox_move #frame_stand_hit {
	font: 700 16pt "Forte";
	color:  rgb(150,150,150);
	background-color:  transparent;
	border-radius: 10px;	
}

#groupbox_move QLabel {
	background-color: transparent;
	font: 700 16pt "Forte";
	color: rgba(180,180,180,200)
}

#groupbox_move QPushButton {
border:none;
background-color: transparent;
}


#groupbox_move QPushButton::hover {
background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0.1 rgba(0, 0, 0, 0), stop:1 rgba(212,185,58,80));

}

#groupbox_move #button_double::hover {
background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0.1 rgba(0, 0, 0, 0), stop:1 rgba(166,42,53,100));

}

#groupbox_move Line {
background-color: rgba(212,185,58,100);
}
"""

