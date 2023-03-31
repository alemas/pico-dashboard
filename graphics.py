from displayio import Palette
from displayio import TileGrid
from displayio import OnDiskBitmap
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font

# COLORS
BLACK = 0x000000
WHITE = 0xFFFFFF
LIGHT_GRAY = 0xde5563
TEAL = 0x00ceef
RED = 0xde5563
MAGENTA = 0xc52d84



# PALETTES
def make_palette(colors) -> Palette:
    palette = Palette(len(colors))
    for i in range(len(colors)):
        palette[i] = colors[i]
    return palette

WHITE_PALETTE = make_palette([WHITE])
BLACK_PALETTE = make_palette([BLACK])
BLACK_AND_WHITE_PALETTE = make_palette([BLACK, WHITE])
WIFI_ICON_PALETTE = make_palette([BLACK, WHITE, LIGHT_GRAY, TEAL, RED])



# FONTS
def make_font(font_name) -> bitmap_font.BDF:
    font_path = "/fonts/" + font_name + ".bdf"
    font = bitmap_font.load_font(font_path)
    return font

# FONT_PIXELOPERATOR_16 = make_font("PixelOperator-16")
# FONT_PIXELOPERATOR_32 = make_font("PixelOperator-32")
# FONT_PIXELOPERATOR_BOLD_16 = make_font("PixelOperator-Bold-16")
# FONT_PIXELOPERATOR_BOLD_32 = make_font("PixelOperator-Bold-32")

# FONT_DOGICA_PIXEL_8 = make_font("Dogica_Pixel-8")
# FONT_DOGICA_PIXEL_16 = make_font("Dogica_Pixel-16")
# FONT_DOGICA_PIXEL_BOLD_8 = make_font("Dogica_Pixel_Bold-8")
# FONT_DOGICA_PIXEL_BOLD_16 = make_font("Dogica_Pixel_Bold-16")

FONT_LUCIDA_GRANDE_16 = make_font("LucidaGrande-16")
FONT_LUCIDA_GRANDE_12 = make_font("LucidaGrande-12")
FONT_LUCIDA_GRANDE_BOLD_12 = make_font("LucidaGrande-Bold-12")
FONT_LUCIDA_GRANDE_BOLD_16 = make_font("LucidaGrande-Bold-16")

# FONT_CALIBRI_16 = make_font("Calibri-16")
# FONT_CALIBRI_BOLD_16 = make_font("Calibri-Bold-16")



# LABEL
def make_label(x, y, font, text, color):
    lbl = label.Label(font, text=text, color=color)
    lbl.x = x
    lbl.y = y
    return lbl



# IMAGES

def make_image(image_name, transparent=True) -> TileGrid:
    image_path = "/img/" + image_name + ".bmp"
    image = OnDiskBitmap(image_path)
    if transparent:
        palette = image.pixel_shader
        palette.make_transparent(0)

    tile_grid = TileGrid(image, pixel_shader=image.pixel_shader)

    return tile_grid
