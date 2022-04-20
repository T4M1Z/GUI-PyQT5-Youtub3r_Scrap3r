import os
from threading import Thread
import numpy as np
import time
import shutil
    
# from links_scraping import scrap_1
# from py_mongo import MongoDB
# from socket_manager import receive_packet, send_packet
# from channel_scraping import channel_scraping





# class main:
#     def __init__(self, url, yt_name):
#         self.url = url
#         self.yt_name = yt_name


    # def folder_cleaning(self):
    #     folders = ["output","csv","comments_json"]

    #     # take number of elements inside the folder
    #     try:
    #         new_folder = os.listdir("output")[0].replace("csv","backup")

    #         # copy folder_backup into database fodler
    #         if not os.path.exists(new_folder):
    #             os.makedirs("database/"+new_folder)
    #         for folder in folders:
    #             dest_dir = os.path.join("database/"+new_folder, os.path.basename(folder))
    #             if not os.path.exists(dest_dir):
    #                 shutil.copytree("database/"+new_folder,dest_dir)

    #         # Delete all files inside folders
    #         for folder in folders:
    #             for file in os.listdir(folder):
    #                 os.remove(folder+"\\"+file)

    #     except Exception as e: print(f"[ERROR Empty Folder] {e}")

    # def start_channel_scraping(self):

    #     print(self.url)    
    #     print(self.yt_name)    
        # ---------------------- #
        # Start Channel Scraping
        # _______________________#
    
    
    #     scrap = channel_scraping()
    #     self.channel_info_box = scrap.youtube(self.url, self.yt_name)
    #     self.yt_name = self.channel_info_box["username"]

    # def start_threads_links_scraping(self, check=False):
    #         # ---------------------- #
    #         # Start Threading
    #         # _______________________#


    #         if not check:
    #             # Take links scraped from the channel
    #             with open("links.txt", "r") as file:
    #                 a = file.read()
    #             # clean array links
    #             links_full = np.array(a.split("\n"))
    #             index = np.argwhere(links_full=="")
    #             links_full = np.delete(links_full, index)
    #             links_full = np.unique(links_full)

    #         else:
    #             links_full = [i for k,i in check.items()]
            

    #         # ---------------------- #
    #         # Quantity of Cluster [1/3]
    #         # _______________________#
    #         if CLUSTER == 1:
    #             pc1 = np.array_split(links_full, POWER)


    #         elif CLUSTER == 2:
    #             links_half = np.array_split(links_full, 2)
    #             pc1 = np.unique(links_half[0])
    #             pc1, pc2 = np.array_split(pc1, POWER), links_half[1]

    #             with open("links_cluster/links_pc_scuola.txt", "w") as f:
    #                 for link in pc2:
    #                     f.write(link)
    #                     f.write("\n")
    #             # Invia i link a pc2
    #             r = send_packet().listen()

    #         elif CLUSTER == 3:
    #             links_half = np.array_split(links_full, 3)
    #             pc1, pc2, pc3 = links_half[0], links_half[1], links_half[2]


    #         # ---------------------- #
    #         # Threads House
    #         # _______________________#

    #         # Put threads inside list with the function that contain ---->  .fast_scraping_1([links_full dei link], [nome del csv])
    #         if thread_allow:
    #             threads = []                                                    
    #             for n in range(POWER):                                     
    #                 threads.append(Thread(target = lambda links, name: scrap_1().fast_scraping_1(links, name), args=(pc1[n],f"test_{n+1}")))

    #             # Starting the threads
    #             for thread in threads:
    #                 thread.start()

    #             # Wait until the thread terminates
    #             for thread in threads:  # This blocks the calling thread until the thread whose join() 
    #                 thread.join()       # Method is called terminates – either normally or through an
    #                                     # unhandled exception – or until the optional timeout occurs.

    #             # --------------------- #




    #         # Rimane in attesa del file costruito dall'altro pc
    #         if CLUSTER > 1:
    #             # ---------------------- #
    #             # Recive Data from Cluster
    #             # _______________________# 
    #             receive_packet().listen()

    #         # CODICE BACK-END DA IMPLEMENTARE 
        

    # def pandas_cleaning_data(self, check=False):
    #     # ---------------------- #
    #     # Pandas Data Cleaning
    #     # _______________________# 
    #     from pandas_cleaning import Cleaning

    #     if not check:
    #         self.channel_info = Cleaning(self.yt_name).cleaning_channel(self.channel_info_box)
    #     self.videos_info = Cleaning(self.yt_name).clean_df_videos()
    #     comments_video = Cleaning(self.yt_name).json_comment() #da modifcare per togliere la parte all'interno di py_mongo con il with open etc.... (si ripete 2 volte)

    #     # ultimo inserimento finale <-- da correggere 


        
    # def database_data_send_check(self):
    #     # ---------------------- #
    #     # MongoDB Send Data
    #     # _______________________# 

    #     db = MongoDB(self.yt_name, self.channel_info)
    #     db.insert_channel_video()
    #     db.insert_comments(self.videos_info)
    #     # check = db.check_comments()
    
    #     # if len(check) > 1:
    #     #     self.folder_cleaning()
    #     #     self.start_threads_links_scraping(check)
    #     #     self.pandas_cleaning_data(check)
    #     #     db.restore_comment(check)
        
            


thread_allow = True
CLUSTER = 1   # form 1 to 3
POWER = 7 # n of threads

# if __name__ == "__main__":

#     start_time = time.time()

#     url ="https://www.youtube.com/c/GiovanniFois/videos"
#     yt_name = url.split("/")[4] 

#     main = main(url, yt_name)

#     # ---------------------------------- #

#     # main.folder_cleaning()
#     main.start_channel_scraping()
#     # main.start_threads_links_scraping()
#     main.pandas_cleaning_data()
#     main.database_data_send_check()

#     # ---------------------------------- #


#     print("RUN 1--- %s seconds ---" % (time.time() - start_time))