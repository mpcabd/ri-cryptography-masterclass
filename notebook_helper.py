import ipywidgets as widgets

from ciphers import BlockCipher
from IPython.display import display

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
    value="""
    <link href="https://fonts.cdnfonts.com/css/pigpen" rel="stylesheet">
    <p style="font-family: 'Pigpen', sans-serif; font-size: 18pt;">ABCDEFGHI NOPQRSTUV JKLM WXYZ</p>
    """
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