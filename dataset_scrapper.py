from utils import *

# define the music categories
categories = [
    "Andalusi",
    "Rai",
    "Chaabi",
    "Gnawa",
    "Aita",
    "Moroccan Pop",
    "Moroccan Rap",
    "Moroccan Rock",
    "Amazigh Folk"
]

# define the number of songs to scrap per category
number_of_songs = 5

# define the path to save the dataset
dataset_path = "data/"

# create the dataset folder if it doesn't exist
if not os.path.exists(dataset_path):
    os.makedirs(dataset_path)

# create the dataset subfolders if they don't exist
for category in categories:
    if not os.path.exists(dataset_path + category):
        os.makedirs(dataset_path + category)

# create a list of youtube links for each category
links = {
    "Andalusi": [
        "https://www.youtube.com/watch?v=WnOLcSk8tTA",
        "https://www.youtube.com/watch?v=fp28KqrpnMw",
        "https://www.youtube.com/watch?v=LYGHpOluV1w",
        "https://www.youtube.com/watch?v=vuwN2JM6Wfg",
        "https://www.youtube.com/watch?v=g2vOcMxXan0"
    ],
    "Rai": [
        "https://www.youtube.com/watch?v=0Kfi5-QQIH0&list=PL47B58B163E3C2FE2",
        "https://www.youtube.com/watch?v=i_h60MvJ6g0&list=PL47B58B163E3C2FE2&index=3",
        "https://www.youtube.com/watch?v=PfgQuhwYqCY",
        "https://www.youtube.com/watch?v=uGboXSD0kFM&list=PL47B58B163E3C2FE2&index=12",
        "https://www.youtube.com/watch?v=Pp8N8eTLJ6w"
    ],
    "Chaabi": [
        "https://www.youtube.com/watch?v=i_CHZbvYJaI",
        "https://www.youtube.com/watch?v=O2Au75xK4ig",
        "https://www.youtube.com/watch?v=c0_C85n6jks",
        "https://www.youtube.com/watch?v=PYyUATg43VY",
        "https://www.youtube.com/watch?v=bNgwA-Nk_1o"
    ],
    "Gnawa": [
        "https://www.youtube.com/watch?v=K-xymUfJCgw",
        "https://www.youtube.com/watch?v=6QoFweDKpRs",
        "https://www.youtube.com/watch?v=lwnZarzSvJE",
        "https://www.youtube.com/watch?v=g731hsz0558",
        "https://www.youtube.com/watch?v=0xQHdSnP_o4"
    ],
    "Aita": [
        "https://www.youtube.com/watch?v=BAakP22SS7Q",
        "https://www.youtube.com/watch?v=8qyrd4pIrbw",
        "https://www.youtube.com/watch?v=AMc08Rw5ulY",
        "https://www.youtube.com/watch?v=gyL5fBhs3rE",
        "https://www.youtube.com/watch?v=O1f3vomw6DQ"
    ],
    "Moroccan Pop": [
        "https://www.youtube.com/watch?v=_Fwf45pIAtM&list=RDQM2RaL6Gk08sM&start_radio=1",
        "https://www.youtube.com/watch?v=Ph_tbASm31Y&list=RDQM2RaL6Gk08sM&index=16",
        "https://www.youtube.com/watch?v=BYKWNazJFpU&list=RDQM2RaL6Gk08sM&index=28",
        "https://www.youtube.com/watch?v=6sVxpn_6ReQ&list=RDQM2RaL6Gk08sM&index=43",
        "https://www.youtube.com/watch?v=07gpeX2-pIE"
    ],
    "Moroccan Rap": [
        "https://www.youtube.com/watch?v=Nlw6a-qhKEI",
        "https://www.youtube.com/watch?v=57Np3hjurvw",
        "https://www.youtube.com/watch?v=eI44JgK-lsI",
        "https://www.youtube.com/watch?v=lcIgjJ0b-5U",
        "https://www.youtube.com/watch?v=0ee2gtGo_Ok"
    ],
    "Moroccan Rock": [
        "https://www.youtube.com/watch?v=lNl2LUqKWrA&list=PLaGPY5hSZPm1hMLPy-w-krX_X14cV32WO",
        "https://www.youtube.com/watch?v=WfDTjh9372g&list=PLaGPY5hSZPm1hMLPy-w-krX_X14cV32WO&index=4",
        "https://www.youtube.com/watch?v=Pg91p-WL0Ws&list=PLaGPY5hSZPm1hMLPy-w-krX_X14cV32WO&index=8",
        "https://www.youtube.com/watch?v=puNFHTPYYTc&list=PLaGPY5hSZPm1hMLPy-w-krX_X14cV32WO&index=13",
        "https://www.youtube.com/watch?v=q1-tRV-UDT8",
    ],
    "Amazigh Folk": [
        "https://www.youtube.com/watch?v=tVhBKzhLwqM",
        "https://www.youtube.com/watch?v=8KO9qdvicpA&list=RDQMfYboW428Bcc&start_radio=1",
        "https://www.youtube.com/watch?v=VmZDEC-YvMk&list=RDQMfYboW428Bcc&index=6",
        "https://www.youtube.com/watch?v=8qcSdqc7QYo&list=RDQMfYboW428Bcc&index=8",
        "https://www.youtube.com/watch?v=asrtZaOj4Qg"
    ]
}

# download the videos and convert them to wav
for category in categories:
    for i in range(number_of_songs):
        print("Downloading " + category + " song " + str(i + 1) + "...")
        # check if the video is already downloaded
        if os.path.exists(dataset_path + category + "/" + category + str(i + 1) + ".wav"):
            print("Song " + str(i + 1) + " already exists!")
            continue
        yt = YouTube(
            links[category][i],
            on_progress_callback=on_progress,
            on_complete_callback=on_complete,
            use_oauth=False,
            allow_oauth_cache=True
        )
        try:
            yt.streams.filter(file_extension='mp4', res="360p").first().download(output_path=dataset_path + category, filename=category + str(i + 1) + ".mp4")
        except:
            print("Error downloading " + category + " song " + str(i + 1) + "!")
            continue

        # Convert video to audio (WAV)
        input_file = dataset_path + category + "/" + category + str(i + 1) + ".mp4"
        output_file = dataset_path + category + "/" + category + str(i + 1) + "_full.wav"
        convert_mp4_to_wav(input_file, output_file)
        os.remove(input_file)
        duration_sec = 180  # Duration in seconds
        input_file = output_file
        output_file = dataset_path + category + "/" + category + str(i + 1) + ".wav"
        crop_wav(input_file, output_file, 0, duration_sec)
        os.remove(input_file)

print("Done!")