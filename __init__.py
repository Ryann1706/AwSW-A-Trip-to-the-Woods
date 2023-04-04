
from modloader import modast, modinfo
from modloader.modclass import Mod, loadable_mod
import jz_magmalink as ml

@loadable_mod
class AWSWMod(Mod):
    name = "A Trip to the Woods"
    version = "0.1"
    author = "Ryann1706"
    dependencies = ["MagmaLink", "Chaos_Knight core mod.", "Not-so-Tragic Hero"]

    def mod_load(self):
        ml.find_label("eck_anna_amelyarc") \
            .search_say("Good night, [player_name].", depth=2000) \
            .search_if("eckannaadopt == True", depth=2000).branch_else() \
            .search_python("persistent.eckannaendingseend = \"D\"") \
            .hook_to("ryann_atttw_start")

    def mod_complete(self):
        pass

