"""
AI-Powered Song Recommender 🎵🎭

This program suggests songs based on your mood using sentiment analysis. 
Just describe how you're feeling, and it will recommend songs that match your vibe!
"""

import random
from textblob import TextBlob

print("!!! AI-Powered Song Recommender 🎵🎭 !!!")
print("Tell me how you're feeling, and I'll suggest a song for you!")

songs = {
    "happy": [
        "Gazab Ka Hai Din", "Dil Chahta Hai", "Dil Dhadakne Do", "Dil Diyan Gallan",
        "Madhubala", "Ud-Daa Punjab", "Atak Gaya", "Ilahi", 
        "Khaabon Ke Parinday", "Matargashti", "Ghungroo", "Manja", "Love You Zindagi", 
        "Senorita", "Shubhaarambh", "Badtameez Dil", "Sooraj Dooba Hai", "Desi Girl"
    ],
    "sad": [
        "Channa Mereya", "Kabira", "Agar Tum Saath Ho", "Phir Le Aaya Dil", 
        "Ae Dil Hai Mushkil", "Roke Na Ruke Naina", "Mann Bharrya", "Tum Hi Ho", 
        "Milne Hai Mujhse Aayi", "Ya Rabba", "Bhula Dena", "Tere Bina", "Nadaan Parindey", 
        "Hamari Adhuri Kahani", "Sunn Raha Hai", "Emptiness (Tune Mere Jaana)", "Tu Hi Re"
    ],
    "motivational": [
        "Zinda", "Lakshya Title Track", "Aashayein", "Kar Har Maidan Fateh", 
        "Ruk Jaana Nahin", "Brothers Anthem", "Jai Ho", "Roobaroo", "Mitwa (Kabhi Alvida Na Kehna)", 
        "Yeh Hosla", "Chak Lein De", "Apna Time Aayega", "Besabriyaan", "Kandhon Se Milte Hain Kandhe", 
        "Dhaakad", "Kuch Kariye", "Badal Pe Paon Hai"
    ],
    "party": [
        "Kala Chashma", "Chokra Jawan", "Ghungroo", "Bom Diggy", 
        "Abhi Toh Party Shuru Hui Hai", "Tamma Tamma Again", "The Breakup Song", 
        "Aankh Marey", "Gallan Goodiyan", "High Heels Te Nachche", "Saturday Saturday", 
        "Radha (Student of the Year)", "Swag Se Swagat", "First Class", "Cutiepie"
    ],
    "study": [
        "Choti Si Asha", "Kholo Kholo", "Chak De India", "Chale Chalo", 
        "Yeh Honsla", "Ruk Jaana Nahin", "Maa (Taare Zameen Par)", "Ilahi", 
        "Tu Bhoola Jise", "Sapno Se Bhare Naina", "Udaan Theme", "Aarambh Hai Prachand","Zinda"
    ],
    "romantic": [
        "Hamma Song", "Tum Hi Ho", "Tera Ban Jaunga", "Tera Hone Laga Hoon", 
        "Tum Se Hi", "Sanam Teri Kasam", "Pee Loon", "Janam Janam", "Shayad", 
        "Raabta", "Tujh Mein Rab Dikhta Hai", "Sun Saathiya", "Tum Prem Ho",
        "Kaun Tujhe", "Pehli Nazar Mein", "Main Rang Sharbaton Ka"
    ],
    "retro": [
        "O Mere Dil Ke Chain", "Roop Tera Mastana", "Lag Ja Gale", "Pal Pal Dil Ke Paas",
        "Mere Sapno Ki Rani", "Chura Liya Hai Tumne", "Ek Ajnabee Haseena Se", 
        "Yeh Shaam Mastani", "Gulabi Aankhen", "Hamen Tumse Pyar Kitna", "Tere Bina Zindagi Se", 
        "Ae Mere Humsafar", "Bheegi Bheegi Raaton Mein", "Dum Maaro Dum", "Chhukar Mere Mann Ko"
    ],
    "indie": [
        "Udd Gaye", "Chaand Baaliyan", "Liggi", "Kasoor", "Tera Zikr", 
        "Kho Gaye Hum Kahan", "Baatein Ye Kabhi Na", "Ilahi", "Alag Aasmaan", 
        "Mai Ni Meriye", "Dil Mere", "Woh Baarishein", "Baahon Mein", "Dil tu jaan tu", "Nadaniya"
    ],
    "neutral": [
        "Tera Yaar Hoon Main", "Raabta", "Kun Faya Kun", "O Rangrez", 
        "Kaise Hua", "Humdard", "Maa", "Ae Watan", "Ekla Chalo Re", 
        "Kaisi Paheli Zindagani", "Ik Onkar", "Namo Namo", "Yun Hi Chala Chal", 
        "Hawayein", "O Saathi", "Dil Hai Chhota Sa"
    ]
}

while True:
    user_input = input("\nDescribe your mood (or type 'exit' to stop): ").lower()
    
    if user_input == "exit":
        print("Bye bye!! Have a great day! 🎧✨")
        break
    
    # Sentiment Analysis
    sentiment = TextBlob(user_input).sentiment.polarity
    mood = "neutral"

    # Keyword-based Mood Detection
    if "retro" in user_input:
        mood = "retro"
    elif "indie" in user_input:
        mood = "indie"
    elif "romantic" in user_input:
        mood = "romantic"
    elif "study" in user_input:
        mood = "study"
    elif "party" in user_input:
        mood = "party"
    elif "bored" in user_input:
        mood = random.choice(["happy", "party", "motivational"])
    elif "heartbreak" in user_input or "cheated" in user_input:
        mood = "sad"
    elif "demotivated" in user_input or "lost" in user_input:
        mood = "motivational"
    elif sentiment > 0.2:
        mood = "happy"
    elif sentiment < -0.2:
        mood = "sad"

    # Ensure valid mood
    if mood not in songs:
        mood = "neutral"
    
    # Recommend Songs
    print("\n🎵 Based on your mood, listen to: " + ", ".join(random.sample(songs[mood], 3)))
