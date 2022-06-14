import caesar
import ciphers
import ipywidgets as widgets
import string

from enigma.machine import EnigmaMachine
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
        display(SVG(data=caesar.caesar(rot)))
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
    
def render_decryption_tool(encrypted_message):
    message = widgets.Text(value=encrypted_message, continuous_update=True, layout=widgets.Layout(width='800px'))
    my_vars = {}
    my_vars['mapping'] = dict({c: c for c in set(encrypted_message.strip()) if c in string.ascii_letters})

    def reset():
        my_vars['mapping'] = dict({c: c for c in set(encrypted_message.strip()) if c in string.ascii_letters})
        out.clear_output()
        with out:
            print(f'Original message:\n{encrypted_message}\n')
            print(f'What we have so far:\n{encrypted_message.lower()}')

    reset_btn = widgets.Button(description='Reset')
    reset_btn.on_click(lambda b: reset())
    
    mappers = list(
        widgets.Dropdown(
            options=string.ascii_lowercase,
            value=c.lower(),
            description=f'{c}:',
            disabled=False,
            layout=widgets.Layout(width='90px'),
            style={'description_width': '20px'},
        )
        for c in sorted(my_vars['mapping'].keys())
    )
    table = widgets.GridBox(mappers, layout=widgets.Layout(grid_template_columns="repeat(3, 100px)"))

    def handler(message, **mappers):
        for k, v in mappers.items():
            c = k[-1].upper()
            my_vars['mapping'][c] = v
        output = ''.join(my_vars['mapping'].get(c, c) for c in message)
        print(f'Original message:\n{message}\n')
        print(f'What we have so far:\n{output}')

    observed = {f'mapper_{m.value}': m for m in mappers}
    observed['message'] = message
    out = widgets.interactive_output(handler, observed)
    
    reset()

    display(widgets.VBox((
        widgets.Label(value='Enter your message below:'),
        message,
        widgets.Label(value='Change the mapping as we go here:'),
        table,
        reset_btn,
        out
    )))
    
def render_enigma():
    rotors = []
    ring_settings = []
    starting_positions = []
    labels = []
    nth = ('1st', '2nd', '3rd')
    for i in range(3):
        rotors.append(widgets.Dropdown(
            options=['I', 'II', 'III', 'IV', 'V'],
            value='I',
            disabled=False,
            # layout=widgets.Layout(width='350px')
        ))
        ring_settings.append(widgets.IntSlider(
            min=0,
            max=25,
        ))
        starting_positions.append(widgets.SelectionSlider(
            options=string.ascii_uppercase,
        ))
    reflector = widgets.Dropdown(options=['B', 'C'])
    plugboard_settings = widgets.Text()
    configure_button = widgets.Button(description='Configure')
    reset_button = widgets.Button(description='Reset')
    message = widgets.Text()
    keyboard = {c: widgets.Button(description=c) for c in string.ascii_uppercase}
    out = widgets.Output()
    pressed_out = widgets.Output()
        
    # initial setup
    def reset(btn):
        rotors[0].value = 'II'
        rotors[1].value = 'IV'
        rotors[2].value = 'V'
        ring_settings[0].value = 1
        ring_settings[1].value = 20
        ring_settings[2].value = 11
        starting_positions[0].value = 'B'
        starting_positions[1].value = 'L'
        starting_positions[2].value = 'A'
        reflector.value = 'B'
        plugboard_settings.value = 'AV BS CG DL FU HZ IN KM OW RX'
        message.value = 'NIBL FMYM LLUF WCAS CSSN VHAZ'
        out.clear_output()
        pressed_out.clear_output()

    reset_button.on_click(reset)
    reset(reset_button)
    
    my_vars = {}
    
    def handle_configuration(btn):
        my_vars['machine'] = EnigmaMachine.from_key_sheet(
            rotors=' '.join(r.value for r in rotors),
            reflector=reflector.value,
            ring_settings=tuple(rs.value for rs in ring_settings),
            plugboard_settings=plugboard_settings.value)
        my_vars['machine'].set_display(''.join(sp.value for sp in starting_positions))
    
    configure_button.on_click(handle_configuration)
    handle_configuration(configure_button)
    
    def handle_key_press(key):
        c = my_vars['machine'].key_press(key)
        display = my_vars['machine'].get_display()
        for i in range(3):
            starting_positions[i].value = display[i]
        with out:
            print(c, end='')
        with pressed_out:
            print(key, end='')
    
    def generate_handler(key):
        return lambda btn: handle_key_press(key)

    for key, btn in keyboard.items():
        btn.on_click(generate_handler(key))
        
    keyboard_grid = widgets.VBox((
        widgets.HBox(tuple(keyboard[c] for c in 'QWERTYUIOP')),
        widgets.HBox(tuple(keyboard[c] for c in 'ASDFGHJKL')),
        widgets.HBox(tuple(keyboard[c] for c in 'ZXCVBNM')),
    ))
    play = widgets.Play(
        value=-1,
        min=-1,
        max=len(message.value.replace(' ', '')) - 1,
        step=1,
        interval=1000,
        disabled=False,
        show_repeat=False,
    )
    def handle_play(change):
        m = message.value.replace(' ', '')
        handle_key_press(m[play.value])
    play.observe(handle_play, names='value')

    display(
        widgets.HBox((
            message,
            play,
        )),
        widgets.HBox(starting_positions),
        keyboard_grid,
        widgets.VBox((
            widgets.Label(value='Pressed so far: '),
            pressed_out,
        )),
        widgets.VBox((
            widgets.Label(value='Output: '),
            out,
        )),
    )