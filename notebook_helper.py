import ciphers
import ipywidgets as widgets

from IPython.display import display, Markdown, SVG

def _handle_cipher(c, message):
    encrypted_text = c.cipher(message)
    decrypted_text = c.decipher(encrypted_text)
    display(Markdown(f'**Original text:** {message}\n\n**Encrypted text:** {encrypted_text}\n\n**Decrypted text:** {decrypted_text}'))

def _handle_block_cipher(message, print_table):
    c = ciphers.BlockCipher(print_table=print_table)
    _handle_cipher(c, message)
    
def _handle_scale_cipher(message, rot, print_mapping):
    c = ciphers.SlidingScaleCipher(rot)
    if print_mapping:
        display(SVG(data=caesar(rot)))
    _handle_cipher(c, message)
        
def _handle_random_cipher(message, print_mapping):
    c = ciphers.RandomMappingCipher(print_mapping=print_mapping)
    _handle_cipher(c, message)

def _handle_emoji_cipher(message, print_mapping):
    c = ciphers.RandomMappingEmojiCipher(print_mapping=print_mapping)
    _handle_cipher(c, message)

def render_block_cipher(initial_message='Masterclass'):
    message = widgets.Text(value=initial_message, continuous_update=True)
    print_table = widgets.Checkbox(
        value=True,
        description='Print table?',
        disabled=False,
        indent=False
    )
    out = widgets.interactive_output(_handle_block_cipher, {'message': message, 'print_table': print_table})

    display(widgets.VBox((
        widgets.Label(value='Enter your message below:'),
        message,
        print_table,
        out
    )))
    
def render_scale_cipher(initial_message='Masterclass'):
    message = widgets.Text(value=initial_message, continuous_update=True)
    print_mapping = widgets.Checkbox(
        value=True,
        description='Print mapping?',
        disabled=False,
        indent=False
    )
    rot = widgets.IntSlider( value=13, min=0, max=26, step=1, description='Scale rotation: ', continuous_update=True)
    out = widgets.interactive_output(_handle_scale_cipher, {'message': message, 'rot': rot, 'print_mapping': print_mapping})

    display(widgets.VBox((
        widgets.Label(value='Enter your message below:'),
        message,
        rot,
        print_mapping,
        out
    )))
    
def render_random_cipher(initial_message='Masterclass'):
    message = widgets.Text(value=initial_message, continuous_update=True)
    print_mapping = widgets.Checkbox(
        value=True,
        description='Print mapping?',
        disabled=False,
        indent=False
    )
    randomise = widgets.Button(description='Randomise')
    out = widgets.interactive_output(_handle_random_cipher, {'message': message, 'print_mapping': print_mapping})
    def refresh(btn=None):
        out.clear_output()
        with out:
            _handle_random_cipher(message.value, print_mapping.value)
    randomise.on_click(refresh)
    
    display(widgets.VBox((
        widgets.Label(value='Enter your message below:'),
        message,
        print_mapping,
        randomise,
        out
    )))
    
def render_emoji_cipher(initial_message='Masterclass'):
    message = widgets.Text(value=initial_message, continuous_update=True)
    print_mapping = widgets.Checkbox(
        value=True,
        description='Print mapping?',
        disabled=False,
        indent=False
    )
    randomise = widgets.Button(description='Randomise')
    out = widgets.interactive_output(_handle_emoji_cipher, {'message': message, 'print_mapping': print_mapping})
    def refresh(btn=None):
        out.clear_output()
        with out:
            _handle_emoji_cipher(message.value, print_mapping.value)
    randomise.on_click(refresh)
    
    display(widgets.VBox((
        widgets.Label(value='Enter your message below:'),
        message,
        print_mapping,
        randomise,
        out
    )))
    
