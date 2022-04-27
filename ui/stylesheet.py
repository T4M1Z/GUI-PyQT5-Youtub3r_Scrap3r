from unicodedata import name


input_style = """
    QLineEdit{
        background-color:  rgb(214, 214, 214);
        color: #545454;
        border: 1px solid  #ffffff;
        border-radius:2px;
        padding-left:7px;
    }

    QLineEdit::hover{
        background-color:  rgb(210, 210, 210);
        }

    QLineEdit::focus{
	    border:1px solid  rgb(121,121, 121);
    }
"""
input_style_error = """
    QLineEdit{
        background-color:  rgb(194, 194, 194);
        color: #545454;
        border: 1px solid  rgb(195,75,75);
        border-radius:2px;
        padding-left:7px;
    }

    QLineEdit::hover{
        background-color:  rgb(210, 210, 210);
        }

    QLineEdit::focus{
	    border:1px solid  rgb(195,75,75);
    }
"""

db_offline = """
    QLabel{
    background-color: rgb(55, 55, 55);
	color: rgb(227, 87, 87);
    border: 1px solid  rgb(91, 91, 91);
    border-bottom-left-radius:0px;
    border-top-left-radius:2px;
    border-bottom-right-radius:0px;
    border-top-right-radius:2px;
    padding:5px;
    }
"""

db_online = """
    QLabel{
    background-color: rgb(55, 55, 55);
    color: rgb(106, 255, 128);
    border: 1px solid  rgb(91, 91, 91);
    border-bottom-left-radius:0px;
    border-top-left-radius:2px;
    border-bottom-right-radius:0px;
    border-top-right-radius:2px;
    padding:5px;
    }
"""

no_flag = """
    QLabel{
        image: url(:/flags/icons/flags/none.svg);
        border:none;
        background-color: qlineargradient(spread:pad, x1:0, y1:0.0116818, x2:1, y2:1, stop:1 rgba(0, 0, 0, 0));
}"""

def flag(name):
    return """
        QLabel{
            image: url(:/flags/icons/flags/"""+name+""".svg);
            border:none;
            background-color: qlineargradient(spread:pad, x1:0, y1:0.0116818, x2:1, y2:1, stop:1 rgba(0, 0, 0, 0));
    }"""

no_photo_profile ="""
    QLabel{
        border:2px solid rgb(90, 90, 90);
        background-color: rgb(89, 89, 89);
        border-image: url(:/channel/icons/channel/profile.jpg);
    }"""

new_photo_profile ="""
    QLabel{
        border:2px solid rgb(90, 90, 90);
        background-color: rgb(89, 89, 89);
        border-image: url(:/channel/icons/channel/profile_new.jpg);
    }"""

def left_panel_btn(status):
    return """
    QPushButton{
        background-color: rgb(81, 81, 81);
    border-top-right-radius: 6px;
    border-bottom-right-radius: 6px;
        image: url(:/16x16/icons/16x16/cil-caret-"""+status+""".png);
    }

    QPushButton:hover{
    background-color: rgb(71, 71, 71);
    }

    QPushButton:pressed{
    background-color: rgb(75, 75, 75);
    }
    """


def radius_maximize(n):
    close_btn_rad = """QPushButton{
        background-color: rgb(59, 59, 59);
        image: url(:/16x16/icons/16x16/cil-x.png);
        border:0px;
    background-color: rgb(44, 44, 44);
    border-radius:0px;
    border-top-right-radius: """+n+"""px;
    }

    QPushButton::hover{
        background-color: rgb(195, 92, 92);
        image: url(:/16x16/icons/16x16/cil-x.png);
    }

    QPushButton::pressed{
        background-color: rgb(29, 29, 29);
        image: url(:/16x16/icons/16x16/cil-x.png);
    }"""


    frame_btn_rad = """
    background-color: rgb(44, 44, 44);
    border:0px;
    border-top-right-radius:3px;
    border-top-left-radius:0px;
    border-bottom-left-radius:0px;
    border-bottom-right-radius:3px;
    border-top-right-radius: """+n+"""px;
    """

    window_btn_rad = """
    background-color: rgb(59, 59, 59);
    border:0px;
    border-top-right-radius: """+n+"""px;
    """

    frame_top_rad = """
        background-color: rgb(44, 44, 44);
        border:0px;
        border-top-left-radius: """+n+"""px;
        border-top-right-radius: """+n+"""px;
    """

    page_title_rad = """
    background-color: rgb(195, 75, 75);
    border-bottom-right-radius:26px;
    border:0px;
    border-top-left-radius: """+n+"""px;
    """

    title_frame_rad = """
    background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(53, 59, 69, 0), stop:1 rgba(91, 99, 115, 0));
    border-top-left-radius: """+n+"""px;
    """

    return close_btn_rad, frame_btn_rad, window_btn_rad, frame_top_rad, page_title_rad, title_frame_rad





