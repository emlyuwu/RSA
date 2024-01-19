from consolemenu import *
from consolemenu.items import *

import Encode
import RSAkeygen

menu = ConsoleMenu("Cryptography tools by an idiot", "      Menu", exit_menu_char="0")

RSAGEN = FunctionItem("Generate RSA Keys", RSAkeygen.ext_run, menu=menu, should_exit=False, menu_char="5")
encode = FunctionItem("Encode messages with RSA keys.", Encode.encode, menu=menu, should_exit=False,
                      menu_char="6")
decode = FunctionItem("Decode messages with RSA keys.", Encode.decode, menu=menu, should_exit=False,
                      menu_char="7")

menu.append_item(RSAGEN)
menu.append_item(encode)
menu.append_item(decode)

menu.show()
