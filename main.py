import asyncio
import random
from datetime import datetime
from os import getenv
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, Message, CallbackQuery

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ===================== KONTENTLAR (Uzun va boyitilgan) =====================

STORIES = {
    "happy": [
        "🌟 **Baxtning kaliti qayerda?** \n\nQadimda bir yigit baxt sirini o'rganish uchun dunyodagi eng donishmand insonning huzuriga boribdi. Donishmand unga bir qoshiqda ikki tomchi yog' berib: 'Saroyimni aylanib chiq, lekin qoshiqdagi yog' to'kilmasin', debdi. Yigit qaytib kelgach, donishmand: 'Saroyimdagi tilla buyumlarni, bog'imdagi gullarni ko'rdingmi?' deb so'rabdi. Yigit faqat qoshiqqa qaragani uchun hech narsani ko'rmaganini aytibdi. \n\nIkkinchi safar yigit hamma go'zallikni ko'rib kelibdi, lekin qoshiqdagi yog' to'kilib ketgan ekan. Shunda donishmand debdi: 'Baxt sirining ma'nosi — dunyoning barcha go'zalliklaridan bahramand bo'lish, lekin qo'lingdagi ikki tomchi yog'ni (o'zligingni va mas'uliyatingni) unutmaslikdir'. ✨",
        "😊 **Tabassumning kuchi.** \n\nBir kuni bir kishi ko'chada juda g'amgin ketayotgan bolakayni ko'ribdi. U bolaga qarab shunchaki samimiy jilmayib qo'yibdi. Bolakayning kayfiyati ko'tarilib, u ham yo'lida uchragan bir qariya otaxonga salom beribdi. Otaxon xursand bo'lib, do'kondagi sotuvchiga yaxshi gapiribdi. Sotuvchi esa kechqurun uyiga borib, xotiniga guldasta sovg'a qilibdi. Birgina kichik tabassum zanjir kabi o'nlab insonlarning kunini yoritdi. Har lahza — baxt ulashish imkoniyati!"
    ],
    "sad": [
        "🕯 **Sog'inch va xotira.** \n\nInson yoshi ulg'aygani sari narsalarning narxiga emas, ularning qadriga e'tibor bera boshlar ekan. Bolalikda onamiz pishirgan issiq nonning hidi, otamizning qadoq qo'llari bilan boshimizni silashi — bularning hammasi bugun biz uchun eng qimmatli xotira. Sog'inch bizga o'tmishimizni eslatadi, lekin hozirgi lahzalarni qadrlashimiz uchun dars ham beradi. Yaqinlaringiz hali yonigizda ekan, ularga 'Sizni yaxshi ko'raman' deyishga kechikmang. 💔",
        "🌊 **Daryo va dengiz hikoyasi.** \n\nDaryo dengizga quyilishidan oldin qo'rquvdan titradi. U ortiga qaradi — o'tgan uzoq yo'li, tog'lar, o'rmonlar... Oldinda esa cheksiz va qo'rqinchli ummon. Daryo dengizga qo'shilsa, yo'q bo'lib ketishini bilar edi. Lekin orqaga yo'l yo'q. Daryo tavakkal qilib dengizga kirdi. Shunda u tushunib yetdi: u yo'q bo'lib ketmadi, u dengizning o'ziga aylandi! Ba'zida yo'qotish deb o'ylaganimiz — aslida ulkanroq narsaning boshlanishidir."
    ]
}

PSYCHOLOGY_TIPS = {
    "family": "🏠 **Oila haqida chuqur mulohaza:** \n\nOila — bu mukammal insonlar jamlanmasi emas, balki bir-birining kamchiliklarini sevishni o'rgangan insonlar ittifoqidir. Psixologlar aytishicha, haftada bir marta hamma ishlarni chetga surib, oila a'zolari bilan 2 soat davomida telefonsiz suhbatlashish ruhiy sog'lomlikning asosidir. Oila — bu bo'ronli dunyodagi yagona xavfsiz bandargohdir. Uni asrang!",
    "forgive": "🙏 **Kechirishning ruhiy foydasi:** \n\nKechirish — bu sizga yomonlik qilgan insonni oqlash emas, balki o'sha insonning yukini o'z yelkangizdan uloqtirishdir. Nafrat bilan yashash — bu zaharni o'zingiz ichib, boshqa odamning o'lishini kutishga o'xshaydi. Kechirganingizda, miyangizdagi stress gormonlari (kortizol) kamayadi va qalbingizda yangi maqsadlar uchun joy ochiladi."
}


