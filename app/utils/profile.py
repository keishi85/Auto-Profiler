from PIL import Image, ImageDraw, ImageFont
import math
import os

template_text = {
    "name": "Taro",
    "age": "22",
    "country": "Turkey",
    "mbti": "ISTJ",
    "favorite": "お肉を食べることが好きです\n焼肉に行きたい\n野菜も好きです",
    "question1": "question1question1question1",
    "question2": "question2",
    "question3": "question3",
    "answer1": "answer1question1question1",
    "answer2": "answer2",
    "answer3": "answer3",
}

template_personality = [80, 100, 50, 60, 75]

# 黒，
sub_color = [(0, 0, 0, 128), (70, 0, 70, 128), (0, 80, 100, 128), (170, 0, 0, 128), (0, 60, 0, 128)]


class Profile:
    def __init__(self, template_path, font_path, output_path=None, color=1, language="ENG"):
        self.template_path = template_path
        self.color = color
        self.laguage = language
        self.font_path = font_path
        self.output_path = output_path

        # if output_path is not None:
        #     self.save_profile()

    def create_profile(self, text_list, picture, country_img):

        # プロフィール帳のcolorを決定 (color=1:緑・紫, 2:紫・青, 3:黄・赤, 4:青・緑)
        self.deside_color(text_list["mbti"])

        # プロフィール帳のひな型を作成
        self.output_profile = Image.open(os.path.join(self.template_path, f"template{self.color:02d}.png")).convert("RGBA")

        self.draw_free_text(text=text_list["name"], position=(750, 820), ancher="right", max_width=250)
        self.draw_text(text=text_list["age"], position=(750, 1000), ancher="right")
        self.draw_free_text(text=text_list["favorite"], position=(480, 1380), ancher="center", max_width=540)
        self.draw_text(text=text_list["country"], position=(1200, 160))
        self.draw_text(text=text_list["mbti"], position=(1335, 1480))

        self.draw_free_text(text=text_list["question1"], position=(160, 1770), ancher="left", max_width=1040)
        self.draw_free_text(text=text_list["question2"], position=(160, 1980), ancher="left", max_width=1040)
        self.draw_free_text(text=text_list["question3"], position=(160, 2190), ancher="left", max_width=1040)
        self.draw_free_text(text=text_list["answer1"], position=(1570, 1850), ancher="right", max_width=840)
        self.draw_free_text(text=text_list["answer2"], position=(1570, 2052), ancher="right", max_width=840)
        self.draw_free_text(text=text_list["answer3"], position=(1570, 2270), ancher="right", max_width=840)

        self.draw_image(image=picture, position=(178, 192))
        self.draw_country_image(image=country_img, position=(830, 292), image_size=(760, 360))
        self.draw_pentagon(center=(1288, 1172), radius=template_personality)

        return self.output_profile

    def draw_image(self, image, position, target_size=450):
        # 貼り付ける画像のリサイズ
        image = resize_and_crop(image, target_size=target_size)
        # 背景画像に貼り付ける
        self.output_profile.paste(image, position, image)

    def draw_country_image(self, image, position, image_size):
        image = image.resize(image_size)
        # 背景画像に貼り付ける
        self.output_profile.paste(image, position, image)

    def draw_text(self, text, position, color=(0, 0, 0), font_size=80, ancher=None):
        # フォントを定義
        font = ImageFont.truetype(self.font_path, size=font_size)
        # ImageDrawオブジェクトを作成
        draw = ImageDraw.Draw(self.output_profile)

        font = ImageFont.truetype(self.font_path, size=font_size)
        text_bbox = draw.textbbox((0, 0), text, font=font)

        fixed_position = self.fix_text_positon(position, text_bbox, ancher)

        # 画像にテキストを描画

        draw.text(fixed_position, text, fill=color, font=font)

    def draw_free_text(self, text, position, ancher="center", color=(0, 0, 0), font_size=80, max_width=540):
        # フォントを定義
        font = ImageFont.truetype(self.font_path, size=font_size)
        draw = ImageDraw.Draw(self.output_profile)
        # テキストのサイズを取得
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]

        # フォントサイズを自動で縮小する処理（二分探索を使用）
        if max_width is not None and text_width > max_width:
            min_size = 1
            max_size = font_size

            while min_size < max_size:
                mid_size = (min_size + max_size) // 2
                font = ImageFont.truetype(self.font_path, size=mid_size)
                text_bbox = draw.textbbox((0, 0), text, font=font)
                text_width = text_bbox[2] - text_bbox[0]

                if text_width <= max_width:
                    min_size = mid_size + 1
                else:
                    max_size = mid_size - 1

            # 縮小したフォントサイズを最終的に適用
            font_size = min_size - 1

        font = ImageFont.truetype(self.font_path, size=font_size)
        text_bbox = draw.textbbox((0, 0), text, font=font)

        fixed_position = self.fix_text_positon(position, text_bbox, ancher=ancher)
        # 画像にテキストを描画
        draw.text(fixed_position, text, fill=color, font=font)

    def fix_text_positon(self, position, text_bbox, ancher="center"):
        fixed_position = position
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        # アンカーによるテキスト位置の調整
        if ancher == "center":
            fixed_position = (position[0] - text_width // 2, position[1] - text_height // 2)
        elif ancher == "left":
            fixed_position = (position[0], position[1] - text_height // 2)
        elif ancher == "right":
            fixed_position = (position[0] - text_width, position[1] - text_height // 2)
        elif ancher == "top":
            fixed_position = (position[0] - text_width // 2, position[1])
        elif ancher == "bottom":
            fixed_position = (position[0] - text_width // 2, position[1] - text_height)

        return fixed_position

    def deside_color(self, mbti):
        if mbti in ["ISTJ", "ISFJ", "ESTJ", "ESFJ"]:
            self.color = 4
        elif mbti in ["INTJ", "INTP", "ENTJ", "ENTP"]:
            self.color = 2
        elif mbti in ["ISTP", "ISFP", "ESTP", "ESFP"]:
            self.color = 3
        elif mbti in ["INFJ", "INFP", "ENFJ", "ENFP"]:
            self.color = 1

    def save_profile(self):

        # 結果を保存
        self.output_profile.save(self.output_path)

        # または結果を表示
        self.output_profile.show()

    def draw_pentagon(self, center, radius, fill_color=(255, 0, 0), outline_color=(0, 0, 0)):

        # 五角形を描画するための新しい画像を作成
        pentagon_image = Image.new("RGBA", self.output_profile.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(pentagon_image)
        # 中心座標を指定
        cx, cy = center

        # 五角形の頂点を計算
        points = []
        for i in range(5):
            angle = math.radians(72 * i - 90)  # 72度ごとに頂点を配置 (-90は最初の頂点を上に向けるため)
            x = cx + 2.5 * radius[i] * math.cos(angle)
            y = cy + 2.5 * radius[i] * math.sin(angle)
            points.append((x, y))

        draw.polygon(points, fill=sub_color[self.color])

        # 五角形画像を元の画像に貼り付け
        self.output_profile = Image.alpha_composite(self.output_profile, pentagon_image)


def resize_and_crop(image, target_size=450):
    # 画像のサイズを取得
    original_width, original_height = image.size

    # アスペクト比を保持してリサイズ
    aspect_ratio = original_width / original_height

    if aspect_ratio > 1:  # 横長の画像
        new_height = target_size
        new_width = int(aspect_ratio * target_size)
    else:  # 縦長または正方形の画像
        new_width = target_size
        new_height = int(target_size / aspect_ratio)

    # 画像をリサイズ
    image = image.resize((new_width, new_height), Image.LANCZOS)

    # クロップする位置を計算（画像の中心を基準）
    left = (new_width - target_size) // 2
    top = (new_height - target_size) // 2
    right = (new_width + target_size) // 2
    bottom = (new_height + target_size) // 2

    # 画像をクロップ
    image = image.crop((left, top, right, bottom))
    return image


if __name__ == "__main__":
    template_path = r"app\static\data\image\template"
    output_path = r"./test/image/output.png"
    font_path = r"app\static\data\font\nicoca_v2.ttf"
    profile = Profile(template_path=template_path, output_path=output_path, font_path=font_path)

    output_profile = profile.create_profile(
        text_list=template_text,
        picture=Image.open(r"./app\static\data\image\no_image.png").convert("RGBA"),
        country_img=Image.open(r"app\static\data\image\images.png").convert("RGBA"),
    )
    output_profile.show()
