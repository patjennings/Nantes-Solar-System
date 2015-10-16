from mapnik import register_fonts, FontEngine
custom_fonts_dir = '/Users/thomas/Library/Fonts'
register_fonts(custom_fonts_dir)
for face in FontEngine.face_names(): print face