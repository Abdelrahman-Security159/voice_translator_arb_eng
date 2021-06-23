verb = {                    # word + ي - ت - يون
    "id":'verb',
    "add":"ضيف",
    "buy":"شتري",
    "want":"ريد",
    "wear":"رتدي",
    "walk":"مشي",
    "try":"ستطيع",
    "talk":"تكلم",
    "take":"أخذ",
    "tired":"تعب",
    "tell":"خبر",
    "run":"جري",
    "miss":"فتقد",
    "need":"حتاج",
    "is":"كون",
    "have":"لديه",
    "care": "عتني",
    "call" : "تصل",
    "can": "ستطيع",
    "be" : "كون", 
    "do": "فعل",
    "did" : "فل",
    "done": "إنتهى",
    "drive":"قود",
    "drink":"شرب",
    "like":"حب",
    "hate":"كره",
    "run":"جري",
}               # 24 word

adj = {                     # word + NONE - ه - ون
    "id":'adj',
    "beautiful": "جميل",
    "ugly":"",
    "alone": "وحيد",
    "tall":"طويل",
    "ready":"مستعد",
    "short":"قصير",
    "smile":"مبتسم",
    "absent":"عابس",
    "angry":"غاضب",
    "calm":"هادئ",
    "good": "جيد",
    "hard":"صعب",
    "soft":"ناعم",
    "easy":"سهل",
    "full":"ممتلئ",
    "new": "جديد",
    "high":"عالي",
}               # 10 word

adj_kind = {
    "nadia" : 'ة',
    "man":'',
    "bro":'',
    "men" : 'ون',
    "all" : 'ون',
}               # 5 word

pp = {
    "id":'pp',
    "i":"أنا",
    "i'm":"أنا",
    "he":"هو",
    "it":"انها",
    "she": "هي",
    "they":"هم",
    "you":"انت",
    "we":"نحن",
}               # 8 word

talker = {
    "i" : 'أ',
    "i'm": "أ",
    "you":"ت",
    "he":'ي',
    "she":'ت',
    "they" : 'P',
    "we" : 'ن',
    "it" : 'ت',
}               # 7 word

talk_to = {
    "nadia" : 'ت',
    "man":'ي',
    "bro":'ي',
    "men" : 'P',
    "all" : 'P',
}               # 5 word


name = {
    "id":'name',
    "nadia" : "ناديه",
    "bro" : "اخي",
    "all" : "جميعا",
    "man" : "رجل",
    "men" : "رجال",
}               # 6 word

your = {
    "id":"your",
    "bro":'كَ',
    "man":'كَ',
    "nadia":'كِ',
    "all" : 'هم',
    "men" : 'نا',
}               # 7 word


you = {
    "id" : "you",
    "all" : 'نا',
    "men" : 'نا',
    "it" : 'ها',
    "bro":'كَ',
    "man":'كَ',
    "nadia":"كِ",
}               # 9 word

you_are = {
    "nadia":"تِ",
    "bro" : "تَ",
    "man" : "تَ",
    "men" : "تم",
    "all" : "تم",
}


a_words = {
    "a" : "ال",
    "an": "ال",
    "and": "و",
    "are":"",
    "apple": "تفاحة",
    "alone": adj,
    "add": verb,
    "all" : name,
    "ambulance":" اسعاف",
    "america":"أمريكا",
}               # 5 word

b_words = {
    "ball": "كرة",
    "banana": "موزة",
    "bowder": "مسحوق",
    "be" : verb, 
    "beautiful": adj,
    "bro" : name,
    "buy" : verb,
}               # 2 word

c_words = {
    "car": "سيارة",
    "care": verb,
    "call" : verb,
    "camera": "قُمرَة",
    "can": verb,
    "calendar" : "تقويم",
    "china":"الصين",
}               # 3 word

d_words = {
    "door": "باب",
    "deer" : "غزالة",
    "drama": "دراما",
    "do": verb,
    "did" : verb,
    "done": verb,
    "drive":verb,
    "drink":verb,
}               # 3 word

e_words = {
    "eat" : verb,
    "easy": adj,
    "every":"كل",
    "egypt":"مصر",
    "elephant":"فيل",
}               # 1 word

f_words = {
    "friday":"جمعة",
    "full":adj,
    "friend":"صديق",
}

g_words = {
    "good": adj,
    "goal": "هدف",
}               # 1 word

h_words = {
    "hello": "اهلا",
    "hi": "اهلا",
    "hell":"جحيم",
    "have":verb,
    "he":pp,
    "hacker":'مخترق',
    "hard":adj,
    "hate":verb,
    "help":"مساعت",
    "high": adj,
    "how" : "كيف",
}               # 4 word

i_words = {
    "i":pp,
    "i'm":pp,
    "is":verb,
    "it":pp,
    "icecream":"مثلجات",
}

l_words = {
    "love": verb,
    "lion": "أسد",
    "like" : verb,
    "length": "طول",
}               # 2 word
m_words = {
    "miss":verb,
    "monday":"الإثنين",
    "men" : name,
    "man" : name,
    "my"  : your,
    "me"  : "ي",
}               # 1 word

n_words = {
    "nadia" : name,
    "need" : verb,
    "new":adj,
    "now":"الأن",
}

r_words = {
    "really":"حقا",
    "road":"طريق",
    "run":verb,
    "ready":adj,
}               # 3 word

s_words = {
    "she": pp,
    "sun":"شمس",
    "sure":"حقا",
    "soft":adj,
    "suterday":"سبت",
    "sunday":"أحد",
}               # 2 word

t_words = {
    "try":verb,
    "tell":verb,
    "talk":verb,
    "take":verb,
    "they":pp,
    "there":"هناك",
    "tired":verb,
    "the":"ال",
    "tall":adj,
    "tuesday":"الثلاثاء",
    "thursday":"الخميس",
    "to" : "أن",
    "today":"اليوم",
    "this":"هذا",
}               # 2 word

v_words = {
    "voice" : "صوت",
    
}

w_words = {
    "we":pp,
    "want":verb,
    "wear":verb,
    "walk":verb,
    "what":"ماذا",
    "when":"متى",
    "where":"أين",
    "will":"سوف",
    "well":"بئر",
    "wednesday":"الاربعاء",
}               # 4 word

y_words = {
    "you":you,
    "your":your,
    "yours":"ملكك",
    "young":"شاب",
}               # 3 word

z_words = {
    "zoo":"حديقة الحيوان",
}               # 1 word

curbus = {
    'a' : a_words,
    'b' : b_words,
    'c' : c_words,
    'd' : d_words,
    'e' : e_words,
    'f' : f_words,
    'g' : g_words,
    'h' : h_words,
    'i' : i_words,
    'l' : l_words,
    'm' : m_words,
    'n' : n_words,
    'r' : r_words,
    's' : s_words,
    't' : t_words,
    'v' : v_words,
    'w' : w_words,
    'y' : y_words,
    'z' : z_words
    }