caesar = lambda rot: f"""<svg xmlns="http://www.w3.org/2000/svg" xml:space="preserve" width="300px" height="300px" version="1.1" style="shape-rendering:geometricPrecision; text-rendering:geometricPrecision; image-rendering:optimizeQuality; fill-rule:evenodd; clip-rule:evenodd"
viewBox="0 0 5000 5000"
 xmlns:xlink="http://www.w3.org/1999/xlink">
 <defs>
  <style type="text/css">
   <![CDATA[
    .str0 {{stroke:black;stroke-width:27.7756}}
    .fil3 {{fill:none}}
    .fil4 {{fill:black}}
    .fil1 {{fill:#E9E9E9}}
    .fil0 {{fill:white}}
    .fil5 {{fill:black;fill-rule:nonzero}}
    .fil2 {{fill:#868686;fill-rule:nonzero}}
   ]]>
  </style>
 </defs>
 <g id="Layer_x0020_1">
  <metadata id="CorelCorpID_0Corel-Layer"/>
  <path class="fil0" d="M2500 0c1381,0 2500,1119 2500,2500 0,1381 -1119,2500 -2500,2500 -1381,0 -2500,-1119 -2500,-2500 0,-1381 1119,-2500 2500,-2500zm0 1000c828,0 1500,672 1500,1500 0,828 -672,1500 -1500,1500 -828,0 -1500,-672 -1500,-1500 0,-828 672,-1500 1500,-1500z"/>
  <path class="fil1" d="M2500 511c1098,0 1989,891 1989,1989 0,1098 -891,1989 -1989,1989 -1098,0 -1989,-891 -1989,-1989 0,-1098 891,-1989 1989,-1989z"/>
  <path class="fil2" d="M2500 497c553,0 1054,224 1416,587 363,362 587,863 587,1416 0,553 -224,1054 -587,1416 -362,363 -863,587 -1416,587 -553,0 -1054,-224 -1416,-587 -363,-362 -587,-863 -587,-1416 0,-553 224,-1054 587,-1416 362,-363 863,-587 1416,-587zm1397 606c-358,-357 -852,-578 -1397,-578 -545,0 -1039,221 -1397,578 -357,358 -578,852 -578,1397 0,545 221,1039 578,1397 358,357 852,578 1397,578 545,0 1039,-221 1397,-578 357,-358 578,-852 578,-1397 0,-545 -221,-1039 -578,-1397z"/>
  <path class="fil3" d="M2500 14l0 994m359 44l240 -965m563 215l-465 879m296 206l662 -742m396 449l-821 562m166 318l931 -351m141 579l-987 119m0 357l988 119m-141 578l-931 -350m-166 318l820 562m-395 449l-662 -742m-296 207l465 879m-564 215l-239 -965m-360 44l0 994m-599 -73l239 -965m-338 -129l-465 879m-493 -344l662 -742m-237 -269l-820 562m-277 -530l931 -350m-84 -347l-987 119m0 -595l987 119m85 -347l-931 -351m276 -529l821 562m237 -269l-662 -742m493 -343l465 879m338 -129l-240 -965"/>
  <path class="fil2" d="M2514 14l0 994 -28 0 0 -994 28 0zm332 1035l240 -966 26 7 -239 965 -27 -6zm828 -741l-465 879 -24 -13 465 -879 24 13zm-192 1070l663 -742 20 18 -662 742 -21 -18zm1076 -273l-820 563 -16 -23 821 -562 15 22zm-667 856l931 -351 10 26 -931 350 -10 -25zm1079 254l-987 119 -4 -27 988 -119 3 27zm-987 449l987 119 -3 27 -987 -119 3 -27zm840 724l-931 -350 9 -26 931 350 -9 26zm-1084 -57l820 562 -15 23 -821 -562 16 -23zm406 1033l-662 -742 21 -19 662 742 -21 19zm-935 -552l465 880 -25 12 -465 -879 25 -13zm-124 1105l-240 -966 27 -6 240 965 -27 7zm-572 -925l0 994 -28 0 0 -994 28 0zm-627 918l240 -965 27 6 -240 966 -27 -7zm-72 -1085l-465 879 -25 -12 465 -880 25 13zm-981 520l662 -742 21 19 -662 742 -21 -19zm443 -991l-821 562 -15 -23 820 -562 16 23zm-1109 8l931 -350 9 26 -931 350 -9 -26zm852 -671l-987 119 -3 -27 987 -119 3 27zm-987 -503l988 119 -4 27 -987 -119 3 -27zm1066 -202l-931 -350 10 -26 931 351 -10 25zm-642 -903l821 562 -16 23 -820 -563 15 -22zm1040 313l-662 -742 20 -18 663 742 -21 18zm-147 -1101l465 879 -24 13 -465 -879 24 -13zm777 760l-239 -965 26 -7 240 966 -27 6z"/>
  <path class="fil4" d="M2193 159l-21 161 86 -12 -65 -149zm-30 -33l49 -7 136 290 -42 6 -34 -76 -105 15 -11 82 -42 6 49 -316zm537 145l-12 111 48 6c24,2 42,0 53,-7 11,-7 17,-21 19,-40 3,-20 -1,-35 -11,-45 -9,-11 -26,-17 -49,-20l-48 -5zm14 -125l-10 92 47 5c20,2 35,0 45,-7 9,-7 15,-18 17,-35 2,-16 -1,-27 -9,-35 -8,-8 -22,-13 -42,-15l-48 -5zm-38 -39l90 10c31,4 54,13 70,28 15,16 21,36 19,60 -2,19 -8,33 -19,43 -10,10 -24,15 -42,16 20,5 34,15 44,30 10,16 14,34 11,56 -3,28 -14,47 -34,59 -19,12 -47,16 -83,13l-89 -10 33 -305zm639 455c-12,1 -23,1 -35,0 -11,-1 -22,-4 -34,-8 -37,-14 -60,-38 -71,-71 -10,-34 -7,-74 11,-121 17,-47 41,-80 71,-98 30,-19 63,-21 100,-8 11,5 22,10 31,17 10,6 18,14 26,23l-15 39c-6,-11 -14,-21 -23,-29 -10,-8 -20,-14 -31,-18 -25,-10 -47,-7 -67,8 -20,14 -37,42 -52,81 -15,39 -19,71 -14,95 5,24 21,41 46,50 11,4 23,6 35,6 12,0 25,-2 37,-6l-15 40zm344 160c29,20 54,26 75,20 21,-6 44,-28 69,-65 26,-37 38,-67 36,-89 -2,-22 -17,-43 -46,-62l-16 -12 -134 197 16 11zm154 -224c38,26 60,56 64,89 4,33 -8,71 -38,115 -29,43 -60,68 -92,76 -33,8 -68,-1 -106,-27l-52 -35 173 -253 51 35zm405 337l122 135 -26 23 -94 -104 -67 61 89 99 -25 24 -90 -100 -82 74 96 107 -26 24 -124 -138 227 -205zm351 469l85 158 -31 17 -65 -122 -79 42 59 111 -31 16 -59 -110 -129 69 -19 -37 269 -144zm-4 775c-12,-8 -23,-18 -31,-31 -9,-12 -15,-26 -19,-41 -9,-38 -3,-71 19,-98 21,-28 57,-48 105,-60 49,-12 89,-11 121,4 33,14 53,40 63,78 3,13 4,25 3,37 0,12 -3,25 -7,37l-41 10c7,-13 12,-26 14,-38 2,-13 1,-25 -2,-38 -6,-26 -21,-43 -45,-51 -23,-8 -55,-7 -95,3 -42,10 -70,24 -87,42 -17,17 -22,39 -15,66 2,8 5,16 8,22 4,6 9,12 15,16l79 -20 -10 -43 33 -8 20 81 -128 32zm320 314l-1 42 -125 -1 -1 113 125 1 0 42 -306 -3 1 -42 145 2 1 -114 -145 -1 0 -42 306 3zm-49 593l-43 164 -34 -9 17 -62 -228 -61 -17 62 -33 -9 43 -164 34 9 -17 62 228 61 17 -62 33 9zm-434 390l43 23c-16,6 -30,13 -41,22 -11,9 -20,20 -27,32 -9,17 -11,32 -6,43 5,12 20,25 44,38l150 83 37 -69 31 17 -58 105 -180 -100c-34,-18 -54,-38 -61,-58 -7,-20 -3,-45 14,-75 6,-11 14,-22 23,-32 8,-10 19,-20 31,-29zm-56 635l-28 30 -100 -92 13 188 -33 35 -11 -172 -216 -32 34 -37 180 30 -4 -46 -88 -81 28 -30 225 207zm-430 408l-34 24 -151 -226 -122 82 -20 -29 158 -105 169 254zm-479 277l-52 19 -102 -129 3 165 -53 18 -102 -288 36 -13 90 255 -3 -170 30 -11 106 133 -91 -254 36 -13 102 288zm-554 157l-51 8 -138 -235 36 249 -40 6 -43 -303 52 -8 137 235 -35 -249 39 -6 43 303zm-718 -145c-5,44 -4,77 3,97 7,20 21,31 42,34 20,2 36,-6 48,-24 11,-18 19,-50 24,-94 5,-45 4,-77 -3,-97 -7,-21 -21,-32 -42,-34 -21,-2 -37,5 -48,23 -11,19 -19,50 -24,95zm-43 -5c6,-53 18,-92 38,-116 19,-24 46,-34 81,-31 34,4 58,20 72,48 14,28 18,68 12,121 -6,53 -19,92 -38,116 -20,25 -47,35 -81,31 -34,-4 -58,-20 -72,-48 -14,-27 -18,-68 -12,-121zm-424 7l41 -107 -45 -17c-18,-7 -34,-7 -47,-2 -14,6 -24,17 -30,34 -7,17 -7,33 0,46 6,13 19,23 37,29l44 17zm27 47l-83 -32c-32,-12 -54,-28 -65,-49 -11,-20 -11,-45 -1,-73 11,-28 27,-46 49,-55 22,-8 49,-6 81,6l44 17 43 -116 39 15 -107 287zm-421 -563c1,1 2,1 4,2 1,1 2,2 3,2 28,20 42,45 41,76 -1,31 -16,69 -46,113 -30,44 -59,72 -88,84 -29,13 -57,9 -86,-11 -28,-19 -42,-44 -41,-76 1,-31 16,-68 46,-113 23,-33 45,-57 66,-72 22,-15 43,-21 64,-18l-11 -56 37 1 11 68zm-131 102c-26,37 -40,66 -43,87 -3,21 4,38 21,50 17,11 35,12 54,1 18,-10 40,-34 65,-71 26,-37 40,-67 43,-88 3,-21 -4,-37 -21,-49 -17,-12 -35,-13 -54,-2 -18,11 -40,35 -65,72zm-367 -355c-5,-9 -8,-20 -7,-30 1,-11 6,-28 15,-51l34 -87 30 33 -33 79c-9,22 -14,39 -13,49 1,11 6,21 15,31l27 29 96 -86 27 31 -227 205 -57 -64c-22,-25 -34,-49 -34,-72 -1,-24 9,-45 31,-65 15,-13 30,-20 47,-20 17,-1 33,6 49,18zm-38 149l80 -73 -30 -34c-13,-14 -26,-22 -39,-24 -13,-1 -27,5 -40,17 -13,12 -20,25 -20,39 0,14 6,28 20,42l29 33zm-417 -572l37 -20c-2,15 -1,29 1,42 3,13 7,25 13,37 9,17 20,29 34,34 13,6 27,5 40,-2 12,-6 19,-15 22,-25 3,-9 1,-25 -4,-45l-6 -21c-7,-29 -8,-52 -2,-70 7,-19 21,-34 43,-45 25,-14 49,-17 71,-8 22,9 41,28 57,59 7,12 13,26 17,40 4,14 7,29 8,45l-39 21c2,-19 1,-35 -1,-50 -3,-15 -7,-28 -14,-41 -10,-18 -22,-30 -36,-36 -13,-6 -27,-5 -42,3 -14,7 -22,16 -25,27 -4,11 -3,26 3,46l6 22c7,28 9,51 3,68 -5,18 -17,31 -37,42 -24,13 -47,15 -70,6 -24,-8 -42,-26 -57,-53 -5,-10 -10,-21 -14,-34 -3,-13 -6,-27 -8,-42zm-145 -354l-57 -226 34 -9 23 93 263 -65 10 40 -263 66 23 93 -33 8zm94 -593l-189 -2 1 -41 207 2c15,0 25,0 32,-1 6,-1 11,-2 14,-4 8,-5 14,-11 19,-19 4,-8 6,-18 6,-30 0,-12 -2,-22 -6,-30 -4,-9 -10,-15 -18,-19 -3,-3 -8,-4 -14,-5 -7,-1 -17,-1 -32,-1l-207 -2 0 -42 188 2c32,0 54,2 67,6 13,4 24,11 32,21 8,9 14,19 18,31 4,12 6,25 6,39 -1,14 -3,27 -7,39 -4,12 -10,22 -18,31 -9,9 -20,16 -33,20 -14,4 -36,5 -66,5zm148 -604l-243 -139 11 -41 272 165 -12 48 -319 8 11 -41 280 0zm-111 -498l19 -35 231 94 -127 -110 21 -38 161 49 -203 -146 19 -35 246 188 -19 34 -179 -52 139 125 -19 34 -289 -108zm320 -502l30 -32 130 28 -38 -128 30 -33 44 165 185 37 -30 33 -147 -34 42 149 -30 33 -50 -185 -166 -33zm410 -392l37 -24 137 71 -13 -154 37 -25 12 195 76 114 -35 24 -76 -115 -175 -86zm530 -298l186 -67 11 29 -70 280 155 -55 11 32 -195 70 -11 -29 66 -278 -142 50 -11 -32z"/>
  <path class="fil4" d="M892 1649l92 85 31 -60 -123 -25zm-34 5l18 -35 242 43 -15 29 -62 -12 -38 74 47 43 -14 29 -178 -171zm329 -276l65 58 24 -29c13,-14 19,-26 19,-36 1,-10 -5,-20 -16,-30 -11,-10 -22,-15 -33,-13 -11,1 -23,9 -34,22l-25 28zm-73 -64l53 47 25 -28c10,-11 15,-22 15,-31 0,-9 -4,-18 -14,-27 -9,-8 -18,-11 -26,-9 -9,1 -18,8 -28,20l-25 28zm-41 6l46 -52c16,-18 33,-29 49,-32 16,-3 32,2 46,15 11,10 17,20 19,30 1,11 -1,22 -9,34 12,-10 25,-15 39,-14 14,1 27,7 40,18 16,14 23,30 22,48 -1,17 -11,37 -29,58l-46 52 -177 -157zm569 -202c-4,8 -9,16 -15,22 -6,7 -13,13 -21,19 -25,17 -50,21 -76,13 -25,-9 -49,-29 -71,-61 -22,-32 -32,-61 -30,-89 1,-27 15,-49 39,-66 8,-5 16,-10 24,-13 9,-3 17,-5 26,-6l19 27c-10,-1 -20,0 -29,2 -9,3 -18,6 -25,11 -17,12 -25,28 -25,47 1,19 10,42 28,68 18,27 36,44 54,52 17,7 35,5 52,-7 7,-5 14,-12 19,-20 6,-7 10,-16 12,-26l19 27zm253 -146c25,-9 40,-22 46,-38 5,-16 2,-41 -11,-73 -12,-33 -25,-54 -40,-62 -14,-9 -34,-9 -59,1l-14 5 64 172 14 -5zm-73 -197c34,-13 62,-13 85,-1 22,12 41,37 55,75 14,38 16,69 7,93 -9,24 -30,42 -64,55l-45 16 -83 -221 45 -17zm392 -107l138 -16 4 26 -108 13 9 70 102 -12 3 26 -102 13 10 85 110 -14 4 27 -142 17 -28 -235zm450 -13l137 17 -3 27 -106 -13 -8 69 96 12 -4 27 -95 -12 -14 112 -32 -4 29 -235zm486 348c-11,4 -22,6 -33,6 -12,0 -23,-2 -35,-7 -28,-11 -45,-29 -53,-55 -8,-26 -5,-57 9,-93 14,-36 32,-61 56,-75 23,-14 49,-16 77,-5 9,3 17,8 25,14 7,6 14,13 20,21l-12 31c-5,-11 -11,-19 -18,-26 -7,-7 -15,-12 -25,-16 -19,-8 -36,-6 -52,6 -15,11 -28,32 -40,62 -12,30 -16,55 -12,73 4,18 15,31 35,39 6,3 12,4 18,4 5,1 11,0 16,-2l23 -59 -32 -12 9 -25 60 24 -36 95zm339 -63l26 19 -56 79 71 51 56 -79 26 19 -137 192 -26 -19 65 -91 -71 -51 -65 91 -26 -19 137 -192zm352 295l84 100 -21 17 -32 -38 -139 118 32 38 -20 17 -84 -101 20 -17 32 38 139 -117 -32 -38 21 -17zm53 448l34 -16c-4,12 -5,24 -5,35 1,11 4,21 9,31 6,14 14,22 24,23 10,2 24,-1 43,-11l119 -58 -27 -54 24 -12 41 83 -143 70c-26,13 -48,17 -63,13 -16,-5 -30,-19 -42,-42 -4,-10 -7,-19 -10,-29 -2,-10 -3,-21 -4,-33zm375 318l7 31 -102 22 123 76 8 36 -113 -69 -116 122 -8 -37 98 -101 -30 -18 -90 19 -7 -31 230 -50zm67 454l-1 32 -208 -5 -3 114 -27 -1 4 -146 235 6zm-38 426l-11 41 -126 7 104 72 -11 41 -227 -63 8 -28 200 56 -108 -74 6 -24 131 -7 -201 -56 8 -28 227 63zm-146 420l-18 36 -209 -17 173 88 -14 28 -210 -108 18 -36 209 18 -173 -89 14 -27 210 107zm-410 390c26,23 47,37 63,42 16,4 29,0 40,-12 10,-12 13,-26 6,-41 -6,-15 -23,-34 -48,-57 -26,-23 -47,-37 -63,-41 -16,-5 -29,-1 -40,11 -10,12 -13,26 -6,41 6,15 22,34 48,57zm-22 25c-30,-27 -49,-52 -56,-75 -6,-24 -1,-45 17,-65 18,-20 38,-28 62,-25 23,4 51,19 82,47 30,27 49,52 56,76 6,23 1,44 -17,64 -17,20 -38,28 -62,25 -23,-4 -51,-19 -82,-47zm-182 271l-50 -73 -31 21c-12,8 -19,18 -21,29 -3,11 0,23 8,34 8,12 17,18 28,20 12,2 23,-1 35,-10l31 -21zm41 4l-57 39c-21,15 -41,21 -59,19 -18,-2 -33,-13 -46,-32 -14,-19 -18,-38 -14,-55 5,-18 18,-34 40,-49l30 -21 -54 -78 27 -18 133 195zm-540 16c0,0 1,-1 2,-1 2,-1 3,-1 3,-1 25,-10 47,-7 66,7 20,15 36,41 51,80 14,38 19,70 14,93 -5,24 -20,40 -45,49 -25,10 -47,7 -66,-7 -19,-15 -36,-41 -51,-80 -11,-29 -16,-54 -16,-74 0,-20 6,-36 17,-49l-40 -17 16 -23 49 23zm5 129c13,32 25,54 37,65 11,12 25,15 40,9 15,-6 23,-17 25,-33 1,-16 -4,-41 -16,-73 -12,-33 -24,-55 -36,-66 -12,-12 -26,-15 -41,-9 -15,6 -23,17 -25,33 -1,17 4,41 16,74zm-385 74c-8,-1 -16,-4 -22,-9 -7,-5 -15,-16 -26,-33l-39 -60 34 -4 35 56c10,16 18,26 25,30 7,4 16,5 26,4l30 -3 -12 -100 32 -3 29 234 -65 8c-26,3 -46,0 -62,-10 -15,-10 -23,-26 -26,-48 -2,-16 1,-29 8,-40 7,-11 18,-18 33,-22zm77 90l-10 -83 -35 4c-15,2 -26,6 -33,14 -6,8 -9,19 -7,33 2,13 7,23 16,29 9,7 20,9 35,7l34 -4zm-545 10l4 -33c9,8 18,14 27,18 10,4 19,7 29,8 15,2 27,0 37,-6 9,-6 15,-15 16,-26 1,-11 -1,-19 -6,-25 -5,-6 -15,-12 -30,-18l-16 -6c-21,-8 -36,-18 -45,-30 -9,-12 -12,-28 -10,-47 3,-22 12,-38 27,-48 15,-10 36,-14 62,-10 11,1 22,4 33,7 11,4 22,9 32,15l-4 34c-11,-9 -22,-16 -32,-21 -10,-5 -21,-8 -32,-10 -16,-1 -29,1 -38,7 -10,6 -16,15 -17,28 -2,12 0,21 6,28 5,7 15,13 30,18l16 6c21,8 36,17 45,29 8,11 12,25 10,41 -3,21 -12,37 -27,48 -16,11 -35,15 -59,12 -8,-1 -18,-3 -27,-6 -10,-4 -20,-8 -31,-13zm-286 -66l-168 -65 10 -26 68 27 75 -195 30 11 -75 196 69 27 -9 25zm-332 -324l-85 119 -26 -19 93 -130c7,-9 11,-16 14,-21 2,-4 3,-8 4,-11 0,-7 -1,-14 -4,-20 -3,-6 -9,-12 -16,-17 -8,-6 -15,-9 -22,-10 -7,-1 -13,0 -20,3 -3,1 -6,4 -9,7 -3,4 -8,10 -15,19l-93 131 -26 -19 85 -118c13,-20 25,-33 33,-39 8,-7 17,-11 27,-12 10,-1 19,0 28,3 9,3 18,7 27,14 9,6 16,13 22,21 5,8 9,16 11,25 2,10 1,20 -2,30 -4,10 -12,25 -26,44zm-315 -363l-195 92 -21 -25 224 -99 25 30 -135 205 -22 -26 124 -177zm-362 -150l-14 -28 162 -105 -126 32 -14 -30 102 -81 -182 64 -14 -28 227 -72 13 27 -111 91 139 -33 14 27 -196 136zm-174 -426l-8 -34 76 -70 -98 -32 -8 -34 124 46 105 -101 8 33 -87 79 112 39 8 34 -139 -51 -93 91zm-66 -435l1 -34 105 -55 -102 -60 0 -34 128 79 106 3 -1 32 -105 -3 -132 72zm46 -467l41 -148 23 6 145 169 34 -123 26 8 -43 154 -23 -6 -146 -166 -31 113 -26 -7z" style="transform: rotate({ int((4 - rot) * (360.0 / 26.0))}deg);transform-origin: center;"/>
  <path class="fil5" d="M2500 0c690,0 1315,280 1768,732 452,453 732,1078 732,1768 0,690 -280,1315 -732,1768 -453,452 -1078,732 -1768,732 -690,0 -1315,-280 -1768,-732 -452,-453 -732,-1078 -732,-1768 0,-690 280,-1315 732,-1768 453,-452 1078,-732 1768,-732zm1748 752c-447,-448 -1065,-724 -1748,-724 -683,0 -1301,276 -1748,724 -448,447 -724,1065 -724,1748 0,683 276,1301 724,1748 447,448 1065,724 1748,724 683,0 1301,-276 1748,-724 448,-447 724,-1065 724,-1748 0,-683 -276,-1301 -724,-1748z"/>
  <path class="fil0 str0" d="M2500 1008c824,0 1492,668 1492,1492 0,824 -668,1492 -1492,1492 -824,0 -1492,-668 -1492,-1492 0,-824 668,-1492 1492,-1492z"/>
 </g>
</svg>"""

