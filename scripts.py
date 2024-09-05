import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi as YTA

st.write('Hello')

link = st.text_input(label='YouTube 영상 주소를 입력해주세요')

if link:
    id = link.split('/')
    vid_id = id[-1]
    print(vid_id)
    data = YTA.get_transcript(vid_id, languages=['ko','en'])
    ttl=''
    for tt in data:
        ttl+=" " +tt['text']
    st.write(ttl)