# ===================== KEYBOARDS =====================

def main_menu():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="💖 Oila va Rishtalar", callback_data="family_long"))
    builder.row(InlineKeyboardButton(text="🙏 Kechirim Falsafasi", callback_data="forgive_long"))
    builder.row(InlineKeyboardButton(text="📖 Katta Hikoyalar Kitobi", callback_data="story_hub"))
    builder.row(InlineKeyboardButton(text="🎲 Kuchaytirilgan Challenge", callback_data="challenge_plus"))
    builder.row(InlineKeyboardButton(text="⏳ Hayot Mazmuni", callback_data="life_meaning"))
    return builder.as_markup()


# ===================== HANDLERS =====================

@dp.message(CommandStart())
async def cmd_start(message: Message):
    text = (
        f"🌟 **Assalomu alaykum, {message.from_user.full_name}!**\n\n"
        "Siz oddiy botga emas, balki ruhiy xotirjamlik va mazmunli lahzalar markazi — **Moments Hub**ga keldingiz. ✨\n\n"
        "Bu yerda biz qisqa javoblar bilan cheklanmaymiz. Biz bilan birga chuqur mulohaza yuriting, hayotingizdagi muhim qadriyatlarni qayta kashf qiling.\n\n"
        "**Marhamat, o'zingizni qiziqtirgan bo'limni tanlang:**"
    )
    await message.answer(text, reply_markup=main_menu(), parse_mode="Markdown")


@dp.callback_query()
async def process_callbacks(callback: CallbackQuery):
    data = callback.data

    # 1. Oila bo'limi (Uzun javob)
    if data == "family_long":
        await callback.message.edit_text(
            PSYCHOLOGY_TIPS["family"],
            reply_markup=main_menu(),
            parse_mode="Markdown"
        )

    # 2. Kechirim (Uzun javob)
    elif data == "forgive_long":
        await callback.message.edit_text(
            PSYCHOLOGY_TIPS["forgive"],
            reply_markup=main_menu(),
            parse_mode="Markdown"
        )

    # 3. Hikoyalar (Uzun va tanlovli)
    elif data == "story_hub":
        builder = InlineKeyboardBuilder()
        builder.row(InlineKeyboardButton(text="😊 Ijobiy (Uzun)", callback_data="get_story_happy"))
        builder.row(InlineKeyboardButton(text="🕯 Falsafiy (Uzun)", callback_data="get_story_sad"))
        builder.row(InlineKeyboardButton(text="🔙 Asosiy Menyu", callback_data="back"))
        await callback.message.edit_text("Qaysi yo'nalishdagi hikoyani o'qishni istaysiz?",
                                         reply_markup=builder.as_markup())

    elif data.startswith("get_story_"):
        s_type = data.split("_")[2]
        story = random.choice(STORIES[s_type])
        await callback.message.answer(story, parse_mode="Markdown")
        await callback.answer("Hikoya tayyor!")

    # 4. Hayot mazmuni (Yangi bo'lim)
    elif data == "life_meaning":
        msg = (
            "⏳ **Vaqt haqida haqiqat:** \n\n"
            "Tasavvur qiling, har tong sizning hisobingizga 86,400 dollar tushadi. Uni faqat o'sha kuni ishlatishingiz mumkin, kechqurun esa qolgan pul yonib ketadi. Nima qilgan bo'lardingiz? Albatta, har bir sentni foydali narsaga sarflashga urinardingiz. \n\n"
            "Aslida, har kuni sizga **86,400 soniya** beriladi. Uni qanday sarflashingiz sizning kelajagingizni belgilaydi. Hech kimda yo'q narsa — bu sizning aynan hozirgi lahzangizdir!"
        )
        await callback.message.edit_text(msg, reply_markup=main_menu(), parse_mode="Markdown")

    elif data == "back":
        await callback.message.edit_text("Asosiy menyu:", reply_markup=main_menu())

    await callback.answer()


async def main():
    print("🚀 Moments Hub Professional ishga tushdi...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())