_old_text_ = """
block_cipher = BlockCipher()

message = 'Hello world! This is RI master class' # input('Enter a message: ')
ciphered_message = block_cipher.cipher(message, print_table=True)
deciphered_message = block_cipher.decipher(ciphered_message)
print(ciphered_message)
print(deciphered_message)

from ciphers import HalfReversedAlphabetCipher, SlidingScaleCipher
half = HalfReversedAlphabetCipher()

sliding_ciphers = tuple(SlidingScaleCipher(r) for r in range(27))
selected_cipher = sliding_ciphers[13]

message = widgets.Text(
    value='Masterclass',
    placeholder='Type something',
    description='Message:',
    disabled=False,
    continuous_update=True,
)


rot_slider = widgets.IntSlider(
    value=13,
    min=0,
    max=26,
    step=1,
    description='Scale rotation: ',
    disabled=False,
    continuous_update=True,
    orientation='horizontal',
    readout=True,
    readout_format='d'
)

caption = widgets.Label(value='hhh')

def refresh_caption(change=None):
    caption.value = selected_cipher.cipher(message.value)

def handle_slider_change(change):
    global selected_cipher
    selected_cipher = sliding_ciphers[change.new]
    refresh_caption()
    
refresh_caption()

rot_slider.observe(handle_slider_change, names='value')
message.observe(refresh_caption, names='value')
display(message, rot_slider, caption)

l = widgets.Label(value="Using some variation of Pegpen")

h = widgets.HTML(
    value='''
    <link href="https://fonts.cdnfonts.com/css/pigpen" rel="stylesheet">
    <p style="font-family: 'Pigpen', sans-serif; font-size: 18pt;">ABCDEFGHI NOPQRSTUV JKLM WXYZ</p>
    '''
)

display(l, h)

_rotor = lambda v, p: widgets.Dropdown(
    options=['I', 'II', 'III', 'IV', 'V'],
    value=v,
    description=f'{p.title()} rotor:',
    disabled=False,
    layout=widgets.Layout(width='350px')
)
_26_slider = lambda d, v: widgets.IntSlider(min=0, max=25, value=v, description=d, layout=widgets.Layout(width='350px'))
_az_slider = lambda d, v: widgets.SelectionSlider(options='ABCDEFGHIJKLMNOPQRSTUVWXYZ', value=v, description=d, layout=widgets.Layout(width='350px'))
_span3 = lambda: widgets.Layout(width='1600px', grid_column='span 3')

left_rotor = _rotor('II', 'left')
middle_rotor = _rotor('IV', 'middle')
right_rotor = _rotor('V', 'right')

left_rotor_ring_setting = _26_slider('Ring setting:', 1)
middle_rotor_ring_setting = _26_slider('Ring setting:', 20)
right_rotor_ring_setting = _26_slider('Ring setting:', 11)

left_rotor_starting_position = _az_slider('Position:', 'B')
middle_rotor_starting_position = _az_slider('Position:', 'L')
right_rotor_starting_position = _az_slider('Position:', 'A')

reflector = widgets.Dropdown(options=['B', 'C'], value='B', description='Reflector:',     layout=widgets.Layout(width='350px'))

plugboard_settings = widgets.Text(value='AV BS CG DL FU HZ IN KM OW RX')

widgets.GridBox((
    left_rotor, middle_rotor, right_rotor,
    # widgets.Label(value='Ring setting is an initial internal rotation of the rotor, it is not visible from outside.', layout=_span3()),
    widgets.VBox((widgets.HTML(value='''<b>Plugboard settings</b><p>Here you can configure the plugboard.<br>
                  You can pick up to 10 uppercase character pairs. A character must not be used twice.<br>
                  For example, you can enter "AB CD EF" but you cannot enter "AB AD EF".'''),
                  plugboard_settings),
                  layout=_span3()),
    left_rotor_ring_setting, middle_rotor_ring_setting, right_rotor_ring_setting,
    left_rotor_starting_position, middle_rotor_starting_position, right_rotor_starting_position, 
    reflector, widgets.Box(), widgets.Box(),
    widgets.VBox((widgets.HTML(value='''<b>Plugboard settings</b><p>Here you can configure the plugboard.<br>
                  You can pick up to 10 uppercase character pairs. A character must not be used twice.<br>
                  For example, you can enter "AB CD EF" but you cannot enter "AB AD EF".'''),
                  plugboard_settings),
                  layout=_span3())
), layout=widgets.Layout(width='1600px', grid_template_columns='repeat(3, 360px)'))

from enigma.machine import EnigmaMachine

# setup machine according to specs from a daily key sheet:
machine = EnigmaMachine.from_key_sheet(
       rotors=' '.join((left_rotor.value, middle_rotor.value, right_rotor.value)),
       reflector=reflector.value,
       ring_settings=[left_rotor_ring_setting.value, middle_rotor_ring_setting.value, right_rotor_ring_setting.value],
       plugboard_settings=plugboard_settings.value)

# set machine initial starting position
starting_position = ''.join((left_rotor_starting_position.value, middle_rotor_starting_position.value, right_rotor_starting_position.value))
machine.set_display(starting_position)
ciphertext = 'NIBLFMYMLLUFWCASCSSNVHAZ'
plaintext = machine.process_text(ciphertext, replace_char='X')
print(plaintext)
machine.set_display(starting_position)
print(machine.process_text(plaintext, replace_char='X'))
"""