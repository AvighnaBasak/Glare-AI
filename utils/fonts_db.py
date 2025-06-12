# utils/fonts_db.py

FONTS = [
    # 1. System/Classic Fonts
    *[(name, "system") for name in [
        "Arial","Arial Black","Calibri","Cambria","Candara","Century Gothic",
        "Comic Sans MS","Consolas","Courier New","Georgia","Impact",
        "Lucida Console","Lucida Sans Unicode","Palatino Linotype",
        "Segoe UI","Tahoma","Times New Roman","Trebuchet MS","Verdana",
        "Franklin Gothic Medium","Garamond","Gill Sans","Helvetica",
        "Monaco","Optima","Rockwell","Bodoni MT","Brush Script MT",
        "Copperplate","Didot"
    ]],

    # 2. Google / Clean / Modern Fonts
    *[(name, "google") for name in [
        "Roboto","Open Sans","Lato","Montserrat","Raleway","Poppins",
        "Source Sans Pro","Oswald","Merriweather","Nunito","Quicksand",
        "Ubuntu","PT Sans","Libre Franklin","Fira Sans","Cabin","Barlow",
        "Inconsolata","Muli","Work Sans","Oxygen","Karla",
        "Archivo Narrow","Cormorant Garamond","Exo 2"
    ]],

    # 3. Display / Handwritten / Bold / Funky Fonts
    *[(name, "display") for name in [
        "Bebas Neue","Lobster","Playball","Fredoka One","Black Ops One",
        "Amatic SC","Kaushan Script","Abril Fatface","Indie Flower",
        "Comfortaa","Baloo Bhai","Bungee","Cinzel","Patua One",
        "Righteous","Satisfy","Yellowtail","Cherry Swash","Special Elite",
        "Dancing Script","Pacifico","Josefin Sans"
    ]],

    # 4. Y2K / Chrome / Retro-Digital Fonts
    *[(name, "y2k") for name in [
        "VCR OSD Mono","OCR A Std","Data 70","Terminal Dosis","Orbitron",
        "Digital-7","LCD Solid","Neuropol X","SF Pixelate","Zorque",
        "Bitstream Vera Sans Mono","ChicagoFLF","ChicagoFLF Alternate",
        "System 90","Gopher"
    ]],

    # 5. Cyberpunk / Futuristic / Tech Fonts
    *[(name, "cyberpunk") for name in [
        "Cyberpunk","Neuropol","Exo","Sarpanch","Blade Runner Movie Font",
        "Datalegreya","Code Pro","Geometric 415","Space Mono","VT323",
        "Audiowide","Major Mono Display","Glitch","Raster","Monofett",
        "Teko","Quantico","SquareFont","IBM Plex Mono","OCR-A Extended",
        "Alfa Slab One","Input Mono"
    ]],

    # 6. Grunge / Distressed / Punk Fonts
    *[(name, "grunge") for name in [
        "Special Elite","VT323","TrashHand","Birth of a Hero","Feast of Flesh BB",
        "28 Days Later","Bleeding Cowboys","You Murderer BB","CF Bad Weather",
        "CF One Two Trees","Top Secret","Capture it","Face Your Fears"
    ]],

    # 7. Gothic / Baroque / Ornate Fonts
    *[(name, "gothic") for name in [
        "Cinzel Decorative","UnifrakturCook","MedievalSharp","Old English Text MT",
        "Blackletter686 BT","Deutsch Gothic","Cloister Black","Gothic Ultra OT",
        "IM Fell English","Fraktur BT"
    ]],

    # 8. Decorative / Art Deco / Whimsical
    *[(name, "decorative") for name in [
        "Cinzel Decorative","Playfair Display","Great Vibes","Mystery Quest",
        "Mountains of Christmas","Ballet","Art Deco W01 Inline","Art Nouveau Caps",
        "Euphoria Script","Titan One"
    ]],
]
