from unicodedata import name


input_style = """
    QLineEdit{
        background-color: rgb(55, 55, 55);
        color: rgb(255, 255, 255);
        border: 1px solid  rgb(91, 91, 91);
        border-bottom-left-radius:0px;
        border-top-left-radius:2px;
        border-bottom-right-radius:0px;
        border-top-right-radius:2px;
        padding:5px;
    }

    QLineEdit::hover{
        background-color: rgb(59, 59, 59);
        }

    QLineEdit::focus{
        border:1px solid  rgb(121,121, 121);
    }
"""
input_style_error = """
    QLineEdit{
        background-color: rgb(55, 55, 55);
        color: rgb(255, 255, 255);
        border:1px solid rgb(195, 75, 75);
        border-bottom-left-radius:0px;
        border-top-left-radius:2px;
        border-bottom-right-radius:0px;
        border-top-right-radius:2px;
        padding:5px;
    }

    QLineEdit::hover{
        background-color: rgb(59, 59, 59);
        }

    QLineEdit::focus{
        border:1px solid rgb(195, 75, 75);
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

