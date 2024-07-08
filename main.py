import streamlit as st
import streamlit_authenticator as stauth



import yaml
from yaml.loader import SafeLoader

with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

authenticator.login()

if st.session_state["authentication_status"]:
    authenticator.logout()
    st.write(f'ようこそ *{st.session_state["name"]}* さん！')
    st.title('Counter Example')
    if 'count' not in st.session_state:
        st.session_state.count = 0

    increment = st.button('Increment')
    if increment:
        st.session_state.count += 1

    st.write('Count = ', st.session_state.count)
elif st.session_state["authentication_status"] is False:
    st.error('ユーザー名/パスワードが不正です')
elif st.session_state["authentication_status"] is None:
    st.warning('ユーザー名とパスワードを入力してください')
