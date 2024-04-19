from PIL import Image, ImageFilter


def rotate(path, output, angle: int):
    orig = Image.open(path)
    out = orig.rotate(angle)
    out.save(output)


def convert(path, output):
    orig = Image.open(path)
    out = orig.convert('RGB')
    out.save(output)
