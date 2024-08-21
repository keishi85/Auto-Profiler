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
    def __init__(self, template_path, font_path, output_path, color=0, language="ENG"):
        self.template_path = template_path
        self.color = color
        self.laguage = language
        self.output_profile = Image.open(self.template_path)
        self.font_path = font_path
        self.output_path = output_path

        self.create_profile()

        self.save_profile()

    def create_profile(self):

        self.draw_text(text=template_text["name"], position=(550, 790))
        self.draw_text(text=template_text["age"], position=(550, 980))
        self.draw_text(text=template_text["favorite"], position=(250, 1350))
        self.draw_text(text=template_text["country"], position=(1200, 160))
        self.draw_text(text=template_text["mbti"], position=(1335, 1480))

        self.draw_image(image=Image.open("./test/image/images.png").convert("RGBA"), position=(178, 192))

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
        self.output_profile.save(self.output_path)

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


if __name__ == "__main__":
    template_path = r"./test/image/template.png"
    output_path = r"./test/image/output.png"
    font_path = r"./test/nicoca_v2.ttf"
    profile = Profile(template_path=template_path, output_path=output_path, font_path=font_path)
