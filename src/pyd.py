import PySimpleGUI as sg
import src.functions as functions

HEADER = ("Latin Modern Mono", 20)
BUTTON = ("Latin Modern Mono", 15)
TEXT = ("Latin Modern Mono", 13)


def audio_dl(link, dir, window):
    window.Hide()
    functions.downloadAudio(link, dir)
    window.UnHide()


def video_dl(link, dir, window):
    window.Hide()
    functions.downloadVideo(link, dir)
    window.UnHide()


def single_vid(link, dir, window):
    window.Hide()
    functions.download_single_video(link, dir)
    window.UnHide()


def main():
    # Define a black-white theme
    sg.theme('Black')

    # Define the layout
    layout = [
        [sg.Text("YouTube Playlist downloader", font=HEADER)],
        [sg.Text("Enter the playlist/video URL:", font=TEXT),
                 sg.InputText(key="link")],
        [sg.Text("Enter the download directory", font=TEXT),
                 sg.InputText(key="directory")],
        [sg.Button("Download audio", font=BUTTON, key="audio"), sg.Button(
            "Download with video", font=BUTTON, key="video"), sg.Button("Exit", font=BUTTON, key="exit")]
    ]

    window = sg.Window("YouTube Playlist downloader", layout)

    while True:
        directory = ""
        event, values = window.read()

        if event == "exit":
            break

        elif event == "audio":
            if not (values["directory"].endswith("/")):
                directory = values["directory"]
            else:
                directory = values["directory"]

            if "playlist" in values["link"]:
                window.Hide()
                functions.downloadAudio(values["link"], directory)
                window.UnHide()
            else:
                window.Hide()
                functions.download_single_audio(values["link"], directory)
                window.UnHide()

        elif event == "video":
            if not (values["directory"].endswith("/")):
                directory = values["directory"]
            else:
                directory = values["directory"]

            if "playlist" in values["link"]:
                window.Hide()
                functions.downloadVideo(values["link"], directory)
                window.UnHide()
            else:
                window.Hide()
                functions.download_single_video(values["link"], directory)
                window.UnHide()
        
        elif event == sg.WIN_CLOSED:
            break

if __name__ == '__main__':
    main()