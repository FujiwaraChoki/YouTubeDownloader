#!/bin/bash

from pytube import Playlist, YouTube
import ffmpy
from termcolor import colored
import os
import PySimpleGUI as sg
import requests
from PIL import Image

def get_thumbnail(url):
    file = open("tmp/thumbnail.gif", "wb")
    file.truncate(0)
    file.close()
    r = requests.get(url)
    with open("tmp/thumbnail.png", "wb") as f:
        f.write(r.content)
    im = Image.open("tmp/thumbnail.png")
    im.save("tmp/thumbnail.gif", "GIF")
    os.system("rm tmp/thumbnail.png")
    

def downloading(title, description, url, thumbnail_url):
    get_thumbnail(thumbnail_url)
    sg.theme('Black')

    layout = [
        [sg.Text(title, font=("Latin Modern Mono", 20))],
        [sg.Image("tmp/thumbnail.gif")],
        [sg.Text(description, font=("Latin Modern Mono", 15))],
        [sg.Text("URL: {}".format(url), font=("Latin Modern Mono", 15))],
        [sg.Text("Downloading...", font=("Latin Modern Mono", 30))]
    ]

    window = sg.Window("Downloading...", layout, size=(1700, 1000), finalize=True)

    return window


def downloadAudio(link, directory):
    playlist = Playlist(link)
    for video in playlist.videos:
        download_page = downloading(video.title, video.description, video.watch_url, video.thumbnail_url)
        if "//" in video.title or "/" in video.title or " " in video.title:
            video.title = video.title.replace(" ", "_").replace("//", "_").replace("/", "_")
        audio = video.streams.get_audio_only()
        audio.download(filename=video.title + ".mp4", output_path=directory)
        audioTitle = audio.title

        new_filename = directory + audioTitle + '.mp3'
        default_filename = directory + audioTitle + '.mp4'

        print(colored('{}\nURL : {}\n\n'.format(video.title, video.watch_url), 'yellow'))
        ff = ffmpy.FFmpeg(
            inputs={default_filename : None},
            outputs={new_filename : None}
        )
        ff.run()
        download_page.close()
        print(colored("Downloaded : {} with url : {}".format(video.title, video.watch_url), 'green'))
    command = "rm -rf " + directory + "'*.mp4'"
    os.system(command)
    sg.Popup("Downloaded all videos in the playlist.")

def downloadVideo(link, directory):
    playlist = Playlist(link)
    for video in playlist.videos:
        download_page = downloading(video.title, video.description, video.watch_url, video.thumbnail_url)
        if "//" in video.title or "/" in video.title or " " in video.title:
            video.title = video.title.replace(" ", "_").replace("//", "_").replace("/", "_")
        video.title = video.title.replace(" ", "_").replace("/", "_")

        print(colored('{}\nURL : {}\n\n'.format(video.title, video.watch_url), 'yellow'))
        video.streams.\
            filter(type='video', progressive=True, file_extension='mp4').\
            order_by('resolution').\
            desc().\
            first().\
            download(directory)
        download_page.close()
        print(colored("Downloaded : {} with url : {}".format(video.title, video.watch_url), 'green'))
    sg.Popup("Downloaded all videos in the playlist.")

def download_single_video(link, directory):
    video = YouTube(link)
    download_page = downloading(video.title, video.description, video.watch_url, video.thumbnail_url)
    if "//" in video.title or "/" in video.title or " " in video.title:
        video.title = video.title.replace(" ", "_").replace("//", "_").replace("/", "_")
    video.title = video.title.replace(" ", "_").replace("/", "_")

    print(colored('{}\nURL : {}\n\n'.format(video.title, video.watch_url), 'yellow'))
    video.streams.\
        filter(type='video', progressive=True, file_extension='mp4').\
        order_by('resolution').\
        desc().\
        first().\
        download(directory)
    download_page.close()
    print(colored("Downloaded : {} with url : {}".format(video.title, video.watch_url), 'green'))
    sg.Popup("Downloaded the video.")

def download_single_audio(link, directory):
    video = YouTube(link)
    download_page = downloading(video.title, video.description, video.watch_url, video.thumbnail_url)
    if "//" in video.title or "/" in video.title or " " in video.title:
        video.title = video.title.replace(" ", "_").replace("//", "_").replace("/", "_")
    audio = video.streams.get_audio_only()
    audio.download(filename=video.title + ".mp4", output_path=directory)
    audioTitle = audio.title

    new_filename = directory + audioTitle + '.mp3'
    default_filename = directory + audioTitle + '.mp4'

    print(colored('{}\nURL : {}\n'.format(video.title, video.watch_url), 'yellow'))
    ff = ffmpy.FFmpeg(
        inputs={default_filename : None},
        outputs={new_filename : None}
    )
    ff.run()
    download_page.close()
    print(colored("Downloaded : {} with url : {}".format(video.title, video.watch_url), 'green'))
    command = "rm -rf " + directory + "'*.mp4'"
    os.system(command)
    sg.Popup("Downloaded the audio.")