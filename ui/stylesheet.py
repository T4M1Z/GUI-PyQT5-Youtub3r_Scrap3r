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
        border:1px solid rgb(195, 75, 75);
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
	color: rgb(195, 75, 75);
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
