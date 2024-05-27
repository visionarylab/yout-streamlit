import streamlit as st

from service.staging import Staging
from service.video_downloader import VideoDownloader

def download_video(youtube_url,start_second):

    staging = Staging("tmp")
    staging_path = staging.run()

    file_bytes,filepath,filename = VideoDownloader(youtube_url,start_second).run(staging_path)
    st.session_state['video_downloaded'] = True
    st.session_state['video_filename'] = filename
    st.session_state['video_filepath'] = filepath
    st.session_state['video_bytes'] = file_bytes

    staging.free()

st.title("Video Downloader")

youtube_url = st.text_input("Youtube URL:",placeholder="Enter here...")
st.button("Get Video", on_click=download_video,args=(youtube_url,0))

if 'video_downloaded' in st.session_state:
    st.download_button(label="Video Download",data=st.session_state['video_bytes'],file_name=st.session_state['video_filename'],mime='application/octet-stream')