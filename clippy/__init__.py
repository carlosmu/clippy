# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

####################################
# IMPORT MODULES
####################################

from . import btn_clipping_presets
from . import user_prefs
from . import op_apply_clipping

bl_info = {
    "name": "Clippy",
    "author": "Carlos Mu <carlos.damian.munoz@gmail.com>, Gez <twitter.com/gez>",
    "blender": (2, 83, 0),
    "version": (1, 0, 0),
    "category": "Camera",
    "location": "View Tab of 3D-View Sidebar / Camera Properties",
    "description": "Clipping presets for viewport and camera",
    "warning": "",
    "doc_url": "https://blendermarket.com/products/clippy",
    "tracker_url": "https://blendermarket.com/creators/carlosmu",
}

####################################
# REGISTER/UNREGISTER
####################################
def register():
    op_apply_clipping.register()
    btn_clipping_presets.register()
    user_prefs.register()

def unregister():
    op_apply_clipping.unregister()
    btn_clipping_presets.unregister()
    user_prefs.unregister()