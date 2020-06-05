from PIL import Image, ImageFont, ImageDraw, ImageColor


def add_num(image, text):
    font = ImageFont.truetype("arial.ttf", 50)
    fontcolor = ImageColor.colormap.get('red')
    draw = ImageDraw.Draw(image)
    width, height = image.size
    draw.text((width - 50, 30), text, font=font, fill=fontcolor)
    image.save("D://1234.jpg")


if __name__ == '__main__':
    image = Image.open('D://123.jpg')
    text = "4"
    add_num(image, text)