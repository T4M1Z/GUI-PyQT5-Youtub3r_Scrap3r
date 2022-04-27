from ui.main_ui import Ui_MainWindow
from functions import UIFunctions
from ui import stylesheet
from scraper_channel.channel_scraping import Channel_Scraping
from scraper_channel.test_db import MongoDB

from widget.central_panel.central_panel import CenterPanel
from widget.channel_history.channel_history import ChannelHistory
from widget.db_offline.db_offline import DBOffline
from widget.db_history_channel.db_history_channel import DBHistoryChannel

from database.db_access import DBConnection

from animation import Animation, FaderWidget