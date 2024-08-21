from io import BytesIO
import os

from PIL import Image, ImageDraw, ImageFont

template_text = {
    "name": "Taro",
    "age": "22",
    "country": "Turkey",
    "mbti": "ISTJ",
    "favorite": "お肉を食べること",
    "quesition1": "question1",
    "quesition2": "question2",
    "quesition3": "question3",
    "answer1": "answer1",
    "answer2": "answer2",
    "answer3": "answer3",
}


class Profile:
    def __init__(self, template_path="/app/app/static/data/image/template.png", font_path="/app/app/static/data/font/nicoca_v2.ttf", color=0, language="ENG"):
        self.template_path = template_path
        self.color = color
        self.laguage = language
        self.output_profile = Image.open(self.template_path)
        self.font_path = font_path

    """
        data: 辞書(key: Value)
        country_map: PIL Image
    """
    def create_profile(self, data, country_map):

        self.draw_text(text=data["name"], position=(550, 790))
        self.draw_text(text=data["age"], position=(550, 980))
        self.draw_text(text=data["favorite_things"], position=(250, 1350))
        self.draw_text(text=data["country"], position=(1200, 160))
        self.draw_text(text=data["mbti"], position=(1335, 1480))

        self.draw_image(image=Image.open("/app/app/static/data/image/images.png").convert("RGBA"), position=(178, 192))

        self.save_profile()

        return self.output_profile

    def draw_image(self, image, position, image_size=(450, 450)):
        # 貼り付ける画像のリサイズ
        image = image.resize(image_size)
        # 背景画像に貼り付ける
        self.output_profile.paste(image, position, image)

    def draw_text(self, text, position, color=(0, 0, 0), font_size=80):
        # フォントを定義
        font = ImageFont.truetype(self.font_path, size=font_size)
        # ImageDrawオブジェクトを作成
        draw = ImageDraw.Draw(self.output_profile)
        # 画像にテキストを描画
        draw.text(position, text, fill=color, font=font)

    def save_profile(self):

        # 結果を保存
        self.output_profile.save("/app/app/static/data/image/output_profile.png")

        # または結果を表示
        self.output_profile.show()


def resize_and_center_crop(image, size=(256, 256)):
    """
    画像を指定サイズにリサイズし、中心を切り抜く関数
    image: PIL Imageオブジェクト
    size: (width, height) - 切り抜くサイズのタプル
    """
    width, height = image.size
    target_width, target_height = size

    # サイズが大きい場合のみリサイズと切り抜きを行う
    if width > target_width or height > target_height:
        # リサイズを保持しつつ中心を切り抜く
        left = (width - target_width) / 2
        top = (height - target_height) / 2
        right = (width + target_width) / 2
        bottom = (height + target_height) / 2

        image = image.crop((left, top, right, bottom))

    return image


def paste_image(background_path, overlay_path, output_path, position=(0, 0)):
    """
    背景画像に別の画像を貼り付ける関数
    background_path: str - 背景画像のパス
    overlay_path: str - 貼り付ける画像のパス
    output_path: str - 保存する画像のパス
    position: (x, y) - 貼り付ける位置
    """


if __name__ == "__main__":
    template_path = r"test/image/template.png"
    output_path = r"./test/image"
    font_path = "./test/nicoca_v2.ttf"
    profile = Profile(template_path=template_path, font_path=font_path)
