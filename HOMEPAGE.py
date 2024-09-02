import streamlit as st
from PIL import Image

st.set_page_config(page_title="RECOMMENDATION SYSTEM", layout="wide")
st.sidebar.success("SELECT A PAGE ABOVE.")
st.button("Page")

# Load images
img_contact = Image.open("Pics\\kushal_mangal.jpg")
img_contac = Image.open("Pics\\animal.jpg")
img_conta = Image.open("Pics\\daughter_of_wolf.jpg")
img_cont = Image.open("Pics\\thenun.jpg")
img_con = Image.open("Pics\mysterious_island.jpg")
img_co = Image.open("Pics\\the_black_hole.jpg")
img_c = Image.open("Pics\\hacker.jpg")
img_b = Image.open("Pics\\2067movie.jpg")
img_d = Image.open("Pics\\piku1.jpg")
img_e = Image.open("Pics\\pi.jpg")
img_f = Image.open("Pics\\12fail.jpg")
img_g = Image.open("Pics\\agent2.jpg")
img_h = Image.open("Pics\\goodbye.jpg")
img_i = Image.open("Pics\\spykids2.jpg")

st.header("ALL TIME BOLLYWOOD & HOLLYWOOD HITS")

with st.container():
    st.write("---")

movies = [
    {"image": img_contact, "title": "Khushal Mangal", "description": """ "Khushal Mangal" is a Bollywood romantic comedy film directed by Manoj Sharma, released in 2019. The movie stars Priyanka Panchal, Chandrachur Singh, and Brijendra Kala in lead roles.""", "url": "https://youtu.be/1rALK2Fi2Zg?si=w6SGHYhw6UF8wEIf"},
    {"image": img_contac, "title": "Animal", "description": """Animal is a 2023 Indian Hindi-language action drama film co-written, directed and edited by Sandeep Reddy Vanga and produced by T-Series Films, Bhadrakali Pictures and Cine1 Studios. The film stars Ranbir Kapoor, Anil Kapoor, Bobby Deol, Rashmika Mandanna and Tripti Dimri.""", "url": "https://youtu.be/6Ez-EQ_f6gY?si=JAEpbU_S29xwt5NA"},
    {"image": img_conta, "title": "Daughter of the Wolf", "description": """Daughter of the Wolf is a 2019 Canadian action thriller film directed by David Hackl and written by Nika Agiashvili. The film stars Gina Carano and Richard Dreyfuss. Clair Hamilton is a military veteran whose son Charlie has been kidnapped.""", "url": "https://youtu.be/G9LGseUEFdI?si=tfRs65uslgoo3VrV"},
    {"image": img_cont, "title": "The Nun", "description": """The Nun is a 2018 American gothic supernatural horror film directed by Corin Hardy and written by Gary Dauberman, from a story by Dauberman and James Wan. It serves as a spiritual spin-off to The Conjuring 2 and is the fifth installment in The Conjuring shared universe.""", "url": "https://youtu.be/VSaEdshUCzA?si=rNGbi_ct4-Ws7Pz3"},
    {"image": img_con, "title": "Mysterious Island", "description": """Mysterious Island (UK: Jules Verne's Mysterious Island) is a 1961 science fiction adventure film about prisoners in the American Civil War who escape in a balloon and then find themselves stranded on a remote island populated by giant and tiny animals. Loosely based upon the 1874 novel The ..""", "url": "https://youtu.be/YsasEgkfJJ8?si=sLMy1B8vx5K8LZKS"},
    {"image": img_co, "title": "The Black Hole", "description": """The Black Hole is a 1979 American science fiction film directed by Gary Nelson and produced by Walt Disney Productions. The film stars Maximilian Schell, Robert Forster, Joseph Bottoms, Yvette Mimieux, Anthony Perkins and Ernest Borgnine, while the voices of the main robot characters are provided ...""", "url": "https://youtu.be/HSaQoVOFS1U?si=P1MV0lqiu6L0aKyF"},
    {"image": img_b, "title": "2067", "description": """2067 is a 2020 Australian science fiction film directed and written by Seth Larney from a treatment by Gavin Scott Davis (itself from Larney's own idea), and starring Kodi Smit-McPhee and Ryan Kwanten. In the year 2067, Earth has been devastated by climate change and an ongoing nuclear war.""", "url": "https://youtu.be/1rALK2Fi2Zg?si=w6SGHYhw6UF8wEIf"},
    {"image": img_c, "title": "Hackers", "description": """Hackers is a 1995 American crime thriller film directed by Iain Softley and starring Jonny Lee Miller, Angelina Jolie, Jesse Bradford, Matthew Lillard, Laurence Mason, Renoly Santiago, Lorraine Bracco, and Fisher Stevens. The film follows a group of high school hackers and their involvement ...""", "url": "https://youtu.be/mp-_vGwddaM?si=PxJvpf3g_l8fGGEa"},
    {"image": img_f, "title": "12th FAIL", "description": """12th Fail" is a poignant and relatable film that delves into the struggles and pressures faced by students in the Indian education system. The movie follows the journey of a student who fails his 12th-grade exams and the subsequent challenges he encounters in a society that often judges individuals based on academic performance ...""", "url": "https://youtu.be/NR645ohya00?si=91CGMgAuUc8NGOVB"},
    {"image": img_e, "title": "Pirarate Island", "description": """"Pirate Island" is an engaging adventure that captivates readers with its thrilling narrative and vivid imagery. The novel immerses readers in a world of swashbuckling pirates, hidden treasures, and daring escapades...""", "url": "https://youtu.be/nv9I9LNzzY4?si=-xifDy4cxEgPv2f7"},
    {"image": img_d, "title": "PIKU", "description": """"Piku" is a delightful and heartwarming film that beautifully captures the complexities of family relationships while also infusing humor and charm into its narrative. Directed by Shoojit Sircar, the film revolves around the quirky dynamics between an eccentric father-daughter duo, played impeccably by Amitabh Bachchan and Deepika Padukone...""", "url": "https://youtu.be/yYr8q0y5Jfg?si=P44kVDMFb5jyJqtR"},
    {"image": img_g, "title": "AGENT", "description": """"Agent" is its impressive performances. The lead actor delivers a compelling portrayal of the protagonist, capturing the complexities of his character with finesse. Supported by a talented ensemble cast, each actor brings depth and authenticity to their roles, elevating the overall viewing experience...""", "url": "https://youtu.be/xBefFUF_PQs?si=nhE0usckGugo_NdE"},
    {"image": img_h, "title": "GOODBYE", "description": """"Goodbye Indian" is an emotional rollercoaster that showcases the brilliance of Bollywood legend Amitabh Bachchan. The film revolves around themes of love, loss, and reconciliation, set against the backdrop of Indian culture and society...""", "url": "https://youtu.be/mp-_vGwddaM?si=PxJvpf3g_l8fGGEa"},
    {"image": img_i, "title": "Spy Kids-2", "description": """"Spy Kids 2: The Island of Lost Dreams" is a thrilling sequel that takes the adventure to a whole new level. Directed by Robert Rodriguez, this family-friendly film continues the story of Carmen and Juni Cortez, young spies who embark on a mission to a mysterious island filled with fantastical creatures and hidden dangers...""", "url": "https://youtu.be/KrBnxqKF0d8?si=15smQAWTIrM2b7i1"}

]
# Custom CSS for the blue button
st.markdown("""
    <style>
        .watch-button {
            display: inline-block;
            margin-top: 10px;
            padding: 10px 20px;
            background-color: #BEE3F9;
            color: white;
            border-radius: 5px;
            text-decoration: none;
            border: 2px solid #000000;
            transition: background-color 0.3s, color 0.3s;
            position: relative;
            transition: all 0.4s ease;
        }
        .watch-button:hover {
            background-color: #FFFFFF;
            color: #000000;
            box-shadow: 0px 0px 33px #D30000;
        }
    </style>
""", unsafe_allow_html=True)

# Display movies in two columns
for i in range(0, len(movies), 2):
    with st.container():
        st.write("##")
        col1, col2 = st.columns(2)
        with col1:
            st.image(movies[i]["image"], width=300)
            st.header(movies[i]["title"])
            st.write(movies[i]["description"])
            st.markdown(f"<a href='{movies[i]['url']}' class='watch-button'>Watch Movie</a>", unsafe_allow_html=True)
        if i + 1 < len(movies):
            with col2:
                st.image(movies[i + 1]["image"], width=300)
                st.header(movies[i + 1]["title"])
                st.write(movies[i + 1]["description"])
                st.markdown(f"<a href='{movies[i + 1]['url']}' class='watch-button'>Watch Movie</a>", unsafe_allow_html=True)
               

with st.container():
    st.write("---")
    st.header("About us")
    st.subheader("Welcome to codewthR_recomender system - Your Ultimate Movie Companion!")
    st.write("""At codewthR_recomender, we believe that every movie lover deserves personalized recommendations tailored to their unique tastes and preferences. Whether you're a cinephile searching for hidden gems or a casual""")
