
import os
import shutil
import re
import datetime
import time

def MoveFolders():
    os.chdir(os.path.join("D:", "\\TV Shows"))
    dir_list = [name for name in os.listdir(".") if os.path.isdir(name)]
    os.chdir(os.path.join("D:", "\\New Downloads"))
    new_downloads_list = [name for name in os.listdir(".") if os.path.isdir(name)]
    source = os.path.join("D:", "\\New Downloads")
    destination = os.path.join("D:", "\\TV Shows")
    current_time = str(datetime.datetime.now())+ '\t'
    for torrent in new_downloads_list:
        torrentFound = False
        for name in dir_list:
            name_parts = name.split(' ')
            if CheckExactMatch(torrent.lower(), name_parts):
                full_destination = os.path.join(destination, name)
                try:
                    torrentFound = True
                    if os.path.exists(os.path.join(full_destination,torrent)):
                        file = open("LOG 4 Already Existing Folders.txt", "a") 
                        file.write("\n") 
                        file.write(current_time)
                        file.write(torrent)
                        file.write(' --> ')
                        file.write(full_destination)
                        file.write('\n')
                        file.close() 
                    else:
                        print( f'Folder "{torrent}" has been moved to "{name}" directory inside TV Shows ')
                        shutil.move(os.path.join(source, torrent), full_destination)
                        file = open("LOG 4 Moved Folders.txt", "a") 
                        file.write("\n") 
                        file.write(current_time)
                        file.write(torrent)
                        file.write(' --> ')
                        file.write(full_destination)
                        file.write('\n')
                        file.close() 
                except:
                    print('Something\'s up')
                break
        
        if torrentFound:
            print(f'{torrent} has a match in TV SHOWS')
        else:
            file = open("LOG 4 Not Found Folders.txt", "a")
            file.write("\n ") 
            file.write(current_time)
            file.write(torrent)
            file.write('\n')
            file.close() 
            print(f'Log File created! and {torrent} has not found a match in TV Shows')
                    
def CheckExactMatch(torrent, name_parts):
    torrent_words = GetTorrentParts(torrent)
    parts_matched = []
    for part in name_parts:
        for word in torrent_words:
            if word == part.lower():
                parts_matched.append(1)
                break
    if len(parts_matched) == len(name_parts):
        return True
    return False

def GetTorrentParts(torrent_name):
    torrent_parts = []
    word_in_torrent = ''
    # is_last_word = False
    tor_length = len(torrent_name)-1
    for i, char in enumerate(torrent_name):
        if ord(char) >= ord('a') and ord(char) <= ord('z') or ord(char) >= ord('A') and ord(char) <= ord('Z'):
            word_in_torrent += char
            if i==tor_length:
                torrent_parts.append(word_in_torrent)
        elif ord(char) >= ord('0') and ord(char) <= ord('9'):
            word_in_torrent += char
            if i==tor_length:
                torrent_parts.append(word_in_torrent)
        else:
            torrent_parts.append(word_in_torrent)
            word_in_torrent = ''
    return torrent_parts

if __name__ == "__main__":
    MoveFolders()
