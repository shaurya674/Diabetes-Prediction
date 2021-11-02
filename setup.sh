mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"shauryapatel674@gmail.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=true\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
