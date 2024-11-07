import re

# คำศัพท์ในแต่ละ Unit
unit_6_vocab = [
    "angry", "careless", "cheerful", "in a hurry", "noisy", "patient",
    "anxious about her baby", "enthusiastic about music", "late for a flight",
    "TIMU", "reluctant to say goodbye", "access", "cozy", "delighted", "deserve",
    "downside", "fine dining", "hosts", "paradise"
]

unit_8_vocab = [
    "art scene", "bike lanes", "nightlife", "pedestrians", "public transportation",
    "vehicle traffic", "air quality", "cost of living", "crime rate", "housing prices",
    "job opportunities", "public parks", "school system", "shops and restaurants"
]

unit_12_vocab = [
    "article", "breaking news", "camera operator", "citizen journalist", "headline",
    "news site", "reporter", "weather report", "blogger", "broadcast", "business",
    "column", "editor", "journalist", "politics", "update", "contagious", "oppose",
    "protesters", "rescue", "attraction", "consequences", "curiosity", "negativity bias",
    "overall", "satisfies", "survival", "trust"
]

# คำศัพท์ทั้งหมด
all_vocab = {
    "Unit 6": unit_6_vocab,
    "Unit 8": unit_8_vocab,
    "Unit 12": unit_12_vocab
}

# ข้อความที่ให้มา
paragraph = """
Scene 1: News on TV
Reporter: "A murder occurred at a seaside villa among a group of students who gathered for a holiday. Arm Minhyo was found dead in his room. The police have yet to identify the killer, but they suspect that one of the friends present might be involved..."
Ton: “I can't believe... this happened to us. It's breaking news, how can this be true?”
Phak: “Why... Why did this happen? This is like a crime story right out of a news article...”
Tang: “We’ll never be able to forget this, the consequences are just too much…”

Scene 2: Flashback, Before the Incident
Oong: “I never thought we’d all be here together like this! And the beach is like paradise, right? It feels so warm and welcoming.”
Ton: “Yeah! This is exactly the kind of place for us! It’s so rare we get to meet up like this. It feels cozy here.”
Arm: “Yeah, let’s see who’s getting dragged into the ocean first!”
Phak: “How about we get started on the food? I’m getting hungry!”
Tang: “Mmm, I’m really craving fine dining... or BBQ! Ton, are you ready to be our trip’s chef?”
Ton: “Of course! Tell me what you want to eat, but you’re all serving yourselves tonight! But no complaints if you get a little careless with your servings.”

Scene 3: A Peaceful Night
Arm: “Remember when we went camping as kids, and someone tricked us into thinking there was a monster? We all ran for our lives!”
Tang: “Oh yeah, that was Oong’s doing! He’s the one who started it all, making us run like crazy!”
Oong: “Hey, you guys were just scared! I was just adding some fun to the atmosphere!”
Phak: “Fun? More like a nightmare! I remember being scared for a whole week!”
Ton: “But even after all that, you’re still the friend we trust. You're the one who kept our spirits cheerful.”
Phak: “I can’t believe I’m still friends with someone who used to be so mischievous…”

Scene 4: Heading to Bed
Phak: “Okay, everyone, we’re swimming early tomorrow, so don’t get too hungover.”
Arm: “Of course! I’ll be the first to jump into the sea.”
Oong: “Oh, we’ll see about that, Arm. You’re the first we’ll throw in!”
Ton: “Don’t be too anxious, Oong, we’ll let Arm enjoy the water first.”

Scene 5: The Unexpected Incident
Phak: “Arm! Arm! What’s going on?”
Ton: “What happened? Who would do this to Arm? This is unbelievable, how could something like this happen here, in such a peaceful place?”
Tang: “This can’t be… We were just talking to him before bed. Why…?”
Oong: “...No one knows what happened, but we have to find out. We need to find some answers.”
Ton: “This is becoming a real-life nightmare.”

Scene 6: Rising Suspicion
Phak: “I hate to think this way, but… could it be one of us?”
Ton: “How can you say that? We’re friends, aren’t we?”
Tang: “But who else could have done this? We rented this house; it’s just the five of us…”
Oong: “There’s no need to look for anyone else... We need to call the police. This is becoming more like an investigation.”
Police Officer: “We’ll inform you of the autopsy results later, but for now, everyone should come to the station.”
Oong: “It was me… I killed Arm.”
Phak: “What? Why would you do that, Oong? We’re friends, aren’t we?”
Oong: “I’m sorry… but there’s something from my past… something I couldn’t let go of. It drove me to this…”

Scene 7: Back to the Present
Reporter: “The police have arrested the perpetrator in the murder case. The investigation is ongoing.”
Tang: “Wait… wasn’t that Oong?”
Phak: “I’ve known for a while, but why did it have to end this way?”
Ton: “Sigh… All of our good memories have been ruined. I never thought something like this would happen in our circle of friends. It’s like a headline we never expected to see.”
Oong: “But I can still be friends with everyone, right?”
Ton: “I’m reluctant to say goodbye to everything we had.”
"""

# ฟังก์ชันตรวจหาคำศัพท์ใน paragraph
def find_vocabulary(paragraph, vocab_dict):
    results = {}
    # ตรวจหาแต่ละคำศัพท์ในพารากราฟ
    for unit, vocab_list in vocab_dict.items():
        found_words = []
        for word in vocab_list:
            # ใช้ regular expression เพื่อตรวจหาคำศัพท์ในข้อความ
            if re.search(r'\b' + re.escape(word) + r'\b', paragraph, re.IGNORECASE):
                found_words.append(word)
        if found_words:
            results[unit] = found_words
    return results

# หาคำศัพท์ที่พบในพารากราฟ
found_vocab = find_vocabulary(paragraph, all_vocab)

# แสดงผลลัพธ์
for unit, words in found_vocab.items():
    for word in words:
        print(f"{unit}: {word}")
