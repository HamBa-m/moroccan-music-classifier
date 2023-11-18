from utils import *


# create a list of youtube links for each category
links = {
    "Andalusi": [
        "https://www.youtube.com/watch?v=WnOLcSk8tTA",
        "https://www.youtube.com/watch?v=fp28KqrpnMw",
        "https://www.youtube.com/watch?v=LYGHpOluV1w",
        "https://www.youtube.com/watch?v=vuwN2JM6Wfg",
        "https://www.youtube.com/watch?v=g2vOcMxXan0",
        "https://www.youtube.com/watch?v=vyqyQM1bNrA&pp=ygUQYW5kYWx1c2lhbiBtdXNpYw%3D%3D",
        "https://www.youtube.com/watch?v=EE8cHyjCNLE&pp=ygUQYW5kYWx1c2lhbiBtdXNpYw%3D%3D",
        "https://www.youtube.com/watch?v=jh3bwHc1PZc&pp=ygUQYW5kYWx1c2lhbiBtdXNpYw%3D%3D",
        "https://www.youtube.com/watch?v=bkUYJImXlrQ&pp=ygUQYW5kYWx1c2lhbiBtdXNpYw%3D%3D",
        "https://www.youtube.com/watch?v=kvTSWRAh5Tc&pp=ygUQYW5kYWx1c2lhbiBtdXNpYw%3D%3D",
        "https://www.youtube.com/watch?v=A-jzhHWkYoU&pp=ygUQYW5kYWx1c2lhbiBtdXNpYw%3D%3D",
        "https://www.youtube.com/watch?v=eIlZtydpKqc&pp=ygUQYW5kYWx1c2lhbiBtdXNpYw%3D%3D",
        "https://www.youtube.com/watch?v=wjYBglwr8aA&pp=ygUQYW5kYWx1c2lhbiBtdXNpYw%3D%3D",
        "https://www.youtube.com/watch?v=KgBjmpPtPMQ&pp=ygUQYW5kYWx1c2lhbiBtdXNpYw%3D%3D",
        "https://www.youtube.com/watch?v=g2vOcMxXan0&pp=ygUQYW5kYWx1c2lhbiBtdXNpYw%3D%3D",
    ],
    "Rai": [
        "https://www.youtube.com/watch?v=0Kfi5-QQIH0&list=PL47B58B163E3C2FE2",
        "https://www.youtube.com/watch?v=i_h60MvJ6g0&list=PL47B58B163E3C2FE2&index=3",
        "https://www.youtube.com/watch?v=PfgQuhwYqCY",
        "https://www.youtube.com/watch?v=uGboXSD0kFM&list=PL47B58B163E3C2FE2&index=12",
        "https://www.youtube.com/watch?v=Pp8N8eTLJ6w",
        "https://www.youtube.com/watch?v=E2pDHoBFL-A&list=PL47B58B163E3C2FE2&index=14&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=H7rhMqTQ4WI&list=PL47B58B163E3C2FE2&index=15&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=B14g-a29GNU&list=PL47B58B163E3C2FE2&index=16&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=mtiaNZ-evWs&list=PL47B58B163E3C2FE2&index=28&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=0Kfi5-QQIH0&list=PL47B58B163E3C2FE2&index=1&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=i_h60MvJ6g0&list=PL47B58B163E3C2FE2&index=3&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=2X37yy_-YxI&list=PL47B58B163E3C2FE2&index=4&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=TM-2XmzB59w&list=PL47B58B163E3C2FE2&index=5&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=Lf5xcBSV5B8&list=PL47B58B163E3C2FE2&index=6&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=YAgr_S8VsvI&list=PL47B58B163E3C2FE2&index=8&pp=iAQB8AUB"
    ],
    "Chaabi": [
        "https://www.youtube.com/watch?v=i_CHZbvYJaI",
        "https://www.youtube.com/watch?v=O2Au75xK4ig",
        "https://www.youtube.com/watch?v=c0_C85n6jks",
        "https://www.youtube.com/watch?v=PYyUATg43VY",
        "https://www.youtube.com/watch?v=bNgwA-Nk_1o",
        "https://www.youtube.com/watch?v=bHZ1s3BlTSk&list=PLNWojXpFjS6cwHivX911naCD1Y0b5rTbo&index=1&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=IvIY7r1SWH4&list=PLNWojXpFjS6cwHivX911naCD1Y0b5rTbo&index=2&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=Sjrd1aP5cRo&list=PLNWojXpFjS6cwHivX911naCD1Y0b5rTbo&index=3&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=U7Vq-4eLBYk&list=PLNWojXpFjS6cwHivX911naCD1Y0b5rTbo&index=5&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=U5o-7BZznLo&list=PLNWojXpFjS6cwHivX911naCD1Y0b5rTbo&index=7&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=EeiEHMrKBGI&list=PLNWojXpFjS6cwHivX911naCD1Y0b5rTbo&index=11&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=7QIPy7uCnEk&list=PLNWojXpFjS6cwHivX911naCD1Y0b5rTbo&index=13&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=X_IagvTGFmg&list=PLNWojXpFjS6cwHivX911naCD1Y0b5rTbo&index=15&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=xMRB9b9XsdM&list=PLNWojXpFjS6cwHivX911naCD1Y0b5rTbo&index=10&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=HKgXn6cjhNs&list=PLNWojXpFjS6cwHivX911naCD1Y0b5rTbo&index=12&pp=iAQB8AUB",
    ],
    "Gnawa": [
        "https://www.youtube.com/watch?v=K-xymUfJCgw",
        "https://www.youtube.com/watch?v=6QoFweDKpRs",
        "https://www.youtube.com/watch?v=lwnZarzSvJE",
        "https://www.youtube.com/watch?v=g731hsz0558",
        "https://www.youtube.com/watch?v=0xQHdSnP_o4",
        "https://www.youtube.com/watch?v=wgeRF3YOngs&list=PLnOSH5j1sQh-qDyPnE9fC83yAbjEmWU23&index=1&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=dlyHEOFLp58&list=PLnOSH5j1sQh-qDyPnE9fC83yAbjEmWU23&index=2&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=dlLwDnls4rM&list=PLnOSH5j1sQh-qDyPnE9fC83yAbjEmWU23&index=3&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=LAY5E5ZL7fo&list=PLnOSH5j1sQh-qDyPnE9fC83yAbjEmWU23&index=4&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=VnegQ7op9Tc&list=PLnOSH5j1sQh-qDyPnE9fC83yAbjEmWU23&index=5&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=keVvkR7jBTs&list=PLnOSH5j1sQh-qDyPnE9fC83yAbjEmWU23&index=6&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=0lsr67ZXKyA&list=PLnOSH5j1sQh-qDyPnE9fC83yAbjEmWU23&index=8&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=p2vdvCy2qho&list=PLnOSH5j1sQh-qDyPnE9fC83yAbjEmWU23&index=10&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=T6ikMujr-Zg&list=PLnOSH5j1sQh-qDyPnE9fC83yAbjEmWU23&index=13&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=i7wVtGOVt8c&list=PLnOSH5j1sQh-qDyPnE9fC83yAbjEmWU23&index=17&pp=iAQB8AUB",
    ],
    "Aita": [
        "https://www.youtube.com/watch?v=BAakP22SS7Q",
        "https://www.youtube.com/watch?v=8qyrd4pIrbw",
        "https://www.youtube.com/watch?v=AMc08Rw5ulY",
        "https://www.youtube.com/watch?v=gyL5fBhs3rE",
        "https://www.youtube.com/watch?v=O1f3vomw6DQ",
        "https://www.youtube.com/watch?v=hjlUhQfRQkw&pp=ygUNbW9yb2NjYW4gYWl0YQ%3D%3D",
        "https://www.youtube.com/watch?v=1WqoPNG9Ol8&pp=ygUNbW9yb2NjYW4gYWl0YQ%3D%3D",
        "https://www.youtube.com/watch?v=FkW-aZI0ZzA&pp=ygUNbW9yb2NjYW4gYWl0YQ%3D%3D",
        "https://www.youtube.com/watch?v=oSG4cltsWfQ&pp=ygUNbW9yb2NjYW4gYWl0YQ%3D%3D",
        "https://www.youtube.com/watch?v=qg2j6JGXo5E&pp=ygUObW9yb2NjYW4gYWxvdWE%3D",
        "https://www.youtube.com/watch?v=BAakP22SS7Q&pp=ygULYWxvdWEgc29uZ3M%3D",
        "https://www.youtube.com/watch?v=QOJ9w96v7IQ&pp=ygULYWxvdWEgc29uZ3M%3D",
        "https://www.youtube.com/watch?v=cerPT1PbY3I&pp=ygUQYWxvdWEgYWl0YSBzb25ncw%3D%3D",
        "https://www.youtube.com/watch?v=oflEFjv172E&pp=ygUQYWxvdWEgYWl0YSBzb25ncw%3D%3D",
        "https://www.youtube.com/watch?v=-nW6DyVCwNs&pp=ygUQYWxvdWEgYWl0YSBzb25ncw%3D%3D"
    ],
    "Moroccan Pop": [
        "https://www.youtube.com/watch?v=_Fwf45pIAtM&list=RDQM2RaL6Gk08sM&start_radio=1",
        "https://www.youtube.com/watch?v=Ph_tbASm31Y&list=RDQM2RaL6Gk08sM&index=16",
        "https://www.youtube.com/watch?v=BYKWNazJFpU&list=RDQM2RaL6Gk08sM&index=28",
        "https://www.youtube.com/watch?v=6sVxpn_6ReQ&list=RDQM2RaL6Gk08sM&index=43",
        "https://www.youtube.com/watch?v=07gpeX2-pIE",
        "https://www.youtube.com/watch?v=59LAMFrqACg&list=PLME9drm1zCz9C8w26Qy1EIoik7ODKX467&index=8&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=QMbg-1kzvCI&list=PLME9drm1zCz9C8w26Qy1EIoik7ODKX467&index=10&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=ZfIZNKRp2-o&list=PLME9drm1zCz9C8w26Qy1EIoik7ODKX467&index=11&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=IaUiTZAVt9E&list=PLME9drm1zCz9C8w26Qy1EIoik7ODKX467&index=15&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=2GEp_x2HaLo&list=PLME9drm1zCz9C8w26Qy1EIoik7ODKX467&index=18&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=_pM4t96M7Ls&list=PLME9drm1zCz9C8w26Qy1EIoik7ODKX467&index=20&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=oSRCdp5dNTQ&list=PLME9drm1zCz9C8w26Qy1EIoik7ODKX467&index=23&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=qPF-vFYAho0&list=PLME9drm1zCz9C8w26Qy1EIoik7ODKX467&index=26&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=eJl3piSM6Qw&list=PLME9drm1zCz9C8w26Qy1EIoik7ODKX467&index=28&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=9ElVG86Y2LM&list=PLME9drm1zCz9C8w26Qy1EIoik7ODKX467&index=32&pp=iAQB8AUB"
    ],
    "Moroccan Rap": [
        "https://www.youtube.com/watch?v=Nlw6a-qhKEI",
        "https://www.youtube.com/watch?v=57Np3hjurvw",
        "https://www.youtube.com/watch?v=eI44JgK-lsI",
        "https://www.youtube.com/watch?v=lcIgjJ0b-5U",
        "https://www.youtube.com/watch?v=0ee2gtGo_Ok",
        "https://www.youtube.com/watch?v=-qrUBZg4484&list=PLstCfioSvedI1B_pnjBsyDxOMYVJwqx_N&index=1&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=sGTVnOrUFY4&list=PLstCfioSvedI1B_pnjBsyDxOMYVJwqx_N&index=6&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=sTBo3r_4emo&list=PLstCfioSvedI1B_pnjBsyDxOMYVJwqx_N&index=9&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=3-nTD831gPE&list=PLstCfioSvedI1B_pnjBsyDxOMYVJwqx_N&index=11&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=u1Hmaho998c&list=PLstCfioSvedI1B_pnjBsyDxOMYVJwqx_N&index=15&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=JSrGw5HftbY&list=PLstCfioSvedI1B_pnjBsyDxOMYVJwqx_N&index=17&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=HtQNS33m1JA&list=PLstCfioSvedI1B_pnjBsyDxOMYVJwqx_N&index=19&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=X0MKKYepF70&list=PLstCfioSvedI1B_pnjBsyDxOMYVJwqx_N&index=23&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=s7ugH-ExzZc&list=PLstCfioSvedI1B_pnjBsyDxOMYVJwqx_N&index=24&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=z361iPEtADM&list=PLstCfioSvedI1B_pnjBsyDxOMYVJwqx_N&index=25&pp=iAQB8AUB",
    ],
    "Moroccan Rock": [
        "https://www.youtube.com/watch?v=lNl2LUqKWrA&list=PLaGPY5hSZPm1hMLPy-w-krX_X14cV32WO",
        "https://www.youtube.com/watch?v=WfDTjh9372g&list=PLaGPY5hSZPm1hMLPy-w-krX_X14cV32WO&index=4",
        "https://www.youtube.com/watch?v=Pg91p-WL0Ws&list=PLaGPY5hSZPm1hMLPy-w-krX_X14cV32WO&index=8",
        "https://www.youtube.com/watch?v=puNFHTPYYTc&list=PLaGPY5hSZPm1hMLPy-w-krX_X14cV32WO&index=13",
        "https://www.youtube.com/watch?v=q1-tRV-UDT8",
        "https://www.youtube.com/watch?v=hi_Qdp9Tvyo&list=PLrvWRYzZiC0jt4r1mkgD3ox5g2j879Lx1&index=2&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=9aO1bsxXyYw&list=PLrvWRYzZiC0jt4r1mkgD3ox5g2j879Lx1&index=3&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=-OLjXaTXQI0&list=PLrvWRYzZiC0jt4r1mkgD3ox5g2j879Lx1&index=5&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=10GNvG78PCU&list=PLrvWRYzZiC0jt4r1mkgD3ox5g2j879Lx1&index=10&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=-VGkP6aAUHU&list=PLrvWRYzZiC0jt4r1mkgD3ox5g2j879Lx1&index=12&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=u7HEOayILCY&list=PLrvWRYzZiC0jt4r1mkgD3ox5g2j879Lx1&index=15&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=H8obQro7fys&list=PLrvWRYzZiC0jt4r1mkgD3ox5g2j879Lx1&index=22&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=dOhhHU70lC8&list=PLrvWRYzZiC0jt4r1mkgD3ox5g2j879Lx1&index=24&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=9pIYbuFrNfY&list=PLrvWRYzZiC0jt4r1mkgD3ox5g2j879Lx1&index=29&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=tVhBKzhLwqM&list=PLrvWRYzZiC0jt4r1mkgD3ox5g2j879Lx1&index=33&pp=iAQB8AUB",
    ],
    "Amazigh Folk": [
        "https://www.youtube.com/watch?v=tVhBKzhLwqM",
        "https://www.youtube.com/watch?v=8KO9qdvicpA&list=RDQMfYboW428Bcc&start_radio=1",
        "https://www.youtube.com/watch?v=VmZDEC-YvMk&list=RDQMfYboW428Bcc&index=6",
        "https://www.youtube.com/watch?v=8qcSdqc7QYo&list=RDQMfYboW428Bcc&index=8",
        "https://www.youtube.com/watch?v=asrtZaOj4Qg",
        "https://www.youtube.com/watch?v=boiiiVh52v4&list=PLBfxX84beS7AFtC0d2WYUhc7qDiXFuUmx&index=2&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=2e_MqpC3b3M&list=PLBfxX84beS7AFtC0d2WYUhc7qDiXFuUmx&index=7&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=5C1u_MFahhw&list=PLBfxX84beS7AFtC0d2WYUhc7qDiXFuUmx&index=11&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=opIagrc6mNQ&list=PLBfxX84beS7AFtC0d2WYUhc7qDiXFuUmx&index=18&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=CviCqehbvkc&list=PLBfxX84beS7AFtC0d2WYUhc7qDiXFuUmx&index=21&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=utwkujvEwiI&list=PLBfxX84beS7AFtC0d2WYUhc7qDiXFuUmx&index=25&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=isI_oIiaDuQ&list=PLBfxX84beS7AFtC0d2WYUhc7qDiXFuUmx&index=27&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=0bsAimAUB00&list=PLBfxX84beS7AFtC0d2WYUhc7qDiXFuUmx&index=30&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=IrVzCgwF2n8&list=PLBfxX84beS7AFtC0d2WYUhc7qDiXFuUmx&index=34&pp=iAQB8AUB",
        "https://www.youtube.com/watch?v=uR2aivOjeQ8&list=PLBfxX84beS7AFtC0d2WYUhc7qDiXFuUmx&index=40&pp=iAQB8AUB",
    ]
}

# define the path to save the dataset
dataset_path = "data/"

# create the dataset folder if it doesn't exist
if not os.path.exists(dataset_path):
    os.makedirs(dataset_path)

# create the dataset subfolders if they don't exist
for category in links.keys():
    if not os.path.exists(dataset_path + category):
        os.makedirs(dataset_path + category)

# download the videos and convert them to wav
for category in links.keys():
    for i in range(len(links[category])):
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
            yt.streams.filter(file_extension='mp4', res="360p").first().download(
                output_path=dataset_path + category, filename=category + str(i + 1) + ".mp4")
        except:
            print("Error downloading " + category + " song " + str(i + 1) + "!")
            continue

        # Convert video to audio (WAV)
        input_file = dataset_path + category + \
            "/" + category + str(i + 1) + ".mp4"
        output_file = dataset_path + category + \
            "/" + category + str(i + 1) + "_full.wav"
        convert_mp4_to_wav(input_file, output_file)
        os.remove(input_file)
        duration_sec = 180  # Duration in seconds
        input_file = output_file
        output_file = dataset_path + category + \
            "/" + category + str(i + 1) + ".wav"
        crop_wav(input_file, output_file, 0, duration_sec)
        os.remove(input_file)

print("Done!")
