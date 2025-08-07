from cryptography.fernet import Fernet

# key + password + text to encrypt = random text
# random text + key + password = text to encrypt

# هذا توضيح أن التشفير يحتاج إلى:
# مفتاح (key)
# نص صريح (مثل كلمة مرور)
# والنتيجة ستكون نص مشفر (random text).
# وعند فك التشفير، نحتاج إلى نفس المفتاح والنص المشفر لاسترجاع النص الأصلي.


"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
هذه الدالة تُستخدم مرة واحدة فقط لإنشاء مفتاح التشفير وتخزينه في ملف اسمه
key.key
"""


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


# master_pwd = input("What is the master password? ")
# i can ignore this line
key = load_key()  # + master_pwd.encode()
fer = Fernet(key)
"""
input(...): يطلب من المستخدم إدخال كلمة مرور رئيسية.

load_key(): يحصل على المفتاح من الملف.

master_pwd.encode(): يحوّل كلمة المرور من string إلى bytes لأن Fernet يتعامل مع bytes.

fer = Fernet(key):

ينشئ كائن مسؤول عن التشفير وفك التشفير باستخدام المفتاح.
"""


def view():
    with open("password.txt", "r") as r:
        for line in r.readlines():
            data = line.rstrip()
            user, passw = data.split(" | ")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())


"""
with open("password.txt", "r") as r: يفتح الملف الذي فيه الحسابات وكلمات المرور المشفرة.

for line in r.readlines(): يقرأ كل سطر في الملف.

line.rstrip(): يزيل الفراغات أو \n في نهاية السطر.

user, passw = data.split(" | "): يفصل اسم الحساب وكلمة المرور المشفرة.

fer.decrypt(passw.encode()): يفك تشفير كلمة المرور.

لماذا نستخدم الاثنين معًا؟
لأننا:

نحول إلى bytes عندما نشفر أو نفك التشفير (encode()).

نحول إلى string عندما نكتب إلى ملف أو نعرض للمستخدم (decode()).

هما مش ضد بعض، بل مكملين لبعض علشان نتعامل مع المكتبة ونخزن البيانات بشكل سليم.

"""


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("password.txt", "a") as f:
        f.write(name + " | " + fer.encrypt(pwd.encode()).decode() + "\n")


"""
pwd.encode(): تحويل كلمة المرور إلى bytes.

fer.encrypt(...): تشفير كلمة المرور.

.decode(): تحويل النتيجة إلى string حتى نقدر نخزنها في ملف نصي.

f.write(...): يضيف السطر إلى الملف بصيغة:
"""


while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view/add), press q to quit? "
    ).lower()

    if mode == "q":
        break

    if mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid mode.")
        continue
